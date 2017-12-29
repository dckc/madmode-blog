date: 2005-11-30
title: 'MathML as a rule interchange format'
published: True
tags: ['breadcrumbs']

@@<a href="http://lists.w3.org/Archives/Public/public-rdf-dawg/2004OctDec/0370">Nov 2004 work on SPARQL testing</a>

<a href="http://www.w3.org/2001/sw/DataAccess/mathml-rules.xml">SPARQL defns in MathML, N3</a>
<a href="http://www.w3.org/2001/sw/DataAccess/mathmlRules.xsl">mathmlRules.xsl</a>, which converts a little bit of MathML to N3.

<pre>
    &lt;math xmlns="http://www.w3.org/1998/Math/MathML"> 
      &lt;apply>
	&lt;forall/> 
	&lt;bvar> 
	  &lt;ci>x&lt;/ci> 
	&lt;/bvar>
	&lt;apply>
	  &lt;implies/> 
	  &lt;apply>&lt;ci>Man&lt;/ci>&lt;ci>x&lt;/ci>&lt;/apply>

	  &lt;apply>&lt;ci>Mortal&lt;/ci>&lt;ci>x&lt;/ci>&lt;/apply>
	&lt;/apply>
      &lt;/apply> 
    &lt;/math>
</pre>