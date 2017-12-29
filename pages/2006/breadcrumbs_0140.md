date: 2006-06-02
title: 'Exporting databases in the Semantic Web with SPARQL, D2R, dbview, ARC, and such'
published: True
tags: ['breadcrumbs', 'www2006', 'EDI', 'travel', 'sparql']

<div>

<p>The <a href="http://www2006.org/developers/">developer track</a> at
<a href="http://www2006.org/">WWW2006</a> last week in Edinburgh was
really cool; you had to show up on time or you couldn't fit in the
room!  One of the coolest talks was <cite><a
href="http://www2006.org/programme/item.php?id=d22">D2R-Server -
Publishing Relational Databases on the Web as
SPARQL-Endpoints.</a></cite>. I see <a
href="http://www.wiwiss.fu-berlin.de/suhl/bizer/d2r-server/">D2R
Server</a> is released now. Cool.</p>

<p>Yes, storing RDF in a SQL database using 3-column tables (or 4 or 5
or 6...) is cool as far as it goes, but I'm gland we're finally seeing
more work on taking existing SQL databases (whose schemas are not
designed with RDF in mind) and exporting them as RDF.</p>

<p>TimBL wrote a design note on <a
href="http://www.w3.org/DesignIssues/RDB-RDF.html">Relational
Databases on the Semantic Web</a> in 1998. In 2002, I wrote <a
href="http://www.w3.org/2000/10/swap/dbork/dbview.py">dbview.py</a>, a
couple hundred lines of python that implements parts of it.  Rob
Crowell picked it up and the <a
href="http://dig.csail.mit.edu/2006/dbview/dbview.py">2005/2006
version of dbview.py</a> now does foreign keys and backlinks.</p>

<p>D2R gets points for using RDF for their configuration/mapping
info. The <a
href="http://www.wiwiss.fu-berlin.de/suhl/bizer/d2r-server/resources/d2r-server-slides-www2006.pdf">slides</a>
showed turtle/n3.  <em>Why are the dbin brainlets in XML but not RDF?
I wonder.</em></p>

<p>D2R Server has a mapping layer; dbview assumes that will be handled
with rules. The choice of URIs for column names is interesting. D2R
uses <tt>jdbc:mysql://127.0.0.1/wordpress#users1</tt>, but dbview is
all about embedding a SQL database in HTTP space, so we use URIs like
<tt>http://db.example/orders/customers/custno/1#item</tt>.  In dbview,
the decisions about when to use <tt>/</tt> and when to use <tt>#</tt>
are made so that the result is <a
href="http://www.w3.org/2006/Talks/0302-browsedata-tbl/">browseable</a>.
In D2R, the default URIs don't matter as much because it's expected
that they'll be mapped to a more well-known ontology/schema like
foaf.</p>

<p>dbview is still just a few hundred lines of python; we haven't
integrated the <a href="http://lists.w3.org/Archives/Public/public-cwm-announce/2005JulSep/0000.html">SPARQL parser that Yosi developed for cwm</a>, nor
integrated EricP's work on
<a href="http://www.w3.org/2003/01/21-RDF-RDB-access/">federated query</a>.</p>

<p>Speaking of federated query... on Wednesday at the conference, I
saw <a href="http://www.cs.umbc.edu/~finin/">Tim Finin</a> in the <a
href="http://www2006.org/posters/">poster session</a>.  He showed me
something the <a href="http://swoogle.umbc.edu/">swoogle</a> folks are
cooking up: you give it a SPARQL query, and it looks at the terms used
in your query and suggests documents you should put in your SPARQL
dataset to run your query against. I hope to hear more about that.</p>

<p>Somewhere in EricP's work is one of the several SPARQL-to-SQL
rewriters out there... oh... I thought the HP tech report, <cite><a
href="http://www.hpl.hp.com/techreports/2005/HPL-2005-170.html">A
relational algebra for SPARQL</a></cite> was another one, but
it seems to be by Richard Cyganiak, one of the D2R guys.</p>

<p>Benjamin Nowack's <a href="http://www.bnode.org/archives1/55">Feb
2006 item</a> announced a SPARQL-to-SQL rewriter for his <a
href="http://arc.web-semantics.org/">ARC RDF store</a> for PHP.</p>

<p>Hmm... maybe it's time for a <a
href="http://esw.w3.org/topic/ScheduledTopicChat">ScheduledTopicChat</a>
on SPARQL, SQL, and RDF? If you're interested, suggest a couple times
that would be good for you in a comment or in mail to <a
href="mailto:connolly@w3.org,www-archive@w3.org">me and a public
archive</a>.</p>

<div><em>tags:
<a rel="tag"
href="http://del.icio.us/connolly/www2006">www2006</a>
<a rel="tag"
href="http://del.icio.us/connolly/EDI">EDI</a>,
<a rel="tag"
href="http://del.icio.us/connolly/travel">travel</a>
<a rel="tag"
href="http://del.icio.us/connolly/sparql">sparql</a>
</em></div>

</div>