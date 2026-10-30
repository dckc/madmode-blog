"""Pour CSL-JSON into the XHTML bibliography conventions of xhlt91.

https://www.w3.org/2004/04/xhlt91/ : a <dl class="bib">; each <dt> has
the BibTeX entry type as its class and the citation key as its id; the
<dd> holds a <cite> for the title (with a link) and direct children
classed by BibTeX field name (author, journal, year, ...). Humans read
the page; xh2bib.xsl can still get BibTeX out of it.
"""

from dataclasses import dataclass

# CSL type -> BibTeX entry type; anything else is misc.
BIBTEX_TYPE = {
    "article-journal": "article",
    "article-magazine": "article",
    "article-newspaper": "article",
    "book": "book",
    "chapter": "incollection",
    "paper-conference": "inproceedings",
    "report": "techreport",
    "thesis": "phdthesis",
}


@dataclass(frozen=True)
class Part:
    """One piece of an entry: text between `before` and `after`, classed by BibTeX field.
    The title is the `cite` part, linked when there's a URL."""
    cls: str
    text: str
    before: str = ", "
    after: str = ""
    href: str | None = None


@dataclass(frozen=True)
class BibEntry:
    key: str
    bibtype: str
    year: str
    date_rest: str
    parts: tuple[Part, ...]

    @property
    def end(self) -> str:
        """Close with a period, unless the last part already did (e.g. "Ltd.")."""
        last = self.parts[-1]
        return "" if (last.text + last.after).endswith(".") else "."


def publishable(entry: dict) -> dict:
    """Working notes ("TODO: …", "placeholder …") stay in the repo; finished notes go public."""
    note = entry.get("note", "")
    if note.startswith(("TODO", "placeholder")):
        return {k: v for k, v in entry.items() if k != "note"}
    return entry


def names(people: list[dict]) -> str:
    full = [p.get("literal") or f"{p.get('given', '')} {p.get('family', '')}".strip()
            for p in people]
    if len(full) > 3:
        return f"{full[0]} et al."
    if full[-1] == "et al.":
        return f"{', '.join(full[:-1])} et al."
    return full[0] if len(full) == 1 else f"{', '.join(full[:-1])} and {full[-1]}"


def iso_date(issued: dict) -> tuple[str, str]:
    """Year, plus the rest of the ISO date (e.g. "-03-17"), as given: month and day are optional."""
    year, *rest = issued["date-parts"][0]
    return str(year), "".join(f"-{n:02d}" for n in rest)


def legal_case_parts(e: dict) -> list[Part]:
    """Case citation order: title, volume reporter page (court)."""
    parts = []
    if "volume" in e:
        parts += [Part("volume", e["volume"]),
                  Part("journal", e.get("container-title", ""), before=" "),
                  Part("pages", e.get("page", ""), before=" ")]
    elif "number" in e:
        parts.append(Part("number", e["number"], before=", No. "))
    if "authority" in e and e.get("container-title") != "U.S.":  # U.S. Reports: Supreme Court goes without saying
        parts.append(Part("institution", e["authority"], before=" (", after=")"))
    return parts


def entry_parts(e: dict) -> tuple[Part, ...]:
    head = [Part("author", names(e["author"]), before="")] if "author" in e else []
    title = Part("cite", e["title"], before=", " if head else "", href=e.get("URL"))
    if e["type"] == "legal_case":
        tail = legal_case_parts(e)
    else:
        container = "booktitle" if e["type"] in ("paper-conference", "chapter") else "journal"
        fields = [
            ("editor", names(e["editor"]) + ", ed." if "editor" in e else None),
            (container, e.get("container-title")),
            ("series", e.get("collection-title")),
            ("publisher", e.get("publisher")),
            ("type", e.get("genre")),
            ("number", e.get("number")),
            ("volume", e.get("volume")),
            ("pages", e.get("page")),
            ("address", e.get("event-place") or e.get("publisher-place")),
        ]
        tail = [Part(cls, text) for cls, text in fields if text]
    note = [Part("note", e["note"], before=" (", after=")")] if "note" in e else []
    return tuple(head + [title] + tail + note)


def bib_entries(csl: list[dict]) -> list[BibEntry]:
    out = []
    for e in map(publishable, csl):
        year, date_rest = iso_date(e["issued"])
        out.append(BibEntry(e["id"], BIBTEX_TYPE.get(e["type"], "misc"),
                            year, date_rest, entry_parts(e)))
    return out
