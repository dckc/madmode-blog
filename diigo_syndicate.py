"""diigo_render -- render diigo bookmarks for blog syndication

TODO:
 - page per year

see also: project/diigo-bak/bkmkeep.py
"""

from datetime import datetime
from sys import stderr
import json

import jinja2

PATH = 'projects/diigo-bak/diigo-bookmarks-shared.ndjson'

tenv = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


def main(argv, cwd):
    [_, infile] = argv
    lines = (cwd / infile).open()
    count_bookmarks_by_year(lines)


def count_bookmarks_by_year(lines):
    cr_by_yr = {}
    up_by_yr = {}

    def incr(d, k):
        d[k] = d.setdefault(k, 0) + 1

    for item in each_item(lines):
        incr(cr_by_yr, parse_date(item['created_at']).year)
        incr(up_by_yr, parse_date(item['updated_at']).year)
        # print(render_item(item), file=stderr)

    for d in [cr_by_yr, up_by_yr]:
        print('----', file=stderr)
        for k in sorted(d.keys()):
            print(k, d[k], file=stderr)


def each_item(lines):
    return map(json.loads, lines)


def parse_date(txt):
    '''
    >>> parse_date('2024/05/11 17:48:28 +0000')
    datetime.datetime(2024, 5, 11, 17, 48, 28, tzinfo=datetime.timezone.utc)
    '''
    return datetime.strptime(txt, '%Y/%m/%d %H:%M:%S %z')


def render_item(item):
    return template.render(item)


tenv.filters['parse_date'] = parse_date

ITEM_TEMPLATE = '''
<div class="item">
<h3><a href="{{url}}">{{title}}</a></h3>
<br />
{% if tags != "no_tag" -%}
<ul class="tags">
{% for tag in tags.split(',') -%}
 <li>{{ tag }}</li>
{% endfor -%}
</ul>
{% endif -%}

{% for bq in annotations -%}
 <blockquote>{{ bq.content }}</blockquote>
{% endfor -%}

<dl>
  <dt>created</dt><dd>
    <time datetime="{{created_at | parse_date}}">
    {{(created_at | parse_date).strftime('%a %d %B %H:%M') }}</time></dd>
  <dt>updated</dt><dd>{{updated_at | parse_date}}</dd>
</dl>
<hr />
</div>
'''

template = tenv.from_string(ITEM_TEMPLATE)


if __name__ == '__main__':
    def _script():
        from sys import argv
        from pathlib import Path

        main(argv=argv[:], cwd=Path('.'))

    _script()
