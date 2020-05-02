date: 2006-02-07
title: 'python, javascript, and PHP, oh my!'
published: True
tags: ['breadcrumbs', 'installation', 'javascript', 'python', 'quality', 'testing', 'programming']

<p>My habits for developing quality code in python are bumping up against the fact that the deployment platforms for the web client and server are javascript and PHP, respectively.</p>
  
<p>I love the python <a href="http://www.python.org/doc/lib/module-doctest.html">doctest module</a>. <a href="http://www.w3.org/2000/10/swap/uripath.py">uripath.py</a>
is a pretty good example of how I like to use it to simultaneously document and test code:</p>

<pre>
def splitFrag(uriref):
    """split a URI reference between the fragment and the rest.

    Punctuation is thrown away.

    e.g.
    
    >>> splitFrag("abc#def")
    ('abc', 'def')
[...]

def splitFragP(uriref, punct=0):
    """split a URI reference before the fragment

    Punctuation is kept.
    
    e.g.

    >>> splitFragP("abc#def")
    ('abc', '#def')
[...]
</pre>

<p>Another important way that python is self-documenting is that it meets the <a href="http://www.w3.org/TR/1998/NOTE-webarch-extlang-19980210#Ambiguity">unambiguity requirement</a>: you can pick up any .py file and trace every identifier back to what it refers to by following your nose:</p>
<ul>
 <li>for local variables, normal static scoping rules work; just scan up and look for an assignment or a function parameter</li>
 <li>for imported names, find the relavent import statement. <em><tt>from foo import *</tt> is evil, of course.</em></li>
 <li>global variables are explicitly declared as such</li>
</ul>

<p>OK, full disclosure: you need to know the <a href="http://www.python.org/doc/lib/built-in-funcs.html">python built-ins</a>, and when you see <tt>paramx.methody(z)</tt>, you have an unbounded search for <tt>methody</tt>, which makes doctests that show what class paramx comes from pretty important.
Mapping from the relevant import statement to the corresponding .py file may involve the usual search path nightmares; python doesn't solve that. <em>redfoot's <a href="http://redfoot.net/2002/12/03/redfoot-1.7.3/doc/helloworld.html">red_import </a> is interesting. And I'm not sure if <a href="http://peak.telecommunity.com/DevCenter/PythonEggs">eggs</a> are a step in the right direction or the wrong direction; gotta <a href="http://del.icio.us/connolly/installation">study them more</a>.</em> I try to ground import statements in the web a la:</p>

<pre>
import MySQLdb # MySQL for Python
               # http://sourceforge.net/projects/mysql-python
               # any Python Database API-happy implementation will do.
</pre>

<p>... so that you can follow your nose from the <tt>ImportError</tt> traceback to resolve the dependency.</p>

<p>Now timbl has started migrating the swap/cwm stuff to javascript. Let's look at <a href="http://groups.csail.mit.edu/dig/2005/ajar/ajaw/rdf/uri.js">uri.js</a>:</p>

<pre>
/** return the protocol of a uri **/
function uri_protocol(uri) {
...
</pre>

<p>Thanks for trying to document each function,
but that sort of comment isn't worthwhile; the risk that it'll get out of sync with the code is greater than the information it provides. Back to naming...</p>
 
<pre>
function URIjoin(given, base) {
...
	if (base&lt;0) {alert("Invalid base URL "+ base); return given}
</pre>

<p>Where does <tt>alert</tt> come from?
Is that in the ECMAScript standard? Or in some Netscape devedge stuff?</p>

<p>But more importantly: why not raise an exception? Javascript does have throw/catch, no?
Is it not the norm to use them? As I argued
in
<a href="http://groups.google.com/group/comp.lang.perl.tk/msg/a371b49a9276332">my contribution to the Python, Tcl and Perl, oh my! thread in 1996</a>, the community norms are at least as important, if not more important, than the language features, when it comes to developing quality code.</p>

<p>I keep running into javascript and PHP code that I want to read and wishing for doctests because I can't figure out which end is up.</p>

<p>Whence comes kb in this bit from <a href="http://groups.csail.mit.edu/dig/2005/ajar/ajaw/rdf/term.js">term.js</a>? Do I face an unbounded search?</p>

<pre>
RDFFormula.prototype.fromNT = function(str) {
	var len = str.length
	var x
	if (str[0] == '&lt;') return kb.sym(str.slice(1,len-1))
</pre>



<p>Maybe I just need to study the standard libraries a bit more, but I hear that the drupal project has coding conventions lots of people like for developing quality PHP code; I hope to study those. And the PEAR community must have some norms and best practices. I went looking for  javascript testing stuff and ran into <a href="http://openjsan.org/">JSAN</a>, a CPAN work-alike. That sort of infrastructure naturally reinforces quality norms.</p>


<p>See also: delicious tags <a rel="tag" href="http://del.icio.us/connolly/javascript">javascript</a>,
<a rel="tag" href="http://del.icio.us/connolly/python">python</a>,
<a rel="tag" href="http://del.icio.us/connolly/quality">quality</a>,
<a rel="tag" href="http://del.icio.us/connolly/testing">testing</a>,
<a rel="tag" href="http://del.icio.us/connolly/programming">programming</a>.</p>