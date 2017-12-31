title: Fun and Frustration with Scala
date: 2010-01-18
tags: ['programming', 'scala']
published: true

<b>Fun and Frustration with Scala</b>

<p> <p>
In a <a href='http://www.yes-no-cancel.co.uk/2009/09/18/the-python-paradox-is-now-the-scala-paradox/'>September
item</a>, Martin Kleppmann says:<br>

<p> 
<blockquote>Scala in 2009 has the place which Python had in
2004.</blockquote>

<p> <p>
I bookmarked <a href='http://www.scala-lang.org/docu/files/api/index.html'>Scala</a>
(the language; not the band ;-) back in June 2007, but I
didn't find a good excuse to try it out until <a href='http://www.w3.org/People/all#bertails'>Alexandre
Bertails</a>, the new W3C webmaster, suggested adding scala
to the php/perl/python/java mix that powers w3.org. He gave
a great <a href='http://codingdojo.org/cgi-bin/wiki.pl?PreparedKata'>PreparedKata</a>
on scala. I have now built a couple little projects using
Scala. The experience brings me back to a <a href='http://groups.google.com/group/comp.lang.perl.tk/msg/a371b49a9276332'>June
1996 Usenet posting</a>, where I wrote: <br>

<p> 
<blockquote>
<p>Modula-3 was more fun to learn than I had had in years.
The precision, simplicity, and discipline employed in the
design of the language and libraries is refreshing and
results in a system with amazing complexity management
characteristics. 
<p>I have high hopes for Java. I will miss a few of
Modula-3's really novel features. The way interfaces,
generics, exceptions, partial revelations, structural typing
+ brands come together is fantastic. But Java has threads,
exceptions, and garbage collection, combined with more hype
than C++ ever had.
<p>I'm afraid that the portion of the space of problems for
which I might have looked to python and Modula-3 has been
covered -- by perl for quick-and-dirty tasks, and by Java
for more engineered stuff. And both perl and Java seem more
economical than python and Modula-3. 
</blockquote>

<p> <p>
I'm happy to say that I was wrong; python matured quickly
enough that I use it for most of the spectrum. The libraries
matured quickly enough to allow me to get away from perl.
And I'm pretty happy that I avoided Java long enough for
scala to come along and fill in the bits of Modula-3 that
Java lacks.<br>

<p> 
<p>
The main reason I never did pick up Java is that the main
part of my job was project management, i.e. on the <a href='http://www.paulgraham.com/makersschedule.html'>manager's
schedule</a>, and an hour isn't enough to do any software
engineering. It <i>is</i> enough time to <a href='http://www.advogato.org/article/1008.html#9'>write,
test, and document</a> some python code! I'm doing more
software development these days; working on the <a href='http://neurocommons.org/page/ImmPort/JmolViz'>UI part
of a Science Commons project</a> last summer finally gave me
several days in a row to dig in and learn JavaScript
development. And I had to interface to a Java API in JMOL,
so I dipped my toe in the Java waters <a href='http://neurocommons.org/page/ImmPort/PDB#Appendix:_Implementation_Notes_and_dependencies'>using
Jython</a>. I got it working, but since I largely depend on
<a href='http://www.cis.upenn.edu/~edloper/projects/doctestmode/'>doctest
mode for emacs</a> and never got jython working there, it's
only manually tested.<br>

<p> 
<p>
I can now write, test, and document scala code, though it's
about equal parts fun and frustration at this point. <br>

<p> 
<p>
The first frustration was finding that there's nothing like
the python tutorial on the scala web site. The tour of scala
was very tasty, but didn't teach me enough to read scala
code and be confident about what's going on. I tried reading
the language spec, but got lost in abstractions (that's one
thing Java has over scala; GJS's Java spec is a joy to
read). Alexander eventually got me to read <a href='http://www.artima.com/shop/programming_in_scala'>the
ebook</a>, which is quite good, though not freely available.
Shortly after that I discovered the video of Martin
Odersky's FODEM talk; I think that one pleasant hour could
have substituted for several earlier frustrating hours on
the scala web site. And I discovered the <a href='http://programming-scala.labs.oreilly.com/'>O'Reilly
scala book</a>; people say it's nowhere near as good, but
I'm going to try to migrate to it for reference purposes,
since I can more easily share what I find there.<br>

