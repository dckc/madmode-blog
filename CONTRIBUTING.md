## POLA, OCap Discipline for Python

When writing python, follow [OCap Python Style](https://github.com/dckc/awesome-ocap/blob/master/style-guide/ocap-py-style-guide.md).
([local copy](./docs/ocap-py-style-guide.md) )

Use the [disciplined_python_check.py](./tools/disciplined_python_check.py) checker.

(These tools are to appear near https://github.com/dckc/awesome-ocap/wiki/DisciplinedPython .)

## red/green TDD

Whenever the user reports a bug, reproduce it with a (failing) unit test before fixing it.

> I'm not [always] disciplined enough to write the tests first every time; if the code I write works the first time, I sometimes let myself get away with it. But I'm doing pretty well about doing test-driven debugging, at least. I write tests for any code that doesn't work the first time. And I write tests when I refactor and change things. The confidence to make changes that comes from having tests in place is very freeing. -- [madmode 2006](https://www.madmode.com/2006/advogato_entry0044.html)

## Cite External Design Constraints

Where a function or type is constrained by, for example, the dbus
protocol or xdg desktop notification protocol, cite the docs for it by
title, url, date, and version

## Give Credit where Credit is Due

where APIs are taken from jeepny, cite it likewise.

## Makefile style

Keep `Makefile` targets short; if a target needs loops, conditionals,
traps, retries, or several commands, move that logic to a script.

## Commit Discipline: atomic, conventional

Use conventional commits:

 - feat: for new "product features"
   - normally includes relevant test
 - fix: for bugs (red/green TDD!)
 - test: for changes to tests that are independent of feat/fix
 - refactor: when there's no externally visible behavior change
 - docs: for no code changes
 - build: for dev tools, build stuff
 - chore: for misc

Use best practices for atomic commits. One for each substantial
accomplishment or lesson learned. Headline space is precious. Use it
wisely! Put the most impactful words early in the headline. Keep it to
78 chars.

This project is in an early, exploratory phase: feel free to commit
before back-tracking.