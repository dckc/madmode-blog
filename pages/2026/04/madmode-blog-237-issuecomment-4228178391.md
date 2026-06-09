---
title: "Obsidian-LiveSync: Self-Hosted (mostly)"
date: 2026-04-11
tags:
  - github
  - syndicated
  - vm
  - sync
  - self-hosted
  - mobile
  - writing
published: true
summary: Self-hosted Obsidian sync using CouchDB on Proxmox LXC, secured with Tailscale.
---

Self-hosted [Obsidian LiveSync](https://github.com/vrtmrz/obsidian-livesync) using CouchDB on Proxmox LXC container, secured with Tailscale VPN and end-to-end encryption.

![near-realtime sync](https://user-images.githubusercontent.com/45774780/137355323-f57a8b09-abf2-4501-836c-8cb7d2ff24a3.gif)

## Proxmox VM / Container Host

I have [Proxmox VE 9.1](https://www.proxmox.com/en/downloads) running on an old (circa 2013) laptop. It has USB 3 ports, but only USB 2 seems to work for booting from a thumb drive.
SHA256SUM: `6d8f5afc78c0c66812d7272cde7c8b98be7eb54401ceb045400db05eb5ae6d22`

```mermaid
sequenceDiagram
    actor USER as Operator
    participant HP as HP Envy<br/>Laptop<br/>

    USER->>HP: Boot Proxmox 9.1.1<br/>ISO (USB 2)
    create participant PVE as pve1 Host
    HP->>PVE: Create pve1 host

    USER->>PVE: root password
    PVE->>PVE: Generate SSH host keys
    PVE->>PVE: Get DHCP lease (192.168.x.y)
    PVE->>PVE: Start web UI
    PVE->>USER: Installation complete
```

## apache-couchdb container

After flailing around trying to figure out CouchDB, I re-discovered [Proxmox VE Scripts](https://community-scripts.org/), especially [apache-couchdb](https://community-scripts.org/scripts/apache-couchdb).

```mermaid
sequenceDiagram
    actor USER as Operator
    participant PVE as pve1 Host
    participant CS as Proxmox VE<br/>Scripts

    USER->>PVE: ssh root@pve1

    USER->>PVE: curl /ct/apache-couchdb.sh |<br/>bash
    PVE->>CS: GET /ct/apache-couchdb.sh
    CS->>PVE: apache-couchdb.sh
    PVE->>PVE: Download Debian LXC image
    PVE->>PVE: pct create ...

    create participant CT as apache-couchdb
    PVE->>CT: apt install couchdb
    create participant DBA as admin
    CT->>DBA: create admin user
    CT->>USER: admin password, Erlang Cookie
```

## Sync from workstation to CouchDB

[obsidian-livesync](https://github.com/vrtmrz/obsidian-livesync) has a nifty
"everything in 1 URL" setup mechanism, but I only found docs for doing it on fly.io.

More flailing: after I installed the plugin, I couldn't find the [setup wizard](https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/quick_setup.md). It turns out: I neglected to turn it on.

Then I puzzled over which usernames and passwords are for what. Eventually, I passed the wizard's connection test, and all was well.

```mermaid
sequenceDiagram
    actor USER as Operator
    participant BLD as obsidian<br/>Desktop
    participant DBA as admin
    participant CDB as couchdb<br/>

    DBA->>CDB: Configure CORS<br/>for Obsidian
    DBA->>CDB: Create dckb-obsidian user
    DBA->>CDB: Create dckb database
    create participant dckb as dckb<br/>database
    CDB->>dckb: create
    DBA->>CDB: grant dckb-obsidian<br/>roles on dckb DB

    USER->>BLD: enable LiveSync plugin
    USER->>BLD: Test CouchDB connection
    BLD->>dckb: Test CouchDB connection
    BLD->>dckb: Initial sync
```

## Mobile Sync

To expose CouchDB for mobile use, I used the [Proxmox Tailscale add-on](https://community-scripts.org/scripts/add-tailscale-lxc), since I've used **tailscale** before. _Maybe I'll find a more open alternative in due course, but that's for another day._

I tweaked the CouchDB host in Obsidian on my workstation to the tailscale `100.x.y.z` address, and then I let it generate a handy setup URI.

```mermaid
sequenceDiagram
    actor USER as Operator
    participant BLD as obsidian<br/>Desktop
    participant PVE as pve1<br/>(Proxmox Host)
    participant CT as apache-couchdb CT
    participant ANDR as Obsidian<br/>mobile
    participant TAIL as Tailscale<br/>Network

    Note over PVE,CT: Expose CouchDB via Tailscale
    Note over USER,PVE: not shown: Proxmox VE<br/>scripts
    USER->>PVE: add-tailscale-lxc.sh
    PVE->>CT: Install Tailscale
    PVE->>CT: Reboot container
    CT->>TAIL: tailscale up<br/>(authenticate)

    Note over BLD,ANDR: Sync Workstation via Tailscale
    BLD->>TAIL: tailscale up (authenticate)
    USER->>BLD: set LiveSync URL to tailscale addr
    BLD->>CT: Test CouchDB connection
    BLD->>BLD: Generate setup URI

    Note over ANDR,CT: Sync Mobile
    ANDR->>TAIL: Install Tailscale app<br/>& authenticate
    BLD->>ANDR: setup URI<br/> (manual)
    ANDR->>CT: Initial sync

    Note over BLD,ANDR: Ongoing Sync
    loop Live Sync
        BLD->>CT: Push file changes (chunks)
        CT->>ANDR: Pull changes via _changes feed
        ANDR->>CT: Push file changes (chunks)
        CT->>BLD: Pull changes via _changes feed
    end
```

---

*Originally appeared as [a comment on obsidian + livesync for personal notes](https://github.com/dckc/madmode-blog/issues/237#issuecomment-4228178391).*
