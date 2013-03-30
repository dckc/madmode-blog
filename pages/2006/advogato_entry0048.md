title: appscript and office automation
date: 2006-12-08
tags: ['python', 'office', 'mac']
published: true

<p> <p> <p>
  My wife does office work for a local professional and
whenever I
  see her doing work that I know the computer could do for
her, I
  chip in. The end-of-the-month scramble is a clear case:
they take
  client reports, print them out and then manually sort them by
  officer and fax them out.

<p> <p> <p>
  Surely I could do better with <a href=
  "http://www.faxaway.com/">faxaway,</a> I thought. The only
  question was: since the reports are in MS Word and the
database
  is in FileMaker Pro, all on a Mac laptop, how much would I
have
  to sell my soul to Apple and Microsoft in the process?

<p> <p> <p>
  <a href="http://appscript.sourceforge.net/">appscript</a>
let me
  drive the process from python. I did <a
href="http://dm93.org/z2001/HyperSchool">quite a bit of
HyperTalk
  programming</a>, but somehow I'm still a bit mystified by
  AppleScript: which are the language keywords and which are the
  application vocabulary? The <a href=
 
"http://pythonmac.org/wiki/FileMakerProAppscriptingOverview">FileMakerAppscriptingOverview</a>
  made it trivial to crib bits like:

<p> <p> <pre>
    fm = app("FileMaker Pro")
    if not fm.databases[db].exists():
        fm.open(FSSpec(path % db))
        return fm.databases[db]
</pre>
<p>
FSSPec is deprecated in the <a href=
"http://developer.apple.com/documentation/Carbon/Reference/File_Manager/Reference/reference.html">
  Carbon docs</a>, but I never did figure out a replacement.

<p> <p> <p>
  appscript's integration of AppleScript references into python
  with its and con is particularly cute, but I pulled a bit
of hair
  out before I figured out how to use it:

<p> <p> <pre>
def officerFax(db, oName, cName):
    # hmm... I'm not sure why this str() is necessary...
    officers = db.tables['officers'].records[
            its.fields['name'].cellValue == str(oName)]
</pre>
<p>
  If FileMaker has a way to use real SQL, I can't find it. Plus,
  we're running a PowerPC version on an intel MacBook with only
  0.5GB of RAM. Emulating FileMaker and MS Word is using a
lot of
  RAM, I suspect. I looked into open source alternatives and
found
  that <a href=
  "http://www.openoffice.org/product/base.html">OpenOffice's
  Base</a> looks quite capable, and I'm sure oowriter would
do the
  job as an MS Word replacement. I hope the <a href=
 
"http://udk.openoffice.org/python/python-bridge.html">python-uno
  bridge</a> works on OS X so that I can switch the whole
operation
  over one of these moths.

<p> <p> <p>
  I did pay a price for not doing it The Apple Way. <a href=
  "http://developer.apple.com/qa/qa2001/qa1018.html">Technical
  Q&amp;A QA1018 Using AppleScript to send an email with an
  attachment</a> shows exactly how to attach a report to a mail
  message and send it to faxaway. I was able to create and
address
  a mail message from python/appscript, but making the
attachment
  stumped me. After verifying that the AppleScript example does
  work as advertised, I gave up and wrote a separate
  <tt>mailfaxes.py</tt> program that uses python's <a href=
  "http://docs.python.org/lib/module-email.html">email</a> and
  <a href=
  "http://docs.python.org/lib/module-smtplib.html">smtplib</a>
  modules and skips Mail.app altogether. I had to be a little
  careful since the laptop runs python2.3 and the email modules
  have been rearranged a bit in python 2.4 and 2.5, but it was
  reasonably straightforward.

<p> <p> <p>
  Driving MS Word was, predicably, even klunkier:

