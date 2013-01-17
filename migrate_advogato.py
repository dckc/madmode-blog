
from datetime import datetime  # not easy to tame .now(); darn
import re


def page_saver(openw, pfx='advogato_'):
    def save(name, title, date, what, tags=()):
        out = openw(date[:4], pfx + name[:-len('.html')] + '.md')
        out.write(MARKDOWN_YAML_TEMPLATE % (title, date, tags, what))
    return save

MARKDOWN_YAML_TEMPLATE = '''
title: %s
date: %s
tags: %s
published: true

%s'''.strip()


def mkpages(j, save):
    for name, when, what in j:
        m = TITLE_PATTERN.match(what.strip())
        if m:
            title = m.group('title')
            title = ' '.join(title.split())
        else:
            title = when.date().strftime('%d %b %Y')

        date = str(when.date())
        save(name, title, date, what, tags=rel_tag(what))


TITLE_PATTERN = re.compile(
    r'^<(?:b|strong)[^>]*>(?P<title>[^<]+)</(?:b|strong)>',
    flags=re.MULTILINE)


def rel_tag(markup):
    r'''
    >>> rel_tag('<a rel="tag" href="http://del.icio.us/connolly/scm">')
    ['scm']

    >>> rel_tag('<a rel="tag" href="http://groups.csail.mit.edu/dig/">')
    []

    Cheating:
    >>> rel_tag("<a href='http://delicious.com/connolly/programming'>")
    ['programming']
    '''
    # [('text..', 'a', 'href=...'), ...]
    tags = [tuple(([txt] + tag.split(' ', 1) + [None])[:3])
            for txt, tag
            in [t.split('<', 1) for t in markup.split(">") if '<' in t]]

    links = [rest for txt, n, rest in tags
             if n == 'a' and ('rel="tag"' in rest or
                              "rel='tag'" in rest
                              or 'http://delicious.com/connolly/' in rest)]
    tags = [ref.split('/')[-1]
             for ref in 
             [m.group('ref')
              for m in [REF_PATTERN.search(txt) for txt in links]
              if m]]
    return [tag for tag in tags if tag]  # prune empty tags


REF_PATTERN = re.compile(
    r'''href=['"](?P<ref>[^'"]+)["']''')


class Journal(object):
    def __init__(self, listdir, what_when):
        self.__listdir = listdir
        self.__what_when = what_when

    def __iter__(self):
        for n in self.__listdir():
            if not n.endswith('.html'):
                continue
            what, mtsec = self.__what_when(n)
            when = datetime.fromtimestamp(mtsec)
            yield (n, when, what)


if __name__ == '__main__':
    def _initial_caps():
        import sys
        import os
        from os import path
        src, dest = sys.argv[1:3]

        def what_when(n):
            where = path.join(src, n)
            return open(where).read(), path.getmtime(where)

        def mkf(yyyy, name):
            d = os.path.join(dest, yyyy)
            if not path.exists(d):
                os.mkdir(d)
            return open(os.path.join(dest, yyyy, name), 'w')

        return dict(j=Journal(lambda: os.listdir(src), what_when),
                    save=page_saver(mkf))

    mkpages(**_initial_caps())
