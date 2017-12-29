date: 2005-11-21
title: 'SKOS, SIOC, and drupal taxonomy'
published: True
tags: ['breadcrumbs']

I've been playing around with the drupal taxonomy module. Why doesn't XML2005 show up under <a href="http://dig.csail.mit.edu/breadcrumbs/taxonomy/term/7">conferences</a>?

I wonder how to export the results as <a href="http://www.w3.org/2004/02/skos/">SKOS</a>.
(see <a href="http://lists.w3.org/Archives/Public/public-esw-thes/2005Jun/0007.html">earlier noodling with SKOS</a>)

I found the <a href="http://rdfs.org/sioc/ns#">SIOC schema</a>... it seems to create aliases for several widely-known terms. Ugh. I wonder why. <em>update... the SIOC folks are aware of this and are discussing the relationship with foaf and skos.</em> And it uses multiple domains as if the meaning was the disjunction, despite resolution of the issue of <a href="http://www.w3.org/2000/03/rdf-tracking/#rdfs-domain-and-range">What should the semantics of multiple domain and range properties be?</a>
