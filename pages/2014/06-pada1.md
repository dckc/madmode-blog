title: A Start in the Craft of Quality Software Development
date: 2014-06-28
tags: [web, programming, learning, collaboration, scala, quality]
published: true

I've taken on an open source software development apprentice.

He's passionate about music and gaming, so we looked at
[The Music Suite](http://music-suite.github.io/docs/ref/) as an
introduction to Haskell, but it's too bleeding edge: the *Hello World*
example has an extraneous dependency on [unix][], which won't fly on
his Windows development machine. I looked into re-arranging the
dependencies, but even on linux, the released version doesn't install
cleanly. We looked at haskell games, but installing OpenGL doesn't
look like instant gratification either.

[unix]: http://hackage.haskell.org/package/unix

It turns out he has an idea for a web site to automate some game
player-ranking stuff that he does.

He's done some Java development, so I thought perhaps using
[Joe-E](http://code.google.com/p/joe-e/) would be a good way to expose
him to [object capability security][erights], but Joe-E evidently went
fallow in 2011. I can't get it to work with any handy version of
Eclipse.

[erights]: http://erights.org/elib/capability/ode/ode-capabilities.html]

[Starting with Scala][scala] seems reasonable; it was
[my bridge from python to functional programming][71], after all.

[scala]: http://www.scala-lang.org/documentation/getting-started.html
[71]: ../2010/advogato_entry0071.html

As I had hoped, the tools have matured.  While I'm an emacs addict, I
don't think I should infect the next generation, so I'm happy to find
that [IntelliJ is open source][ide] and its plug-in support does as
well or better at things like:

 - [Publishing a Project on GitHub][pub]
 - [Markdown syntax support][md]

[ide]: http://www.jetbrains.com/idea/download/download_thanks.jsp
[pub]: http://www.jetbrains.com/idea/webhelp/publishing-a-project-on-github.html
[md]: http://plugins.jetbrains.com/plugin/5970?pr=phpStorm

[IntelliJ gets along with SBT][sbt] now too, granting wishes for
software from our peers via [maven](http://search.maven.org/).

[sbt]: http://confluence.jetbrains.com/display/IntelliJIDEA/Getting+Started+with+SBT

The raw data for the player ranking is on the Web, so our first two
wishes were:

  - an HTTP client library ([dispatch][]) and
  - an HTML parse/query library ([jsoup](http://jsoup.org/)).

[dispatch]: http://dispatch.databinder.net/Dispatch.html

Dispatch makes good use of [types][], and using jsoup involved only a
little [adaptation between Java and Scala types][1072784]. He was
pretty excited when he saw the program extracting various bits of
information about each match.

[types]: http://en.wikipedia.org/wiki/Functional_programming#Type_systems
[1072784]: http://stackoverflow.com/questions/1072784/how-can-i-convert-a-java-iterable-to-a-scala-iterable

The next episode looks to be [deployment with Google App Engine][deploy].

[deploy]: http://www.jetbrains.com/idea/features/google_app_engine.html
