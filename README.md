My blog
=======

These are the whole code and contents of my [madmode
weblog](http://www.madmode.com/). It's a fork of [Nicolas
Perriault](http://nicolas.perriault.net/)'s work: [static website
generator with
flask](https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/).

Installation
------------

Note: you need a working installation of Python and [pip](http://pypi.python.org/pypi/pip).

    $ git co ...
    $ cd ...
    $ virtualenv --no-site-packages `pwd`/env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt

Deploying
---------

**Don't deploy this as is.** It's my personal weblog, remember? The code has been opensourced for educational purpose only.

Also, see the [License section](#license) of this document for more information about contents copyright.

Usage
-----

The `site` exec at the root of the repository is the only command you'll need to call to make this whole crap work:

To serve the website locally (optionaly in `DEBUG=True` mode):

    $ ./site serve --debug
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

This is useful when you want to see changes without having to rebuild the whole suite.

To build the static website:

    $ ./site build

Generated HTML files and assets will go to the `./build/` directory.

To deploy the website (caveat: my server address is harcoded ^^):

    $ ./site deploy

There's also two commands for creating new posts and add new photos:

    $ ./site post code --title="My title"
    Created /Users/niko/Sites/nperriault/pages/code/2012/my-title.md
    $ cat pages/code/2012/my-title.md
    title: My title
    date: 2012-10-05
    published: false

Same for the `./site photo` command.

License
-------

Contents in `./pages` and `./static/photography` (blog posts and photos) are licensed under the terms of the [Creative Commons BY-NC-SA license](http://creativecommons.org/licenses/by-nc-sa/3.0/).

The original Python code, templates, CSS & javascript is released
under the terms of [a very liberal
license](http://sam.zoy.org/wtfpl/). I dedicate my contributions to
the public domain.

**Important note: You can freely reuse parts of the project code, but
  you can't republish the blog with its contents as is publicly on the
  Interwebs.**
