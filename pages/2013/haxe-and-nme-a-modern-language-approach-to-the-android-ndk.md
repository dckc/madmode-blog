title: "haxe and NME: a modern language approach to the android NDK"
date: 2013-05-04
published: true
tags: [games, mobile, programming, javascript, android]
summary: Things are still rough around the edges, but it looks like
  there's plenty of mature functionality in the middle. This looks
  like the most promising approach I've seen for game development for
  android and HTML5.

I vaguely recall discovering <a href="http://haxe.org/">haxe</a> quite
a while ago. While its site is very shiny, overblown claims like this
made it look more like proprietary marketing glitz than maturity in
an open source project:

> If you could only learn one programming language, <em>Haxe</em> would be it.
> It's universal. It's powerful. It's easy-to-use.

But I'm doing some maintenance on a PHP customization and I'd really
like the computer to help me get it right. Brian McKenna is a
developer I follow for <a href="http://brianmckenna.org/blog/">his
work integrating functional programming with Javascript</a>, so when I
saw him tweeting about haxe, I wanted to take another look.

I'll leave the rest of the PHP story for another episode, but in
short, haxe seems to have lots of the goodies from scala (type
inference, sum and product types, pattern matching etc. on top of a
Java-like OOP language) without the slow compiles and general Java
bloat.

Haxe is "a web language" but its roots are in the flash game
development world. <a href="http://www.nme.io/">NME</a> is the current
media engine library with support for deployment to "Windows, Mac,
Linux, iOS, Android, BlackBerry, Flash and even HTML5".  It was
launched in 2007 and these days its functionality and performance
compete with Adobe Air.

Out of curiosity, I tried the android target from the
<a href="http://www.nme.io/developer/documentation/getting-started/">
Getting Started</a> docs:

    nme setup android
    nme create ActuateExample
    nme test android

I didn't win right away; I went to <a
href="http://www.nme.io/community/irc/">#nme on freenode</a> and
reported:

    <DanC_> harrumph. downloaded gigabytes of android SDK stuff only to get:
     ActuateExample$ nme test android
     Uncaught exception - C Stack Overflow
     Error : 

But a minute later, I was making progress:

    <DanC_> build works... wild... ndk...
     this looks easier than scala for android

And fifteen minutes later:

    <DanC_> ok... I'm blown away. `ant debug install` and there it is, running on my phone.
     1.77MB

The `setup` step downloaded the whole android SDK and NDK. The `build`
step produces C++ code and an ant `build.xml` file. Plug in the phone,
run `ant`, and there it is, on the phone, with animated balls bouncing
around.

The other examples were hit-and-miss:

    <DanC_> gen/android/widget/Toast.hx:151: characters 6-24 : native.#JNI has no field callMember
     that was from 19-AndroidJNI
     NyanCat doesn't work in html5
     $ nme test neko
     Sys_error("null/temp_8224482.neko: No such file or directory")
     this works: SimpleOpenGLView$ nme test neko -64
     blank screen again, black this time: SimpleOpenGLView$ nme test linux -64
     works: SimpleOpenGLView$ nme test html5

Then I got adventurous and tried to upgrade to haxe 3 and nme 4 to run
<a href="https://github.com/nitrobin/spinehx" >spinehx</a> and got all
out of whack:

    <DanC_> spinehx$ nme test html5
     Error: : unknown option `--js-modern'.

So things are still rough around the edges, but it looks like there's
plenty of mature functionality in the middle. This looks like the most
promising approach I've seen for game development for android and
HTML5.

I'm curious to know how well it supports the overall android API, with
notifications and intents and such. I'm also tempted to try it out for
REST style apps with AngularJS, like <a
href="https://bitbucket.org/DanC/finquick">finquick</a>.