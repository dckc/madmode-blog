#!/usr/bin/python3
"""Process census snapshot, logged to the journal.

Context: `pstree -s -p $$` showed PIDs in the millions after only a few
days of uptime (e.g. bash(2252311), script(3282662)). We're collecting
these aggregate stats to determine whether that is normal PID allocation
on this machine or whether some process is burning through the PID space
abnormally fast.

Runs as one process: it reads /proc and writes to journald's socket
itself. The shell version started ~30 helpers (ls, sort, tr, logger, ...)
every 30s, adding to the churn it was measuring.

PROC_FORKS (processes created since boot, from /proc/stat) is the
churn measure: it only goes up, so the rate between any two snapshots is
exact however far apart they are. PROC_MAX_PID stops meaning "newest"
once PIDs wrap at pid_max.

Export with procmon-csv.
"""

from collections import Counter
from socket import AF_UNIX, SOCK_DGRAM
import struct

JOURNAL_SOCKET = "/run/systemd/journal/socket"
TOP_NEWEST = 3
TOP_COMMS = 10


def median(sorted_pids):
    """
    >>> median([]), median([1, 5, 9]), median([1, 4, 7, 10])
    (0, 5, 5)
    """
    n = len(sorted_pids)
    if n == 0:
        return 0
    if n % 2 == 1:
        return sorted_pids[n // 2]
    return (sorted_pids[n // 2 - 1] + sorted_pids[n // 2]) // 2


def top_comms(comms, n=TOP_COMMS):
    """Most common command names, e.g. "49 brave,37 code".

    A process leak shows up as one name's count climbing.

    >>> top_comms({1: "code", 2: "brave", 3: "code", 4: "brave", 5: "brave"})
    '3 brave,2 code'
    """
    counts = sorted(Counter(comms.values()).items(), key=lambda kv: (-kv[1], kv[0]))
    return ",".join(f"{count} {name}" for name, count in counts[:n])


def parse_forks(stat_text):
    """Processes created since boot, from /proc/stat.

    >>> parse_forks("cpu  1 2 3\\nprocesses 4158211\\nprocs_running 2\\n"), parse_forks("")
    (4158211, 0)
    """
    for line in stat_text.splitlines():
        if line.startswith("processes "):
            return int(line.split()[1])
    return 0


def census_fields(pids, comms, ppids, forks):
    """Journal fields for one snapshot.

    pids: sorted live PIDs; comms: pid -> command name;
    ppids: pid -> parent PID for (at least) the newest PIDs;
    forks: processes created since boot.

    >>> fields = dict(census_fields([1, 50, 90], {1: "init", 50: "bash", 90: "git"}, {90: 50}, 1234))
    >>> fields["PROC_TOP1_COMM"], fields["PROC_TOP1_PCOMM"], fields["PROC_TOP2_PCOMM"], fields["PROC_FORKS"]
    ('git', 'bash', '?', 1234)
    """
    fields = [
        ("MESSAGE", "process census snapshot"),
        ("SYSLOG_IDENTIFIER", "procmon"),
        ("PROC_COUNT", len(pids)),
        ("PROC_FORKS", forks),
        ("PROC_MIN_PID", pids[0] if pids else 0),
        ("PROC_MAX_PID", pids[-1] if pids else 0),
        ("PROC_MEDIAN_PID", median(pids)),
        ("PROC_TOP_COMMS", top_comms(comms)),
    ]
    # Newest (highest-numbered) processes, with their parent.
    for i, pid in enumerate(reversed(pids[-TOP_NEWEST:]), start=1):
        ppid = ppids.get(pid, 0)
        fields += [
            (f"PROC_TOP{i}_PID", pid),
            (f"PROC_TOP{i}_COMM", comms.get(pid, "?")),
            (f"PROC_TOP{i}_PPID", ppid),
            (f"PROC_TOP{i}_PCOMM", comms.get(ppid, "?")),
        ]
    return fields


def journal_payload(fields):
    """Encode fields in journald's native protocol (systemd.journal-fields).

    Values containing a newline get a length prefix.

    >>> journal_payload([("A", 1), ("M", "a\\nb")])
    b'A=1\\nM\\n\\x03\\x00\\x00\\x00\\x00\\x00\\x00\\x00a\\nb\\n'
    """
    out = bytearray()
    for key, value in fields:
        k, v = key.encode(), str(value).encode()
        if b"\n" in v:
            out += k + b"\n" + struct.pack("<Q", len(v)) + v + b"\n"
        else:
            out += k + b"=" + v + b"\n"
    return bytes(out)


def parse_ppid(status_text):
    """
    >>> parse_ppid("Name:\\tbash\\nPPid:\\t1234\\n"), parse_ppid("")
    (1234, 0)
    """
    for line in status_text.splitlines():
        if line.startswith("PPid:"):
            return int(line.split()[1])
    return 0


def read_comms(proc, exclude):
    """pid -> command name for live PIDs; drops PIDs that exit mid-scan."""
    comms = {}
    for entry in proc.iterdir():
        if not entry.name.isdigit() or int(entry.name) == exclude:
            continue
        try:
            comms[int(entry.name)] = (entry / "comm").read_text().rstrip("\n")
        except (FileNotFoundError, ProcessLookupError):
            pass
    return comms


def read_ppid(process):
    try:
        return parse_ppid((process / "status").read_text())
    except (FileNotFoundError, ProcessLookupError):
        return 0


def journal_sender(socket, address):
    sock = socket(AF_UNIX, SOCK_DGRAM)

    def send(fields):
        sock.sendto(journal_payload(fields), address)

    return send


def main(proc, socket, self_pid):
    journal_send = journal_sender(socket, JOURNAL_SOCKET)
    comms = read_comms(proc, exclude=self_pid)
    pids = sorted(comms)
    ppids = {pid: read_ppid(proc / str(pid)) for pid in pids[-TOP_NEWEST:]}
    forks = parse_forks((proc / "stat").read_text())
    journal_send(census_fields(pids, comms, ppids, forks))
    return 0


if __name__ == "__main__":
    def _script_io():
        from os import getpid
        from pathlib import Path
        from socket import socket

        return main(proc=Path("/proc"), socket=socket, self_pid=getpid())

    raise SystemExit(_script_io())
