title: Using hCard, XSLT, and RDF to sync the family cellphones
date: 2005-06-26
tags: ['mobile', 'contacts', 'microformats']
published: true

<b>Using hCard, XSLT, and RDF to sync the family cellphones</b>

<p> Mary got a new Motorola V188, which iSync supports. Buoyed by the success of moving the kitchen calendar from paper to iCal, I took her paper address book and keyed it into Apple's addressbook. Now I want to sync (or at least copy) several of the categories (family, medical) from the contacts in my gizmo to hers.

<p> In <a href="http://dev.w3.org/cvsweb/2001/palmagent/" rel="tag">palmagent</a>, <tt>dangerSync.py</tt> produces <tt>contact.rdf</tt>; I could use N3 rules to convert that to a vCard RDF vocabulary, and then do a syntactic RDF to vCard syntactic transform, but I'm a little down on N3 rules lately; the rules I use to process my calendar are  <em>really</em> slow. I have been thinking about having <tt>dangerSync.py</tt> spit out .ics format directly. Or maybe having it spit out RDF diffs is the way to go...


<p> Meanwhile, there's <a href="http://developers.technorati.com/wiki/hCard">hCard</a>, whence comes <a href="http://suda.co.uk/projects/X2V/">X2V</a> including <tt>xhtml2vcard.xsl</tt>. And I'm a big fan of using XHTML to archive important data anyway, so I think I'll write some XSLT to convert <tt>contact.rdf</tt> to XHTML and then use <tt>xhtml2vcard.xsl</tt> to get vcard syntax.

<p> <em>grumble... advogato diary entries don't have titles, do they?</em>

<p> <b>Tags</b>: <a href="http://developers.technorati.com/wiki/hCard">hCard</a>, <a rel="tag" href="http://dm93.org/z2001/WearableGizmo">WearableGizmo</a>, <a href="http://dev.w3.org/cvsweb/2001/palmagent/" rel="tag">palmagent</a>, <a href="http://www.w3.org/DesignIssues/Diff">RDF diff/sync</a>, <a rel="tag" href="http://groups.csail.mit.edu/dig/">DIG</a>
