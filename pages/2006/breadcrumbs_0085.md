date: 2006-02-10
title: 'bnf2turtle -- write a turtle version of an EBNF grammar'
published: True
tags: ['breadcrumbs']

<p>In order to cross one of the few remaining t's on the SPARQL spec, I wrote
<a href="http://www.w3.org/2001/sw/DataAccess/rq23/bnf2turtle.py">bnf2turtle.py</a> today. It turned out to be such a nice piece of code that I elaborated the module documentation using
<a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html">ReStructuredText</a>. It's checked into the SPARQL spec editor's draft materials, but I'll probably move it to the swap codebase presently. Meanwhile, here's the formatted version of the documentation:</p>

<blockquote>
<table class="docinfo" frame="void" rules="none">
<col class="docinfo-name" />
<col class="docinfo-content" />
<tbody valign="top">
<tr><th class="docinfo-name">Author:</th>
<td><a class="first last reference" href="http://www.w3.org/People/Connolly/">Dan Connolly</a></td></tr>
<tr><th class="docinfo-name">Version:</th>
<td>$Revision: 1.13 $ of 2006-02-10</td></tr>
<tr><th class="docinfo-name">Copyright:</th>
<td><a class="first reference" href="http://www.w3.org/Consortium/Legal/2002/copyright-software-20021231">W3C Open Source License</a> Share and enjoy.</td></tr>

</tbody>
</table>
<div class="section">
<h2><a id="usage" name="usage">Usage</a></h2>
<p>Invoke a la:</p>
<pre class="literal-block">
python bnf2turtle.py foo.bnf &gt;foo.ttl
</pre>
<p>where foo.bnf is full of lines like:</p>
<pre class="literal-block">
[1] document ::= prolog element Misc*
</pre>
<p>as per the <a class="reference" href="http://www.w3.org/TR/2004/REC-xml11-20040204/#sec-notation">XML formal grammar notation</a>. The output is <a class="reference" href="http://www.dajobe.org/2004/01/turtle/">Turtle</a> -
Terse RDF Triple Language:</p>

<pre class="literal-block">
:document rdfs:label &quot;document&quot;; rdf:value &quot;1&quot;;
 rdfs:comment &quot;[1] document ::= prolog element Misc*&quot;;
 a g:NonTerminal;
  g:seq (
    :prolog
    :element
    [ g:star
      :Misc
     ]
   )
.
</pre>
</div>
<div class="section">
<h2><a id="motivation" name="motivation">Motivation</a></h2>
<p>Many specifications include grammars that look formal but are not
actually checked, by machine, against test data sets. Debugging the
grammar in the XML specification has been a long, tedious manual
process. Only when the loop is closed between a fully formal grammar
and a large test data set can we be confident that we have an accurate
specification of a language <a class="footnote-reference" href="#id2" id="id1" name="id1">[1]</a>.</p>

<p>The grammar in the <a class="reference" href="http://www.w3.org/DesignIssues/Notation3">N3 design note</a> has evolved based on the original
manual transcription into a python recursive-descent parser and
subsequent development of test cases. Rather than maintain the grammar
and the parser independently, our <a class="reference" href="http://www.w3.org/2002/02/mid/1086902566.21030.1479.camel&#64;dirk;list=public-cwm-bugs">goal</a> is to formalize the language
syntax sufficiently to replace the manual implementation with one
derived mechanically from the specification.</p>
<table class="docutils footnote" frame="void" id="id2" rules="none">
<colgroup><col class="label" /><col /></colgroup>
<tbody valign="top">
<tr><td class="label"><a class="fn-backref" href="#id1" name="id2">[1]</a></td><td>and even then, only the syntax of the language.</td></tr>
</tbody>
</table>
</div>

