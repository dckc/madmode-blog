published: False

in #plone on FreeNode:

--- #plone :http://plone.org/
<DanC> I'm trying to migrate some photos etc. out of a very old Zope DB. It ran on Zope 2.7.7. Building Zope2.7.7 says "install python 2.3.5". Building python2.3.5 leads to a core dump https://gist.github.com/4477717
   clues?

<supton> DanC: OS platform?
<DanC> Ubuntu 12.04
<-- toutpt has quit (Quit: toutpt)
<supton> DanC: google says https://github.com/utahta/pythonbrew/issues/84

Ori Peleg (orip) wrote on 2008-11-05:	 #4
There's a workaround without disabling optimization: http://orip.org/2008/10/building-python-235-on-ubuntu-intrepid.html

Short version: add BASECFLAGS=-U_FORTIFY_SOURCE to the 'configure' command line.
https://bugs.launchpad.net/ubuntu/+source/gcc-defaults/+bug/286334
<-
https://github.com/utahta/pythonbrew/issues/84

no longer happy with my personal wiki
10 Jun 2005 connolly
http://www.advogato.org/person/connolly/diary/25.html

struggling to get my data out of Zope
8 Dec 2008 connolly
http://www.advogato.org/person/connolly/diary/58.html


connolly@flanders:~/src$ du -sh Zope-2.7.7-final/
32M	Zope-2.7.7-final/
connolly@flanders:~/src$ ls -ld Zope-2.7.7-final/
drwxr-xr-x 10 connolly www 4096 Dec 21  2008 Zope-2.7.7-final/
-rw-r--r-- 1 connolly www  1103 Jul 10  2005 README.txt

connolly@pav:~/src$ rsync -av dm93.org:src/Zope-2.7.7-final/ Zope-2.7.7-final/
...
sent 62053 bytes  received 22922766 bytes  779146.41 bytes/sec
total size is 22698447  speedup is 0.99


road not taken:

# Python package index requirements for zope-rescue
#
# In progress
# for notes, see logs of #swig on FreeNode for Jan 7
# http://chatlogs.planetrdf.com/swig/2013-01-07#T19-37-12
#
# Usage:
# Making a virtual environment is recommended:
#  % mkdir zenv
#  % cd zenv
#  % virtualenv .
#  % . bin/activate
#
# Then:
#  (zenv)% pip install -r requirements.txt

#Zope2

# After installing Zope2, I got:
#    from zope.location.interfaces import IPossibleSite
# ImportError: cannot import name IPossibleSite

# Thanks to maurits Jul 2012 http://stackoverflow.com/a/11546162 :
# http://download.zope.org/Zope2/index/2.13.19/versions.cfg
# No Joy there either

# from http://www.roxburgh.net/projects/squeezezope/ :
# virtualenv -p python2.6 --no-site-packages zope2.12
# cd zope2.12
# bin/easy_install-2.6 -i http://download.zope.org/Zope2/index/2.12.5 Zope2
#
# Well, something's not right:
#   File "/home/connolly/zenv/local/lib/python2.7/site-packages/Zope2-2.12.5-py2.7-linux-x86_64.egg/Zope2/App/startup.py", line 71, in startup
#     DB = dbtab.getDatabase('/', is_root=1)
#AttributeError: 'NoneType' object has no attribute 'getDatabase'

# I found my earlier work; it's based on Zope-2.7.7-final
# 
# 66876823e53fbd0d4a8a7262d7ce251b  Zope-2.7.7-final.tgz
# 2.8M Zope-2.7.7-final.tgz
# But the earliest version of Zope2 on download.zope.org is
# 2.12.0a4/               25-Apr-2009 09:58

# Let's try the current version, 
# 2.13.19/                31-Oct-2012 14:18    - 
