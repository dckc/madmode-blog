"""ELF binary size analyzer — sections, functions, strip comparison.

Reports how every byte of an ELF executable is used.  Supports
comparing two files (e.g. unstripped vs stripped).

Function-boundary analysis uses objdump call-target parsing;
per-function labels and descriptions are hardcoded for a specific
Zig binary (yo.zig) and are not generally applicable.

ELF structures follow the ELF Specification v1.2, 2001-05, TIS Committee.
https://refspecs.linuxfoundation.org/elf/elf-spec.pdf
"""

# Parse logic is pure: takes bytes, returns structures.  All I/O
# authority (file reading, subprocess, output) is injected.

from __future__ import annotations

import re
import struct
from dataclasses import dataclass
from typing import Iterator, Sequence


@dataclass
class ElfHeader:
    # ELF constants from the ELF Specification v1.2, §4-7.
    ELFMAG = b"\x7fELF"
    CLASS64 = 2
    DATA2LSB = 1

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

    @classmethod
    def parse(cls, data: bytes) -> ElfHeader | None:
        if len(data) < 64 or data[:4] != cls.ELFMAG:
            return None
        if data[4] != cls.CLASS64 or data[5] != cls.DATA2LSB:
            return None
        return cls(
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


@dataclass
class Section:
    SHT_NOBITS = 8

    name: str
    sh_type: int
    sh_offset: int
    sh_size: int

    @classmethod
    def parse_sections(cls, data: bytes, hdr: ElfHeader) -> list[Section]:
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
                struct.unpack_from("<Q", chunk, 24)[0],
                struct.unpack_from("<Q", chunk, 32)[0],
            ))
            if i == hdr.e_shstrndx:
                strtab_off = struct.unpack_from("<Q", chunk, 24)[0]
                strtab_size = struct.unpack_from("<Q", chunk, 32)[0]
        sections = []
        for name_off, stype, soff, ssize in raw:
            name = ""
            if strtab_off and name_off < strtab_size:
                end = data.index(b"\0", strtab_off + name_off)
                name = data[strtab_off + name_off : end].decode("ascii", errors="replace")
            sections.append(cls(
                name=name,
                sh_type=stype,
                sh_offset=soff,
                sh_size=ssize,
            ))
        return sections

    @classmethod
    def sum_name(cls, sections: Sequence[Section], names: list[str]) -> int:
        return sum(
            s.sh_size for s in sections
            if s.name in names and s.sh_type != cls.SHT_NOBITS
        )


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


def _report_findings(
    data: bytes, sections: Sequence[Section], hdr: ElfHeader,
    func_lines: list[str] | None,
) -> Iterator[str]:
    file_size = len(data)
    ehdr_size = 64
    phdr_size = hdr.e_phnum * hdr.e_phentsize
    text_size = Section.sum_name(sections, [".text"])
    rodata_size = Section.sum_name(sections, [".rodata"])
    eh_frame_size = Section.sum_name(sections, [".eh_frame", ".eh_frame_hdr"])
    shdr_size = hdr.e_shnum * hdr.e_shentsize
    shstrtab_size = Section.sum_name(sections, [".shstrtab"])
    comment_size = Section.sum_name(sections, [".comment"])

    accounted = (
        ehdr_size + phdr_size + text_size + rodata_size + eh_frame_size
        + shdr_size + shstrtab_size + comment_size
    )
    other = file_size - accounted

    yield f"  Main findings ({file_size} B):"
    yield ""

    def _line(label: str, size: int, note: str = "") -> str:
        pct = size / file_size * 100
        padded = label.ljust(34)
        if note:
            return f"  - {padded} {size:4d} B ({pct:3.0f}%)  — {note}"
        else:
            return f"  - {padded} {size:4d} B ({pct:3.0f}%)"

    yield _line("ELF headers + PHDR", ehdr_size + phdr_size, "the OS loader tax")

    text_pct = text_size / file_size * 100
    yield (f"  - .text (code)                     {text_size:4d} B ({text_pct:3.0f}%)"
           "  — actual machine code, broken into:")
    if func_lines:
        for line in func_lines:
            yield f"    {line}"
    else:
        yield "    (run with --functions for per-function breakdown)"

    yield _line(".rodata (payloads)", rodata_size,
                "compiled D-Bus messages, SASL auth string, bus path")

    yield _line(".eh_frame / .eh_frame_hdr", eh_frame_size,
                "exception handling metadata (could be stripped)")

    yield _line("Section headers", shdr_size, "could be removed")
    yield _line(".shstrtab", shstrtab_size, "section name string table")
    yield _line(".comment", comment_size, "linker version info")

    if other:
        yield _line("Gap / page padding", other,
                     "alignment waste (eliminated by strip)")


def _function_report(elf_path, run) -> list[str]:
    proc = run(["objdump", "-d", elf_path], capture_output=True, text=True)
    if proc.returncode != 0:
        return ["    objdump failed"]

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


def _compose_report(
    files: list[str],
    datas: list[bytes],
    headers: list[ElfHeader],
    sections_list: list[list[Section]],
    functions_flag: bool,
    run,
) -> Iterator[str]:
    for i in range(len(files)):
        func_lines = None
        if functions_flag and i == 0:
            func_lines = _function_report(files[0], run)
        yield ""
        yield from _report_findings(datas[i], sections_list[i], headers[i],
                                    func_lines)

    if len(files) > 1:
        yield ""
        pct = (len(datas[0]) - len(datas[1])) / len(datas[0]) * 100
        yield (f"  Savings from strip:"
               f" {len(datas[0]) - len(datas[1]):4d} B ({pct:.0f}%)")
        yield ("  Strip packs non-loadable sections (.comment, .shstrtab,")
        yield ("  section-headers) into page 0 instead of page 1, removing")
        yield ("  ~1.6 KiB of page-alignment padding.")


def main(argv: list[str], cwd, run, stdout) -> int:
    files: list[str] = []
    functions_flag = False

    for a in argv[1:]:
        if a == "--functions":
            functions_flag = True
        elif a.startswith("--"):
            print(f"Unknown flag: {a}", file=stdout)
            return 2
        else:
            files.append(a)

    if not files:
        print("Usage: analyze.py [--functions] <elf> [<elf2>]", file=stdout)
        return 1

    datas = []
    for p in files:
        path = cwd / p
        datas.append(path.read_bytes())

    headers = [ElfHeader.parse(d) for d in datas]
    if any(h is None for h in headers):
        print("Not a valid ELF64 binary", file=stdout)
        return 1
    headers_list: list[ElfHeader] = [h for h in headers if h is not None]

    sections_list = [Section.parse_sections(d, h)
                     for d, h in zip(datas, headers_list)]

    for line in _compose_report(files, datas, headers_list, sections_list,
                                functions_flag, run):
        print(line, file=stdout)

    return 0


if __name__ == "__main__":
    def _script_io() -> int:
        import subprocess
        import sys
        from pathlib import Path

        return main(
            argv=list(sys.argv),
            cwd=Path.cwd(),
            run=subprocess.run,
            stdout=sys.stdout,
        )
    raise SystemExit(_script_io())
