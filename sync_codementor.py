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
    '''Least-authority style filesystem access.
    '''
    def __init__(self, ops, path):
        (openf, ) = ops
        self.setBytes = lambda bs: openf(path, 'w').write(bs)

        def descendant(sub):
            d = path_join(path, sub)
            if not d.startswith(path):
                raise IOError('%s not under %s', d, path)
            return d

        self.subEdFile = lambda sub: Editable(ops, descendant(path, sub))

    def __div__(self, sub):
        return self.subEdFile(sub)

    @classmethod
    def mkArgEd(cls, argv, ops):
        '''Write access only to files/directories given on the command line.
        '''
        def argEd(arg_path):
            if arg_path not in argv:
                raise IOError(arg_path)
            return Editable(ops, arg_path)
        return argEd


@contextmanager
def event(ctx, msg, *args):
    log.info(''.join(ctx) + msg, *args)
    ctx.append(' > ')
    yield
    ctx.pop()
    log.info(''.join(ctx) + '... done.')


if __name__ == '__main__':
    def _invoked_as_script():
        '''Access privileged APIs and give main() the least authority it needs.

        .. note:: Privileged APIs are not visible outside this
                  function, and they are accessed only if this file is
                  called as a script, not when imported as a module.

        '''
        from __builtin__ import open as openf
        from sys import argv
        from logging import basicConfig
        from mechanize import Browser

        main(argv[:],
             mkBrowser=lambda: Browser(),
             argEd=Editable.mkArgEd(argv, (openf, )),
             basicConfig=basicConfig)

    _invoked_as_script()
