'''mm_ipy -- convert ipython notebook to markdown for madmode blog
'''
from IPython.config import Config
from IPython.nbconvert import HTMLExporter
from IPython.nbformat import current as nbformat


def main(argv, arg_rd, arg_wr,
         encoding='utf-8'):
    notebook_fn, article_fn = argv[1:3]

    notebook_txt = arg_rd(notebook_fn).read()
    with arg_wr(article_fn) as outfp:
        for chunk in article_of(notebook_txt):
            outfp.write(chunk.encode(encoding))


def article_of(notebook_txt):
    notebook = nbformat.reads_json(notebook_txt)

    hide, meta = article_meta(notebook)
    for ix in sorted(hide, reverse=True):
        del notebook.worksheets[0].cells[ix]

    for n, v in meta:
        yield '%s: %s\n' % (n, v)
    yield '\n'

    exportHtml = HTMLExporter(config=Config({'HTMLExporter':
                                             {'default_template': 'basic'}}))

    body, resources = exportHtml.from_notebook_node(notebook)
    # [txt[:100] for txt in resources['inlining']['css']]

    yield body


def article_meta(notebook,
                 meta_start='<pre class="about yaml">',
                 meta_end='</pre>'):
    def find_cell(test):
        return ((i, cell['source'])
                for i, cell in enumerate(notebook.worksheets[0].cells)
                if test(cell)).next()

    h1_ix, h1 = find_cell(
        lambda cell: (cell['cell_type'] == 'heading'
                      and cell['level'] == 1))

    meta_ix, meta_txt = find_cell(
        lambda cell: cell['source'].startswith(meta_start))

    meta = [line.split(': ', 1)  # name: value
            for line in meta_txt.split('\n')
            if not (line.startswith(meta_start)
                    or line.startswith(meta_end))]

    return [h1_ix, meta_ix], [('title', repr(str(h1)))] + meta


if __name__ == '__main__':
    def _with_caps():
        from sys import argv

        def arg_rd(n):
            if n not in argv:
                raise IOError
            return open(n)

        def arg_wr(n):
            if n not in argv:
                raise IOError
            return open(n, 'w')

        main(argv[:], arg_rd, arg_wr)

    _with_caps()
