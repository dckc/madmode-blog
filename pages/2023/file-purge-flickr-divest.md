title: Divesting from Flickr in the Annual File Purge
date: 2023-01-03
tags: [photos, storage, backup, python, jupyter]
published: true

I spent much of this year's annual file purge recovering from [Flickr going back on their 1TB storage offer](https://blog.flickr.net/en/2022/04/19/update-free-account-limit-changes-and-enforcement-start-may-1-2022/).

While [tinkering with Genode](https://github.com/dckc/madmode-blog/issues/49) and catching up on Metamath (RIP, Norm Megill), I made a lot of use of github issues as my lab notebook; I can search copies of my comments in my email since [I'm a closet librarian and I don't trust cloud services completely](https://www.madmode.com/2021/closet-librarian-approach-cloud-services). One of these searches led me to the pile of monthly **"account in violation free account limits"** nasty-grams building up since May:

 - [Update: Free account limit changes and enforcement start May 1, 2022\. \| Flickr Blog](https://blog.flickr.net/en/2022/04/19/update-free-account-limit-changes-and-enforcement-start-may-1-2022/)

Back in 2015, I mostly knew better, but I did take them up on their terabyte storage offer:

> My photostream on flickr goes back to [Dec 2004](https://www.flickr.com/photos/dckc/archives/date-posted/2004/12/calendar/) when it was big in the open web community. I could never bring myself to go premium, but in May 2013 when they announced the terabyte storage offer, I dusted it off. - [MadMode: Syncing a 5 Year iPhoto Library with flickr](../2015/photo-flickr-explore.html)

I have about 50GB of files from a Flickr data request Feb 17, 2019 on an external SSD. I didn't take the time to keep the private data separate from the code and other detailed notes, but briefly, I

 - verified access to 47GB of data from a March 2019 Flickr data request (`72157706876334384_ff8f2206a90f_part1.zip` etc.) by copying it from an external SSD to an internal NVMe.
   - Why did that take 20 minutes? Oops... I used a USB2 cable and so lost USB3 "SuperSpeed"
 - verified that I can recover a favorite album from iPhoto
   - dealt with the fact that the `photo_NNN.json` files don't actually contain the name of the `abc_NNN_xyz.jpg` media files
   - joined the flickr ids with iPhoto ids using records from the 2015 upload process
     - used nix to bring up a juypter notebook environment with the relevant goodies: `nix-shell -p "python3.withPackages(ps: with ps; [ipython jupyter numpy pandas pillow flickrapi progress crc32c])"`
   - made a simple HTML list of links to photos
   - reverse-engineered the way Web-iPhoto would make an album of those photos from iPhoto files:
     - wrote out `albums` and `photos` JSON
       - discovered the README docs were incomplete and the code needs `tree` too.
 - verified that I can recover a favorite keyword from Apple photos
   - reified the keyword as a directory with symlinks to the relevant photo files
   - toured [simonwillison's dogsheep-photos work](https://simonwillison.net/2020/May/21/dogsheep-photos/) and [osxphotos](https://github.com/RhetTbull/osxphotos) while decoding the Apple photos database.
   - evaluated [photoprism](https://photoprism.app/), an "AI-Powered Photos App for the Decentralized Web" in hopes that open source AI would help me curate interesting photos the way Apple's applied [computer-vision research](https://machinelearning.apple.com/research/recognizing-people-photos) did for Simon
     - wow! nicely packaged!
     - bulk import with move option for canonical naming: `2015/10/20150510_015146_88F59DFB.jpg`
       - that hash is a Castagnoli [crc32c](https://pypi.org/project/crc32c/), the one with hardware support, not the one from the python stdlib.
 - deleted all 10,000+ non-private photos using the [flickr API](https://stuvel.eu/software/flickrapi/) so I'll stop getting those monthly nasty-grams.
   - learned to use the [progress](https://pypi.org/project/progress/) package to see that it would take about an hour

I made lots of [diigo bookmarks and annotations](https://www.diigo.com/user/dckc-madmode) too.

### Footnote on Apple photos dates

[Apple support discussion Apr 2015](https://discussions.apple.com/message/27873467#27873467) gives us some clues about the database schema, which seems to be an [Aperture](https://en.wikipedia.org/wiki/Photos_(application)) database (`apdb`).

> Aperture uses Core Data, which is a database-independent abstraction layer, and thus does not use the native SQLite encoding for dates (juliandate), but rather the NSDate format, which should be a double-precision number of seconds since the reference date (2001-01-01 00:00:00 GMT). -- [majid 2011-05-03](https://majid.info/blog/aperture-internals/#comment-4860)