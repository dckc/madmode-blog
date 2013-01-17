
from datetime import datetime  # not easy to tame .now(); darn


def page_saver(openw):
    def save(name, title, date, what):
        out = openw(name[:-len('.html')] + '.md')
        out.write(MARKDOWN_YAML_TEMPLATE % (title, date, what))
    return save

MARKDOWN_YAML_TEMPLATE = '''
title: %s
date: %s
published: true

%s'''.strip()


def mkpages(j, save):
    for name, when, what in j:
        title = when.date().ctime()
        date = str(when.date())
        save(name, title, date, what)


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

        return dict(j=Journal(lambda:
                                  os.listdir(src), what_when),
                    save=page_saver(lambda name:
                                        open(os.path.join(dest, name), 'w')))

    mkpages(**_initial_caps())
