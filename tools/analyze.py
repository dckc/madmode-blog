"""ELF binary size analyzer — sections, segments, functions, strings.

Reports how every byte of an ELF executable is used.  Supports
comparing two files (e.g. unstripped vs stripped).

ELF structures follow the ELF Specification v1.2, 2001-05, TIS Committee.
https://refspecs.linuxfoundation.org/elf/elf-spec.pdf
"""

# Parse logic is pure: takes bytes, returns structures.  All I/O
# authority (file reading, subprocess, output) is injected.

# Function-boundary analysis via call-target parsing of objdump output.

import re
import struct
from dataclasses import dataclass
from typing import Callable, Sequence


# ELF constants  (ELF Specification v1.2 §4-7)

SHT_NULL = 0
SHT_PROGBITS = 1
SHT_NOBITS = 8
SHT_STRTAB = 3

PT_PHDR = 6
PT_LOAD = 1
PT_DYNAMIC = 2
PT_TLS = 7
PT_GNU_EH_FRAME = 0x6474e550
PT_GNU_RELRO = 0x6474e552
PT_GNU_STACK = 0x6474e551

SHF_WRITE = 1
SHF_ALLOC = 2
SHF_EXECINSTR = 4

PF_R = 4
PF_W = 2
PF_X = 1

ELFMAG = b"\x7fELF"
ELFCLASS64 = 2
ELFDATA2LSB = 1

SEGMENT_TYPE_NAMES = {
    PT_PHDR: "PHDR",
    PT_LOAD: "LOAD",
    PT_DYNAMIC: "DYNAMIC",
    PT_TLS: "TLS",
    PT_GNU_EH_FRAME: "GNU_EH_FRAME",
    PT_GNU_RELRO: "GNU_RELRO",
    PT_GNU_STACK: "GNU_STACK",
}


@dataclass
class ElfHeader:
    e_type: int
    e_machine: int
    e_entry: int
    e_phoff: int
    e_shoff: int
    e_flags: int
    e_ehsize: int
    e_phentsize: int
    e_phnum: int
    e_shentsize: int
    e_shnum: int
    e_shstrndx: int


@dataclass
class Section:
    name: str
    sh_type: int
    sh_flags: int
    sh_addr: int
    sh_offset: int
    sh_size: int


@dataclass
class Segment:
    p_type: int
    p_flags: int
    p_offset: int
    p_vaddr: int
    p_filesz: int
    p_memsz: int


def parse_elf_header(data: bytes) -> ElfHeader | None:
    if len(data) < 64 or data[:4] != ELFMAG:
        return None
    if data[4] != ELFCLASS64 or data[5] != ELFDATA2LSB:
        return None
    return ElfHeader(
        e_type=struct.unpack_from("<H", data, 16)[0],
        e_machine=struct.unpack_from("<H", data, 18)[0],
        e_entry=struct.unpack_from("<Q", data, 24)[0],
        e_phoff=struct.unpack_from("<Q", data, 32)[0],
        e_shoff=struct.unpack_from("<Q", data, 40)[0],
        e_flags=struct.unpack_from("<I", data, 48)[0],
        e_ehsize=struct.unpack_from("<H", data, 52)[0],
        e_phentsize=struct.unpack_from("<H", data, 54)[0],
        e_phnum=struct.unpack_from("<H", data, 56)[0],
        e_shentsize=struct.unpack_from("<H", data, 58)[0],
        e_shnum=struct.unpack_from("<H", data, 60)[0],
        e_shstrndx=struct.unpack_from("<H", data, 62)[0],
    )


def parse_sections(data: bytes, hdr: ElfHeader) -> list[Section]:
    if hdr.e_shoff == 0 or hdr.e_shnum == 0:
        return []
    raw = []
    strtab_off = 0
    strtab_size = 0
    for i in range(hdr.e_shnum):
        off = hdr.e_shoff + i * hdr.e_shentsize
        chunk = data[off : off + 64]
        raw.append((
            struct.unpack_from("<I", chunk, 0)[0],
            struct.unpack_from("<I", chunk, 4)[0],
            struct.unpack_from("<Q", chunk, 8)[0],
            struct.unpack_from("<Q", chunk, 24)[0],
            struct.unpack_from("<Q", chunk, 32)[0],
        ))
        if i == hdr.e_shstrndx:
            strtab_off = struct.unpack_from("<Q", chunk, 24)[0]
            strtab_size = struct.unpack_from("<Q", chunk, 32)[0]
    sections = []
    for name_off, stype, sflags, soff, ssize in raw:
        name = ""
        if strtab_off and name_off < strtab_size:
            end = data.index(b"\0", strtab_off + name_off)
            name = data[strtab_off + name_off : end].decode("ascii", errors="replace")
        sections.append(Section(
            name=name,
            sh_type=stype,
            sh_flags=sflags,
            sh_addr=0,
            sh_offset=soff,
            sh_size=ssize,
        ))
    return sections


