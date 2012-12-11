
from datetime import datetime


def main():
    import sys
    import os
    src, dest = sys.argv[1:3]
    j = Journal(src,
                os.listdir, os.path.join,
                os.path.getmtime, open)
    mkpages(dest, j, os.path.join, open)


def mkpages(dest, j, join, open):
    for name, when, what in j:
        where = join(dest, name[:-len('.html')] + '.md')
        out = open(where, 'w')
        title = when.date().ctime()
        date = str(when.date())
        out.write('title: %s\ndate: %s\npublished: true\n\n %s' % (
            title, date, what))


class Journal(object):
    def __init__(self, path, listdir, join, getmtime, open):
        self.path = path
        self.__listdir = listdir
        self.__getmtime = getmtime
        self.__join = join
        self.__open = open

    def __iter__(self):
        for n in self.__listdir(self.path):
            if not n.endswith('.html'):
                continue
            where = self.__join(self.path, n)
            mtsec = self.__getmtime(where)
            when = datetime.fromtimestamp(mtsec)
            what = self.__open(where).read()
            yield (n, when, what)


if __name__ == '__main__':
    main()
