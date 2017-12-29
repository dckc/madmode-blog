date: 2006-11-11
title: 'Celebrating OWL interoperability and spec quality'
published: True
tags: ['breadcrumbs']

<div>
<p>In a <cite><a href="http://composing-the-semantic-web.blogspot.com/2006/07/standards-and-pseudo-standards.html">Standards and Pseudo Standards</a></cite> item in July, 
Holger Knublauch gripes that SQL interoperability is still
tricky after all these years, and UML is still shaking out bugs,
while RDF and OWL are really solid. I hope GRDDL and SPARQL will get
there soon too.<p>

<p>At the <a href="http://owl-workshop.man.ac.uk/OWLWorkshop06.html">OWL: Experiences and Directions</a> workshop in Athens today, as the community
gathered to talk about problems they see with OWL and what they'd like to add to OWL, I felt compelled to point out (using a few <a href="http://www.w3.org/2006/11dc-athens/owl-quality">slides</a>) that:</p>
<ul>
<li>XML interoperability is quite good and tools are pretty much ubiquitous, but don't forget the XML Core working group has fixed over 100 errata in the specifications since they were originally adopted in 1998.</li>
<li>HTML interoperability is a black art; the specification is only a small part of what you need to know to build interoperable tools.</li>
<li>XML Schema interoperability is improving, but interoperability problem reports are still fairly common, and it's not always clear from the spec which tool is right when they disagree.</li>
</ul>
<p>And while the <a href="http://www.w3.org/2001/sw/WebOnt/errata">OWL errata</a> do include a repeated sentence and a missing word, there have
been <b>no substantive problems reported in the normative specifications</b>.
</p>

<p>How did we do that? The OWL deliverables include:</p>
      <ul>
	<li>Rigorous <a href="http://www.w3.org/TR/owl-semantics/">normative specification</a> using mathematical logic
	<ul>
	  <li>based on mature research results</li>
	</ul>
	</li>
	<li><a href="http://www.w3.org/TR/owl-features/">Overview</a>,
	<a href="http://www.w3.org/TR/owl-guide/">Guide</a>,
	<a href="http://www.w3.org/TR/owl-ref/">Reference</a>, also part of the standard
	<ul>
	  <li>Note <a href="http://www.w3.org/2005/11/Translations/Lists/OverviewRecs.html#owl-semantics-23">translations</a> in French, Hungarian, Japanese contributed by the community.</li>
	</ul>
	</li>
        <li>100s of <a href="http://www.w3.org/TR/owl-test/">tests</a> developed concurrent with the spec
	<ul>
	  <li>demonstrating each feature</li>
	  <li>capturing <a href="http://www.w3.org/2001/sw/WebOnt/webont-issues.html">dozens of issues</a></li>
	</ul>
	</li>
      </ul>

<div  style="float: right"><img src="http://www.w3.org/2006/11dc-athens/owl-test-screen.png"  alt="OWL test results screenshot" /></div>
<p> Jeremy and Jos did great work on the tests. And Sandro's approach
to getting test results back from the tool developers was particularly inspired.
He asked them to publish their test results <em>as RDF data in the web</em>.
Then he provided <em>immediate feedback</em> in the form of an <a href="http://www.w3.org/2003/08/owl-systems/test-results-out">aggregate
report</a> that included updates <em>live</em>. After our table of test results had
columns from one or two tools, several other developers came out of the
woodwork and said "here are my results too." Before long we had results
from a dozen or so tools and our
<a href="http://www.w3.org/2001/sw/WebOnt/impls">implementation report</a>
was compelling.</p>

<p>The <a href="http://www.w3.org/2001/sw/grddl-wg/td/testlist1">GRDDL tests</a> are coming along nicely; Chime's <a href="http://lists.w3.org/Archives/Public/public-grddl-wg/2006Nov/0052.html">message on implementation and testing</a> shows that the spec is quite straightforward to implement, and he updated the test harness so that we should be able to support
<a href="http://www.w3.org/TR/EARL10-Schema/">Evaluation and Report Language (EARL)</a> soon.</p>

<p>SPARQL looks a bit more challenging, but I hope we start to get
some solid reports from developers about the <a href="http://www.w3.org/2001/sw/DataAccess/tests/">SPARQL test collection</a> soon too.</p>

<div>tags: <a href="http://www.w3.org/QA/">QA</a>, GRDDL, SPARQL, OWL, RDF, Semantic Web</div>
</div>