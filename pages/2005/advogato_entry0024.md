title: 17 May 2005
date: 2005-05-17
tags: []
published: true

Got tired of the manual login-and-download-statement ritual with my bank, and since
<a href="https://wwwsearch.sourceforge.net/ClientForm/
">ClientForm</a> and
<a href="https://wwwsearch.sourceforge.net/ClientCookie/">ClientCookie</a>
are such a joy and python has SSL built-in,
I cooked up <a href="https://dev.w3.org/cvsweb/2000/quacken/grabst.py">grabst.py</a> that automates it. Heaven forbid the bank website should allow me to just bookmark my statement so I could directly GET (with SSL and password auth) it, without all the frames and javascript malarky.
