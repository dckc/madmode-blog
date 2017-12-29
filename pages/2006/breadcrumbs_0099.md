date: 2006-03-19
title: 'using JSON and templates to produce microformat data'
published: True
tags: ['breadcrumbs']

<p>In <cite>
<a href="http://dig.csail.mit.edu/breadcrumbs/node/96">Getting my Personal Finance data back with hCalendar and hCard</a></cite>, I discussed using <a href="http://www.json.org/">JSON</a>-style records as an intermediate structure between tab-separated transaction report data and hCalendar.
I just took it a step further in <a href="http://dev.w3.org/cvsweb/2001/palmagent/">palmagent</a>; <tt>hipsrv.py</tt> uses <a href="http://lesscode.org/projects/kid/">kid</a> templates, so the markup can be tweaked independently of the normalization and SPARQL-like filtering logic. I expect to be able to do RDF/XML output thru templates too.</p>

<p>Working at the JSON level is nice; when I want to make a list of 3 numbers, I can just do that, unlike in XML where I have to make up names and think about whether to use a space-separated microparsed attribute value or a massively redundant element structure.</p>

<p>It brings me back to my <a href="http://www.w3.org/People/Connolly/9703-web-apps-essay.html">March 1997 essay for the Web Apps issue on Distributed Objects</a> and <a href="http://www.w3.org/OOP/interfaces/vhll.isl">noodling on VHLL types in ILU</a>.</p>
<!--break-->
<p> In <a href="http://www.w3.org/OOP/interfaces/SExpr.isl">SExpr.isl</a>, I wrote:</p>

<blockquote>
<pre>
(* table allows natural marshalling of:
	perl associative arrays
	scheme hash tables
	python dictionarys
	postscript dictionaries
	SmallTalk dictionaries
*)
</pre>
</blockquote>

<p>I'm not sure how far this approach goes; it's more convenient than the RDF data model in a lot of ways, but I'm not sure about namespace mixing, not to mention object sharing. I wonder how long I can go before I hit those issues...</p>

<p><em>I don't have as much energy to write this the 2nd time; firefox 1.5 crashed and ate the 1st draft just as I was finishing it. :-{</em></p>







