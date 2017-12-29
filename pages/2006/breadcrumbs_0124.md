date: 2006-04-06
title: 'Consensus and community review in open source and open standards'
published: True
tags: ['breadcrumbs']

<div>

<p>Consensus is a core value of <a href="http://www.w3.org/" title="World Wide Web Consortium">W3C</a> and lots of other open standards
and open source communities.  I used to think that a decision where
almost everybody agreed except a few objectors was an example of
consensus. That was based on my experience in the <a href="http://www.ietf.org/" title="Internet Engineering Task Force">IETF</a>, with its
"rough consensus and running code" mantra. Then I learned that this is
quite a stretch with respect to the normal dictionary meaning of
"consensus".</p>

<p>The debian community seems to be examining the meaning of "consensus":</p>

<blockquote>

<p>Many things are done on behalf of the project without every
individual member supporting them - for instance, Mark is vigorously
opposed to Debian UK being granted a trademark license, even though
Branden (and therefore the project) granted one. The key difference
here is the difference between consensus and unanimity.</p>

<address><a href="http://mjg59.livejournal.com/60764.html?mode=reply">Matthew Garrett 2006-04-04 </a></address>
</blockquote>

<p>Definitions of "consensus" vary. The <a
href="http://en.wikipedia.org/wiki/Consensus">wikipedia article on
consensus</a> has a good synthesis: <q> Achieving consensus requires
serious treatment of every group member's considered opinion.</q></p>

<p><a
href="http://www.w3.org/2005/10/Process-20051014/policies.html#Consensus">W3C's
consensus policy</a> formally distinguishes the case of even one
objection from consensus:</p>

<blockquote>
<p>The following terms are used in this document to describe the level of support for a decision among a set of eligible individuals:</p>

<ol>
   <li> Consensus: A substantial number of individuals in the set support the decision and nobody in the set registers a Formal Objection. Individuals in the set may abstain. Abstention is either an explicit expression of no opinion or silence by an individual in the set. Unanimity is the particular case of consensus where all individuals in the set support the decision (i.e., no individual in the set abstains).</li>
   <li>Dissent: At least one individual in the set registers a Formal Objection.</li>
</ol>

<p>...</p>

<p>In some cases, even after careful consideration of all points of
view, a group might find itself unable to reach consensus. The Chair
<strong>may</strong> record a decision where there is dissent (i.e.,
there is at least one Formal Objection) so that the group may make
progress (for example, to produce a deliverable in a timely
manner). Dissenters cannot stop a group's work simply by saying that
they cannot live with a decision. When the Chair believes that the
Group has duly considered the legitimate concerns of dissenters as far
as is possible and reasonable, the group <strong>should</strong> move
on.</p>

</blockquote>

<p>That last bit is important, since "you can't schedule consensus,"
another lesson I learned from Michael Sperberg-McQueen. And we do try
to schedule our deliverables.</p>

<p>The RDF Data Access Working Group (<a
href="http://www.w3.org/2001/sw/DataAccess/">DAWG</a>) has been
working on SPARQL for quite a while now. Our first public release was
October 2004. Since then, we have handled <a href="http://lists.w3.org/Archives/Public/public-rdf-dawg-comments/">comments</a> from a few dozen
people and tried to reach consensus with them.  We weren't always
successful. Our <a
href="http://www.w3.org/2001/sw/DataAccess/crq349">request for
Candidate Recommendation</a> shows the outstanding formal objections,
each one of which got reviewed by The Director. Though W3C did grant
that request for Candidate Recommendation status for SPARQL today
(yay!), we need to go back over some of the comments and make test
cases and maybe some clarifications. I hope that, in the process, we
can address some of the concerns of those with formal objections and
achieve consensus with them.</p>

<p>Also, I remember a time <em>though I can't confirm from <cite><a
href="http://www.ietf.org/tao.html">The Tao of IETF</a></cite> or any
of the other records that I searched</em> when people and companies
who wanted to deploy new technology on the Internet were expected to
submit their proposal for community review before deploying widely.  I
wrote a <a
href="http://lists.w3.org/Archives/Public/www-tag/2005Apr/0033">message
on squatting on link relationship names, x-tokens, registries, and URI-based extensibility</a> to www-tag in April 2005, with concerns about
several mechanisms which were deployed, some at
giga-scale, as far I can tell, without any community review. I think I'll repeat just about the whole thing:</p>

<hr />

<p>When somebody wants to deploy a new idiom or a new term in the
Web, they're more than welcome to make up a URI for it...</p>

