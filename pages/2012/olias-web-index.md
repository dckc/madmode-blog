date: 2012-12-30
published: true
tags: ['Web history', 'HTML', 'Austin']
title: 'OLIAS Web Index, circa 1994'
summary: '"The best way to find information since the card catalog"'

In preparation for the 1994 Seybold Seminar, a few months after Mark
Gaither and I wrapped James Clark's SGML parser in a CGI script to
create the first online [HTML markup validation service][svc], the
OLIAS team at [Hal Software Systems][halsoft] put together an _Index
to the World Wide Web_:

[halsoft]: http://en.wikipedia.org/wiki/HAL_Computer_Systems#HAL_Software_System
[svc]: http://en.wikipedia.org/wiki/W3C_Markup_Validation_Service

<figure>
      <a href="https://picasaweb.google.com/lh/photo/mUr1Wz8CLWN2AQragTKYi4J1EVuJnG1DZLbb2jubdao?feat=embedwebsite">
         <img src="https://lh6.googleusercontent.com/-eqTpt__cJZI/UBqDxYKGObI/AAAAAAAAAU8/p-YZBD2_fcA/s400/IMG_20120802_084220.jpg" height="300" width="400"
	 alt="OLIAS Index to the World Wide Web CD cover" />
      </a>
<figcaption><strong>Index to the World Wide Web</strong><br />
<em>The best way to find information since the card catalog</em><br />
Copyright (c) 1994 HaL Computer Systems, Inc.
</figcaption>
</figure>

OLIAS was state-of-the-art for electronic publishing, at the time:

> Newsgroups: comp.text.sgml  
> Date: 26 Sep 1994 19:15:08 UT  
> From: John Eadie <jme@c-art.com>  
> Organization: Computing Art Inc  
> Message-ID: <182@c-art-w.wimsey.bc.ca>  
> References: <1994Sep21.011746.14931@rat.csc.calpoly.edu>  
> Subject: Re: SGML Viewers and Formatters  
> 
> [Mr. Raytrace]
> 
> >   I am looking for an SGML viewer that supports hypertext links and that
> >   takes care of formatting the documents.  We are hoping to publish SGML
> >   documents on a CD-ROM, using a Windows based viewer.
>
> .. several viewers described ..
>
> You might also consider OLIAS, by HaL Computer Systems -- the browser is
> designed to access multiple sources of SGML including the www using the
> same interface.  The windows port is available soon.
> 
> To show off the OLIAS searching capabilities HaL handed out CD-ROMs at
> Seybold the week before last, that contain an SGML Info Library with 100k
> abstracts from www documents.  On the CD-ROM you get the infolib, a
> browser, plus the Broker that accesses www through your local firewall.
> Anybody that would like to try an OLIAS `Index to the World-Wide Web'
> CD-ROM (for SPARC) can contact me ..
>
> -jme
>
> Ps: OLIAS Version1.1 features architectural forms dtd-to-dtd conversion, an
> incorporated parser, a more complete web-browser, etc, etc.
> 
> --  
> John Eadie  _COMPUTING ART Inc_  
>   klee wyck Cottage, 120 Keith Road, West Vancouver BC  V7T 1L3  
>    # jme@c-art.com #  416.287.6811 -or- 604.922.5104  Fax 604.922.5194  
> 
> `The monks who did not buy printing presses are now making wine.  In the
years ahead, some of us will make the same choice'  Steven Cherry, ELSEVIER
> </pre>

Presuming license to re-publish for the purpose of historical preservation,
I ripped a copy and put it online:

  - [OLIAS.iso][iso] 337M  
    md5sum: de687dc2d49aa3a4d6dc7d7676411ec8

[iso]: https://archive.org/download/olias_202112/OLIAS.iso

The index format is highly optimized for minimal seeking on a CD,
and hence incomprehensible without running OLIAS itself:

> The OLIAS Web Index demonstration software supports one client and two server configurations. The client configuration requires a Sun SPARC workstation running SunOS 4.1.x (Solaris 1.1.1), up to 350MB of disk space, and either X11R5 or Open Windows. The server configurations can be a machine on the client system's LAN that is connected to the Internet and running either a SOCKS server or a Web proxy server process.

Getting it running would be a retrocomputing exercise for
another day, though I did get as far as finding
[Installing SunOS 4.1.1 to Sun3 Emulated in TME 0.8 on Linux][sunos]
Mar 2011 by hyunghwan chung.

[sunos]: http://www.abiyo.net/retrocomputing/installingsunos411tosun3emulatedintme08onlinux


