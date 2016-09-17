def main(argv, stdout, environ, connect):
    username = argv[1]
    webdav = connect(
        environ['SITE_DOMAIN'], username=username,
        password=environ['SITE_PASSWORD'],
        protocol='https',
        # We serve webdav at /remote.php/webdav for Owncloud's benefit
        # -- https://github.com/mnutt/davros/issues/44
        # Davros should probably do a better job of handling ...
        # double slashes before remote.php, resulting in the url
        # looking like //remote.php/webdav
        # https://github.com/mnutt/davros/issues/41#issuecomment-247787540
        path='remote.php/webdav/')

    print >>stdout, webdav
    print >>stdout, webdav.ls()


if __name__ == '__main__':
    def _script():
        from sys import argv, stdout
        from os import environ

        from easywebdav import connect

        main(argv, stdout, environ, connect)
    _script()
