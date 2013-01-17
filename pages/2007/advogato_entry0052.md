title: 05 Jun 2007
date: 2007-06-05
tags: ['office', 'debian', 'ubuntu', 'linux', 'hardware']
published: true

Not only does the <a
href="http://xorg.freedesktop.org/wiki/nv">nv driver</a> not
do 3D acceleration, it doesn't seem to do 1600x1050
resolution either.

<p> <p> The nvidia module in the debian non-free section blanked
the 
screen and locked up so badly it required a reboot. When
investigating options, that gets old real fast.

<p> <p> In #debian, the channel bot said:

<p> <p> <pre>
&lt;dpkg&gt; from memory, nvidia_post_etch is update-pciids
&amp;&amp;
apt-get install module-assistant nvidia-kernel-source
&amp;&amp; m-a
prepare &amp;&amp; m-a a-i nvidia &amp;&amp; apt-get install
nvidia-glx &amp;&amp;
depmod -a &amp;&amp; modprobe nvidia &amp;&amp;
dpkg-reconfigure xserver-xorg
</pre>

<p> <p> But that produced the same symptoms.

<p> <p> Besides... debian fonts are ugly, and they seem to be
chosen by a zillion different configuration options;
it seems to be a full-time job just finding them all.

<p> <p> So I'm running Ubuntu now. I'm not sure how I feel about
that.

<p> <p> I replaced the amd64 installation with the stock
(quicken-friendly) i386 stuff.

<p> <p> It comes with evolution 2.10, I think. Slightly more
polished. I wonder if subscribing to password-protected
calendars works.

<p> <p> My code to print MS Word docs to PDF fell over; something
about templates. So I'm trying to use OpenOffice instead.
I <em>almost</em> got it working. Let's see if ubuntu
support will help me out with this...

<p> <p> <a
href="https://bugs.launchpad.net/ubuntu/+source/openoffice.org/+bug/118789">Bug
#118789: trouble using ExportFormFields in uno API; PDF form
controls are exported even when set to False</a>

<p> tags: <a rel="tag"
href="http://del.icio.us/connolly/office">office</a>,
<a rel="tag"
href="http://del.icio.us/connolly/debian">debian</a>,
<a rel="tag"
href="http://del.icio.us/connolly/ubuntu">ubuntu</a>,
<a rel="tag" href="http://del.icio.us/connolly/linux">linux</a>,
<a rel="tag"
href="http://del.icio.us/connolly/hardware">hardware</a>,
