
import xml.etree.ElementTree as ET
import datetime

import yaml


def main():
    import sys
    import os
    blogger_atom_filename, dest_path = sys.argv[1:3]
    dest = MarkDownAssets(dest_path, os, open)
    migrate(open(blogger_atom_filename), dest)


class MarkDownAssets(object):
    def __init__(self, base, os, open,
                 pfx='http://www.madmode.com/'):
        self.base = base
        self.os = os
        self.open = open
        self.pfx = pfx

    def store(self, id_, addr, title, content, published, updated, tags):
        out = self.mkdest(id_, addr)

        out.write(yaml.dump(dict(
            title=title,
            published=(True if addr else False),
            date=published,
            updated=updated,
            tags=tags)))
        out.write('\n\n')
        if content:
            out.write(content.encode('utf-8'))
        out.close()

    def mkdest(self, id_, addr):
        os = self.os
        if addr:
            if not addr.startswith(self.pfx):
                raise ValueError(addr)
            path = addr[len(self.pfx):]
        else:
            path = id_

        if path.endswith('.html'):
            path = path[:-len('.html')]
        path = path + '.md'

        path = os.path.join(self.base, path)
        d = os.path.dirname(path)
        if not os.path.exists(d):
            os.makedirs(d)

        out = self.open(path, 'w')
        return out


def migrate(srcfp, dest):
    tree = ET.parse(srcfp)
    root = tree.getroot()

    atom = 'http://www.w3.org/2005/Atom'
    kind = 'http://schemas.google.com/blogger/2008/kind'
    ns = 'http://www.blogger.com/atom/ns#'

    for entry in root.iter('{%s}entry' % atom):
        if not entry.findall("{%s}category[@term='%s#post']" % (atom, kind)):
            continue

        id_ = entry.find('{%s}id' % atom).text
        title = entry.findall('{%s}title' % atom)[0].text
        content = entry.find('{%s}content' % atom).text
        published = _d(entry.find('{%s}published' % atom).text)
        updated = _d(entry.find('{%s}updated' % atom).text)

        post_elts = entry.findall('{%s}link[@rel="alternate"]' % atom)
        if post_elts:
            addr = post_elts[0].attrib['href']
        else:
            addr = None

        tags = [category.attrib['term']
                for category in
                entry.findall('{%s}category[@scheme="%s"]' % (atom, ns))]

        dest.store(id_, addr, title, content, published, updated, tags)


def _d(s):
    return datetime.datetime.strptime(s[:10], '%Y-%m-%d').date()


if __name__ == '__main__':
    main()
