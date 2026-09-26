'''

Render ZWiki pages to HTML, without starting Zope.

Where zout2.py dumps each object's raw `data`/`raw`, this asks ZWiki itself to
render. ZWikiPage.render() dispatches on the page's page_type (e.g.
'structuredtext' -> Products/ZWiki/pagetypes/stx.py), which formats the wiki
markup and resolves WikiWord/InterWiki links. `bare=1` skips the site skin
(standard_wiki_header/footer), which needs an authenticated REQUEST.

Needs the ZWiki product installed in the instance (see `make products`).

Usage:

    # every ZWikiPage under a store path
    INSTANCE_HOME=/tmp/zope-instance zrender.py z2001 /tmp/out

    # one recovered source file (e.g. the 2008 bzr export, whose text is
    # HTML-entity-escaped, so it is unescaped first)
    INSTANCE_HOME=/tmp/zope-instance zrender.py --file SOURCE /tmp/out [NAME]

Follows the DisciplinedPython style guide: helpers receive narrow
capabilities, never ambient filesystem or environment authority.
'''

import htmlentitydefs
import logging
import posixpath
import re

log = logging.getLogger(__name__)

# The site name used in the archived pages' <title>, e.g.
# "dm93 TheOriginalHypertext". Policy data, not authority.
SITE_NAME = 'dm93'


class RootedPath(object):
    """A minimal pathlib-like capability rooted at one location.

    Python 2.3 has no pathlib, so this supports only the operations this
    script needs: joining a name, creating the directory, reading a source
    file, and writing rendered HTML. The filesystem primitives are held
    privately, so a holder of a RootedPath cannot recover broad filesystem
    authority.
    """

    def __init__(self, location, open_file, make_dir, path_exists):
        self.__location = location
        self.__open_file = open_file
        self.__make_dir = make_dir
        self.__path_exists = path_exists

    def join(self, name):
        return RootedPath(posixpath.join(self.__location, name),
                          self.__open_file, self.__make_dir, self.__path_exists)

    __div__ = join
    __truediv__ = join

    def ensure_dir(self):
        if not self.__path_exists(self.__location):
            self.__make_dir(self.__location)

    def read_bytes(self):
        stream = self.__open_file(self.__location, 'rb')
        try:
            return stream.read()
        finally:
            stream.close()

    def write_bytes(self, data):
        stream = self.__open_file(self.__location, 'wb')
        try:
            stream.write(data)
        finally:
            stream.close()

    def __str__(self):
        return self.__location

    def __repr__(self):
        return 'RootedPath(%r)' % self.__location


def unescape(text):
    """Undo the HTML entity escaping the filesystem export applied to source."""
    def _entity(match):
        name = match.group(1)
        if name.startswith('#'):
            return unichr(int(name[1:]))
        return htmlentitydefs.entitydefs.get(name, match.group(0))
    return re.sub(r'&(#?[0-9A-Za-z]+);', _entity, text)


def parse_args(args):
    """Turn command-line designations into (mode, source, dest_name, name)."""
    if args and args[0] == '--file':
        source = args[1]
        dest_name = args[2]
        if len(args) > 3:
            name = args[3]
        else:
            name = posixpath.basename(source)
        return ('file', source, dest_name, name)
    return ('tree', args[0], args[1], None)


def render_page(page):
    """Render one ZWikiPage; return its HTML, or None if rendering fails."""
    try:
        return page.render(bare=1)
    except Exception, error:
        log.warning('skipping %s: %s', page.id(), error)
        return None


def render_file(page_type, context, text, name):
    """Render recovered source text as the page named `name`."""
    page = page_type(text, __name__=name).__of__(context)
    return render_page(page)


def render_tree(page_type, context, store_path):
    """Render every page at or under a store path; yield (id, HTML) pairs."""
    obj = context.unrestrictedTraverse(store_path)

    if isinstance(obj, page_type):
        html = render_page(obj)
        if html is not None:
            yield obj.id(), html
        return

    for id_, child in obj.objectItems():
        if isinstance(child, page_type):
            html = render_page(child)
            if html is not None:
                yield id_, html
        else:
            log.debug('not a %s: %s (%s)', page_type.__name__, id_,
                      child.__class__.__name__)


def wrap_page(name, html):
    """Wrap a bare page body in a minimal document naming the site and page."""
    return (
        '<!DOCTYPE html>\n'
        '<html>\n<head>\n'
        '<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />\n'
        '<title>%s %s</title>\n'
        '</head>\n<body>\n'
        '<h1>%s</h1>\n'
        '%s'
        '</body>\n</html>\n'
    ) % (SITE_NAME, name, name, html)


def write_page(dest_path, name, html):
    """Write one rendered page to dest_path/<name>.html."""
    out = dest_path / ('%s.html' % name)
    document = wrap_page(name, html)
    out.write_bytes(document)
    log.info('%8d bytes: %s', len(document), out)


def main(argv, cwd, environ, open_file, make_dir, path_exists, configure, app):
    logging.basicConfig()
    log.setLevel(logging.INFO)

    mode, source, dest_name, name = parse_args(argv)

    root = RootedPath(cwd, open_file, make_dir, path_exists)
    dest = root / dest_name
    dest.ensure_dir()

    conf = posixpath.join(environ['INSTANCE_HOME'], 'etc', 'zope.conf')
    configure(conf)
    wiki_root = app()

    # ZWiki lives in $INSTANCE/Products, importable only after configure().
    from Products.ZWiki.ZWikiPage import ZWikiPage
    context = wiki_root.unrestrictedTraverse('z2001')

    if mode == 'file':
        text = unescape((root / source).read_bytes())
        html = render_file(ZWikiPage, context, text, name)
        if html is not None:
            write_page(dest, name, html)
    else:
        for id_, html in render_tree(ZWikiPage, context, source):
            write_page(dest, id_, html)


if __name__ == '__main__':
    def _script_io():
        from os import environ, getcwd, mkdir
        from os.path import exists
        from sys import argv
        from Zope import configure, app

        args = list(argv[1:])
        del argv[:]  # Zope's startup parses the process argv
        return main(
            argv=args,
            cwd=getcwd(),
            environ=dict(environ),
            open_file=open,
            make_dir=mkdir,
            path_exists=exists,
            configure=configure,
            app=app,
        )

    raise SystemExit(_script_io())
