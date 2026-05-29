#!/usr/bin/env -S node --experimental-strip-types

/** CLI for sending desktop notifications via D-Bus.
 *
 * Analogous to notify-send(1) from libnotify, uses the
 * org.freedesktop.Notifications interface directly.
 *
 * Desktop Notifications Specification, v1.3, 2024-08-18.
 * https://specifications.freedesktop.org/notification-spec/latest/
 *
 * D-Bus Specification v0.43, 2024-10-29 — SASL auth and wire format.
 * https://dbus.freedesktop.org/doc/dbus-specification.html */

import { pathToFileURL } from "node:url";
import type { Socket } from "node:net";
import { buildHelloPayload } from "./src/dbus_msg.ts";
import {
  buildNotifyPayload,
  type NotificationPortal,
  type Notification,
  type SupportedOptions,
} from "./src/notification.ts";

/** Collect all data received within a time window. */
function collectWindow(
  socket: Socket,
  windowMs: number,
  setTimeout: (cb: () => void, ms: number) => void,
): Promise<Buffer> {
  return new Promise((resolve) => {
    const chunks: Buffer[] = [];
    const onData = (data: Buffer) => chunks.push(data);
    socket.on("data", onData);
    setTimeout(() => {
      socket.off("data", onData);
      resolve(Buffer.concat(chunks));
    }, windowMs);
  });
}

/** Resolve with the first data chunk, or reject on timeout. */
function firstData(
  socket: Socket,
  timeoutMs: number,
  setTimeout: (cb: () => void, ms: number) => void,
): Promise<Buffer> {
  return new Promise<Buffer>((resolve, reject) => {
    const cleanup = () => socket.off("data", onData);
    const onData = (data: Buffer) => {
      cleanup();
      resolve(data);
    };
    socket.on("data", onData);
    setTimeout(() => {
      cleanup();
      reject(new Error("D-Bus reply timeout"));
    }, timeoutMs);
  });
}

/** Wraps a connected D-Bus socket: SASL auth and send/receive.
 *
 * Modeled after DBusSock in send_test.py (jeepney sans-io pattern). */
class DBusSock {
  static readonly #METHOD_RETURN = 2;

  readonly #sock: Socket;
  readonly #setTimeout: (cb: () => void, ms: number) => void;

  constructor(sock: Socket, setTimeout: (cb: () => void, ms: number) => void) {
    this.#sock = sock;
    this.#setTimeout = setTimeout;
  }

  /** Check whether a reply buffer represents a method-return (type byte 2). */
  static isMethodReturn(data: Buffer): boolean {
    return data.length >= 2 && data[1] === DBusSock.#METHOD_RETURN;
  }

  /** Extract notification ID from a Notify method-return body (single u32). */
  static parseReplyId(data: Buffer): number {
    if (data.length < 16) throw new Error("Reply too short for D-Bus header");
    const fieldsLen = data.readUInt32LE(12);
    const bodyOff = ((16 + fieldsLen + 7) >>> 3) << 3;
    if (bodyOff + 4 > data.length) throw new Error("Reply body too short for u32");
    return data.readUInt32LE(bodyOff);
  }

  /** Connect and wrap. */
  static async connect(
    socket: Socket,
    setTimeout: (cb: () => void, ms: number) => void,
  ): Promise<DBusSock> {
    await new Promise<void>((resolve, reject) => {
      socket.once("connect", () => resolve());
      socket.once("error", reject);
    });
    return new DBusSock(socket, setTimeout);
  }

