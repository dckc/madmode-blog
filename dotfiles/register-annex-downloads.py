#!/usr/bin/env python3
"""
register-annex-downloads

Usage:
    register-annex-downloads copied-history.sqlite *.tar.gz *.zip ...

For each file:
  - look up its git-annex key
  - get expected size from the annex key, when possible
  - search Chromium/Brave downloads tables first
  - match by basename and, when available, total_bytes
  - register matching download URLs with git-annex
"""

# TODO: Consider a --json mode that emits git-annex-like result records to stdout.

import argparse
import logging
import re
from subprocess import CalledProcessError


def parse_args(argv, to_path):
    ap = argparse.ArgumentParser()
    ap.add_argument("history_db", type=to_path)
    ap.add_argument("files", nargs="+", type=to_path)
    ap.add_argument("-n", "--dry-run", action="store_true")
    ap.add_argument("--fallback-urls-table", action="store_true")
    return ap.parse_args(argv[1:])


class MissingFile(Exception):
    pass


class NotAnnexed(Exception):
    pass


class GitAnnexLookup:
    __size_re = re.compile(r"-s(\d+)--")

    def __init__(self, run):
        self.__run = run

    def __annex_output(self, args):
        cmd = ["git", "annex", *args]
        completed = self.__run(cmd, check=True, text=True, capture_output=True)
        return completed.stdout.strip()

    def lookup_key(self, path):
        return self.__annex_output(["lookupkey", path])

    @classmethod
    def size_from_key(cls, key):
        m = cls.__size_re.search(key)
        return int(m.group(1)) if m else None


class LoggingRegisterUrl:
    @staticmethod
    def command(key, url):
        return ["git", "annex", "registerurl", key, url]

    def register_url(self, key, url):
        cmd = self.command(key, url)
        cmd_text = " ".join(repr(part) if " " in part else part for part in cmd)
        logging.info("+ %s", cmd_text)


class GitAnnexRegisterUrl(LoggingRegisterUrl):
    def __init__(self, run):
        self.__run = run

    def register_url(self, key, url):
        super().register_url(key, url)
        self.__run(self.command(key, url), check=True)


class DownloadHistory:
    download_urls_query = """
    select distinct
           d.target_path,
           d.total_bytes,
           d.received_bytes,
           c.url
    from downloads d
    join downloads_url_chains c
      on d.id = c.id
    where d.target_path like ?
       or c.url like ?
    order by d.start_time desc, c.chain_index asc
    """

    visit_urls_query = """
    select distinct url
    from urls
    where url like ?
    order by last_visit_time desc
    """

    def __init__(self, conn):
        self.__conn = conn

    def download_urls(self, filename, expected_size=None):
        cur = self.__conn.cursor()
        like = f"%{filename}%"
        cur.execute(self.download_urls_query, (like, like))

        rows = []
        for target_path, total_bytes, received_bytes, url in cur.fetchall():
            size_ok = (
                expected_size is None
                or total_bytes in (None, 0, expected_size)
                or received_bytes == expected_size
            )
            if size_ok:
                rows.append((url, target_path, total_bytes, received_bytes))

        return rows

    def visit_urls(self, filename):
        cur = self.__conn.cursor()
        cur.execute(self.visit_urls_query, (f"%{filename}%",))
        return [row[0] for row in cur.fetchall()]


def register_download_matches(registrar, key, matches):
    seen = set()
    for url, target_path, total_bytes, received_bytes in matches:
        if url in seen:
            continue
        seen.add(url)
        logging.info("download: %s", target_path)
        logging.info("bytes:    total=%s received=%s", total_bytes, received_bytes)
        logging.info("url:      %s", url)
        registrar.register_url(key, url)


def register_downloads(
    file,
    annex,
    registrar,
    history,
    fallback_urls_table=False,
):
    logging.info("== %s", file)
    if not file.exists():
        raise MissingFile(file)

    try:
        key = annex.lookup_key(file)
    except CalledProcessError:
        raise NotAnnexed(file)

    expected_size = GitAnnexLookup.size_from_key(key)
    actual_size = file.stat().st_size
    logging.info("key:  %s", key)
    logging.info("size: file=%s annex=%s", actual_size, expected_size)

    if expected_size is not None and actual_size != expected_size:
        logging.warning("file size does not match annex key size: %s", file)

    matches = history.download_urls(file.name, expected_size)
    if matches:
        register_download_matches(registrar, key, matches)
        return

    logging.info("no matching downloads rows")
    if not fallback_urls_table:
        return

    urls = history.visit_urls(file.name)
    if not urls:
        logging.info("no matching urls rows")
        return

    for url in urls:
        logging.info("url fallback: %s", url)
        registrar.register_url(key, url)


def main(argv, cwd, connect, run):
    args = parse_args(argv, lambda argument: cwd / argument)
    annex = GitAnnexLookup(run)
    registrar = LoggingRegisterUrl() if args.dry_run else GitAnnexRegisterUrl(run)
    conn = connect(args.history_db)
    history = DownloadHistory(conn)

    try:
        for path in args.files:
            try:
                register_downloads(
                    path,
                    annex,
                    registrar,
                    history,
                    fallback_urls_table=args.fallback_urls_table,
                )
            except MissingFile:
                logging.error("missing: %s", path)
            except NotAnnexed:
                logging.error("not annexed: %s", path)
    finally:
        conn.close()

    return 0


if __name__ == "__main__":

    def _script_io():
        from pathlib import Path
        import sqlite3
        import subprocess
        import sys

        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

        return main(
            argv=list(sys.argv),
            cwd=Path.cwd(),
            connect=sqlite3.connect,
            run=subprocess.run,
        )

    raise SystemExit(_script_io())
