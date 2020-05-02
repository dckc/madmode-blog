'''Reverse-syndicate articles published via Codementor.io

Usage:
  sync_codementor [--debug] USERNAME DEST_DIR

Options:
--debug  verbose logging

'''

import logging
from posixpath import join as path_join
from contextlib import contextmanager

import docopt
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)


def main(argv, mkBrowser, argEd, basicConfig):
    cli = docopt.docopt(__doc__, argv[1:])

    basicConfig(level=logging.DEBUG if '--debug' in cli
                else logging.INFO)

    profile = Profile(cli['USERNAME'], ua=mkBrowser())
    profile.download_articles([], argEd(cli['DEST_DIR']))


class Profile(object):
    def __init__(self, username, ua,
                 site='https://www.codementor.io/'):
        self.username = username
        profile_addr = site + username

        # define these here to limit scope of ua.
        def go_home(ctx):
            with event(ctx, 'Visiting site homepage: %s ...', site):
                ua.open(site)
        self.go_home = go_home

        def read_profile(ctx):
            with event(ctx, 'opening profile: %s', profile_addr):
                return ua.open(profile_addr).read()
        self.read_profile = read_profile

        def get_articles(ctx):
            for parts in self.find_articles(ctx):
                addr, item_id, slug, _title, _abstract, _tags = parts
                with event(ctx, 'getting item: %s', slug):
                    log.debug('article parts: %s', [parts])
                    content = ua.open(addr).read()
                yield item_id, slug, content
        self.get_articles = get_articles

    def find_articles(self, ctx):
        profile_text = self.read_profile(ctx)
        profile_doc = BeautifulSoup(profile_text)
        return [self.article_parts(a.attrs['href'], listing)
                for listing in profile_doc.select('.help-listing')
                for a in listing.select('h4 > a')]

    @classmethod
    def article_parts(cls, addr, summary):
        item_id, slug = addr.split('/')[-2:]
        text = lambda nodes: ''.join(e.text for e in nodes)
        title = text(summary.select('h4'))
        abstract = text(summary.select('p'))
        tags = [e.text.strip() for e in summary.select('.tags')]
        return addr, item_id, slug, title, abstract, tags

    def download_articles(self, ctx, dest_dir):
        with event(ctx, 'downloading articles by %s', self.username):
            for item_id, _slug, content in self.get_articles(ctx):
                dest = dest_dir / (item_id + '.html')
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

        self.subEdFile = lambda sub: Editable(ops, descendant(sub))

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
    log.debug(''.join(ctx) + '... done.')


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