  /** SASL AUTH EXTERNAL handshake over the connected socket. */
  async authenticate(uid: number): Promise<void> {
    const uidHex = Buffer.from(String(uid)).toString("hex");
    this.#sock.write(`\0AUTH EXTERNAL ${uidHex}\r\n`);
    this.#sock.write("NEGOTIATE_UNIX_FD\r\n");
    this.#sock.write("BEGIN\r\n");

    await firstData(this.#sock, 2000, this.#setTimeout);
    for (;;) {
      try {
        await firstData(this.#sock, 10, this.#setTimeout);
      } catch {
        break;
      }
    }
  }

  /** Send a raw D-Bus message and return the reply, or throw on timeout. */
  async send(payload: Uint8Array, timeoutMs: number = 3000): Promise<Buffer> {
    this.#sock.write(payload);
    return await firstData(this.#sock, timeoutMs, this.#setTimeout);
  }

  /** Send a method call and validate the reply is a method-return. */
  async callMethod(payload: Uint8Array, timeoutMs: number = 3000): Promise<Buffer> {
    const data = await this.send(payload, timeoutMs);
    if (!DBusSock.isMethodReturn(data)) throw new Error("D-Bus method call rejected");
    return data;
  }

  close(): void {
    this.#sock.destroy();
  }
}

/** Implementation of NotificationPortal against the notification daemon
 * (org.freedesktop.Notifications) via a D-Bus socket. */
class NotificationsDaemon implements NotificationPortal {
  readonly #dbus: DBusSock;
  readonly #uid: number;
  #connected: boolean = false;

  constructor(dbus: DBusSock, uid: number) {
    this.#dbus = dbus;
    this.#uid = uid;
  }

  async #ensureConnected(): Promise<void> {
    if (this.#connected) return;
    await this.#dbus.authenticate(this.#uid);
    await this.#dbus.callMethod(buildHelloPayload(), 2000);
    this.#connected = true;
  }

  async AddNotification(_id: string, notification: Notification): Promise<void> {
    await this.#ensureConnected();
    const pkt = buildNotifyPayload(notification);
    const nr = await this.#dbus.callMethod(pkt);
    const nid = DBusSock.parseReplyId(nr);
    console.error("Notify: OK (id=%s)", nid);
  }

  async getSupportedOptions(): Promise<SupportedOptions> {
    throw new Error("NotificationsDaemon does not support getSupportedOptions");
  }

  async getVersion(): Promise<number> {
    throw new Error("NotificationsDaemon does not support getVersion");
  }

  async RemoveNotification(_id: string): Promise<void> {
    throw new Error("NotificationsDaemon does not support RemoveNotification");
  }

  async onActionInvoked(_handler: (...args: unknown[]) => void): Promise<void> {
    throw new Error("NotificationsDaemon does not support onActionInvoked");
  }

  close(): void {
    this.#dbus.close();
  }
}

/** Parse CLI args and derive the D-Bus socket path.
 * @throws on missing title or unresolvable uid. */
function parseArgs(
  argv: string[],
  uid: number | undefined,
): { title: string; body: string; uid: number; busPath: string } {
  const title = argv[0] ?? "";
  const body = argv.slice(1).join(" ");
  if (!title) throw new Error("Usage: notify-send.ts <title> [body...]");
  if (uid === undefined) throw new Error("Cannot determine user ID");
  return { title, body, uid, busPath: `/run/user/${uid}/bus` };
}

/** Options for {@link main}. */
interface MainOptions {
  argv: string[];
  getuid: () => number | undefined;
  createConnection: (path: string) => Socket;
  setTimeout: (cb: () => void, ms: number) => void;
}

async function main(options: MainOptions): Promise<number> {
  const { argv, getuid, createConnection, setTimeout } = options;
  const { title, body, uid, busPath } = parseArgs(argv, getuid());

  const dbus = await DBusSock.connect(createConnection(busPath), setTimeout);
  const portal: NotificationPortal = new NotificationsDaemon(dbus, uid);
  try {
    await portal.AddNotification("notify-send", { title, body });
    return 0;
  } finally {
    portal.close();
  }
}

if (
  process.argv[1] &&
  import.meta.url === pathToFileURL(process.argv[1]).href
) {
  async function _script_io(): Promise<number> {
    const net = await import("node:net");
    return main({
      argv: process.argv.slice(2),
      getuid: process.getuid,
      createConnection: net.createConnection,
      setTimeout: globalThis.setTimeout,
    });
  }
  _script_io().then(
    (code) => process.exit(code),
    (err: unknown) => {
      console.error(err);
      process.exit(1);
    },
  );
}
