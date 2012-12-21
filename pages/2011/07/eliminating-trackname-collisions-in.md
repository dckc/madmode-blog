date: 2011-07-07
published: true
tags: [python, music, programming]
title: Eliminating trackname collisions in multi-CD audiobook with mutagen
updated: 2011-07-07


I wanted to listen to an audiobook on my android phone, so&nbsp;I ripped it (using banshee) and copied the tracks, but "track 1"&nbsp;from disc 2 overwrote "track 1" from disc 2.<br />
<br />
So this little ditty uses <a href="http://code.google.com/p/mutagen/wiki/Tutorial">mutagen</a> to rename them to "Disc 01 Track 01"&nbsp;and "Disck 02 Track 02" respectively.<br />
<br />
I have since discovered that ripping this audiobook with iTunes&nbsp;(which consults Gracenotes where banshee consults musicbrainz)&nbsp;yields track names like 1a, 1b, 1c, ..., 2a, 2b, 2c, ... .<br />
<br />
<br />
<pre>import sys
import os

# http://code.google.com/p/mutagen/wiki/Tutorial
import mutagen

def fix(album):
    for dirpath, dirnames, filenames in os.walk(album):
        for track in filenames:
            audio = mutagen.File(os.path.join(dirpath, track))
            print audio['album'], audio['title']
            t = "Disc %02d Track %02d" % (int(audio['discnumber'][0]),
                                          int(audio['tracknumber'][0]))
            audio['title'] = t
            audio.save()

if __name__ == '__main__':
    album = sys.argv[1]
    fix(album)
</pre>