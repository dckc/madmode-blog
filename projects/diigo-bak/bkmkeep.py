from functools import partial
from socket import timeout as socket_timeout
from sys import stderr
from time import sleep
from urlparse import urljoin
from urllib import urlencode
import json
from urllib2 import (HTTPError,
                     HTTPPasswordMgrWithDefaultRealm,
                     URLError,
                     HTTPBasicAuthHandler)


def main(argv, stdout, environ, build_opener):
    username, password_key, apikey = argv[1:4]

    request_timeout = float(environ.get('DIIGO_REQUEST_TIMEOUT_SECONDS', 15))
    max_retries = int(environ.get('DIIGO_MAX_RETRIES', 5))
    retry_base_delay = float(environ.get('DIIGO_RETRY_BASE_DELAY_SECONDS', 1))
    retry_max_delay = float(environ.get('DIIGO_RETRY_MAX_DELAY_SECONDS', 60))

    password_mgr, opener = WebPath.basicAuthOpener(build_opener)
    password_mgr.add_password(None, KB.api_base,
                              username, environ[password_key])

    endpoint = WebPath(KB.api_base, opener, timeout=request_timeout)
    kb = KB(endpoint, username, environ[apikey])
    start = 0
    count = 100
    while True:
        print >>stderr, dict(start=start, count=count)
        it = with_retries(lambda: kb.bookmarks(
            sort=KB.updated_at, start=start, count=count),
            max_retries=max_retries,
            base_delay=retry_base_delay,
            max_delay=retry_max_delay)
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
    def __init__(self, here, opener, timeout=None):
        self._opener = opener
        self._timeout = timeout
        if timeout is None:
            self.open = lambda: opener.open(here)
        else:
            self.open = lambda: opener.open(here, timeout=timeout)
        self.pathjoin = lambda other: WebPath(
            urljoin(here, other), self._opener, timeout=self._timeout)
        self.query = lambda params: WebPath(
            urljoin(here, '?' + urlencode(params)),
            self._opener, timeout=self._timeout)

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


def with_retries(action, max_retries=5, base_delay=1, max_delay=60):
    attempt = 0
    while True:
        try:
            return action()
        except Exception as err:
            if not is_retryable(err):
                raise
            if attempt >= max_retries:
                print >>stderr, dict(event='retry_exhausted',
                                     attempts=attempt + 1,
                                     error=repr(err))
                raise

            delay = min(max_delay, base_delay * (2 ** attempt))
            retry_after = retry_after_seconds(err)
            if retry_after is not None:
                delay = max(delay, retry_after)

            print >>stderr, dict(event='retry',
                                 attempt=attempt + 1,
                                 sleep_seconds=delay,
                                 error=repr(err))
            sleep(delay)
            attempt += 1


def is_retryable(err):
    if isinstance(err, (URLError, socket_timeout)):
        return True
    if isinstance(err, HTTPError):
        return err.code in (408, 425, 429, 500, 502, 503, 504)
    if isinstance(err, ValueError):
        return True
    return False


def retry_after_seconds(err):
    if not isinstance(err, HTTPError):
        return None
    value = err.headers.get('Retry-After')
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None


if __name__ == '__main__':
    def _script():
        from os import environ
        from sys import argv, stdout
        from urllib2 import build_opener

        main(argv=argv[:], stdout=stdout,
             environ=environ,
             build_opener=build_opener)

    _script()
