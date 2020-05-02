title: 30 Apr 2007
date: 2007-04-30
tags: []
published: true

My desktop PC is a frankenstein, with parts from here and
there. It has been crashing and
hanging once a week or so since December, and I was getting
clues in <tt>#hardware</tt> on <a
href="http://freenode.net/">FreeNode</a> about how to
diagnose power supply problems. 

<p> "Put the multimeter away and get yourself a new PC," the
systems guys at W3C told me. Still, it wasn't
until about a month of  
<a href="http://del.icio.us/connolly/hardware">research on
PC hardware</a> that I outsourced the decision to Brian at
the local Micro Center. "I want a quiet machine," I told him.

<p> It came down to a choice between two HP Pavilion machines;
the <a
href="http://h10025.www1.hp.com/ewfrf/wc/product?product=3377275&lc=en&cc=us&dlc=en&submit.y=0&submit.x=0&lang=en&cc=us">a6030n</a>
with <a href="http://en.wikipedia.org/wiki/Amd_live">AMD
Live!</a> (Athlon 64 X2 etc.) and the <a
href="http://www.microcenter.com/single_product_results.phtml?product_id=0257400">a6040n</a>
with <a
href="http://en.wikipedia.org/wiki/Intel_Viiv">Intel
Viiv</a> (Core 2 Duo etc.). I picked the AMD machine...
partly because the
cheaper CPU lets them include 2x the RAM for the same price
or a little less... but partly because Intel is the market
leader and I like to root for the underdog.

<p> I didn't open the box right away when I got it home, because
I wanted to research it just a bit more during the 7 day
return period without risking a restocking fee.
I had some buyer's remorse when I remembered that "at
present the <a href="http://xorg.freedesktop.org/wiki/nv">nv
driver</a> has no 3D acceleration."

<p> I'm still wrestling with so many choices:

<p> <ul>
<li>stick with debian or switch to Ubuntu for integration
and support?
<li>stick with debian sid or switch to a more stable
release?
<p>I used to get a few dozen updates when I'd apt-get
upgrade after my once-a-month business trip; now it seems
that there are hundreds of updates every week; what's going
on?
<li>Install <a
href="http://en.wikipedia.org/wiki/X86-64">x86-64/amd64</a>
packages or stick with i386?
<li>stick with LVM or use the more typical fixed-size
partitions?
<li>stay with reiserfs or go back to ext3?
</ul>

<p> I picked Ubuntu and amd64, at least for starters. I didn't
realize I needed the
alternate CD image to do LVM until <em>after</em> I had
downloaded the desktop image.

<p> The live CD feature is pretty nifty, though it takes longer
to come up than a text installer, which starts to add up if
you're restarting the install as much as I am. I thought
maybe a USB flash disk would be faster than a CD, but it
doesn't seem to be. I guess speed varies quite a bit with
those things, and the one I was using was a very cheap one.

<p> I picked a goal of getting my Quicken-under-wine setup
running as a way to get a feel for the amd64/i386 issue, 
and then I realized... <em>Why am I still tied to
quicken?</em>. 
I have been noodling about <a
href="http://dig.csail.mit.edu/breadcrumbs/node/96">Quicken,
RDF, and JSON</a> for a while; why hasn't anyone done an
AJAX quicken work-alike yet? Of course, the diff/sync
problem is interesting too. The <a
href="http://ibm-slrp.sourceforge.net/">IBM Boca</a> system
looks promising. I digress... that's probably a story for my
<a
href="http://dig.csail.mit.edu/breadcrumbs/blog/2">semantic
web research blog</a> than this one.

<p> On the other hand, the <a
href="http://dig.csail.mit.edu/breadcrumbs/node/187">invited
talk by the Mercurial lead developer</a> probably belongs
here as well as there.
