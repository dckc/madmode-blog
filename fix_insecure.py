import logging
import re

log = logging.getLogger(__name__)


def main(stdin, cwd, urlopener):
    web = WebCheck(urlopener)
    pages = Pages(cwd / 'pages')

    for page, img in grok(stdin):
        doc = pages.doc(page)
        if not doc.exists():
            log.warn('cannot find doc for %s at %s', path, str(doc))
            continue
        if img not in doc.open().read():
            # assume we did it on a previous pass
            continue
        for addr in [img, re.sub('^http:', 'https:', img)]:
            try:
                dest = web.geturl(addr)
            except Exception as lose:
                log.warn('cannot geturl for %s: %s', addr, lose)
            else:
                if dest == img or not dest.startswith('https:'):
                    continue
                pages.edit(doc, img, dest)


def grok(lines):
    path = None
    urls = None

    for line in lines:
        m = re.search(r'Mixed content detected in: (?P<path>.*)', line)
        if m:
            path = m.group('path')
        elif '--> insecure img urls:' in line:
            pass
        else:
            m = re.search(r'  - (?P<url>http.*)', line)
            if m:
                url = m.group('url')
                yield path, url


class WebCheck(object):
    def __init__(self, urlopener):
        self.__urlopener = urlopener

    def geturl(self, img):
        log.info('opening %s ...', img)
        # addr = img.replace('http:', 'https:')
        response = self.__urlopener.open(img)
        return response.geturl()


class Pages(object):
    def __init__(self, store):
        self.__store = store

    def doc(self, path):
        store = self.__store
        tail = re.sub('^/', '', path)
        return (store / tail).with_suffix('.md')

    @classmethod
    def edit(cls, doc, target, replacement):
        with doc.open('rb+') as fp:
            content = fp.read().replace(target, replacement)
            fp.seek(0)
            fp.write(content)
            log.info('edited %s', doc)


class Path(object):
    def __init__(self, here,
                 open, joinpath, exists):
        self.path = here
        self.exists = lambda: exists(here)
        self.open = lambda mode='rb': open(here, mode=mode)
        make = lambda there: Path(there, open, joinpath, exists)
        self.joinpath = lambda other: make(joinpath(here, other))
        self.with_suffix = lambda suffix: make(here.rsplit('.', 1)[0] + suffix)

    def __repr__(self):
        return self.path

    def __div__(self, other):
        return self.joinpath(other)


if __name__ == '__main__':
    def _script():
        from io import open as io_open
        from sys import stdin
        from os.path import join as joinpath, exists
        from urllib2 import build_opener

        logging.basicConfig(level=logging.DEBUG)

        cwd = Path('.',
                   io_open, joinpath, exists)

        main(stdin, cwd, build_opener())

    _script()