def parse_segments(data: bytes, hdr: ElfHeader) -> list[Segment]:
    if hdr.e_phoff == 0 or hdr.e_phnum == 0:
        return []
    segments = []
    for i in range(hdr.e_phnum):
        off = hdr.e_phoff + i * hdr.e_phentsize
        chunk = data[off : off + 56]
        segments.append(Segment(
            p_type=struct.unpack_from("<I", chunk, 0)[0],
            p_flags=struct.unpack_from("<I", chunk, 4)[0],
            p_offset=struct.unpack_from("<Q", chunk, 8)[0],
            p_vaddr=struct.unpack_from("<Q", chunk, 16)[0],
            p_filesz=struct.unpack_from("<Q", chunk, 32)[0],
            p_memsz=struct.unpack_from("<Q", chunk, 40)[0],
        ))
    return segments


# ---- Objdump parsing (call-target function-boundary analysis) ---------------

@dataclass
class Instr:
    addr: int
    nbytes: int
    text: str


@dataclass
class Function:
    start: int
    size: int
    ninstrs: int
    name: str


def parse_objdump(text: str) -> tuple[list[Instr], int]:
    instrs = []
    text_start = 0
    for line in text.splitlines():
        m = re.match(r'^ *([0-9a-f]+):\s+([0-9a-f ]+)\s+(.*)', line)
        if m:
            addr = int(m.group(1), 16)
            hexbytes = m.group(2).strip()
            nb = len(bytes.fromhex(hexbytes)) if hexbytes else 0
            instrs.append(Instr(addr, nb, m.group(3)))
            if text_start == 0:
                text_start = addr
    return instrs, text_start


def find_functions(instrs: Sequence[Instr], text_start: int) -> list[Function]:
    targets = set()
    for ins in instrs:
        m = re.search(r'call\s+0x([0-9a-f]+)', ins.text)
        if m:
            t = int(m.group(1), 16)
            if t >= text_start:
                targets.add(t)

    boundaries = sorted({text_start} | targets)

    groups = {}
    for ins in instrs:
        func = text_start
        for b in reversed(boundaries):
            if b <= ins.addr:
                func = b
                break
        groups.setdefault(func, []).append(ins)

    return [
        Function(
            start=s,
            size=sum(i.nbytes for i in groups[s]),
            ninstrs=len(groups[s]),
            name="_start" if s == text_start else f"func_0x{s:x}",
        )
        for s in sorted(groups)
    ]


# ---- Size computation -------------------------------------------------------

def _sum_name(sections: Sequence[Section], names: list[str]) -> int:
    return sum(
        s.sh_size for s in sections
        if s.name in names and s.sh_type != SHT_NOBITS
    )


# ---- Main findings report ---------------------------------------------------

def _report_findings(
    data: bytes, sections: Sequence[Section], hdr: ElfHeader,
    func_lines: list[str] | None,
    write: Callable[[str], None],
):
    file_size = len(data)
    ehdr_size = 64
    phdr_size = hdr.e_phnum * hdr.e_phentsize
    text_size = _sum_name(sections, [".text"])
    rodata_size = _sum_name(sections, [".rodata"])
    eh_frame_size = _sum_name(sections, [".eh_frame", ".eh_frame_hdr"])
    shdr_size = hdr.e_shnum * hdr.e_shentsize
    shstrtab_size = _sum_name(sections, [".shstrtab"])
    comment_size = _sum_name(sections, [".comment"])

    accounted = (
        ehdr_size + phdr_size + text_size + rodata_size + eh_frame_size
        + shdr_size + shstrtab_size + comment_size
    )
    other = file_size - accounted

    write(f"  Main findings ({file_size} B):")
    write("")

    def _line(label, size, note=""):
        pct = size / file_size * 100
        padded = label.ljust(34)
        if note:
            write(f"  - {padded} {size:4d} B ({pct:3.0f}%)  — {note}")
        else:
            write(f"  - {padded} {size:4d} B ({pct:3.0f}%)")

    _line("ELF headers + PHDR", ehdr_size + phdr_size, "the OS loader tax")

    text_pct = text_size / file_size * 100
    write(f"  - .text (code)                     {text_size:4d} B ({text_pct:3.0f}%)"
          "  — actual machine code, broken into:")
    if func_lines:
        for line in func_lines:
            write(f"    {line}")
    else:
        write("    (run with --functions for per-function breakdown)")

    _line(".rodata (payloads)", rodata_size,
          "compiled D-Bus messages, SASL auth string, bus path")

    _line(".eh_frame / .eh_frame_hdr", eh_frame_size,
          "exception handling metadata (could be stripped)")

    _line("Section headers", shdr_size, "could be removed")
    _line(".shstrtab", shstrtab_size, "section name string table")
    _line(".comment", comment_size, "linker version info")

    if other:
        _line("Gap / page padding", other,
              "alignment waste (eliminated by strip)")


