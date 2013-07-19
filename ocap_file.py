'''ocap_file -- least-privilege interaction with the filesystem, web

Inspired by:

  The Sash file object is quite similar to (though different from) the
  E file object, which has proven in practice to supply simple,
  intuitive, pola-disciplined interaction with the file system::

    type readable = {
         isDir : unit -> bool;
         exists : unit -> bool;
         subRdFiles : unit -> readable list;
         subRdFile : string -> readable;
         inChannel : unit -> in_channel;
         getBytes : unit -> string;
         fullPath : unit -> string;
    }


 * `How Emily Tamed the Caml`__
   Stiegler, Marc; Miller, Mark
   HPL-2006-116

__ http://www.hpl.hp.com/techreports/2006/HPL-2006-116.html

'''

from urlparse import urljoin

import encap


class WebReadable(encap.ESuite):
    '''Read-only wrapping of urllib2 in the Emily/E least-authority API.

    >>> urlopener = _MockMostPagesOKButSome404('Z')
    >>> from urllib2 import Request
    >>> rdweb = WebReadable('http://example/stuff/', urlopener, Request)

    A refinement could fetch content, parse links,
    and enumerate those that point "downward", but
    this implementation doesn't supply directory functionality::

    >>> rdweb.isDir()
    False
    >>> len(rdweb.subRdFiles())
    0

    Check whether a HEAD request gives a 2xx response::
    >>> rdweb.exists()
    True
    >>> s = rdweb.subRdFile('Z')
    >>> s.fullPath()
    'http://example/stuff/Z'
    >>> s.exists()
    False

    Get a reader for the content or just the content::
    >>> rdweb.inChannel().read(4)
    'page'
    >>> rdweb.getBytes()[:4]
    'page'

    No authority is granted to URLs that don't start with `base`::
    >>> rdweb.subRdFile('x/../../y')
    Traceback (most recent call last):
       ...
    LookupError: Path does not lead to a subordinate.

    Hence traversing from `/stuff/Z` to `/stuff/x` is not allowed::
    >>> s.subRdFile('x')
    Traceback (most recent call last):
       ...
    LookupError: Path does not lead to a subordinate.

    .. todo:: consider taking a hint/name parameter for printing.
    '''
    def __new__(cls, base, urlopener, RequestClass):
        '''
        :param base: base URL
        :param urlopener: as from `urllib2.build_opener()`
        :param RequestClass: e.g. `urllib2.Request`
        '''

        def isDir(_):
            return False

        def exists(_):
            class HeadRequest(RequestClass):
                '''
                ack: doshea Jan 15 2010
                How do you send a HEAD HTTP request in Python?
                http://stackoverflow.com/questions/107405/
                '''
                def get_method(self):
                    return "HEAD"

            try:
                urlopener.open(HeadRequest(base))
                return True
            except IOError:
                return False

        def subRdFiles(_):
            return ()

        def subRdFile(_, path):
            there = urljoin(base, path)
            if not there.startswith(base):
                raise LookupError('Path does not lead to a subordinate.')
            return WebReadable(there, urlopener, RequestClass)

        def inChannel(_):
            '''
            .. todo:: wrap result of open() for strict confinement.
            '''
            return urlopener.open(base)

        def getBytes(self):
            return inChannel(self).read()

        def fullPath(_):
            return base

        return cls.make(isDir, exists, subRdFiles, subRdFile, inChannel,
                        getBytes, fullPath)


class _MockMostPagesOKButSome404(object):
    '''Raise 404 for pages containing given strings; otherwise succeed.
    '''
    def __init__(self, bad):
        self.bad = bad

    def open(self, request_or_address, content=None):
        from StringIO import StringIO

        try:
            address = request_or_address.get_full_url()
        except AttributeError:
            address = request_or_address

        if [txt for txt in self.bad if txt in address]:
            raise IOError('404...')

        if content:
            return StringIO('you posted: ' + content)

        return StringIO('page content...')
