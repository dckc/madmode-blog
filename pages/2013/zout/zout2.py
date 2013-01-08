'''

Based on `clues on getting at the data using python
without a running zope`__ ...

__ http://www.zopelabs.com/cookbook/1054240694
http://plope.com/Members/chrism/whatsnew_27
'''

import logging

from ZODB.FileStorage import CorruptedDataError

log = logging.getLogger(__name__)


def dumpdir(path, root, folder):
    obj = root.unrestrictedTraverse(path)

    def walk(items, path, writer):
        for id_, val in items:
            sub = path + [id_]
            log.debug("id: %s", sub)
            try:
                d = val.data
            except AttributeError:
                try:
                    more = val.objectItems()
                except AttributeError:
                    log.warn('skipping class %s', val.__class__.__name__)
                else:
                    walk(more, sub, folder(sub))
            except CorruptedDataError:
                log.warn('Corrupted: %s', sub)
            except EOFError:
                log.warn('IOError: %s', sub)
            else:
                bs = str(d)
                log.info('%10d: %s', len(bs), '/'.join(sub))
                writer(id_).write(bs)

    walk(obj.objectItems(), [], folder([]))


if __name__ == '__main__':
    def _initial_caps():
        import sys
        import os
        from Zope import configure, app

        logging.basicConfig()
        log.setLevel(logging.INFO)
        instance_home = os.environ['INSTANCE_HOME']
        conf = os.path.join(instance_home, "etc/zope.conf")

        log.debug("instance: %s", instance_home)
        log.debug("conf: %s", conf)

        src_url_path, dest_dir_name = sys.argv[1:3]

        del sys.argv[:]  # hmm...
        configure(conf)
        root = app()

        def folder(path):
            dest = os.path.join(dest_dir_name, *path)
            if not os.path.exists(dest):
                log.debug('creating: %s', dest)
                os.mkdir(dest)

            def writer(n):
                d = os.path.join(dest, n)
                log.debug('opening for write: %s', d)
                return open(d, "wb")

            return writer

        return dict(path=src_url_path,
                    folder=folder,
                    root=root)

    dumpdir(**_initial_caps())
