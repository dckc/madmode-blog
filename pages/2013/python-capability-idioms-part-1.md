title: "Capability idioms for python, part 1: scripts vs. modules"
date: 2013-07-25
published: true
tags: programming, python, security, capabilities
summary: "Module-level code uses only authority passed to it by
         callers.  Only the top level script environment is trusted
         with the full authority of the python standard library."


In the python [top-level script
environment](http://docs.python.org/2/library/__main__.html), the
idomatic "conditional script" stanza is:

    if __name__ == "__main__":
        main()

For example, to count the lines in the files given as arguments:

    import sys

    def main():
        for filename in sys.argv[1:]:
            stream = open(filename)
            qty = len([line for line in stream])
            print qty, filename

    if __name__ == '__main__':
        main()

Suppose we re-organize this as:

    def main(argv, open_arg, stdout):
        for filename in argv[1:]:
            stream = open_arg(filename)
            qty = len([line for line in stream])
            print >>stdout, qty, filename

    if __name__ == '__main__':
        def _initial_caps():
            from sys import argv, stdout

            def open_arg(arg):
                if arg not in argv[1:]:
                    raise IOError(
                        'only paths given as arguments can be opened')
                return open(arg)

            return dict(argv=argv[:], stdout=stdout, open_arg=open_arg)

        main(**_initial_caps())

Now `main()` communicates with the outside world only through
[capabilities](http://erights.org/elib/capability/ode/ode-capabilities.html)
passed to it.

Capabilities such as `sys.argv` and `sys.stdout` are visible only
in the `_initial_caps()` trusted computing base. Note that this TCB
is not executed if this module is imported from another module.

The `main()` function is fully unit-testable now, as well:

    import StringIO


    def main(argv, open_arg, stdout):
        r'''
        >>> caps = Mock.caps()
        >>> main(**caps)
        >>> caps['stdout'].getvalue()
        '3 f1\n'
        '''
        for filename in argv[1:]:
            stream = open_arg(filename)
            qty = len([line for line in stream])
            print >>stdout, qty, filename


    class Mock(object):
        @classmethod
        def caps(cls):
            argv = ['prog', 'f1']

            def open_arg(x):
                if x in argv[1:]:
                    return ['line1', 'line2', 'line3']
                raise IOError()

            out = StringIO.StringIO()

            return dict(argv=argv[:], stdout=out, open_arg=open_arg)

    ...
