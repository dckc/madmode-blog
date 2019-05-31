title: Migrated from github pages to netlify for continuous deployment, SSL
date: 2019-05-30
tags: [publishing, programming, python, security]
published: True

A lot of the friction around my blog has been running the build step:
re-constituting python dependencies, running the build, manually
tweaking the results, and committing the build results to github
pages[^1].

[pmoorman](https://github.com/pmoorman) turned me on to
[Netlify](https://www.netlify.com/) last fall, so I gave it a try:
**Holy shnikeys! it worked 1st try with no tweaks whatsoever!** I told
it my build command was `./site build`[^2] and it picked up my
`requirements.txt`, installed the dependencies, built the site and
deployed it.

Fiddling with DNS took quite a bit longer, but I got free SSL for my
trouble. Netflify pointed out a zillion mixed content issues...
enough that I wrote a little
[fix_insecure.py](https://github.com/dckc/madmode-blog/blob/netlify-https/fix_insecure.py)
script to parse their log and make the edits.

While I'm addressing hygene issues, I fixed the dependency
vulerabilities that github pointed out.[^3]
[CONTRIBUTING.md](https://github.com/dckc/madmode-blog/blob/netlify-https/CONTRIBUTING.md)
shows how I bootstrap with direnv and pipenv.

[^1]: I migrated from nearlyfreespeech.net to github pages in 2015.

[^2]: When did I switch to frozen flask? Wow... it was 2012. Time flies.

[^3]: Darn. This footnote markup doesn't work because flask-markdown predates
     [deprecating positional arguments](https://python-markdown.github.io/change_log/release-3.0/#positional-arguments-deprecated).
