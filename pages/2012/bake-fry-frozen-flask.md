title: MadMode goes from fried to baked with Frozen-Flask
date: 2012-12-21
published: true
tags: [publishing, collaboration, programming, python, aaronsw]
summary: 'A couple years ago, I started using blogger because I
          wanted immersive hypermedia editing, and I wanted it for free.
          Well, you get what you pay for.'

A couple years ago, I [started using blogger][bt10] because I wanted
immersive hypermedia editing, and I wanted it for free. Well, you get
what you pay for.

[bt10]: ../2010/05/getting-over-blogging-tool-analysis.html

Using a database-backed, through-the-web blogging tool was a big
change for me, after over a decade of using version-controlled static
files at W3C. Aaron Swartz put it in bumper-sticker form: [Bake, Don't
Fry][as02].

[as02]: http://www.aaronsw.com/weblog/000404

The promise of immersive hypermedia editing didn't quite pan out. Yes,
blogger lets you drop in images and videos. But I'm still all knotted
up about media management. I tried to ignore the fact that paragraphs
are separated by `<br/>` tags, but not all the problems are
invisible. It lets you copy-and-paste chunks of hypertext; but it
tries to preserve not just the structure but the formatting too, and
the result is a mess.

Writing on mobile gizmos isn't quite there yet either.  I wrote a six
page letter with two thumbs on my sidekick years ago, but since going
to a touchscreen, that's not happeneing. Voice recognition is getting
really close, but it still requires a little manual clean-up, and with
no cursor keys, editing is maddening.  Besides, when I want to post
"look what my dog just coughed up!" ephemera, I use twit-face-plus,
not my own imprint.

Static site generators are making a comeback, riding the distributed
version control wave. I bookmarked [Octopress][]
under [publishing][] in Oct 2011:

>  ooh... interesting. nice style/fonts, bake-don't-fry, lots of goodies.

[Octopress]: http://octopress.org/
[publishing]: http://www.diigo.com/user/dckc-madmode/publishing

I'm reluctant to add ruby to my toolset. Nothing against it; it's just
too close to python for comfort... like when my mom studied both
Spanish and French and got the vocabulary mixed up. It took me years
to [flush perl out of my system][71]; I'm not going back.

[71]: http://www.advogato.org/person/connolly/diary/71.html

But Octopress was so far ahead of the python-based offerings that I
did try it one afternoon. I got as far as "2. Install Ruby 1.9.3 ..."
but that version wasn't in my apt sources and I wasn't in the mood to
build from source, so I punted.

Finally I found a [flask-based static blog generator][fgen] by
[Nicolas Perriault][n1k0]. For building web apps at work, I picked
[pyramid][] over flask because flask seemed to rely on globals,
but for a front-side-of-one-page tool, I'm fine with it.

[pyramid]: http://pypi.python.org/pypi/pyramid

[n1k0]: https://github.com/n1k0/nicolas.perriault.net
[fgen]: https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/

His site is organized around sections; I was able to rip those out and
replaced them with tags without much trouble:

    def tag_counts(pages):
        all_tags = [tag for pg in pages
                    for tag in pg.meta.get('tags', ())]
        count_tags = [(tag, len(list(tag_group)))
                       for tag, tag_group in groupby(sorted(all_tags))]
        return sorted(count_tags, key=lambda x: x[0].lower())

...

    @app.route('/search/label/<string:tag>.html')
    def search_tag(tag):
        template = 'archives.html'
        articles = get_pages(pages, tag=tag)
        return render_template(template, pages=articles, tag=tag)


I'm still working out the details of publishing the source, but here's
the change log, lightly edited:

  - migrated published madmode items from blogger  
    `990356e3476f 42: +1291/-0`
  - Merge flask work  
    `bc689b10191e 108: +8711/-0`

    - snapshot of madmode sitemap for migration from blogger  
      `a6223bc11053 2: +28815/-0`
      _see also [sitemap.py][sitemap]_
    - blogger snapshot for Flask migration  
      `a3a43c581955 1: +1789/-520`

  - use .html for /search/label/tag pages, for now  
    `a1d40734bc0b 1: +1/-1`
  - scrub remaining occurrences of Nicolas, esp. contact.html  
    `56b91790e57a 8: +24/-46`
  - show tags in article listings and on articles  
    `1b24ba141732 4: +16/-3`
  - polish up madmode homepage: copy, title, acks; archive links  
    `598ef5591769 5: +71/-33`
  - browse archives by year or by year-month _to match blogger urls_  
    `89069d50ddf0 3: +45/-9`
  - add tag cloud  
    `e65884962fa8 4: +53/-2`
  - toward section-less site: home page renders  
    `536f1692c20c 4: +16/-67`
  - migrate_blogger.py seems to mostly work  
    `5a65ceeb9661 1: +76/-2`
  - migrate_blogger.py can iterate through posts  
    `7c075b5ffefc 1: +22/-0`
  - re-brand for MadMode, 1st draft  
    `874bc9b83067 6: +16/-48`
  - prune pages by Nicolas  
    `4380ba01e181 80: +0/-2243`

[sitemap]: https://bitbucket.org/DanC/palmagent/src/56501d8a2347754ff0240bcac8a6d41b9d7a9d0a/sitemap.py?at=default

I'm releasing it now before analysis paralysis sets in again, but
there are still a few things to clean up and there are, of course, a
number of features on my wish list:

 - side-by-side preview editing, a la trac wysiwyg or AaronSw's [jottit][]
 - comments? twitter track-back, disquss comments
 - recent diigo bookmarks, highlights
 - recent commits from github/bitbucket
 - collect my tweets etc. into weekly items, a la Tim Bray and Norm Walsh
 - jsmath
 - goodies from [pelican][]

[jottit]: https://www.jottit.com/
[pelican]: http://docs.getpelican.com/en/3.1.1/