<p> 
<p>

<p> The next frustration I feared was giving up emacs in favor
of a modern Java IDE. But the friendly folks in the <a href='http://www.scala-lang.org/node/813'>#scala channel</a>
assured me it wasn't necessary:<br>

<p> 
<pre>
&lt;DanC&gt;	I'm an emacs addict, but I gather the way to do
scala is with Eclipse
&lt;paulp&gt;	DanC: don't know where you gathered that but I
would bet eclipse user a minority.
&lt;DanC&gt;	oh.

<p> &lt;DanC&gt;	what do you use?
&lt;paulp&gt;	textmate.
&lt;dcsobral&gt;	jEdit here.
</pre>
<p>
I did give up <b>make</b> for <i>simple build tool</i> (<a href='http://code.google.com/p/simple-build-tool/'>sbt</a>);
I only miss it a little; <a href='http://github.com/stevej/emacs/blob/master/support/sbt.el'>sbt
emacs integration</a> is pretty raw and next-error gets out
of sync about which line to go to (workaround: restart
sbt-shell). Flymake looks cool, but I haven't managed to get
it working.<br>

<p> 
<p>
Giving up doctest is much harder. I learned to use
scalatest, but it's no it's tedious and using the 1.0
version requires using unreleased versions of sbt (which
worked fine for me). ScalaCheck is even more bothersome, as
it uses level 12 scala type inference magic while I'm only a
level 4 apprentice, but at least it rewards you by
generating zillions of test cases for you. None of the scala
test frameworks are integrated with scaladoc, the
documentation framework. Every time I had to fill in a test
name or description I'd think "Why is this not integrated
with docs? An interpreter and REPL are as much a part of the
scala culture as the python culture; surely there's a
<b>doctest for scala</b> out there" and go searching. No
joy. I did find a couple starts at doctest for Java (they
use JavaScript for the REPL; Java itself just doesn't work
that way). I eventually got fed up enough to start my own <a href='http://code.google.com/p/swap-scala/source/browse/src/main/scala/doctest.scala'>doctest.scala</a>,
though it's not feature complete enough to use yet.<br>

<p> 
<p>
"Beautiful is better than ugly." says the <a href='http://www.python.org/dev/peps/pep-0020/'>Zen of
Python</a>, and scala feels pretty elegant. But the next
aphorism is "Explicit is better than implicit." Java clearly
takes this too far with<br>

<p> 
<pre>
FileInputStream x = new FileInputStream(file);
</pre>
<p>
Telling the compiler type type of x once should be enough,
and with scala, it is. But scala has lots more magic that,
all together, can make it hard to read. The complexity shows
up in the compiler diagnostics, which I find misleading more
often than not. Scala has parallel namespaces for types and
values; it's kinda cute, but consider this diagnostic:<br>

<p> 
<pre>

<p> [error]
/home/connolly/projects/rdfsem/src/test/scala/rdfstdtest.scala:137:
not found: value Graph
[error]     val manifest = Graph(WebData.loadRDFXML(args(0)))
[error]                    ^
</pre>
<p>
I sit there pulling my hair out, saying "Graph is imported
10 lines up; are you <i>blind</i>?!?!?!" But what I imported
was the type, not the value. The real problem in that line
of code is that scala is like java in using a <b>new</b>
keyword for instantiating (most) classes, but python habits
die hard.<br>

