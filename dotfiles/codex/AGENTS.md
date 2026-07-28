# User Codex Instructions

## Be concise; optimize for reader attention

Take care to apply [Grice's four maxims](https://en.wikipedia.org/wiki/Cooperative_principle#Grice's_maxims) of conversation: quantity, quality, relation, and manner.

The maxim of **quantity** is: be informative.

Submaxims:

- Make your contribution as informative as is required (for the current purposes of the exchange).
  **Do not make your contribution more informative than is required.**

The maxim of **quality** is: be truthful.

Supermaxim:

- Try to make your contribution one that is true.

Submaxims:

- Do not say what you believe is false.
- Do not say that for which you **lack adequate evidence**.

The maxim of **relation** is: be relevant: the information provided should be relevant to the current exchange and omit any irrelevant information. Do not spend words on things the reader already knows.

The maxim of **manner** is: be clear.

Be brief — i.e., avoid unnecessary verbosity.
Be orderly — i.e., provide information in an order that makes sense, and makes it easy for the recipient to process it.

## POLA, OCap Discipline for Python

When writing python, follow [OCap Python Style](https://github.com/dckc/awesome-ocap/blob/master/style-guide/ocap-py-style-guide.md).
([local copy](~/projects/awesome-ocap/style-guide/ocap-py-style-guide.md) )

Use the [disciplined_python_check.py](~/projects/awesome-ocap/tools/disciplined_python_check.py) checker.

(These tools are to appear near https://github.com/dckc/awesome-ocap/wiki/DisciplinedPython .)

## red/green TDD

Whenever the user reports a bug, reproduce it with a (failing) unit test before fixing it.

> I'm not [always] disciplined enough to write the tests first every time; if the code I write works the first time, I sometimes let myself get away with it. But I'm doing pretty well about doing test-driven debugging, at least. I write tests for any code that doesn't work the first time. And I write tests when I refactor and change things. The confidence to make changes that comes from having tests in place is very freeing. -- https://www.madmode.com/2006/advogato_entry0044.html

## GitHub authentication diagnostics

Do not conclude that GitHub authentication is invalid or expired from a
sandboxed `gh auth status` failure. First rerun `gh auth status` and a direct
read-only request such as `gh api user` with network access. Report an
authentication problem only if those unsandboxed checks fail; distinguish it
from sandbox or network restrictions.
