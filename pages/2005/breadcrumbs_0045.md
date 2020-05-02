date: 2005-12-14
title: 'Toward richtext syndicated feed'
published: True
tags: ['breadcrumbs']

<p>Our <a href="http://dig.csail.mit.edu/breadcrumbs/node/feed">RSS feed</a> is plaintext, so when it's syndicated in <a href="http://planetrdf.com">Planet RDF</a> and the like, there are no links or pictures or even paragraph breaks.</p>

<p>From <a href="http://chatlogs.planetrdf.com/swig/2005-11-22.html#T00-10-36">#swig discussion</a>, I gather that the state-of-the-art is to use <a href="http://norman.walsh.name/2003/09/16/escmarkup">nasty escaped markup</a>, but I'm not up for that. The <a href="http://www.w3.org/2001/sw/RDFCore/">RDF Core WG</a> didn't spend 18 months getting the details of <tt>parseType="Literal"</tt> right for nothing, did we?</p>

<p>I don't know if there are drupal modules available that Do The Right Thing, and due to <a href="/breadcrumbs/node/11">my PHP angst</a> I don't really want to know. But maybe there's a motivated student out there... ?</p>