<p> 
<p>
And that's just the beginning when it comes to mystifying
compiler diagnostics. Be very afraid of "Missing closing
brace `}' assumed here." The missing brace may be very, very
far away. The ScalaCheck docs really need a special decoder
ring due to its use of higher order magic; check this out:<br>

<p> 
<pre>
[error]
/home/connolly/projects/rdfsem/src/test/scala/strquot1.scala:33:
missing parameter type for expanded function ((x0$1) =&gt;
x0$1 match {
[error]   case (s @ (_: String)) =&gt;
dequote(quote(quote(s))).$eq$eq(quote(s))
[error] })
[error]     Prop.forAll((genQuotEsc) {
[error]                              ^
</pre>
<p>
That "<tt>case (s @ ...</tt>" stuff isn't in my code; the
compiler magically conjured it up. I only know from
monkey-see-monkey-do reading of the ScalaCheck docs that the
right answer is:<br>

<p> 
<pre>
    Prop.forAll(genQuotEsc) {
</pre>
<p>
Here the compiler is being sadistically misleading:<br>

<p> 
<pre>
[error]
/home/connolly/projects/rdfsem/src/test/scala/rdfstdtest.scala:103:
not enough arguments for method apply: (n:
Int)org.w3.swap.logic.Term in trait LinearSeqLike.
[error] Unspecified value parameter n.
[error] 	println(manifest.each(u, rdf_type, what).mkString())
[error] 	                                              ^
</pre>
<p>
My sin in this case was to break the <a href='http://programming-scala.labs.oreilly.com/ch03.html#_methods_without_parentheses_and_dots'>rules
for methods without parentheses</a>.<br>

<p> 
<p>
Many thanks to RSchulz and company in #scala for taking my
side in several battles against the compiler's
disinformation campaign.<br>

<p> 
<p>
Once that battle is over, life is much more fun. That is,
after all, much of the value proposition of statically typed
languages, though the global consistency guarantee in the
language and build tools comes with a downside that when you
change a type, you can't just test a few modules without
getting everything in sync. <br>

<p> 
<p>
My <b>debugging</b> tool so far is the trusty println().
When my code hangs, I'm used to hitting ctrl-c and getting a
python backtrace. The java runtime, and hence scala runtime,
just quits with no backtrace when you hit ctrl-c. Ouch.<br>

<p> 
<p>
When I asked about debugging and profiling tools in #scala,
the suggestions I got were about various GUI tools, many of
them commercial. I managed to get <a href='http://jetbrains.net/confluence/display/SCA/Getting+Started+with+IntelliJ+IDEA+Scala+Plugin'>IDEA
with the scala plugin</a> configured to navigate my code,
but it took 20x longer than sbt to build, and before I
managed to learn to use its debugger, I spotted the bug
myself. For <b>profiling</b>, <a href='http://java.sun.com/j2se/1.4.2/docs/tooldocs/windows/java.html'>java
-Xprof</a> worked just fine for my needs, though <a href='http://java.sun.com/javase/6/docs/technotes/tools/share/jvisualvm.html'>jvisualvm</a>
is free and packaged by Ubuntu and I did get it to attach to
my running code; I'm still stumped about how to get it to
tell me which methods are taking the most time, though.<br>

<p> 
<p>
I like the idea that scala is now where python was a few
years ago, i.e. that the frustrations that I'm running into
are rough edges that will get smoothed out soonish. The
cascade that started with scalatest 1.0 requiring using an
unreleased version of sbt continued thru using version
2.8.0.Beta1-RC5 of the compiler and libraries. I still love
python, but I'm happy to restore an elegant statically typed
languge to my toolset after Modula-3 went fallow, especially
one that interoperates with the java platform everywhere
from <a href='http://www.scala-lang.org/node/160'>android</a> mobile
devices to <a href='http://www.scala-lang.org/node/1826'>Google App
Engine</a>.<br>

<p> 
<p>
tags: <a href='http://delicious.com/connolly/programming'>programming</a><br>

<p> 
