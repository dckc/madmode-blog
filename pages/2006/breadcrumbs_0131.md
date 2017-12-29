date: 2006-04-25
title: 'On GData, SPARQL update, and RDF Diff/Sync'
published: True
tags: ['breadcrumbs', 'diff', 'sync', 'sparql', 'calendar', 'web+architecture']

<div>

<p>The <a
href="http://code.google.com/apis/gdata/protocol.html">Google Data
APIs Protocol</a> is pretty interesting. It seems to be based on
the Atom publishing protocol, which is a pretty straightforward
application of HTTP and XML, so that's a good thing.</p>

<p>The query features seem to be less expressive than the <a
href="http://www.w3.org/TR/rdf-sparql-protocol/">SPARQL protocol</a>,
but GData has an update feature, while the <a
href="http://www.w3.org/2001/sw/DataAccess/issues#update">SPARQL
update issue</a> is postponed. Updating at the triple level is
tricky. I helped TimBL refine <cite><a
href="http://www.w3.org/DesignIssues/Diff">Delta: an ontology for the
distribution of differences between RDF graphs</a></cite> a bit, and
there's working code in cwm. But I haven't really managed to use it in
practical settings. My PDA's calendar has an XMLRPC service where I
can update a whole record at a time, just like GData. I assume <a
href="http://caldav.org/">caldav</a> does likewise.</p>

<p>The GData approach to concurrency looks quite reasonable. I haven't
studied the authentication mechanism. I hope to get to that
presently.</p>

<div>tags:
<a rel="tag" href="http://del.icio.us/connolly/diff">diff</a>
<a rel="tag" href="http://del.icio.us/connolly/sync">sync</a>
<a rel="tag" href="http://del.icio.us/connolly/sparql">sparql</a>
<a rel="tag" href="http://del.icio.us/connolly/calendar">calendar</a>
<a rel="tag" href="http://del.icio.us/connolly/web+architecture">web+architecture</a>
</div>
</div>

