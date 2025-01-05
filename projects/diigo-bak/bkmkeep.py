from functools import partial
from sys import stderr
from urlparse import urljoin
from urllib import urlencode
import json
from urllib2 import (HTTPPasswordMgrWithDefaultRealm,
                     HTTPBasicAuthHandler)


def main(argv, stdout, environ, build_opener):
    username, password_key, apikey = argv[1:4]

    password_mgr, opener = WebPath.basicAuthOpener(build_opener)
    password_mgr.add_password(None, KB.api_base,
                              username, environ[password_key])

    endpoint = WebPath(KB.api_base, opener)
    kb = KB(endpoint, username, environ[apikey])
    start = 0
    count = 100
    while True:
        print >>stderr, dict(start=start, count=count)
        it = kb.bookmarks(sort=KB.updated_at, start=start, count=count)
        if not it:
            break
        json.dump(it, stdout, indent=2)
        start += count


class KB(object):
    api_base = 'https://secure.diigo.com/api/v2/'

    created_at, updated_at, popularity = range(1, 4)

    def __init__(self, endpoint, user, apikey):
        self.bookmarks = partial(self._bookmarks, endpoint, user, apikey)

    def _bookmarks(self, endpoint, user, apikey,
                   sort, filter='all', start=0, count=100):
        params = dict(user=user, sort=sort, filter=filter,
                      start=start, count=count,
                      key=apikey)
        it = endpoint / 'bookmarks' & params
        return json.load(it.open())


class WebPath(object):
    def __init__(self, here, opener):
        self.open = lambda: opener.open(here)
        self.pathjoin = lambda other: WebPath(urljoin(here, other), opener)
        self.query = lambda params: WebPath(
            urljoin(here, '?' + urlencode(params)), opener)

    @classmethod
    def basicAuthOpener(self, build_opener):
        '''
        ack: http://docs.python.org/2/howto/urllib2.html
        '''
        password_mgr = HTTPPasswordMgrWithDefaultRealm()
        handler = HTTPBasicAuthHandler(password_mgr)
        opener = build_opener(handler)
        return password_mgr, opener

    def __div__(self, other):
        return self.pathjoin(other)

    def __and__(self, other):
        return self.query(other)


if __name__ == '__main__':
    def _script():
        from os import environ
        from sys import argv, stdout
        from urllib2 import build_opener

        main(argv=argv[:], stdout=stdout,
             environ=environ,
             build_opener=build_opener)

    _script()