<blockquote>
<p>"[URI] is an agreement about how the Internet community allocates names
and associates them with the resources they identify."</p>
<address><a href="http://www.w3.org/TR/webarch/#id-resources">webarch</a>
</address>
</blockquote>

<p>We particularly encourage this for XML vocabularies...</p>

<blockquote>
<p>The purpose of an XML namespace (defined in [XMLNS]) is to allow the
deployment of XML vocabularies (in which element and attribute names are
defined) in a global environment and to reduce the risk of name
collisions in a given document when vocabularies are combined."</p>
<address><a href="http://www.w3.org/TR/webarch/#xml-namespaces">webarch</a>
</address>
</blockquote>

<p>But while making up a URI is pretty straightforward, it's more
trouble than not bothering at all. And people usually don't do any
more work than they have to.</p>

<p>There is a time and a place for just using short strings, but
since short strings are scarce resources shared by the global
community, fair and open processes should be used to manage them.
Witness TCP/IP ports, HTML element names, Unicode characters, and
domain names and trademarks -- different processes, with
different escalation and enforcement mechanisms, but all accepted
as fair by the global community, more or less, I think.</p>

<p>The IETF has a tradition of reserving
tokens starting with "x-" for experimental use, with the expectation
that they'll shed the x- prefix as they're registered by IANA.
But it's not really clear how that transition happens.</p>

<p>Witness <tt>application/x-www-form-urlencoded</tt>. A horrible name, perhaps,
but nobody has enough motivation to change it. It's been all the
way thru the W3C process... twice now: once for HTML 4 and again
in XForms. Hmm... I wonder if it's <a href="http://www.iana.org/assignments/media-types/application/">registered</a>... nope.</p>


<p>A pattern that I'd like to see more of is</p>
<ol>
  <li> start with a URI for a new term</li>
  <li> if it picks up steam, introduce a synonym that
     is a short string thru a fair/open process</li>
</ol>

<p>I'm not sure where the motivation to complete step 2 will come
from, but if it doesn't come at all, that's OK. Stopping with a
URI term is a lot better than getting stuck with something
like x-www-form-urlencoded.</p>

<p>Lately I'm seeing quite the opposite. The HTML specification
includes a <a href="http://www.w3.org/TR/1999/REC-html401-19991224/struct/global.html#h-7.4.4.3">hook</a> for grounding link relationships in URI space, but people aren't using it:</p>

<blockquote>
<p>when Google sees the attribute (rel="nofollow") on hyperlinks, those
links won't get any credit when we rank websites in our search results.</p>
<address><a href="http://www.google.com/googleblog/2005/01/preventing-comment-spam.html">google Jan 2005 announcement</a></address>
</blockquote>

<blockquote>
<p>By adding <tt>rel="tag"</tt> to a hyperlink, a page indicates that the
destination of that hyperlink is an author-designated "tag" (or
keyword/subject) of the current page."</p>
<address><a href="http://developers.technorati.com/wiki/RelTag">technorati RelTag</a></address>
</blockquote>

<blockquote>
<p>What are the prefetching hints?</p>
        
<p>The browser looks for either an HTML &lt;link> tag or an HTTP Link:
        header with a relation type of either next or prefetch.</p>
<address><a href="http://www.mozilla.org/projects/netlib/Link_Prefetching_FAQ.html">mozilla prefetching FAQ</a>
</address>
</blockquote>

<p>Google is sufficiently influential that they form a critical mass
for deploying these things all by themselves. While Google enjoys
a good reputation these days, and the community isn't complaining
much, I don't think what they're doing is fair. Other companies
with similarly influential positions used to play this game
with HTML element names, and I think the community is decided
that it's not fair or even much fun.</p>

<p>Deployment of the technorati RelTag thingy seems much more
grass-roots, peer-to-peer. But even so, it's only a matter
of time before we see a name clash. So perhaps it's fair,
but it doesn't seem wise.</p>

<p>I think all three of these are cases of squatting on the
community resource of link relationship names.</p>

<p>Should all new link relationships go thru the W3C HTML Working
Group? No, of course not. The profile mechanism is there
to decentralize the process.</p>

<p>Should W3C run a registry of link relationship names?
That seems boring and inefficient, to me. It can't possibly
cost less time and effort to apply for a W3C-registered
link relationship name than it can to reserve a domain name
and run a web server, can it?</p>

<p>If Google and Mozilla really
want the community agree to these short names, I'd be
happy to see them use the <a href="http://www.w3.org/Submission/">W3C member submissions process</a>.</p>


</div>

