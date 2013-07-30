title: "Capability idioms for python, part 2: encapsulated method suites"
date: 2013-07-29
tags: ["python", "programming", "security", "capabilities"]
published: true

To get [from objects to
capabilities][odecap], we need **absolute encapsulation**:

> From outside an object, one must not be able to gain access to the
  object's internals without the object's consent, even if one has a
  reference to the object. For operating systems, this corresponds to
  the separation of processes...

[odecap]: http://erights.org/elib/capability/ode/ode-capabilities.html

The [python philisophy][adults] is more casual:

> There is no `private` keyword in Python. ... We are all consenting adults. 

[adults]: http://docs.python-guide.org/en/latest/writing/style.html#we-are-all-consenting-adults

But [Ping demonstrated][ping03], as early as 2003, how to build
method suites from python lexical scopes and private namespaces:

    class Namespace:
        def __init__(self, *args, **kw):
            for value in args:
                self.__dict__[value.__name__] = value
            for name, value in kw.items():
                self.__dict__[name] = value

    class ImmutableNamespace(Namespace):
        def __setattr__(self, name, value):
            raise TypeError('read-only namespace')

    def FileReader(path, name):
        def __repr__():
            return '<FileReader %r>' % name

        def open():
            return ReadStream(__builtin__.open(path, 'r'), name)

        def getsize():
            return os.path.getsize(path)

        def getmtime():
            return os.path.getmtime(path)

        return ImmutableNamespace(__repr__, open, getsize, getmtime, name=name)

[ping03]: http://mail.python.org/pipermail/python-dev/2003-March/034287.html

That's the approach I followed when I [started exploring capabilities
in earnest][dc11] a year and a half ago. But something about it didn't
sit right with me... one of the python lint tools didn't see see those
as methods of the FileReader class and I started wondering if some
idiom with metaclasses would feel more natural. Metaclasses turned out
to be not quite right, but the exploration led me to the custom
`__new__` factory:

    class Readable(ESuite):
        '''Wrap the python file API in the Emily/E least-authority API.
        ...'''
        def __new__(cls, path0, os_path, os_listdir, openf):
            path = os_path.abspath(path0)
    
            def isDir(_):
                return os_path.isdir(path)
    
            def exists(_):
                return os_path.exists(path)
    
            def subRdFiles(_):
                return (subRdFile(n)
                        for n in os_listdir(path))

            def inChannel(_):
                return openf(path)

            ...

            return cls.make(isDir, exists, subRdFiles, inChannel)

... where `make()` comes from:

    class ESuite(object):
        @classmethod
        def make(cls, *args, **kwargs):
            arg_methods = [(f.__name__, f) for f in args]
            suite = dict(arg_methods, **kwargs)
            return type(cls.__name__, (ESuite, object), suite)()

There's an extra level of indentation, and I'm still working on
getting docstrings to work as usual. I do occasionally forget to
update the `cls.make(...)` boilerplate when I add a method; not DRY at
all. Mark Seaborn's [CapPython][ms08] approach uses a static verifier
on completely ordinary python code.  I meant to look into it further,
but this `ESuite` idiom has really grown on me because it's a lot like
scala constructor args:

  1. It gets rid of the repetitive `self._xyz = xyz` stuff in `__init__`
  2. Since the constructor args are all accessed by static scoping,
  pyflakes can check them, unlike `self._xyz`. (That's why I use `_`
  rather than `self` in the method definitions: `self` usually isn't
  needed)

[ms08]: http://lackingrhoticity.blogspot.com/2008/08/introducing-cappython.html
[dc11]: http://www.madmode.com/2011/11/capability-security-in-e-coffescript.html

I've fleshed out a few of the traditional object capability patterns
on top of this `ESuite` idiom and called it
[blacknightcap](https://bitbucket.org/DanC/blackknightcap), since,
while I'm reasonably confident it's compatible with approaches to
[secure python's introspection mechanisms][tav09] and tame the
standard library, I haven't bothered with any of that; so nothing stops
you from just [stepping over the stream][mp75], as it were.

[tav09]: http://tav.espians.com/paving-the-way-to-securing-the-python-interpreter.html
[mp75]: http://en.wikipedia.org/wiki/Black_Knight_(Monty_Python)

I haven't bothered because my use case is not actually hosting
untrusted code but rather just facilitating testing, auditing, and design.
More on that in another episode...
