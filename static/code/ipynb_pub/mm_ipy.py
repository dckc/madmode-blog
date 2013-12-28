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
    # article header yaml stuff
    # @@ assumes values are quoted. TODO: use pyaml?
    for n, v in [('title', 'TODO@@'),
                 ('published', 'false'),
                 ('date', '2013-12-28')]:
        yield '%s: %s\n' % (n, v)
    yield '\n'

    notebook = nbformat.reads_json(notebook_txt)

    exportHtml = HTMLExporter(config=Config({'HTMLExporter':
                                             {'default_template': 'basic'}}))

    body, resources = exportHtml.from_notebook_node(notebook)
    # [txt[:100] for txt in resources['inlining']['css']]

    yield body


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
