title: "Ubuntu 5.10, archive.org, and .torrent files"
date: 2023-12-21
tags: [storage, closet-librarian, archive, ubuntu, linux, protocols]
published: true

I'm ready to say goodbye to my copy of [Ubuntu 5.10 for i386](https://archive.org/details/ubuntu-5.10-pc) on CD, after nearly 2 decades of keeping it as a combination keepsake and software supply chain anchor. I donated it to archive.org:

[![Ubuntu 5.10](https://ia804507.us.archive.org/14/items/ubuntu-5.10-pc/__ia_thumb.jpg)](https://archive.org/details/ubuntu-5.10-pc)

While brainstorming about Merkle trees for file access, I noticed that not only does archive.org OCR the PDF I gave them of the cover and support browsing of the contents of [Ubuntu 5.10 i386.iso](https://ia904507.us.archive.org/view_archive.php?archive=/14/items/ubuntu-5.10-pc/Ubuntu%205.10%20i386.iso), but they provide [ubuntu-5.10-pc_archive.torrent](https://archive.org/download/ubuntu-5.10-pc/ubuntu-5.10-pc_archive.torrent), which means I can have high-performance access to the the full contents of the CDs for just 29k of storage. And brave supports `.torrent` files natively with WebTorrent ([WebTorrent Tutorial](https://webtorrent.io/intro) looks pretty straightforward.)

But what's in that `.torrent` file? Aha! [bencode](https://en.wikipedia.org/wiki/Bencode) from [BEP 3](https://www.bittorrent.org/beps/bep_0003.html#bencoding)! I've heard of it in [OCapN discussion](https://github.com/ocapn/ocapn/issues/1#issuecomment-819652299)
but didn't realize it comes from bittorrent. [BitTorrent bencode format tools](https://www.nayuki.io/page/bittorrent-bencode-format-tools) is really handy, including stopping in a debugger to see the details:

![image](https://github.com/dckc/madmode-blog/assets/150986/39fc8f12-4679-4fe3-91df-30814143c001)

[BCode.hs from haskell-torrent](https://github.com/johngunderman/haskell-torrent/blob/0385d0d4af9778053317d2b7725ef027ae870daf/src/Protocol/BCode.hs#L60-L65) has a crisp specification:

```hs
-- | BCode represents the structure of a bencoded file
data BCode = BInt Integer                       -- ^ An integer
           | BString B.ByteString               -- ^ A string of bytes
           | BArray [BCode]                     -- ^ An array
           | BDict (M.Map B.ByteString BCode)   -- ^ A key, value map
  deriving (Show, Eq)
```

...

```hs
-- | Return the hash of the info-dict in a torrent file
hashInfoDict :: BCode -> IO Digest
hashInfoDict bc =
  do ih <- case info bc of
              Nothing -> fail "Could not find infoHash"
              Just x  -> return x
     let encoded = encode ih
     digest $ L.fromChunks $ [encoded]
```

Playing with [parse-torrent](https://www.npmjs.com/package/parse-torrent) in a [parse\-torrent\-ubuntu\-5\.10 project on StackBlitz](https://stackblitz.com/edit/stackblitz-starters-gcvlq7) is handy in that it shows the `infoHash`, `b890d2e1174a809d1cd0437de30400c542e0a939`, but its JSON output misled me about the real structure: there is no `infoHash` key in the file; there's an `info` dictionary that gets hashed.

Say... Ubuntu offers bittorrent as a download option; maybe they keep a 5.10 `.torrent` file around? I didn't find one from them, but I did find:

- [Ubuntu 5\.10 \(Breezy Badger\) : Canonical Ltd\., Ubuntu community : Internet Archive](https://archive.org/details/Ubuntu-5.10)  
   Source [torrent:urn:sha1:329a357ebd51db73417e1ad767b041291f598ae8](https://archive.org/search.php?query=source%3A%22torrent%3Aurn%3Asha1%3A329a357ebd51db73417e1ad767b041291f598ae8%22)
  Addeddate: 2017-06-20 14:16:31
  Identifier: Ubuntu-5.10

Note the **Source**; yes, [Internet Archive ingests BitTorrents](https://help.archive.org/help/archive-bittorrents/).

Somehow my `Ubuntu 5.10 i386.iso` is 632,262 kb, which is 300 kb larger than theirs (631,962 kb). Maybe some [unused space captured by gnome-disk-utility](https://gitlab.gnome.org/GNOME/gnome-disk-utility/-/issues/321) when I ripped the CD?
