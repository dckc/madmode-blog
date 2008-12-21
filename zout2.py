# clues on getting at the data using python without a running zope... http://www.zopelabs.com/cookbook/1054240694
# http://plope.com/Members/chrism/whatsnew_27

import sys
sys.path.insert(0, '/u/connolly/zope27pfx/lib/python')

import Zope

import os

def main(argv):
    d = os.getcwd()
    root = app()
    dumpdir(argv[1], root, d)

def app(instance_home="/var/lib/zope2.7/instance-dm93-disabled",
	conf="/var/lib/zope2.7/instance-dm93-disabled/etc/zope.conf"):
    progress("configure, .app()...")

    os.environ['INSTANCE_HOME'] = instance_home
    sys.argv = [] # hmm...
    Zope.configure(conf)
    root = Zope.app()	
    return root

def dumpdir(path, root, d):
    obj = root.unrestrictedTraverse(path)

    os.chdir(d)
    progress("iter...")
    progress(d)
    for id,val in obj.objectItems():
	progress("'%s': %d bytes" % (id, len(str(val))))
	open("./" + id, "wb").write(str(val))

def progress(msg):
    import sys
    print >>sys.stderr, msg

if __name__ == '__main__':
    import sys
    main(sys.argv)


