title: Practical production python scripts
date: 2019-07-22
tags: [programming, python, quality]
published: True

In [Writing sustainable Python scripts][vb] ([lobsters
discussion][talk]), the initial prototype looks like:


```python
import sys
for n in range(int(sys.argv[1]), int(sys.argv[2])):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
```

I have a process for turning this sort of thing into production code
that I quite enjoy. I just did it for this code in a [fizzbuzz.py gist][work]:

  1. 1ac9082
  1. 621ddad only run when invoked as script
  1. 4cfa693 ocap discipline: explicit access to argv, stdout
  1. 35e74c6 quick-n-dirty arg parsing
  1. 7cfeeea factor out fizzbuzz() from main()
  1. 8d85c04 module doctest of usage

The bottom line in the [code review checklist][cl] in the shop I run
is: **is this code I would be happy to maintain?**

While I appreciate writing documentation first, it usually takes me a
few iterations of prototyping before I know what it is I want to
document.

I haven't made strict habit of test-driven development, but I do find
factoring out tricky bits of logic and adding unit tests for them
frees my mind up during development. And I do make it a rule to write
tests before fixing any bugs.


## Only run when invoked as script

If this code is good, we want to be able to reuse it by importing it
from other modules. And even if we never reuse this code, we want the
ability to unit test it. So we use the [top level convention][pymain]
(`if __name__ == "__main__":`) to test whether this code is invoked as
a script, but we minimize the code there. As a rule, module level code
shouldn't do anything but define things:

```python


def main():
    for n in range(int(sys.argv[1]), int(sys.argv[2])):
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 3 == 0:
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        else:
            print(n)


if __name__ == '__main__':
    main()
```

## Ocap discipline: explicit access to IO

To facilitate patterns of cooperation without vulnerability, object
capability ([ocap][]) discipline says the only thing globally
accessible should be immutable data. This also supports
[testability][hevery]. `argv` and `stdout` are IO, or at least sources
of non-determinism; object capability discipline calls for passing
these around explicitly.

Of course we have to get them from somewhere. In an object capability
language, they would be passed (directly or indirectly) to `main()`;
we simulate this using `_script_io()`, a function that we only define
and invoke if `__name__ == '__main__`:

```python

def main(argv, stdout):
    for n in range(int(argv[1]), int(argv[2])):
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz", file=stdout)
        elif n % 3 == 0:
            print("fizz", file=stdout)
        elif n % 5 == 0:
            print("buzz", file=stdout)
        else:
            print(n, file=stdout)


if __name__ == '__main__':
    def _script_io():
        from sys import argv, stdout

        main(argv, stdout)

    _script_io()
```

## Quick-n-dirty arg parsing

The code is now testable, so we start looking inside the functions.
Mixing in arg parsing with other logic doesn't smell right:


```
def main(argv, stdout):
    for n in range(int(argv[1]), int(argv[2]))
```

For a little script like this, one or two carefully crafted lines is
all I'd spend on arg parsing:


```python
 def main(argv, stdout):
    [lo_, hi_] = argv[1:3]
    lo, hi = int(lo_), int(hi_)

    for n in range(lo, hi):
        ...
```

If we just invoke this script with no args, the resulting traceback is
often enough of a usage clue, given that the userbase of these scripts
is a handful of devs in the shop (plus jenkins):

```
$ python3 fizzbuzz.py
Traceback ...
  File "fizzbuzz.py", line 4, in main
    [lo_, hi_] = argv[1:3]
...
```

For more involved arg parsing, or perhaps if the userbase were larger,
I prefer [docopt][] to writing (or worse: reading!) elaborate argparse
calls.


### Aside: who asked for fizz and buzz to be parameterized?

Parameterizing fizz and buzz adds testing and maintenance burden.
Unless we've got a customer requirement, let's skip all that.


## Factor out fizzbuzz() from main()

I like to keep our `main()` functions small and separate logic from
IO. Using `yield` in place of `print` is particularly
convenient. Let's add one quick doctest while we're at it:

```python
def main(argv, stdout):
    [lo_, hi_] = argv[1:3]
    lo, hi = int(lo_), int(hi_)

    for word in fizzbuzz(lo, hi):
        print(word, file=stdout)


def fizzbuzz(lo, hi):
    """
    >>> list(fizzbuzz(1, 6))
    [1, 2, 'fizz', 4, 'buzz']
    """
    for n in range(lo, hi):
        if n % 3 == 0 and n % 5 == 0:
            yield "fizzbuzz"
        elif n % 3 == 0:
            yield "fizz"
        elif n % 5 == 0:
            yield "buzz"
        else:
            yield n
```

## Module doctest of usage

Now we can document and test usage together in the module docstring.

I actually started the module doctest earlier in the process, but I
didn't commit it until the end in order to make each commit
demonstrate one part of the process.

```
"""Simple fizzbuzz generator.

The game proceeds with players announcing numbers increasing
sequentially, except for multiples of 3 and 5:

    >>> usage = 'fizzbuzz 1 20'

    >>> from io import StringIO; stdout = StringIO()
    >>> main(usage.split(), stdout)
    >>> print(stdout.getvalue())
    ... #doctest: +ELLIPSIS
    1
    2
    fizz
    4
    buzz
    fizz
    7
    ...
    14
    fizzbuzz
    16
    ...

"""


def main(argv, stdout):
    [lo_, hi_] = argv[1:3]
    lo, hi = int(lo_), int(hi_)

    for word in fizzbuzz(lo, hi):
        print(word, file=stdout)


def fizzbuzz(lo, hi):
    """
    >>> list(fizzbuzz(1, 6))
    [1, 2, 'fizz', 4, 'buzz']
    """
    for n in range(lo, hi):
        if n % 3 == 0 and n % 5 == 0:
            yield "fizzbuzz"
        elif n % 3 == 0:
            yield "fizz"
        elif n % 5 == 0:
            yield "buzz"
        else:
            yield n


if __name__ == '__main__':
    def _script_io():
        from sys import argv, stdout

        main(argv, stdout)

    _script_io()
```

## Reflection

In this example, our 10 line (working!) prototype has turned into 60
lines of code. If a developer asked me to review the original 10 lines
after using it succefully for a few days, and if the cost of a failure
was just a few minutes, I might not bother to touch it.

But the code did mix IO with logic in a way that makes me uneasy.

More often, the cost of a failure is re-running a Jenkins job that
takes hours. And even in early prototype form, scripts are usually
longer than 10 lines and applying these techniques turns up a bug or
two or at least clarifies the security properties of the code.

And in this case, of the resulting 60 lines:

  - 25 are documentation
    - 10 show simulated script output, which is very simple
  - The `main()` function is 6 lines that clearly do nothing
    but parse args, call a function, and output the results
  - The `_script_io()` function is formulaic

The `fizbuzz()` function retains structure of the original 10 line
prototype, with just 4 lines added for documentation / testing.

[vb]: https://vincent.bernat.ch/en/blog/2019-sustainable-python-script
[work]: https://gist.github.com/dckc/d58a04b154d44d46de9abcda84b2a2f0
[eami]: http://www.kumc.edu/miea.html
[cl]: https://informatics.kumc.edu/work/wiki/CodeReviewNotes
[pymain]: https://docs.python.org/3/library/__main__.html
[docopt]: http://docopt.org/
[ocap]: https://en.wikipedia.org/wiki/Object-capability_model
[talk]: https://lobste.rs/s/zoo6tm/sustainable_python_scripts
[hevery]: http://misko.hevery.com/code-reviewers-guide/