# ---- Function breakdown via objdump ----------------------------------------

def _function_report(elf_path, run, write):
    proc = run(["objdump", "-d", elf_path], capture_output=True, text=True)
    if proc.returncode != 0:
        write("    objdump failed")
        return []

    instrs, text_start = parse_objdump(proc.stdout)
    if not instrs:
        return []

    functions = find_functions(instrs, text_start)
    text_size = instrs[-1].addr + instrs[-1].nbytes - instrs[0].addr

    # Known function labels for yo.zig
    known = {
        0x1001564: ("_start entry", "ELF entry point, clears rbp, aligns stack"),
        0x1001572: ("Zig runtime init",
                     "aux-vector parsing, stack setup, mmap,"
                     " init_array dispatch, TLS, exit"),
        0x10017c5: ("main()",
                     "socket, connect, authenticate, sendMessage"
                     " x2, reply parsing"),
        0x1001900: ("sendMessage()", "write + read wrapper"),
        0x1001948: ("TLS init", "arch_prctl ARCH_SET_FS"),
        0x100197a: ("memset", ""),
        0x1001996: ("memcpy", ""),
    }

    lines = []
    for fn in functions:
        ratio = fn.size / text_size * 100
        label, desc = known.get(fn.start, (fn.name, ""))
        if desc:
            lines.append(f"{label:20s}  {fn.size:3d} B  ({ratio:3.0f}% of .text)"
                         f"  — {desc}")
        else:
            lines.append(f"{label:20s}  {fn.size:3d} B  ({ratio:3.0f}% of .text)")

    return lines


# ---- Entry point ------------------------------------------------------------

def main(argv: list[str], cwd, run, write: Callable[[str], None]) -> int:
    files = []
    functions_flag = False

    for a in argv[1:]:
        if a == "--functions":
            functions_flag = True
        elif a.startswith("--"):
            write(f"Unknown flag: {a}")
            return 2
        else:
            files.append(a)

    if not files:
        write("Usage: analyze.py [--functions] <elf> [<elf2>]")
        return 1

    datas = []
    for p in files:
        path = cwd / p
        datas.append(path.read_bytes())

    headers = [parse_elf_header(d) for d in datas]
    if any(h is None for h in headers):
        write("Not a valid ELF64 binary")
        return 1
    headers = [h for h in headers if h is not None]

    sections_list = [parse_sections(d, h) for d, h in zip(datas, headers)]

    for i in range(len(files)):
        func_lines = None
        if functions_flag and i == 0:
            func_lines = _function_report(files[0], run, write)
        write("")
        _report_findings(datas[i], sections_list[i], headers[i],
                         func_lines, write)

    if len(files) > 1:
        write("")
        pct = (len(datas[0]) - len(datas[1])) / len(datas[0]) * 100
        write(f"  Savings from strip:"
              f" {len(datas[0]) - len(datas[1]):4d} B ({pct:.0f}%)")
        write("  Strip packs non-loadable sections (.comment, .shstrtab,")
        write("  section-headers) into page 0 instead of page 1, removing")
        write("  ~1.6 KiB of page-alignment padding.")

    return 0


if __name__ == "__main__":
    def _script_io():
        import subprocess
        import sys
        from pathlib import Path

        def write(msg: str) -> None:
            sys.stdout.write(msg + "\n")

        return main(
            argv=list(sys.argv),
            cwd=Path.cwd(),
            run=subprocess.run,
            write=write,
        )
    raise SystemExit(_script_io())
