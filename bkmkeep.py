from urllib import urlencode

from ocap_file import WebReadable
import encap


def main(argv, mkRd):
    apikey, username, password = argv[1:4]
    rd = mkRd(username, password)
    kb = KB(apikey, rd)
    it = kb.bookmarks()
    import pdb; pdb.set_trace()


class KB(encap.ESuite):
    api_base = 'https://secure.diigo.com/api/v2/'

    def __new__(cls, apikey, rd):
        def get(path, **params):
            return rd.subRdFile(path + '?' + urlencode(params)).getBytes()

        def bookmarks(_, path='bookmarks'):
            return get(path, key=apikey)

        return cls.make(bookmarks)


def mkRdMaker(urllib2, top_level_url):
    '''Return fn to make basic auth WebReadable.

    ack: http://docs.python.org/2/howto/urllib2.html
    '''
    def mkUA(username, password):
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

        password_mgr.add_password(None, top_level_url, username, password)

        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)

        return WebReadable(top_level_url, opener, urllib2.Request)

    return mkUA


if __name__ == '__main__':
    def _initial_caps():
        from sys import argv
        import urllib2

        return dict(argv=argv,
                    mkRd=mkRdMaker(urllib2, KB.api_base))

    main(**_initial_caps())