<p> <p> <p> <p>   <pre>
TMP="fax_job.htm"
def asHTML(w, dirpath, fname):
    """save current doc as HTML
    """
    w.do_Visual_Basic('ActiveDocument.SaveAs FileName:="%s",'
        ' FileFormat:= wdFormatHTML,'
        ' HTMLDisplayOnlyOutput:=True' % (TMP,))
</pre>
<p>
Office X has an AppleScript interface, but it's not as rich
as the Visual Basic API. I got Word to save as HTML (for
processing
with <a href=
"http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup</a>)
but I never did figure out how to tell MS Word which
directory to
put it in. I wrote a posix2mac() routine to convert
<tt>/posix/paths</tt> to <tt>::mac:paths</tt> as used in
AppleScript but that didn't help; I ended up with a hard-coded
kludge.

<p> <p> <p>
  Switching syntaxes with <tt>do_Visual_Basic</tt> is a
little bit
  painful, but when it goes bad the diagnostics are pretty good.
  "ActivePrinter is read-only on the Macintosh," it said, where
  <tt>w.active_printer = p</tt> had just failed silently. The
  modern VB.NET <a href=
 
"http://msdn2.microsoft.com/en-gb/library/microsoft.office.tools.word.document.printout(VS.80).aspx">
  PrintOut</a> documentation isn't hard to find, but it's a
little
  more tricky to find the <a href=
 
"http://msdn2.microsoft.com/en-us/library/aa279125(office.10).aspx">
  2002 PrintOut docs</a> that are more relevant. I never did get
  PrintToFile working, nor did I find a way to script the PDF
  option in Apple's print dialogs. Thank goodness for the <a
href=
 
"http://lists.apple.com/archives/Applescript-users/2006/Aug/msg00336.html">
  Appscript, Word and PDF clue</a> which pointed me to <a href=
 
"http://www.codepoetry.net/projects/cups-pdf-for-mosx">CUPS-PDF
  for Mac OS X</a>. It worked as advertised, though writing
code to
  wait for a new PDF document in ~/Desktop/cups-pdf/ was
tricky; we
  sent a number of reports to the wrong place due to a timing
  bug.

<p> <p> <p>
  The <a href=
 
"http://developer.apple.com/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_python/chapter_17_section_1.html">
  Python Bindings for Quartz 2D</a> rock; composing fax
cover pages
  couldn't be easier than this:

<p> <p> <pre>
htmltxt = coverHTML(oName, fax, subject, pages)
ctx.drawHTMLTextInRect(
        CG.CGDataProviderCreateWithString(htmltxt),
        pageRect.inset(72, 72))
</pre>
<p>
and concatenating several PDFs into one was similarly
straightforward. It doesn't hurt that faxing is Apple's example
application.

<p> <p> <p>For reference:
<pre>
hh-fax2$ hg log --template '#rev#:#node|short#
#date|shortdate# #desc|firstline|strip#\n'
11:7b497e5881d8 2006-12-07 fixed nasty timing bug with PDF
virtual printer
10:5fbd62cf7025 2006-12-07 fixed SMTP details
9:adbc7966d42d 2006-12-07 back to faxaway
8:89f2688b85fc 2006-12-07 smtp host arg
7:eb4eba0ed22c 2006-12-07 mailfaxes.py starting to work
6:c317d0cb9956 2006-12-07 prepares one PDF doc per officer
5:fe8a79a7ed9f 2006-12-06 faxjob.py iterates over reports
and looks up fax numbers
4:52f42112c287 2006-12-06 better diagnostics
3:862514804543 2006-12-04 officer update mostly working
2:61dfc88ab652 2006-12-04 connecting to FM from py works
1:a1f813e53e79 2006-12-02 HTML/CSS page break test
0:aa2d0cc8a7e9 2006-12-02 save as html, doc export working
</pre>

<p> <p> <div>
  Tags: <a href="http://del.icio.us/connolly/python">python</a>
  <a href="http://del.icio.us/connolly/office">office</a> <a
href=
  "http://del.icio.us/connolly/mac">mac</a>
</div>