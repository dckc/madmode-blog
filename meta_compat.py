from itertools import takewhile
import operator

from flask_flatpages import FlatPages
from flask_flatpages.page import Page
from werkzeug.utils import import_string


class MetaCompat(FlatPages):
    def _parse(self, content, path, _rel_path):
        """Parse a flatpage file with support for --- yaml delimiters
        """
        lines = iter(content.split('\n'))

        # Read lines until an empty line is encountered.
        meta_lines = list(takewhile(operator.methodcaller('strip'), lines))
        # Handle ---s compatibl with Jekyl, github
        if meta_lines[0] == '---':
            meta_lines = meta_lines[1:]
        if meta_lines[-1] == '---':
            meta_lines = meta_lines[:-1]
        meta = '\n'.join(meta_lines)

        # The rest is the content. `lines` is an iterator so it continues
        # where `itertools.takewhile` left it.
        content = '\n'.join(lines)

        # Now we ready to get HTML renderer function
        html_renderer = self.config('html_renderer')

        # If function is not callable yet, import it
        if not callable(html_renderer):
            html_renderer = import_string(html_renderer)

        # Make able to pass custom arguments to renderer function
        html_renderer = self._smart_html_renderer(html_renderer)

        # Initialize and return Page instance

        return Page(path, meta, content, html_renderer, folder='')
