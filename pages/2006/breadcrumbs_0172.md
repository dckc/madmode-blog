date: 2006-11-16
title: 'A new Basketball season brings a new episode in the personal information disaster'
published: True
tags: ['breadcrumbs']

<div>
<p>Basketball season is here. Time to copy my son's schedule to my PDA.
The organization that runs the league has their schedules online. (<em>yay!</em>) in HTML. (<em>yay!</em>). But with events separated by all &lt;br>s rather than enclosed in elements. (<em>whimper</em>). Even after running it thru tidy, it looks like:</p>

<pre>
&lt;br />
&lt;b>Event Date:&lt;/b> Wednesday,&#160;11/15/2006&lt;br>
&lt;b>Start Time:&lt;/b> 8:15&lt;br />
&lt;b>End Time:&lt;/b> 9:30&lt;br />
...
&lt;br />
&lt;b>Event Date:&lt;/b> Wednesday,&#160;11/8/2006&lt;br />
&lt;b>Start Time:&lt;/b> 8:15&lt;br />
</pre>

<p>So much for XSLT. Time for a nasty perl hack.</p>

<p>Or maybe not. Between my
<a href="http://www.advogato.org/person/connolly/diary.html?start=44">no more undocumented, untested code</a> new year's resolution and
the maturity of the python libraries,
my usual <a
href="http://www.python.org/doc/lib/module-doctest.html">doctest</a>-driven
development worked fine; I was able to generate JSON-shaped structures
without hitting that <q>oh screw it; I'll just
use perl</q> point; the gist of the code is:</p>

<pre>
def main(argv):
    dataf, tplf = argv[1], argv[2]
    tpl = kid.Template(file=tplf)
    tpl.events = eachEvent(file(dataf))

    for s in tpl.generate(output='xml', encoding='utf-8'):
        sys.stdout.write(s)

def eachEvent(lines):
    """turn an iterator over lines into an iterator over events
    """
    for l in lines:
        if 'Last Name' in l:
            surname = findName(l)
            e = mkobj("practice", "Practice w/%s" % surname)
        elif 'Event Date' in l:
            if 'dtstart' in e:
                yield e
                e = mkobj("practice", "Practice w/%s" % surname)
            e['date'] = findDate(l)
        elif 'Start Time' in l:
            e['dtstart'] = e['date'] + "T" + findTime(l)
        elif 'End Time' in l:
            e['dtend'] = e['date'] + "T" + findTime(l)

next = 0
def mkobj(pfx, summary):
    global next
    next += 1
    return {'id': "%s%d" % (pfx, next),
            'summary': summary,
            }

def findTime(s):
    """
    >>> findTime("&lt;b>Start Time:&lt;/b> 8:15&lt;br />")
    '20:15:00'
    >>> findTime("&lt;b>End Time:&lt;/b> 9:30&lt;br />")
    '21:30:00'
    """
    m = re.search(r"(\d+):(\d+)", s)
    hh, mm = int(m.group(1)), int(m.group(2))
    return "%02d:%02d:00" % (hh + 12, mm)

...
</pre>

<p>It uses
my <a href="http://dev.w3.org/cvsweb/2001/palmagent/">palmagent</a>
hackery: <tt>event-rdf.kid</tt> to produce RDF/XML
which <tt>hipAgent.py</tt> can upload to my PDA. I also used the <tt>event.kid</tt> template to generate an hCalendar/XHTML version for archival purposes, though I didn't use that directly to feed my PDA.</p>


<p>The development took half an hour or so squeezed into this morning:</p>

<pre>
changeset:   5:7d455f25b0cc
user:        Dan Connolly http://www.w3.org/People/Connolly/
date:        Thu Nov 16 11:31:07 2006 -0600
summary:     id, seconds in time, etc.

changeset:   2:2b38765cec0f
user:        Dan Connolly http://www.w3.org/People/Connolly/
date:        Thu Nov 16 09:23:15 2006 -0600
summary:     finds date, dtstart, dtend, and location of each event

changeset:   1:e208314f21b2
user:        Dan Connolly http://www.w3.org/People/Connolly/
date:        Thu Nov 16 09:08:01 2006 -0600
summary:     finds dates of each event

</pre>
</div>

