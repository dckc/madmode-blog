'''

Usage:
  sync_codementor USERNAME DEST_DIR

Options:
--debug  verbose logging

e.g.
https://www.codementor.io/tips/8242643197/how-to-read-time-with-scanf-in-c
'''

import logging
from posixpath import join as path_join
from contextlib import contextmanager

import docopt
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)


def main(argv, mkBrowser, argEd, basicConfig,
         site='https://www.codementor.io/'):
    cli = docopt.docopt(__doc__, argv[1:])

    basicConfig(level=logging.DEBUG if '--debug' in cli
                else logging.INFO)

    ctx = []
    ua = mkBrowser()
    dest_dir = argEd(cli['DEST_DIR'])
    username = cli['USERNAME']
    with event(ctx, 'sync codementor articles by %s', username):
        with event(ctx, 'Visiting site homepage: %s ...', site):
            ua.open(site)

        download_tips(site, username, ctx, ua, dest_dir)


def download_tips(site, username, ctx, ua, dest_dir):
    profile_addr = site + username
    with event(ctx, 'opening profile: %s', profile_addr):
        profile_text = ua.open(profile_addr).read()
    profile_doc = BeautifulSoup(profile_text)
    article_addrs = [a.attrs['href']
                     for a in profile_doc.select('h4 > a')]
    for addr in article_addrs:
        download(ctx, dest_dir, ua, addr)


def download(ctx, dest_dir, ua, addr):
    item_id, slug = addr.split('/')[-2:]
    dest = dest_dir / (item_id + '.html')
    with event(ctx, 'downloading: %s/%s', item_id, slug):
        content = ua.open(addr).read()
    dest.setBytes(content)


class Editable(object):
    def __init__(self, opts, path):
        (openf, ) = opts
        self.setBytes = lambda bs: openf(path, 'w').write(bs)
        self.subEdFile = lambda sub: Editable(opts, path_join(path, sub))

    def __div__(self, sub):
        return self.subEdFile(sub)


@contextmanager
def event(ctx, msg, *args):
    log.info(''.join(ctx) + msg, *args)
    ctx.append(' > ')
    yield
    ctx.pop()
    log.info(''.join(ctx) + '... done.')


if __name__ == '__main__':
    def _privileged_main():
        from __builtin__ import open as openf
        from sys import argv
        from mechanize import Browser

        def argEd(arg_path):
            if arg_path not in argv:
                raise IOError(arg_path)
            return Editable((openf, ), arg_path)

        main(argv[:],
             mkBrowser=lambda: Browser(),
             argEd=argEd,
             basicConfig=logging.basicConfig)

    _privileged_main()
