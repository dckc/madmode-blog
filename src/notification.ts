/** TypeScript types for org.freedesktop.portal.Notification, version 2.
 *
 * XDG Desktop Portal documentation, 2025.
 * https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.Notification.html
 *
 * Properties, methods, and signals as defined by the D-Bus interface.
 * Notification payload modeled as a precise `a{sv}` vardict with
 * optional keys, version-gated fields, and category-specific button purposes. */

import { newMethodCall } from "./dbus_msg.ts";

/** Priority levels for the notification. */
export type Priority = "low" | "normal" | "high" | "urgent";

/** Display hint flags for how the notification should be presented. */
export type DisplayHint =
  | "transient"
  | "tray"
  | "persistent"
  | "hide-on-lockscreen"
  | "hide-content-on-lockscreen"
  | "show-as-new";

/** Standardized notification categories (version 2). */
export type NotificationCategory =
  | "im.received"
  | "alarm.ringing"
  | "call.incoming"
  | "call.ongoing"
  | "call.unanswered"
  | "weather.warning.extreme"
  | "cellbroadcast.danger.presidential"
  | "cellbroadcast.danger.extreme"
  | "cellbroadcast.danger.severe"
  | "cellbroadcast.public-safety"
  | "cellbroadcast.amber-alert"
  | "cellbroadcast.test"
  | "os.battery.low"
  | "browser.web-notification"
  | (string & {});

/** Button purposes understood by the portal.
 * Additional vendor-specific purposes use a `x-vendor.` prefix. */
export type ButtonPurpose =
  | "im.reply-with-text"
  | "call.accept"
  | "call.decline"
  | "call.hang-up"
  | "call.enable-speakerphone"
  | "call.disable-speakerphone"
  | "system.custom-alert"
  | (string & {});

/** A themed icon (GThemedIcon equivalent). */
export interface ThemedIcon {
  readonly themed: readonly string[];
}

/** An icon from raw bytes (GBytesIcon equivalent, deprecated since v2). */
export interface BytesIcon {
  readonly bytes: readonly number[];
}

/** An icon from a memfd file descriptor (version 2). */
export interface FileDescriptorIcon {
  readonly "file-descriptor": number;
}

/** A serialized icon value: an object with exactly one key, or a plain
 * string for backward compatibility (single-name themed icon). */
export type SerializedIcon =
  | ThemedIcon
  | BytesIcon
  | FileDescriptorIcon
  | string;

/** A sound from a memfd file descriptor (version 2). */
export interface FileDescriptorSound {
  readonly "file-descriptor": number;
}

/** A serialized sound value.
 * `"default"` plays the default sound, `"silent"` plays nothing. */
export type SerializedSound = FileDescriptorSound | "default" | "silent";

/** A notification button. */
export interface NotificationButton {
  /** User-visible label. Mandatory unless `purpose` is set. */
  readonly label?: string;
  /** Name of an exported action activated on click. Mandatory. */
  readonly action: string;
  /** Target parameter to send with the action. */
  readonly target?: unknown;
  /** Semantic purpose for the button (version 2). */
  readonly purpose?: ButtonPurpose;
}

/** The notification vardict (`a{sv}`) passed to AddNotification.
 * All keys are optional. */
export interface Notification {
  /** Short title string (may be truncated to one line). */
  readonly title?: string;
  /** Body text (may be wrapped or truncated). */
  readonly body?: string;
  /** Body with XML markup: `<b>`, `<i>`, `<a href="...">` (version 2). */
  readonly "markup-body"?: string;
  /** Serialized icon. */
  readonly icon?: SerializedIcon;
  /** Serialized sound (version 2). */
  readonly sound?: SerializedSound;
  /** Notification priority. */
  readonly priority?: Priority;
  /** Name of an exported action activated on click. */
  readonly "default-action"?: string;
  /** Target parameter for the default action. */
  readonly "default-action-target"?: unknown;
  /** Action buttons. */
  readonly buttons?: readonly NotificationButton[];
  /** Display hints (version 2). */
  readonly "display-hint"?: readonly DisplayHint[];
  /** Content category (version 2). */
  readonly category?: NotificationCategory;
}

/** Options advertised by the notification server. */
export interface SupportedOptions {
  /** Categories the server understands and supports. */
  readonly category?: readonly string[];
  /** Button purposes the server understands and supports. */
  readonly "button-purpose"?: readonly string[];
}

/** Parameter array for the ActionInvoked signal. */
export interface ActionInvokedParameter {
  /** Application-defined target, if one was specified. */
  readonly target?: unknown;
  /** Platform data including `activation-token`. */
  readonly platformData: { readonly "activation-token": string };
  /** User response text, if applicable (e.g. inline reply). */
  readonly userResponse?: string;
}

