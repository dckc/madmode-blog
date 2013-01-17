title: 14 Oct 2005
date: 2005-10-14
tags: []
published: true

My XML 2005 late-breaking news proposal was accepted: <a href="http://2005.xmlconference.org/program/wednesday#lb4">Semantic Web Calendaring: RDF Calendar, hCalendar, and GRDDL</a>. See the <a href="http://www.w3.org/TR/2005/NOTE-rdfcal-20050929/#conc1">conclusions and future work section</a> of the <a href="http://www.w3.org/TR/2005/NOTE-rdfcal-20050929/">RDF Calendar report</a> for some of what I'm going to talk about: getting RDF data out of hCalendar using GRDDL, and then querying it with SPARQL.


<p> <b>Debian Unstable</b>
Turns out I didn't need to build a new kernel to install the nvu debian package. apt allowed me to upgrade libc without removing my win4lin kernel package. After that, installing nvu worked ok.

<p> Trying to upgrade a bunch of other stuff resulted in a conflict between some libraries used by evince.
I had to endure the usual abuse before getting the clues I needed in the #debian channel: <a href="http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=327145">#327145: gnome-desktop-environment: unsatisfiable dependencies</a>. So I had to remove the <tt>gnome</tt> and <tt>gnome-desktop-environment</tt> packages.

<p> <p> tags: rdf, semantic web, calendar, debian