<div class="section">
<h1><a id="related-work" name="related-work">Related Work</a></h1>
<p>Sean Palmer's <a class="reference" href="http://lists.w3.org/Archives/Public/public-cwm-talk/2004OctDec/0029.html">n3p announcement</a> demonstrated the feasibility of the
approach, though that work did not cover some aspects of N3.</p>
<p>In development of the <a class="reference" href="http://www.w3.org/TR/rdf-sparql-query/">SPARQL specification</a>, Eric Prud'hommeaux
developed <a class="reference" href="http://www.w3.org/1999/02/26-modules/User/Yacker">Yacker</a>, which converts EBNF syntax to perl and C and C++
yacc grammars. It includes an interactive facility for checking
strings against the resulting grammars.
Yosi Scharf used it in <a class="reference" href="http://lists.w3.org/Archives/Public/public-cwm-announce/2005JulSep/0000.html">cwm Release 1.1.0rc1</a>, which includes
a SPAQRL parser that is <em>almost</em> completely mechanically generated.</p>

<p>The N3/turtle output from yacker is lower level than the EBNF notation
from the XML specification; it has the ?, +, and * operators compiled
down to pure context-free rules, obscuring the grammar
structure. Since that transformation is straightforwardly expressed in
semantic web rules (see <a class="reference" href="http://www.w3.org/2000/10/swap/grammar/bnf-rules.n3">bnf-rules.n3</a>), it seems best to keep the RDF
expression of the grammar in terms of the higher level EBNF
constructs.</p>
</div>
<div class="section">
<h2><a id="open-issues-and-future-work" name="open-issues-and-future-work">Open Issues and Future Work</a></h2>
<p>The yacker output also has the terminals compiled to elaborate regular
expressions. The best strategy for dealing with lexical tokens is not
yet clear. Many tokens in SPARQL are case insensitive; this is not yet
captured formally.</p>
<p>The schema for the EBNF vocabulary used here (<tt class="docutils literal"><span class="pre">g:seq</span></tt>, <tt class="docutils literal"><span class="pre">g:alt</span></tt>, ...)
is not yet published; it should be aligned with <a class="reference" href="http://www.w3.org/2000/10/swap/grammar/bnf">swap/grammar/bnf</a>

and the <a class="reference" href="http://www.w3.org/2000/10/swap/grammar/bnf2html.n3">bnf2html.n3</a> rules (and/or the style of linked XHTML grammar
in the SPARQL and XML specificiations).</p>
<p>It would be interesting to corroborate the claim in the SPARQL spec
that the grammar is <a href="http://en.wikipedia.org/wiki/LL_parser">LL(1)</a> with a mechanical proof based on N3 rules.</p>
</div>
<div class="section">
<h1><a id="background" name="background">Background</a></h1>
<p>The <a class="reference" href="_http://www.w3.org/2000/10/swap/Primer.html">N3 Primer</a> by Tim Berners-Lee introduces RDF and the Semantic
web using N3, a teaching and scribbling language. Turtle is a subset
of N3 that maps directly to (and from) the standard XML syntax for
RDF.</p>
</div>

</blockquote>

<p>I started with a kludged and broken algorithm for handling the precedence of | vs concatenation in EBNF rules; for a moment I thought the task required a yacc-like LR parser, but then I realized recursive descent would work well enough. A dozen or so doctests later, it did indeed work. I haven't checked the resulting grammar against the SPARQL tests yet, but it sure looks right.</p>

<p>Then I wondered how much of the formal grammar notation from the XML spec I hadn't covered, so I tried it out on the XML grammar (after writing a 20 line XSLT transformation to extract the grammar from the XML REC) and it worked the first time! So I think it's reasonably complete, though it has a few details that are hard-coded to SPARQL.</p>

<p>See also: <a href="http://lists.w3.org/Archives/Public/public-cwm-talk/2006JanMar/0017.html">cwm-talk discussion</a>, <a href="http://swig.xmlhack.com/2006/02/10/2006-02-10.html#1139534124.430522">swig chump entry</a>.</p>
