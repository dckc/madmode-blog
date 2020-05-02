date: 2005-12-14
title: 'Toward better documentation of some schemas for the W3C digital library'
published: True
tags: ['breadcrumbs']

<p>In the <a href="http://www.w3.org/2002/01/tr-automation/">W3C formalized digital library</a>, we supplement the dublin core with <a href="http://www.w3.org/2001/02pd/rec54">a formal model of the W3C Rec-track process</a> and various other schemas.</p>

<p>They were orginally written in N3, and published as RDF/XML. We've tried using CSS to make the RDF/XML browser-friendly, but in N3, it's a royal pain to make a hypertext link from a description of a class or a property, and I'm not even sure it works at all with RDF/XML+CSS. I pretty much prefer using XHTML as the source of most of the knowledge I record, and now that <a href="http://www.w3.org/2003/g/data-view">GRDDL </a> is maturing, I revisited my work on <a href="http://www.w3.org/2000/07/hs78/">representing RDF schemas in XHTML</a>.</p>

<p>And since converting from N3 to XHTML is something the machine can do for me, I'd hate to do it any other way.</p>

<p>To convert the class relationships to an indented list, I want</p>
<ul>
 <li>all the implicit class relationships, not just the stated ones, but</li>
 <li>only the direct super/subclass relationships, not the indirect/redundant ones</li>
</ul>

<p>My working solution,
<a href="http://www.w3.org/2001/02pd/classReport.n3">classReport.n3</a>,
uses this rule to get the class relationships implied by RDFS semantics:</p>

<pre>
@forAll C, C2, SCHEMA, X, P, V.

{
  SCHEMA a Schema; copy ?SC.
  (?SC.log:semantics
   &lt;http://www.w3.org/2000/10/swap/util/rdfs-rules>.log:semantics
   &lt;classDef.n3>.log:semantics
  ).log:conjunction
    log:conclusion ?F
} => { SCHEMA rdfsClosure ?F }.
</pre>

<p>... and here are the rules for making the tree:</p>

<pre>
{
  SCHEMA a Schema; rdfsClosure ?F.
  ?F log:includes { C a rdfs:Class }.
  C log:racine SCHEMA.
  ?F log:notIncludes {
    C rdfs:subClassOf [ rdfs:isDefinedBy SCHEMA].
  }.
} => { SCHEMA root C }.

# direct subclasses
{ ?S a Schema; rdfsClosure ?F.
  ?F log:includes { C rdfs:subClassOf C2 };
     log:notIncludes { C rdfs:subClassOf [ rdfs:subClassOf C2 ] }.
} => { C rdfs:subClassOf C2 }.
</pre>

<p>I use a utility
<a href="http://www.w3.org/2001/02pd/classDef.n3">classDef.n3</a> to connect classes to schemas:</p>

<pre>
{ ?C a rdfs:Class.
  ?C log:racine ?DOC
} => { ?C rdfs:isDefinedBy ?DOC }.
</pre>

<p>Note this only works if you use the <a href="http://esw.w3.org/topic/HashURI">HashURI pattern</a>.</p>

<p>I'm pretty happy with the result so far, though I've only got classes, their labels, and the subclass relationships, so far:</p>

<div>
<ul>
<li><b id='ACaction'>Advisory Committee representative action</b>
<ul>
<li><b id='APreview'>A.P. review</b>
</li>
<li><b id='OrgJoins'>Org. Joins</b>
</li>
<li><b id='PRReview'>PR review</b>
</li>
<li><b id='nomination'>nomination</b>
</li>
</ul>
</li>
<li><b id='ACnotice'>Notice to AC</b>
<ul>
<li><b id='ActivityCreation'>Activity Creation</b>
</li>

<li><b id='ActivityProposal'>Activity Proposal</b>
</li>
<li><b id='CFI'>CFI</b>
</li>
<li><b id='CFP'>CFP</b>

</li>
<li><b id='CFR'>Call for Review</b>
</li>
<li><b id='RECdd'>Rec. dd</b>
</li>
</ul>
</li>
<li><b id='ActivityStatement'>Activity Statement</b>
</li>
<li><b id='Superseded'>supersed Work</b>
</li>
<li><b id='TRPub'>a W3C Technical Report</b>
<ul>
<li><b id='CR'>Candidate Recommendation</b>
</li>
<li><b id='NOTE'>W3C Note</b>

</li>
<li><b id='PER'>W3C Proposed Edited Recommendation</b>

</li>
<li><b id='PR'>W3C Proposed Reccommendation</b>

</li>
<li><b id='REC'>W3C Recommendation</b>
<ul>
<li><b id='FirstEdition'>first Edition of a Recommendation</b>

</li>
</ul>

</li>
<li><b id='RSCND'>W3C Rescinded Recommendation</b>

</li>
<li><b id='WD'>W3C Working Draft</b>
<ul>
<li><b id='LastCall'>Last Call WDWD in Last Call</b>

</li>
<li><b id='Retired'>WD not longer in development</b>

</li>
</ul>
</li>
</ul>
</li>
<li><b id='WGAction'>Working Group action</b>
<ul>
<li><b id='CRreq'>CR req.</b>
</li>
<li><b id='ImpEvidence'>Impl. Evidence</b>

</li>
<li><b id='LCann'>Last Call Ann.</b>

</li>
<li><b id='PRreq'>PR req.</b>

</li>
<li><b id='WDreq'>WD req.</b>

</li>

</ul>
</li>
</ul>
</div>