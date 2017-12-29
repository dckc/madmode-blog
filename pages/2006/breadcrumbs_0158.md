date: 2006-08-11
title: 'Stitching the Semantic Web together with OWL at AAAI-06'
published: True
tags: ['breadcrumbs', 'RdfAndSql', 'AAAI', 'public-sparql-dev', 'citation']

<div>

<p>I was pleased to find that <a
href="http://www.aaai.org/Conferences/AAAI/aaai06.php">AAAI '06</a> in
Boston a couple weeks ago had a spectrum of people I know and don't
know and work that's near and far from my own. The talk about the
DARPA grand challenge was inspiring.</p>

<p>But closer to my work, I ran into Jeff Heflin, who I worked with on
DAML and especially the <a href="http://www.w3.org/TR/webont-req/">OWL
requirements document</a>.  Amid too many papers about ontologies for
the sake of ontologies and threads like <cite><a href=
"http://lists.w3.org/Archives/Public/semantic-web/2006Jul/thread.html#msg56"
>Is there real world RDF-S/OWL instance data?</a></cite>, his <cite><a
href="http://swat.cse.lehigh.edu/pubs/index.html#pan06a">Investigation
into the Feasibility of the Semantic Web</a></cite> is a breath of
fresh air. The introduction sets out their approach this way:</p>

<blockquote>

<p>Our approach
is to use axioms of OWL, the de facto Semantic Web language,
to describe a map for a set of ontologies. The axioms
will relate concepts from one ontology to the other.
... There is a well-established body of research
in the area of automated ontology alignment. This
is <b>not our focus</b>. Instead we investigate the application of
these alignments to provide an integrated view of the Semantic
Web data.</p>

</blockquote>

<p>(emphasis mine). The rest of the paper justifies this approach,
leading up to:</p>

<blockquote>
<p>We first query the knowledge base from the perspective of
each of the 10 ontologies that define the concept Person.
We now ask for all the instances of the concept Person.
The results vary from 4 to 1,163,628. We then map the
Person concept from all the ontologies to the Person
concept defined in the FOAF ontology. We now issue the
same query from the perspective of this map and we get
1,213,246 results. The results now encompass all the data
sources that commit to these 10 ontologies. Note: a pair
wise mapping would have taken 45 mapping axioms to establish
this alignment instead of the 9 mapping axioms that
we used. More importantly due to this network effect of the
maps, by contributing just a single map, one will <q>automatically</q>
get the benefit of all the data that is available in the
network.</p>
</blockquote>

<p>That's fantastic stuff.</p>

<p style="font-size: smaller">We now pause for a <a
href="http://citeseer.ist.psu.edu/online-nature01/">word from Steve
Lawrence; NEC Research Institute</a>, to lament the lack of free
online proceedings for AAAI: <q>Articles freely available online are
more highly cited. For greater impact and faster scientific progress,
authors and publishers should aim to make research easy to access.</q>
OK, now back to the great paper...</p>

<p>Along the way, they give a definition of a <dfn>knowledge
function</dfn>, <samp>K</samp>, that is remarkably similar to <a
href="http://www.w3.org/2000/10/swap/doc/Reach">log:semantics from
N3</a>. They also define a <dfn>commitment function</dfn> that is
basically the <a
href="http://esw.w3.org/topic/OntologicalClosure">ontological closure
pattern</a>.</p>

<p>The approach to querying all this data is something they call DLDB,
which comes from a paper they submitted to the <a
href="http://km.aifb.uni-karlsruhe.de/ws/psss03">ISWC Practical and
Scalable Semantic Systems workshop</a>. <em>Darn! no full text
proceedings online again. Ah...  <a
href="http://www.cse.lehigh.edu/~heflin/pubs/">Jeff's pubs</a> include
a tech report version.</em> To paraphrase: there's a table for each
class and a table for each property that relates rows from the class
tables. They use a DL reasoner to find subclass relationships, and
they make views out of them.  I have never seen this approach to <a
rel="tag" href="http://esw.w3.org/topic/RdfAndSql">RdfAndSql</a>
before; it sure looks promising. I wonder if we can integrate it into
our <a href="/breadcrumbs/node/140">dbview work</a> somehow and
perhaps into our truth-maintenance system in the <a
href="http://dig.csail.mit.edu/TAMI/">TAMI project</a>.</p>

<p>This wasn't the only work at AAAI on scalable, practical knowledge
representation. I caught just a glance at some other papers at the
conference that exploit wikipedia as a dataset in various
algorithms. I hope to study those more.</p>

<p>I also ran into Ben Kuipers, whose <a
href="http://www.cs.utexas.edu/users/qr/algernon.html">Algernon and
Access-Limited Logic</a> has long appealed to me as an approach to
reasoning that might work well when scaled up to Semantic Web data
sets. That work is mostly on hold; we started talking about getting it
going again, but didn't get very far into the conversation. I hope to
pick that up again soon.</p>

<p>I gather the 1.0 release of <a
href="http://opencyc.org/">OpenCyc</a> happened at the conference;
there's a lot of great stuff in cyc, but only time will tell how well
it will integrate with other Semantic Web stuff.</p>

<p>Meanwhile, a handy citation for Heflin's paper...</p>

<ul class="bibliography">
<li id="pan06a" class="inproceedings">
<span class="author">Z. Pan and A. Qasem and J. Heflin</span>
<cite><a href="http://swat.cse.lehigh.edu/pubs/index.html#pan06a">An Investigation into the Feasibility of the Semantic Web</a></cite>. In <span class="booktitle">Proc. of the Twenty First  National Conference on Artificial Intelligence  (AAAI 2006)</span>, <span class="address">Boston, USA</span>, <span class="year">2006</span> (<a href="http://swat.cse.lehigh.edu/pubs/abstracts06.html#pan06a">abstract</a>)
</li>
</ul>

<p>That's marked up using <a
href="http://www.w3.org/2004/04/xhlt91/">an XHTML/LaText/BibTex
idiom</a> that I'm working on so that we get BibTex for free:</p>

<pre>
@inproceedings{pan06a,
title = "{An Investigation into the Feasibility of the Semantic Web}",
    author = {Z. Pan and A. Qasem and J. Heflin},
    booktitle = {Proc. of the Twenty First  National Conference on Artificial Intelligence  (AAAI 2006)},
    year = {2006},
    address = {Boston, USA},
}
</pre>

<div><em>tags:
<a href="http://esw.w3.org/topic/RdfAndSql"
  rel="tag">RdfAndSql</a>,
<a href="http://del.icio.us/connolly/AAAI"
 rel="tag">AAAI</a>,
<a href="http://lists.w3.org/Archives/Public/public-sparql-dev/"
 rel="tag">public-sparql-dev</a>,
<a href="http://microformats.org/wiki/citation"
 rel="tag">citation</a>
</em></div>
</div>




