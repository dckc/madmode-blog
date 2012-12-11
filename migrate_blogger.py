
import xml.etree.ElementTree as ET


def main():
    import sys
    blogger_atom_filename, dest = sys.argv[1:3]
    migrate(open(blogger_atom_filename), dest)


def migrate(srcfp, dest_path):
    tree = ET.parse(srcfp)
    root = tree.getroot()
    atom = 'http://www.w3.org/2005/Atom'
    kind = 'http://schemas.google.com/blogger/2008/kind'
    for entry in root.iter('{%s}entry' % atom):
        if not entry.findall("{%s}category[@term='%s#post']" % (atom, kind)):
            continue


if __name__ == '__main__':
    main()
