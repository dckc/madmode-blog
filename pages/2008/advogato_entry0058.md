title: struggling to get my data out of Zope
date: 2008-12-08
tags: []
published: true

<b>struggling to get my data out of Zope</b>

<p> I found a <a href="http://www.zopelabs.com/cookbook/1054240694">recipe
for iterating over the contents of a Zope store</a>. It
looks promising, but I'm not wining yet. My zope instance
was built with zope 2.7 but the
debian server has 2.9 now; 2.7 doesn't even show up in an
apt-cache search.

<p> This job of migrating dm93.org from Zope was pending an
alternative to Zope for family calendar storage. Now that my
wife's laptop runs Leopard, google calendar works as a host.

<p> Then I somehow lost root when poeple.w3.org was upgraded or
something, and I just recently got around to asking thru
channels to get it back.

<p> Time to swap this job out, I think; here's my current state:

<p> <pre>
connolly@flanders:~$
INSTANCE_HOME=/var/lib/zope2.7/instance-dm93-disabled
PYTHONPATH=/usr/lib/zope2.9/lib/python python
Python 2.4.4 (#2, Oct 22 2008, 19:52:44) 
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2
Type "help", "copyright", "credits" or "license" for more
information.
&gt;&gt;&gt; from Zope2 import app
&gt;&gt;&gt; root=app()
/u2/connolly/dm93/Products/LocalFS/LocalFS.py:51:
DeprecationWarning: Using OFS.content_types is deprecated
(will be removed in Zope 2.11). Instead use
zope.app.contenttypes.
  from OFS.content_types import find_binary
No handlers could be found for logger "Zope"
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in ?
  File "/usr/lib/zope2.9/lib/python/Zope2/__init__.py", line
51, in app
    startup()
  File "/usr/lib/zope2.9/lib/python/Zope2/__init__.py", line
47, in startup
    _startup()
  File "/usr/lib/zope2.9/lib/python/Zope2/App/startup.py",
line 46, in startup
    OFS.Application.import_products()
  File "/usr/lib/zope2.9/lib/python/OFS/Application.py",
line 685, in import_products
    import_product(product_dir, product_name,
raise_exc=debug_mode)
  File "/usr/lib/zope2.9/lib/python/OFS/Application.py",
line 723, in import_product
    raise sys.exc_info()
KeyError
&gt;&gt;&gt; 
</pre>