/** The org.freedesktop.portal.Notification D-Bus interface. */
export interface NotificationPortal {
  /** Options advertised by the notification server. */
  getSupportedOptions(): Promise<SupportedOptions>;

  /** Protocol version of the notification portal. */
  getVersion(): Promise<number>;

  /** Send or update a notification.
   * `id` is application-provided and can be reused to update. */
  AddNotification(id: string, notification: Notification): Promise<void>;

  /** Withdraw a notification by its application-provided ID. */
  RemoveNotification(id: string): Promise<void>;

  /** Emitted when a non-exported action is activated.
   * `parameter` payload: [target?, platformData, userResponse?] */
  onActionInvoked(
    handler: (
      id: string,
      action: string,
      parameter: readonly unknown[],
    ) => void,
  ): Promise<void>;
}

/** Internal: convert a SerializedIcon to a D-Bus variant value `[sig, val]`. */
function serializeIcon(icon: SerializedIcon): [string, unknown] {
  if (typeof icon === "string") {
    return ["s", icon];
  }
  if ("themed" in icon) {
    return ["(sv)", ["themed", ["as", [...icon.themed]]]];
  }
  if ("bytes" in icon) {
    return ["(sv)", ["bytes", ["ay", [...icon.bytes]]]];
  }
  return ["(sv)", ["file-descriptor", ["h", icon["file-descriptor"]]]];
}

/** Internal: convert a SerializedSound to a D-Bus variant value `[sig, val]`. */
function serializeSound(sound: SerializedSound): [string, unknown] {
  if (typeof sound === "string") {
    return ["s", sound];
  }
  return ["(sv)", ["file-descriptor", ["h", sound["file-descriptor"]]]];
}

/** Internal: convert a NotificationButton to a D-Bus a{sv} dict. */
function serializeButton(
  button: NotificationButton,
): Record<string, [string, unknown]> {
  const dict: Record<string, [string, unknown]> = {};
  if (button.label !== undefined) dict.label = ["s", button.label];
  dict.action = ["s", button.action];
  if (button.target !== undefined) dict.target = targetToVariant(button.target);
  if (button.purpose !== undefined) dict.purpose = ["s", button.purpose];
  return dict;
}

/** Internal: wrap arbitrary value as a variant `[sig, val]`. */
function targetToVariant(target: unknown): [string, unknown] {
  if (typeof target === "string") return ["s", target];
  if (typeof target === "number") return ["i", target];
  return ["s", String(target)];
}

/** Convert a typed Notification into the D-Bus `a{sv}` dict representation.
 *
 * Each value is a `[signature, value]` pair suitable for variant packing. */
export function notificationToDict(
  n: Notification,
): Record<string, [string, unknown]> {
  const dict: Record<string, [string, unknown]> = {};
  if (n.title !== undefined) dict.title = ["s", n.title];
  if (n.body !== undefined) dict.body = ["s", n.body];
  if (n["markup-body"] !== undefined)
    dict["markup-body"] = ["s", n["markup-body"]];
  if (n.icon !== undefined) dict.icon = serializeIcon(n.icon);
  if (n.sound !== undefined) dict.sound = serializeSound(n.sound);
  if (n.priority !== undefined) dict.priority = ["s", n.priority];
  if (n["default-action"] !== undefined)
    dict["default-action"] = ["s", n["default-action"]];
  if (n["default-action-target"] !== undefined)
    dict["default-action-target"] = targetToVariant(n["default-action-target"]);
  if (n.buttons !== undefined) {
    dict.buttons = [
      "aa{sv}",
      n.buttons.map((b) => serializeButton(b)),
    ];
  }
  if (n["display-hint"] !== undefined)
    dict["display-hint"] = ["as", [...n["display-hint"]]];
  if (n.category !== undefined) dict.category = ["s", n.category];
  return dict;
}

/** Portal bus name and object path. */
const PORTAL_BUS_NAME = "org.freedesktop.portal.Desktop";
const PORTAL_OBJECT_PATH = "/org/freedesktop/portal/notification";
const PORTAL_INTERFACE = "org.freedesktop.portal.Notification";

/** Build a complete D-Bus method call payload for AddNotification. */
export function buildAddNotificationPayload(
  id: string,
  notification: Notification,
): Uint8Array {
  const dict = notificationToDict(notification);
  return newMethodCall(
    {
      objectPath: PORTAL_OBJECT_PATH,
      busName: PORTAL_BUS_NAME,
      interface: PORTAL_INTERFACE,
    },
    "AddNotification",
    "sa{sv}",
    [id, dict],
  );
}
