from itertools import takewhile
import operator

from flask_flatpages import FlatPages
from flask_flatpages.page import Page
from werkzeug.utils import import_string


class MetaCompat(FlatPages):
    @staticmethod
    def _split_meta(raw):
        """Separate YAML front matter from body.

        Returns (meta_string, body_string).
        """
        lines = iter(raw.split('\n'))
        meta_lines = list(takewhile(operator.methodcaller('strip'), lines))

        if meta_lines and meta_lines[0] == '---':
            meta_lines = meta_lines[1:]
            try:
                end_idx = meta_lines.index('---')
            except ValueError:
                end_idx = len(meta_lines)
            meta = '\n'.join(meta_lines[:end_idx])
            rest = meta_lines[end_idx + 1:]
            tail = list(lines)
            parts = []
            if rest:
                parts.append('\n'.join(rest))
            if tail:
                parts.append('\n'.join(tail))
            body = '\n'.join(parts)
        elif meta_lines and ':' not in meta_lines[0]:
            meta = ''
            body = raw
        else:
            meta = '\n'.join(meta_lines)
            body = '\n'.join(lines)

        return meta, body

    def _parse(self, content, path, _rel_path):
        """Parse a flatpage file with support for --- yaml delimiters
        """
        meta, body = self._split_meta(content)

        # Now we ready to get HTML renderer function
        html_renderer = self.config('html_renderer')

        # If function is not callable yet, import it
        if not callable(html_renderer):
            html_renderer = import_string(html_renderer)

        # Make able to pass custom arguments to renderer function
        html_renderer = self._smart_html_renderer(html_renderer)

        # Initialize and return Page instance

        return Page(path, meta, body, html_renderer, folder='')


def _nocrash():
    r"""Verify pages with non-YAML content or no blank after --- don't crash.

    A page with no YAML front matter (plain text on first line)
    used to crash with
    ``ValueError: dictionary update sequence element #0 has length 1; 2 is required``.
    >>> MetaCompat._split_meta("Hello world\n\nBody")[0]
    ''
    >>> MetaCompat._split_meta("Hello world\n\nBody")[1]
    'Hello world\n\nBody'

    A page with ``---`` delimiters but no blank line after the closing ``---``
    used to crash the same way.
    >>> MetaCompat._split_meta("---\ntags: [foo]\n---\ncontent")[0]
    'tags: [foo]'
    >>> MetaCompat._split_meta("---\ntags: [foo]\n---\ncontent")[1]
    'content'

    Normal YAML front matter is unchanged.
    >>> MetaCompat._split_meta("title: hi\ndate: 2020-01-01\n\nbody")[0]
    'title: hi\ndate: 2020-01-01'
    """
    pass
