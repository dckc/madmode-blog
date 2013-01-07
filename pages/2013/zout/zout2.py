'''

Based on `clues on getting at the data using python
without a running zope`__ ...

__ http://www.zopelabs.com/cookbook/1054240694
http://plope.com/Members/chrism/whatsnew_27
'''

import logging

log = logging.getLogger(__name__)


def dumpdir(path, root, writer):
    obj = root.unrestrictedTraverse(path)

    for id_, val in obj.objectItems():
        bytes = str(val)
        log.info("'%s': %d bytes", id_, len(bytes))
        writer(id_).write(bytes)


if __name__ == '__main__':
    def _initial_caps():
        from sys import argv
        from os import environ
        from os.path import join
        from Zope import configure, app

        logging.basicConfig()
        instance_home = environ['INSTANCE_HOME']
        conf = join(instance_home, "etc/zope.conf")

        log.debug("instance: %s", instance_home)
        log.debug("conf: %s", conf)

        src_url_path, dest_dir_name = argv[1:3]

        del argv[:]  # hmm...
        configure(conf)
        root = app()

        def writer(n):
            dest = join(dest_dir_name, n)
            log.info('opening for write: %s', dest)
            return open(dest, "wb")

        return dict(path=src_url_path,
                    writer=writer,
                    root=root)

    dumpdir(**_initial_caps())
