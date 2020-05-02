title: Grokking Triples from Spreadsheets
date: 2005-05-13
tags: []
published: true

<b>Grokking Triples from Spreadsheets</b>

<p> <p><a href="https://seanmcgrath.blogspot.com/2005_05_08_seanmcgrath_archive.html#111589444959575264">Sean  notes that there are lots of triples in spreadsheets</a>. Yup. After my <a href="https://www.w3.org/People/Connolly/events/#exml2003">Aug 2003 trip to Montreal for Extreme</a>,
I used gnumeric as an RDF authoring tool
to collect all the gas receipts and such; then the
<a href="https://www.w3.org/2003/08dc-ymx/Makefile">Makefile</a> has this stanza to convert it to RDF:

<p> <pre>
triplog.rdf: triplog.xml grokSheet.xsl
	$(XSLTPROC) --novalid <a href="https://www.w3.org/2003/08dc-ymx/grokSheet.xsl">grokSheet.xsl</a> triplog.xml &gt;$@
</pre>

<p> <p>I haven't scrubbed the data, so this is somewhat incomplete as a demo.

<p> <p>Yes, this is another <a href="https://www.w3.org/2004/01/rdxh/spec">GRDDL</a>
style transformation.

<p> <p>A comment on Sean's blog said "don't forget RDBs".
Of course not. See <a href="https://www.w3.org/DesignIssues/RDB-RDF.html">Relational Databases and the Semantic Web</a>;
I hope to update my implementation,
<a href="https://www.w3.org/2000/10/swap/dbork/dbview.py">dbview.py</a>
to use <a href="https://www.w3.org/TR/rdf-sparql-protocol/">SPARQL</a> before too much longer.

<p> <p>Hmm... where are timbl's slides on RDF, trees, tables, and such?
