from urllib import urlencode
import json

from ocap_file import WebReadable
import encap


def main(argv, mkRd, stdout):
    apikey, username, password = argv[1:4]
    rd = mkRd(username, password)
    kb = KB(apikey, rd)
    it = kb.bookmarks(username)
    json.dump(it, stdout, indent=2)


class KB(encap.ESuite):
    api_base = 'https://secure.diigo.com/api/v2/'

    created_at, updated_at, popularity = range(1, 4)

    def __new__(cls, apikey, rd):
        def get(path, **params):
            return rd.subRdFile(path + '?' + urlencode(params)).getBytes()

        def bookmarks(_, user, sort=KB.updated_at, filter='all', count=100,
                      path='bookmarks'):
            body = get(path, user=user, sort=sort, filter=filter, count=count,
                       key=apikey)
            return json.loads(body)

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
        from sys import argv, stdout
        import urllib2

        return dict(argv=argv, stdout=stdout,
                    mkRd=mkRdMaker(urllib2, KB.api_base))

    main(**_initial_caps())
