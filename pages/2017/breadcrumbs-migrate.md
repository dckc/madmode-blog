title: Migrating Breadcrumbs
date: 2017-12-29
tags: [publishing, breadcrumbs, ipynb]
summary: migrating an old drupal blog
published: True

_Breadcrumbs_ was the blog of [DIG][], the Decentralized Information Group at MIT CSAIL.

[DIG]: http://dig.csail.mit.edu/

In a [2015 #microformats chat][2015], I discovered that it was down:

> DanC> grr... the blog is down. http://dig.csail.mit.edu/breadcrumbs/node/228  
> "Unable to connect to database server"  
> _DanC verifies that he has an export of his work there..._  
> DanC> interesting... my backup is evidently python pickles of XMLRPC responses from the API of that CMS (drupal?)  
>     >>> x['dateCreated']  
>     &lt;DateTime '20080306T17:00:05' at 7f20e8aef5f0>  
>     >>> x['dateCreated'].__class__  
>     &lt;class xmlrpclib.DateTime at 0x7f20e444eef0>  

[2015]: http://logs.glob.uno/?c=freenode%23microformats&s=20+Jun+2015&e=20+Jun+2015#c81549

The files are numbered:


```python
def _numbered_files(pattern='[0-9]*',
                    breadcrumbs='/home/connolly/sites/breadcrumbs'):
    from pathlib import Path
    return Path(breadcrumbs).glob(pattern)

breadcrumbs_bak = list(_numbered_files())
sorted(int(f.parts[-1]) for f in breadcrumbs_bak)[:10]
```




    [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



Each is a pickled XMLRPC response:


```python
import pickle

breadcrumbs_xmlrpc = dict((int(f.parts[-1]), pickle.load(f.open('rb'))) for f in breadcrumbs_bak)
x = breadcrumbs_xmlrpc[228]
x['title'], x['dateCreated'], x['dateCreated'].__class__
```




    ('hAudio for microformats mixtapes, in progress',
     <DateTime '20080306T17:00:05' at 7fa8242a5320>,
     <class xmlrpclib.DateTime at 0x7fa82427cf58>)



## MadMode blog pages


```python
from collections import OrderedDict
from __future__ import print_function
from sys import stderr


class BlogWriter(object):
    def __init__(self, pages):
        self._pages = pages

    def addPage(self, body, title, date, tags, published, slug):
        datestr = date.isoformat()
        headings = OrderedDict(title=repr(title),
                               date=datestr[:10],
                               tags="[%s]" % (', '.join("'%s'" % tag for tag in tags)),
                               published=published)
        header = '\n'.join(["%s: %s" % (k, v) for k, v in headings.iteritems()])
        yyyy = datestr[:4]
        page = (self._pages / yyyy / slug).with_suffix('.md')
        print("addPage: ", page, tags, file=stderr)
        with page.open('wb') as out:
            out.write(header)
            out.write('\n\n')
            out.write(body.encode('utf-8'))

def _madmode():
    from pathlib import Path

    return BlogWriter(Path('/home/connolly/sites') / 'madmode-blog' / 'pages')

mmwr = _madmode()
```


```python
from time import mktime
from datetime import datetime
import re


def drupal2md(body):
    body = body.split('</title>', 1)[1]  # remove redundant title
    body = body.replace('\r', '')  # unix newlines
    return body


def findTags(body):
    tags = []
    for txt in body.split('<'):
        if txt.startswith('a '):
            txt = txt[len('a '):]
            attrs = {}
            while '=' in txt and not txt.startswith('>'):
                name, txt = txt.split('=', 1)
                name = name.strip()
                txt = txt.strip()
                _, value, txt = txt.split('"', 2)
                attrs[name] = value
                txt = txt.strip()
            href = attrs.get('href', '')
            if 'tag' in attrs.get('rel', '') or 'del.icio.us' in href:
                if href.endswith('/'):
                    href = href[:-1]
                tags.append(href.split('/')[-1])
    return tags


for postid, item in sorted(breadcrumbs_xmlrpc.items()):
    print(postid, item['title'], file=stderr)
    dt = datetime.fromtimestamp(mktime(item['dateCreated'].timetuple()))
    tags = ['breadcrumbs'] + findTags(item['content'])
    mmwr.addPage(drupal2md(item['content']), title=item['title'], date=dt,
                 tags=tags,
                 published=True, slug='breadcrumbs_%04d' % postid)
```

    4 On OpenID and comment policies
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0004.md ['breadcrumbs']
    5 little burst of PAW demo hacking
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0005.md ['breadcrumbs']
    6 DIG blog wish list
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0006.md ['breadcrumbs', 'connolly']
    7 Fire at Southampton... hope everything's alright soon
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0007.md ['breadcrumbs']
    8 Sourceforge is the place... to sell soap?
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0008.md ['breadcrumbs']
    9 Reflecting blog structure into the Semantic Web with SIOC?
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0009.md ['breadcrumbs']
    10 I'd rather be...
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0010.md ['breadcrumbs']
    11 PHP angst
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0011.md ['breadcrumbs']
    12 Shopping for a client-side blogging editor
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0012.md ['breadcrumbs', 'authoring']
    13 presented Issues in Semantic Web Logic to 6.898
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0013.md ['breadcrumbs']
    14 xchat RFE: "mail a log of this chat to mbox@domain" macro
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0014.md ['breadcrumbs']
    15 U.S. papertrail: the federal register
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0015.md ['breadcrumbs']
    16 XHTML for computer science research papers and bibliographies
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0016.md ['breadcrumbs']
    17 ISWC buzz
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0017.md ['breadcrumbs']
    18 Why isn't bill payee set-up integrated with address book or yellow pages lookup?
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0018.md ['breadcrumbs']
    23 RDF Calendar, GRDDL, Microformats, and all that at XML2005 in Atlanta
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0023.md ['breadcrumbs', 'quality']
    24 SKOS, SIOC, and drupal taxonomy
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0024.md ['breadcrumbs']
    25 sorry about overriding your font size
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0025.md ['breadcrumbs']
    26 Ray Ozzie's take on diff/sync
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0026.md ['breadcrumbs']
    27 a fly-by of XACML
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0027.md ['breadcrumbs']
    28 MathML as a rule interchange format
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0028.md ['breadcrumbs']
    29 GRDDL transform wanted: National Information Exchange Model (NIEM)
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0029.md ['breadcrumbs']
    30 Go-Karting rush tainted by lack of OpenID for bug reporting about hypertext editing
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0030.md ['breadcrumbs']
    45 Toward richtext syndicated feed
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0045.md ['breadcrumbs']
    46 Toward better documentation of some schemas for the W3C digital library
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0046.md ['breadcrumbs']
    47 Brought my hockey skates with me this time
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0047.md ['breadcrumbs']
    52 Connecting DIG Student Projects to the MIT UROP listing
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0052.md ['breadcrumbs']
    55 Drupal, OpenID, and the Mac OS X Keychain
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0055.md ['breadcrumbs']
    56 Wikicompany?
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0056.md ['breadcrumbs']
    57 upgrade to CivicSpace?
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0057.md ['breadcrumbs']
    61 frbr:embodiment is enough without frbr:embodimentOf, no?
    addPage:  /home/connolly/sites/madmode-blog/pages/2005/breadcrumbs_0061.md ['breadcrumbs']
    63 On Google, Jabber, and Jingle and good and evil in IM and IP networks
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0063.md ['breadcrumbs']
    66 Arpeggio in D, a little three chord ditty
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0066.md ['breadcrumbs']
    69 Fun with Policy Aware Web at UMD, AFS/SVN at CSAIL
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0069.md ['breadcrumbs']
    70 Using truth maintenance techniques in RDF stores?
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0070.md ['breadcrumbs']
    77 MadScientistMode
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0077.md ['breadcrumbs']
    78 RSS is dead; long live RSS
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0078.md ['breadcrumbs']
    82 python, javascript, and PHP, oh my!
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0082.md ['breadcrumbs', 'installation', 'javascript', 'python', 'quality', 'testing', 'programming']
    84 tabulator use cases: when can we meet? and PathCross
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0084.md ['breadcrumbs']
    85 bnf2turtle -- write a turtle version of an EBNF grammar
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0085.md ['breadcrumbs']
    86 formally closing the feedback loop
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0086.md ['breadcrumbs']
    87 Using RDF and OWL to model language evolution
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0087.md ['breadcrumbs']
    88 Toward integration of cwm's proof structures with InferenceWeb's PML
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0088.md ['breadcrumbs']
    89 Investigating logical reflection, constructive proof, and explicit provability
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0089.md ['breadcrumbs']
    90 Fun with Embedded RDF and DOAP for the GRDDL profile
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0090.md ['breadcrumbs']
    91 Toward Semantic Web data from Wikipedia
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0091.md ['breadcrumbs', u'connolly']
    92 Reflections on the W3C Technical Plenary week
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0092.md ['breadcrumbs', 'NCE']
    93 Getting (dis)organized for SxSWi in Austin
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0093.md ['breadcrumbs', 'Austin']
    94 Dates in drupal vs planetrdf
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0094.md ['breadcrumbs']
    96 Getting my Personal Finance data back with hCalendar and hCard
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0096.md ['breadcrumbs']
    97 A look at emerging Web security architectures from a Semantic Web perspective
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0097.md ['breadcrumbs']
    98 a quick take on Kiko, a nifty looking calendar service
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0098.md ['breadcrumbs']
    99 using JSON and templates to produce microformat data
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0099.md ['breadcrumbs']
    100 geocoding and hCards for airports from wikipedia
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0100.md ['breadcrumbs', 'geo']
    101 time, context, quoting, and reification
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0101.md ['breadcrumbs']
    102 no more life in a textarea: MozEx and emacs to the rescue!
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0102.md ['breadcrumbs']
    107 hacking soccer schedules into hCalendar and into my sidekick
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0107.md ['breadcrumbs']
    123 A step forward with python and sshagent, and a walk around gnome security tools
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0123.md ['breadcrumbs', 'web', 'policy', 'security', 'python', 'programming']
    124 Consensus and community review in open source and open standards
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0124.md ['breadcrumbs']
    127 busy day in #microformats
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0127.md ['breadcrumbs']
    129 Access control and version control: an over-constrained problem?
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0129.md ['breadcrumbs']
    130 citing W3C specs from WWW conference papers
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0130.md ['breadcrumbs']
    131 On GData, SPARQL update, and RDF Diff/Sync
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0131.md ['breadcrumbs', 'diff', 'sync', 'sparql', 'calendar', 'web+architecture']
    133 RDF, Microformats, and Javascript hacking in person at the 'tute
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0133.md ['breadcrumbs', 'mobile', 'javascript', 'microformats', 'travel', 'calendar', 'BOS', 'bos']
    135 webizing TaskJuggler
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0135.md ['breadcrumbs', 'calendar']
    139 WWW2006 in Edinburgh: Identity, Reference, and Meaning
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0139.md ['breadcrumbs', 'www2006', 'EDI', 'travel', 'web+architecture', 'URI']
    140 Exporting databases in the Semantic Web with SPARQL, D2R, dbview, ARC, and such
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0140.md ['breadcrumbs', 'www2006', 'EDI', 'travel', 'sparql']
    141 Equality and inconsistency in the rules layer
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0141.md ['breadcrumbs']
    142 fun with flock
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0142.md ['breadcrumbs', u'flock', u'writing', u'editing', u'drupal']
    146 converting vcard .vcf syntax to hcard and catching up on CALSIFY
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0146.md ['breadcrumbs']
    148 a walk thru the tabulator calendar view
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0148.md ['breadcrumbs', 'calendar', 'SeedApplications']
    151 Choosing flight itineraries using tabulator and data from Wikipedia
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0151.md ['breadcrumbs']
    154 OpenID, verisign, and my life: mediawiki, bugzilla, mailman, roundup, ...
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0154.md ['breadcrumbs']
    155 tabulator maps in Argentina
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0155.md ['breadcrumbs']
    156 how much do I want to know about drupal?
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0156.md ['breadcrumbs']
    157 on Wikimania 2006, from a few hundred miles away
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0157.md ['breadcrumbs']
    158 Stitching the Semantic Web together with OWL at AAAI-06
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0158.md ['breadcrumbs', 'RdfAndSql', 'AAAI', 'public-sparql-dev', 'citation']
    159 On the Future of Research Libraries at U.T. Austin
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0159.md ['breadcrumbs', 'Austin', 'URI', 'web+architecture']
    160 ACL 2 seminar at U.T. Austin: Toward proof exchange in the Semantic Web
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0160.md ['breadcrumbs', 'Austin', 'semantic', 'web', 'logic', 'research']
    161 Talking with U.T. Austin students about the Microformats, Drug Discovery, the Tabulator, and the Semantic Web
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0161.md ['breadcrumbs', 'Austin', 'semantic', 'web']
    162 Wishing for XOXO microformat support in OmniOutliner
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0162.md ['breadcrumbs']
    163 Trip reporting with flock
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0163.md ['breadcrumbs']
    164 Adding Shoenfield, Brachman books to my bookshelf?
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0164.md ['breadcrumbs']
    165 Now is a good time to try the tabulator
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0165.md ['breadcrumbs']
    171 Celebrating OWL interoperability and spec quality
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0171.md ['breadcrumbs']
    172 A new Basketball season brings a new episode in the personal information disaster
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0172.md ['breadcrumbs']
    178 Modelling HTTP cache configuration in the Semantic Web
    addPage:  /home/connolly/sites/madmode-blog/pages/2006/breadcrumbs_0178.md ['breadcrumbs']
    179 She's a witch and I have the proof (in N3)
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0179.md ['breadcrumbs']
    180 A design for web content labels built from GRDDL and rules
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0180.md ['breadcrumbs']
    187 The Mercurial SCM: great for lots of stuff, but not the holy grail
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0187.md ['breadcrumbs', 'python+scm']
    192 Collaboration and crime at a distance at HASTAC, WWW2007
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0192.md ['breadcrumbs', 'openid', 'hastac', 'Duke', 'RDU', 'digital+media']
    193 IKL by Hayes et al. provides a semantics for N3?
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0193.md ['breadcrumbs']
    194 Linked Data at WWW2007: GRDDL, SPARQL, and Wikipedia, oh my!
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0194.md ['breadcrumbs', u'banff', u'grddl', u'www2007', u'travel']
    198 Units of measure and property chaining
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0198.md ['breadcrumbs']
    201 Soccer schedules, flight itineraries, timezones, and python web frameworks
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0201.md ['breadcrumbs']
    206 FOAF and OpenID: two great tastes that taste great together
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0206.md ['breadcrumbs']
    207 brainstorming, issue tracking, and problem reporting... with tabulator?
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0207.md ['breadcrumbs']
    214 Free Culture: Why buy the Amazon Kindle when you can give and get an OLPC XO-1 for the same price?
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0214.md ['breadcrumbs']
    221 I can only imagine...
    addPage:  /home/connolly/sites/madmode-blog/pages/2007/breadcrumbs_0221.md ['breadcrumbs']
    228 hAudio for microformats mixtapes, in progress
    addPage:  /home/connolly/sites/madmode-blog/pages/2008/breadcrumbs_0228.md ['breadcrumbs']
    229 sidekick calendar subscription for SXSW
    addPage:  /home/connolly/sites/madmode-blog/pages/2008/breadcrumbs_0229.md ['breadcrumbs']
    240 The details of data in documents; GRDDL, profiles, and HTML5
    addPage:  /home/connolly/sites/madmode-blog/pages/2008/breadcrumbs_0240.md ['breadcrumbs']
    246 OpenID "Hello World" on apache still deep magic
    addPage:  /home/connolly/sites/madmode-blog/pages/2009/breadcrumbs_0246.md ['breadcrumbs']
    250 DIG losing the battle with spammers again
    addPage:  /home/connolly/sites/madmode-blog/pages/2009/breadcrumbs_0250.md ['breadcrumbs']
    251 migrating from danger/sidekick to android/G1
    addPage:  /home/connolly/sites/madmode-blog/pages/2009/breadcrumbs_0251.md ['breadcrumbs']
    252 Existentials in ACL2 and Milawa make sense; how about level breakers?
    addPage:  /home/connolly/sites/madmode-blog/pages/2010/breadcrumbs_0252.md ['breadcrumbs']
    253 Map and Territory in RDF APIs
    addPage:  /home/connolly/sites/madmode-blog/pages/2010/breadcrumbs_0253.md ['breadcrumbs']


## PyData Tools


```python
import pandas as pd
dict(pandas=pd.__version__)
```




    {'pandas': u'0.17.1'}




```python
items = pd.DataFrame.from_records(breadcrumbs_xmlrpc.values())
items.postid = items.postid.astype(int)
items = items.set_index('postid')
print(items.dtypes)
items[['title', 'dateCreated']].sort_values('dateCreated').head()
```

    content              object
    dateCreated          object
    description          object
    link                 object
    mt_allow_comments     int64
    mt_convert_breaks    object
    permaLink            object
    title                object
    userid               object
    dtype: object





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>dateCreated</th>
    </tr>
    <tr>
      <th>postid</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>On OpenID and comment policies</td>
      <td>20051024T23:28:49</td>
    </tr>
    <tr>
      <th>5</th>
      <td>little burst of PAW demo hacking</td>
      <td>20051026T20:12:18</td>
    </tr>
    <tr>
      <th>6</th>
      <td>DIG blog wish list</td>
      <td>20051026T20:14:27</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Fire at Southampton... hope everything's alrig...</td>
      <td>20051031T11:59:08</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Reflecting blog structure into the Semantic We...</td>
      <td>20051031T13:18:51</td>
    </tr>
  </tbody>
</table>
</div>




```python
items.loc[[228], ['title', 'dateCreated']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>dateCreated</th>
    </tr>
    <tr>
      <th>postid</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>228</th>
      <td>hAudio for microformats mixtapes, in progress</td>
      <td>20080306T17:00:05</td>
    </tr>
  </tbody>
</table>
</div>


