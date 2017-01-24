title: jukekb - Browse iTunes libraries and upload playlists to Google Music
date: 2015-05-20
tags: [music, python, programming, javascript, cloud-services, digital media]
published: true

*originally published as [jukekb on bitbucket](https://bitbucket.org/DanC/palmagent/src/a2245686a4c19b43a3607a8265f2b1e43b7dd41a/jukekb/?at=default)*

My digital music collection has two parts:

  - the audio files themselves, which are
    - somewhat large
    - readily, though not freely replaceable
    - only licensed copies, not mine to re-publish as I please
  - the playlists, ratings, play logs and counts, which are
    - irreplaceable
    - small

My family has mostly used iTunes over the years, but our libraries
have become somewhat fragmented and redundant. Plus, we carry android
devices. I should be able to get at my old playlists from my new
phone.  But how? Then I discovered [beets][], the "media library management
system for obsessive-compulsive music geeks." I prefer the title
Eric Miller gave me, "closet librarian," but still, it struck a chord.

[beets]: http://beets.radbox.org/

Apple, Google, and Amazon all offer cloud music services. Mostly I
figure the audio files might as well live in the cloud while I just
have cached copies, though there's no garage sale market in digital
media -- the first sale doctrine is much more clear with physical CDs.

Apple doesn't interoperate with android. My wife sometimes buys new
CDs from Amazon, which come with cloud storage copies. But they only
let you upload 250 songs for free. I'm a little leery about Google
these days, but when I found a [python API for Google Music][gm], I
figured I could get my data back, so I decided to dive in.

[gm]: https://unofficial-google-music-api.readthedocs.org/en/latest/reference/mobileclient.html


Design
------

My [first step][s1] was a hello-world [tornado][] service, (tweaked for
[object capapility discipline][ocap]). While modern javascript looks
pretty cool, I'm not nearly as productive with it yet as I am with
python. And tornado's turn-based architecture is pretty close to
node.js.

[s1]: https://bitbucket.org/DanC/palmagent/src/f166e71cf023/jukekb/jukekb.py
[tornado]: http://www.tornadoweb.org/en/stable/web.html
[ocap]: http://www.madmode.com/search/label/capabilities/

Browsing iTunes metadata was straightforward. Sorting by by date added
provided a fun trip down memory lane!

The main challenge was dealing with the evolution of iTunes's file
organization approach.  `ituneslib.Library.path(track)` resolves
`Location` data:

    def path(self, track,
             fixes=['Music',
                    'iTunes Media',
                    'iTunes Media/Music',
                    'iTunes Media/Movies',
                    'iTunes Media/Podcasts',
                    'iTunes Music',
                    'iTunes Music/Music']):

BTW: yay [pathlib][]!

[pathlib]: https://pypi.python.org/pypi/pathlib/

I tried a couple approaches to finding duplicate iTunes tracks via
musicbrainz IDs: first I let the beets tagger grind over my collection
over night. But I was confused by the results. Then I incorporated
the [musicbrainz API][mb] to interactively match iTunes albums to
musicbrainz releases. I was disappointed to learn that beets
records release groups, not releases.

[mb]: http://python-musicbrainzngs.readthedocs.org/en/latest/api/#searching

I also let the Google Music uploader do its thing overnight. But
of course I was left with no record of which of my local copies
matched which item in the cloud, so I'm left with the duplicate
problem all over again.

At this point I was juggling any number of metadata web services, but
then switching to a local app to actually play the song to check that
I had the right one (though beets has a web interface). Reviewing the
state of the art in musicbrainz tools, I re-discovered [quodlibet][],
which has evidently gotten steadily more awesome since I originally
found it. Using its fingerprinting and musicbrainz lookup plugins, I
started to see all sorts of problems with my metadata.

[quodlibet]: https://quodlibet.readthedocs.org/

When it came to *Graceland*, one of my all-time favorites, I went and
tracked down the CD jewel case itself to use the barcode to figure out
which was the relevant release. I started a [dckc discogs collection][col]
in the process. Cool!

[col]: http://www.discogs.com/user/dckc/collection

Quodlibet has [playlist support][pl], but just .m3u and .pls, which
leave me with the same problem: they're just lists of filenames, which
don't have the UI benefits of HTML or even CSV let alone the ability
to survive re-organzation of audio files.

[pl]: https://quodlibet.readthedocs.org/en/latest/guide/browse/playlists.html#playlists

I thought about robust filenames for use in such playlists. What
would be the top of the hierarchy? i.e. the major sort key?

  - by artist?
    - That's how they're on the bookshelf.
      - what about "Various Artists"?
      - We can always re-created a view by artist.
  - by release date?
    - more stable over time

And spaces in filenames are a pain. So omething like:
`release-1986-billy+joel-52nd+street-mbrain3897293/01-movin+out-mbrain2098324`.

I still hope to get there. But meanwhile...

I built a quodlibet plug-in to "reload" my tags from iTunes metadata after
using the edit tags feature to erase all tags in one go. Whee!

And I started my Google Music collection fresh and worked out (most
of) the kinks of incremental upload with records of which Google Music
server ids correspond to which iTunes Persistent IDs.

I'm still thinking about workflows for new music. And I haven't
actually solved the problem of duplicates across iTunes libraries
yet. But when I do, my upload logs should let me clean up my Google
Music collection too.

Usage
-----

*See requirements.txt for prerequisites.*

Get an OAuth token for uploading:

    $ gmbox oauth

Provide password for metadata access:

    $ export GOOGLE_MUSIC_PASSWORD=...
    $ # I like to do:
    $ export GOOGLE_MUSIC_PASSWORD=`ssh-ask-password`

Start the service:

    $ jukekb --db=DB --gmusic=EMAIL LIBRARY...

... where LIBRARY is an iTunes library directory and DB is for upload logs.

The service will report its web address. From there you can

  - browse libraries
  - browse albums and artistss within libraries
  - search
  - browse playlists
  - upload playlists (with the "match" button)
    - already-uploaded songs are added to the Google Music playlist
      without uploading again
      - TODO: cross-library duplicate detection, e.g. using MusicBrains IDs


The scripts have more usage details. Yay [docopt][]!

[docopt]: https://pypi.python.org/pypi/docopt/
