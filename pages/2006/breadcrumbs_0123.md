date: 2006-03-29
title: 'A step forward with python and sshagent, and a walk around gnome security tools'
published: True
tags: ['breadcrumbs', 'web', 'policy', 'security', 'python', 'programming']

<div>

<p>At the <a href="http://www.policyawareweb.org/2005/ftf2/paw-mtg">August PAW meeting</a>, I dropped a pointer in IRC to
 <a href="http://www.w3.org/2000/10/swap/util/sshAuth.py">sshAuth.py</a>,
my attempt to use sshagent to make
digital signatures. I started on it 2003/09,
and I banged my head against a while for quite
a while trying to get it to work.</p>


<p>Last night, while noodling on calendar synchronization and
delegation, I took another run at the problem; this time, it worked!
Thanks to <a href="http://www.lag.net/paramiko/">paramiko</a>:</p>

<pre><code>
from paramiko import Agent, RSAKey, Message
import Crypto.Util.randpool
import binascii

data = "hoopy" # data to sign
user = "connolly" # salt to taste

# get my public key
authkeys = file("/home/%s/.ssh/authorized_keys" % user)
authkeys.next() # skip 1st one
keyd = authkeys.next()
tn, uu, other = keyd.split()
keyblob = binascii.a2b_base64(uu)
pubkey = RSAKey(Message(keyblob))

pool = Crypto.Util.randpool.RandomPool()
a = Agent()
agtkey = a.get_keys()[0]
sigblob = agtkey.sign_ssh_data(pool, data)

print pubkey.verify_ssh_sig(data, Message(sigblob))
</code></pre>

<p>That <tt>skip 1st one</tt> bit took me a while to figure
out. I have 2 keys in my <tt>~/.ssh/authorized_keys</tt> file.
I wonder if <tt>sshAuth.py</tt> would work with that fix.</p>

<p>I also took a look at the state-of-the art in password agents and
managers for gnome. <a
href="http://oss.codepoet.no/revelation/">revelation</a> looks
interesting. I'm still hoping for <a
href="http://dig.csail.mit.edu/breadcrumbs/node/55">something like
OpenID/SXIP integrated with password managers like the OSX
keychain.</a></p>

<p>I took <a
href="http://chatlogs.planetrdf.com/swig/2006-03-29.html#T03-26-51">notes
in the #swig channel</a> while I was at it. I got a kick
out of this exchange:</p>

<pre> 
04:44:59 &lt;Ontogon_> dan, are you talking to yourself?
04:45:32 &lt;dajobe> he's talking to the web
</pre>


<div class="meta">tags:
 <a rel="tag" href="http://del.icio.us/connolly/web">web</a>
 <a rel="tag" href="http://del.icio.us/connolly/policy">policy</a>
 <a rel="tag" href="http://del.icio.us/connolly/security">security</a>
 <a rel="tag" href="http://del.icio.us/connolly/python">python</a>
 <a rel="tag" href="http://del.icio.us/connolly/programming">programming</a>
</div>

</div>


