title: 25 Oct 2007
date: 2007-10-25
tags: []
published: true

  <p><b class="title">Remembering Modula-3</b>

<p> <p> <p> <p><cite><a
href="http://www.amazon.com/gp/redirect.html?ie=UTF8&amp;location=http%3A%2F%2Fwww.amazon.com%2FProgramming-Modula-3-Prentice-Innovative-Technology%2Fdp%2F0135904641%3Fie%3DUTF8%26s%3Dbooks%26qid%3D1193273155%26sr%3D8-1&amp;tag=danconnolly&amp;linkCode=ur2&amp;camp=1789&amp;creative=9325">Systems
Programming with Modula-3</a></cite><img
src="https://www.assoc-amazon.com/e/ir?t=danconnolly&amp;l=ur2&amp;o=1"
width="1" height="1" alt=""
style="border:none !important; margin:0px !important;" />
has been on my
wishlist for years, but after reading the feedback from Tim
Bray's <a
href="http://www.tbray.org/ongoing/When/200x/2007/09/20/Wide-Finder">Wide
Finder</a> project, I finally got my very own copy.

<p> <p> <p> <p>One of the reactions, <a
href="http://www.findinglisp.com/blog/2007/10/stupid-programming-language-tricks.html"
rel="nofollow">Finding Lisp</a>, observes: 

<p> <p> <p> <blockquote>
  Most popular programming languages have the same simple
threads+locks
  paradigm that was popularized with pthreads and Java.<br />
</blockquote>

<p> <p> <p> <p>But Java made everything a monitor.

<p> <p> <p> <p>I learned pthreads while working on a big
horrible C++/<a
href="http://en.wikipedia.org/wiki/Distributed_Computing_Environment">DCE</a>
project, Dazel (later bought by <a
href="http://en.wikipedia.org/wiki/Hewlett-Packard">HP</a>).
One of the guys
there (<em>Jim W?</em>) loaned me
his copy of
<cite>Systems Programming with Modula-3</cite>, where
chapter 4 is a copy of
<cite><a
href="http://gatekeeper.dec.com/pub/DEC/SRC/research-reports/abstracts/src-rr-035.html">An
Introduction to Programming with Threads</a></cite> by
Birrell. It's probably
a good thing that we never followed thru on our dreams to
rewrite the whole
project in Modula-3, but it was good to know about partial
orders on locks
and such while taming the pthread libraries (... and the C++
exception
runtimes; what a nightmare!)

<p> <p> <p> <p>And <em>anybody who had studied the Modula-3
Thread and
IO design would know
better than to make everything a monitor</em>.


<p> <p> <p>A lot of good stuff from Modula-3 lives on in python, and
some in Java,
but DEC got bought by Compaq which got bought by HP, and a
lot of the <a
href="http://en.wikipedia.org/wiki/DEC_Systems_Research_Center">DEC
SRC</a>
goodies seem to be disapearing from the net.


<p> <p> <p> <p>The <a
href="http://en.wikipedia.org/wiki/Modula-3">wikipedia
article on
Modula-3</a> has a "This article does not cite any
references or sources" tag
since July 2006. That looks silly, since a number of books
and articles are
listed. I can see some unsupported claims, though, so I
ordered my own copy
of SPwM3 so I can separate some of the verifyable claims
from the
speculation.

<p> <p> <p> <p>I'd also really like to find a host (other than
the <a
href="http://www.archive.org/web/web.php">wayback
machine</a>) for the
hypertext version of the <a
href="http://web.archive.org/web/20051217112426/http://www.research.compaq.com/SRC/m3sources/html/INDEX.html">SRC
Modula-3 sources</a>; it's a gold-mine of software
engineering theory and
practice; for example, from <a
href="http://web.archive.org/web/20040105144442/www.research.compaq.com/SRC/m3sources/html/fingerprint/src/Fingerprint.i3.html">Fingerprint.m3</a>:

<p> <p> <p> <blockquote>

<p> <p> <p>   <p>The original fingerprint interface offered at
SRC did
not include the
  procedure Combine. The Vesta configuration management
project built a
  system that cached intermediate results for large software
builds.
  Abstractly, this is a special case of the common
subexpression problem
  mentioned previously, and the project used fingerprints as
keys in the
  cache. It is instructive to learn what happened.

<p> <p> <p>   <p>You might think that a simple way to solve the
common
subexpression
  problem without Combine would be to fingerprint the texts
that result from
  printing the expressions represented by the nodes of the
DAG. But if the
  DAG is not a tree, this is a serious error, since the
length of the strings
  produced by printing a DAG can grow geometrically with its
size, and
  therefore the probabilistic guarantee becomes useless even
for quite small
  DAGs.

<p> <p> <p>   <p>Avoiding this error, the Vesta group computed the
fingerprint of a node
  by concatenating the node's label with the {\it
fingerprints} of its
  children---treating these fingerprints as 8-byte texts---
and fingerprinted
  the resulting text. With this strategy, the number of
texts fingerprinted
  is proportional to the number of nodes of the DAG, and the
total length of
  these texts is proportional to the number of edges of the
DAG. Thus the
  method appears efficient and sound.

<p> <p> <p>   <p>Alas, the method is not sound. Recall that the
probabilistic guarantee
  is valid only if the strings being fingerprinted are
independent of the
  magic number. But fingerprints themselves are dependent on
the magic
  number, so the probabalistic guarantee is invalid whenever
fingerprints are
  fingerprinted. The Vesta group was soon debugging an
unexpected
  collision.

<p> <p> <p>   <p>The moral is simple: the procedure Combine is a
convenience, but it is
  also much more than a convenience. It should be the only
way that you ever
  generate a fingerprint from another fingerprint. In
particular, never treat
  a fingerprint as text to be passed to FromText.

<p> <p> <p> </blockquote>

<p> <p> <p> <p>Maybe the <a href="http://www.python.org/psf/">python
foundation</a> would
like to host it? I'm pretty sure Guido has a fondness for
Modula-3.
