date: 2006-02-25
title: 'Fun with Embedded RDF and DOAP for the GRDDL profile'
published: True
tags: ['breadcrumbs']

<p>I just updated the <a href="http://www.w3.org/2003/g/data-view">GRDDL profile page</a> to document the easy way to use GRDDL before the hard way.</p>

<p>This past week I swapped in all sorts of travel details and redid the <a href="http://www.w3.org/People/Connolly/#travl">travel schedule on my homepage</a> as a result; I switched to
<a href="http://microformats.org/wiki/hCalendar">hCalendar</a> rather than my own home-grown schedule dialect while I was at it, and replace my FOAF dialect with
<a href="http://research.talis.com/2005/erdf/wiki/Main/RdfInHtml">Embedded RDF</a>.</p>

<p>Since that went so well, and I don't care to go mucking with XHTML at the DTD level, I took the RDDL and XLink markup out of the GRDDL profile page and replaced it with embedded RDF.</p>

<p>In order to document the domains and ranges of the GRDDL properties, their  <tt>id</tt> attributes had to be on an element that dominates those links, i.e. it had to be on the <tt>dd</tt> element rather than the previous <tt>tt</tt> element. That clashes with the way XMDP uses <tt>id</tt> attributes, so I'm not using XMDP markup either. I'm just using Embedded RDF for the RDF Schema bits.</p>

<p>I figured the link to the <a href="http://lists.w3.org/Archives/Public/public-rdf-in-xhtml-tf/">mailing list archive</a> deserved to be a 1st-class link, so I used <a href="http://usefulinc.com/doap">DOAP</a>. The <a href="http://usefulinc.com/ns/doap">DOAP schema</a> is quite tabulator-happy. Good work there.</p>
