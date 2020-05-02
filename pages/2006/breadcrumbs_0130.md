date: 2006-04-25
title: 'citing W3C specs from WWW conference papers'
published: True
tags: ['breadcrumbs']

<div>
<p>As I said in a <a href="http://lists.w3.org/Archives/Public/www-rdf-interest/2000Jul/0020.html">July 2000 message to www-rdf-interest</a>:
</p>

<blockquote>
<p>
There are very few data formats I trust... when I use
when I use
the computer to capture my knowledge, I pretty
much stick to plain text, XML (esp XHTML, or at least HTML that
tidy can turn into XHTML for me), RCS/CVS, and RFC822/MIME.
I use JPG, PNG, and PDF if I must,
but not for capturing knowledge for exchange, revision, etc.
</p>
</blockquote>

<p>And as I explained in a <a
href="http://www.w3.org/People/Connolly/drafts/html-essay">1994
essay</a>, converting from LaTeX is hard, so I try not to write in
LaTeX either.</p>

<p>The <a href="http://www2006.org/">Web conference</a> has
instructions for submitting <a
href="http://www.sheridanprinting.com/typedept/www.htm">PDF using
LaTeX or MS Word</a> and (<em>finally!</em>) for submitting <a
href="http://www.ecs.soton.ac.uk/~tmb/www2006-xhtml.html">XHTML</a>.
(The <a href="http://www.ecs.soton.ac.uk/~tmb/iw3c2.css">WWW2006 paper
CSS stylesheet</a> is horrible... who wants to read 9pt times on
screen?!?! Anyway...)  So when the <a
href="http://www.ibiblio.org/hhalpin/irw2006/">IRW 2006</a> organizers
told me they'd like a PDF version of <a
href="http://www.w3.org/2006/04/irw65/urisym">my paper</a> in that
style, I dusted off my <cite><a
href="http://www.w3.org/2004/04/xhlt91/">Transforming XHTML to LaTeX
and BibTeX</a></cite> tools and got to work.</p>

<p>My paper cites a number of W3C specs, including <a
href="http://www.w3.org/TR/1999/REC-html401-19991224">HTML 4</a>.  The
<a href="http://www.w3.org/TR/">W3C tech reports index/digital
library</a> has an associated <a
href="http://www.w3.org/2002/01/tr-automation/tr-biblio-ui">bibliography
generator</a>. I fed it <tt>http://www.w3.org/TR/html401</tt> and it
generated a nice bibliographic reference from an RDF data set.  I'm
interested in the ongoing <a
href="http://microformats.org/wiki/citation-formats">citation
microformats work</a> that might make that transformation lossless, since
I need not just XHTML, but BibTex. What I'm doing currently is 
adding some bibtex vocabulary in <tt>class</tt> and <tt>rel</tt> attributes:
</p>

<pre>
&lt;dt class="TechReport">
&lt;a name="HTML4" id="HTML4">[HTML4]&lt;/a>
&lt;/dt>

&lt;dd>&lt;span class="author">Le Hors, Arnaud and Raggett, Dave and
Jacobs, Ian&lt;/span> Editors,
&lt;cite> &lt;a
href="http://www.w3.org/TR/1999/REC-html401-19991224">HTML 4.01
Specification&lt;/a> &lt;/cite>,
&lt;span class="institution">W3C&lt;/span> Recommendation,
24 &lt;span class="month">December&lt;/span> &lt;span class="year">1999&lt;/span>,
&lt;tt class="number">http://www.w3.org/TR/1999/REC-html401-19991224&lt;/tt>.
&lt;a href="http://www.w3.org/TR/html401" title="Latest version of
HTML 4.01 Specification">Latest version&lt;/a> available at
http://www.w3.org/TR/html401 .&lt;/dd>

</pre>

<p>When run thru my xh2bib.xsl, out comes:</p>

<pre>
@TechReport{HTML4,
title = "{
HTML 4.01 Specification
}",
    author = {Le Hors, Arnaud
and Raggett, Dave
and Jacobs, Ian},
    institution = {W3C},
    month = {December},
    year = {1999},
    number = {http://www.w3.org/TR/1999/REC-html401-19991224},
    howpublished = { \url{http://www.w3.org/TR/1999/REC-html401-19991224} }
}
</pre>

<p>I think I should be using <tt>editor =</tt> rather than <tt>author
=</tt> but that didn't work the 1st time I tried and I haven't
investigated further.</p>

<p>In any case, I'm reasonably happy with the <a
href="http://www.w3.org/2006/04/irw65/urisym.pdf">PDF output</a>.</p>
</div>
