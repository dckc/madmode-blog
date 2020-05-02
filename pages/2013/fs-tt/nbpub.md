title: 'Writing Madmode Articles with IPython and Docker'
date: 2013-12-30
published: true
tags: [ipython, python, writing, publishing, docker, installation]
summary: When I was doing exploratory signal processing a year ago, the IPython notebook was obviously a good tool. I tried it again recently for bringing old math notes back to life, and that went well too. So I'm putting a little effort into tooling support.


<div class="text_cell_render border-box-sizing rendered_html">
<p>When I was doing <a href="http://www.madmode.com/2012/light-runner-spelunking.html">exploratory signal processing</a> a year ago, the <a href="#Perez07">IPython notebook</a> was obviously a good tool. I tried it again recently for <a href="http://www.madmode.com/2013/fs-tt/fs86.html">bringing old math notes back to life</a>, and that went well too. So I'm putting a little effort into tooling support.</p>
<p>Hypertext editing with markdown works pretty well, especially a cell at a time. I was a little concerned that I'd miss the ability to select/cut/copy/paste multiple cells like Mathematica or do file-wide search and replace like emacs, but so far I haven't needed to.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Installing-IPython-notebook-via-a-docker-container">Installing IPython notebook via a docker container<a class="anchor-link" href="#Installing-IPython-notebook-via-a-docker-container">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>The Ubuntu 12.04 ipython notebook package isn't up to the task, and between these episodes, my manual installation bit-rotted. I got it running again and jotted down some rough notes for future reference:</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<pre><code>#!/bin/sh
&gt; virtualenv ~/pyenv/pynb
&gt; . ~/pyenv/pynb/bin/activate
(pynb)&gt; pip install ipython
(pynb)&gt; sudo apt-get install libzmq-dev
(pynb)&gt; pip install pyzmq
        ZMQ version detected: 2.1.11
   Warning: Detected ZMQ version: 2.1.11, but pyzmq targets ZMQ 4.0.3.
   Warning: libzmq features and fixes introduced after 2.1.11 will be unavailable.
(pynb)&gt; pip install jinja2
  Downloading Jinja2-2.7.1.tar.gz (377Kb): 377Kb downloaded
(pynb)&gt; pip install tornado
  Downloading tornado-3.1.1.tar.gz (374Kb): 374Kb downloaded
(pynb)&gt; ipython notebook</code></pre>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Those notes quickly get out of date. For example, nbconvert requires pandoc.</p>
<p>Then I realized a docker container would be just the thing. And lo, <a href="https://index.docker.io/u/dckc/ipython-docker/">dckc/ipython-docker</a> is born:</p>
<pre><code>$ sudo docker run -p 8123:8888 -v `/bin/pwd`:/notebooks  -t dckc/ipython-docker
2013-12-31 04:28:05.305 [NotebookApp] Created profile dir: u&#39;/.ipython/profile_default&#39;
2013-12-31 04:28:05.308 [NotebookApp] Using MathJax from CDN: http://cdn.mathjax.org/mathjax/latest/MathJax.js
2013-12-31 04:28:05.320 [NotebookApp] Serving notebooks from local directory: /notebooks
2013-12-31 04:28:05.320 [NotebookApp] The IPython Notebook is running at: http://0.0.0.0:8888/
2013-12-31 04:28:05.321 [NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).</code></pre>
<p>Note http://0.0.0.0:8888/ is an address from inside the container. From outside the container, we use port 8123.</p>
<p>The Control-C message needs some context too: you'd have to attach the container to send it signals via the keyboard. I typically just use <code>sudo docker kill</code> to stop the service. I haven't bothered with the details of starting at boot and such.</p>
<p>Of course, after I got it all working, I found several other <a href="https://index.docker.io/search?q=ipython">ipython images</a> in the index. But I'm not sorry I worked it out for myself.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Getting-started-with-docker">Getting started with docker<a class="anchor-link" href="#Getting-started-with-docker">&#182;</a></h3>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>Docker is moving rapidly, but it's considerably more polished now than when I first looked at it. The <a href="http://docs.docker.io/en/latest/installation/ubuntulinux/">docker apt-repositories for Ubuntu</a> (key fingerprint: 36A1 D786 9245 C895 0F96 6E92 D857 6A8B A88D 21E9) work just fine. My only issue getting it started this time was that I had an old installation lying around in <code>/usr/local/bin</code> and it was getting in the way, and the diagnostics were a little mysterious:</p>
<pre><code>$ sudo docker run -p :8888 -t ipython-notebook
WARNING: The mapping to public ports on your host has been deprecated. Use -p to publish the ports.</code></pre>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Generating-a-static-HTML-version-of-a-notebook">Generating a static HTML version of a notebook<a class="anchor-link" href="#Generating-a-static-HTML-version-of-a-notebook">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>IPython supports conversion to HTML, but out-of-the-box, you either get:</p>
<ol style="list-style-type: decimal">
<li>a stand-alone HTML document
<ul>
<li>with all sorts of CSS that may or may not conflict with a blog style</li>
<li>with no links to blog context</li>
</ul></li>
<li>a stripped-down HTML document body with
<ul>
<li>no style</li>
<li>no syntax highlighting</li>
</ul></li>
</ol>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Fortunately, the API for custom renditions is straightforward and well documented. My <a href="/static/code/ipynb_pub/mm_ipy.py">mm_ipy.py</a> is serviceable, though I'm still working through some issues with <a href="https://github.com/ipython/ipython/pull/4682">pygments vs. javascript code highlighting</a> and such.</p>
<p>Let's import it to take a look:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[1]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">imp</span>

<span class="n">mm_ipy</span> <span class="o">=</span> <span class="n">imp</span><span class="o">.</span><span class="n">load_source</span><span class="p">(</span><span class="s">&#39;mm_ipy&#39;</span><span class="p">,</span> <span class="s">&#39;code/ipynb_pub/mm_ipy.py&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Then let's connect the dots between rst markup in documentation and HTML renditions of values in ipython notebook cell outputs:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[2]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">from</span> <span class="nn">docutils.core</span> <span class="kn">import</span> <span class="n">publish_parts</span>
    
<span class="k">class</span> <span class="nc">Doc</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">it</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">it</span> <span class="o">=</span> <span class="n">it</span>

    <span class="k">def</span> <span class="nf">_repr_html_</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">publish_parts</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">it</span><span class="o">.</span><span class="n">__doc__</span><span class="p">,</span> <span class="n">writer_name</span><span class="o">=</span><span class="s">&#39;html&#39;</span><span class="p">)[</span><span class="s">&#39;html_body&#39;</span><span class="p">]</span>
</pre></div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[3]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">Doc</span><span class="p">(</span><span class="n">mm_ipy</span><span class="p">)</span>
</pre></div>

</div>
</div>

<div class="vbox output_wrapper">
<div class="output vbox">


<div class="hbox output_area"><div class="prompt output_prompt">
    Out[3]:</div>
<div class="box-flex1 output_subarea output_pyout">

<div class="output_html rendered_html">
<div class="document" id="mm-ipy-convert-ipython-notebook-to-markdown-for-madmode-blog">
<h1 class="title">mm_ipy -- convert ipython notebook to markdown for madmode blog</h1>
<p>Usage:</p>
<pre class="literal-block">
$ python article_in.ipynb article_out.md
</pre>
<p>See <span class="func">article_meta</span> for conventions for title, date, tags, etc.</p>
<div class="note">
<p class="first admonition-title">Note</p>
<p class="last">IPython.nbconvert.HTMLExporter has late-binding dependencies
on pandoc, pygments, etc.</p>
</div>
<div class="section" id="acknowledgements">
<h1>Acknowledgements</h1>
<blockquote>
<ul class="simple">
<li><a class="reference external" href="http://nbviewer.ipython.org/github/Carreau/posts/blob/master/06-NBconvert-Doc-Draft.ipynb#noqa">How to Use NBConvert</a> (<a class="reference external" href="https://github.com/Carreau/posts/blob/master/06-NBconvert-Doc-Draft.ipynb">source</a>)
Matthias Bussonnier (Carreau) Dec 01, 2013</li>
</ul>
</blockquote>
</div>
</div>

</div>

</div>
</div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>The notebook should have some article metadata in a markdown cell surrounded by a certain kind of pre tags:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[4]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">Doc</span><span class="p">(</span><span class="n">mm_ipy</span><span class="o">.</span><span class="n">article_meta</span><span class="p">)</span>
</pre></div>

</div>
</div>

<div class="vbox output_wrapper">
<div class="output vbox">


<div class="hbox output_area"><div class="prompt output_prompt">
    Out[4]:</div>
<div class="box-flex1 output_subarea output_pyout">

<div class="output_html rendered_html">
<div class="document">
<p>Collect article metadata from a notebook.</p>
<blockquote>
<p>The title is taken from the (first) heading level 1 cell.</p>
<p>Other metadata is taken from the (first) cell that starts with:</p>
<pre class="literal-block">
&gt;&gt;&gt; print article_meta.func_defaults[0]
&lt;pre class=&quot;about yaml&quot;&gt;
</pre>
<p>Metadata is written in YAML-ish name: value style (see <span class="func">grok_yaml</span>
for details).</p>
<p>The closing tag is ignored:</p>
<pre class="literal-block">
&gt;&gt;&gt; print article_meta.func_defaults[1]
&lt;/pre&gt;
</pre>
</blockquote>
</div>

</div>

</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[5]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">Doc</span><span class="p">(</span><span class="n">mm_ipy</span><span class="o">.</span><span class="n">grok_yaml</span><span class="p">)</span>
</pre></div>

</div>
</div>

<div class="vbox output_wrapper">
<div class="output vbox">


<div class="hbox output_area"><div class="prompt output_prompt">
    Out[5]:</div>
<div class="box-flex1 output_subarea output_pyout">

<div class="output_html rendered_html">
<div class="document">
<p>Quick-n-dirty YAML parser.</p>
<blockquote>
<pre class="doctest-block">
&gt;&gt;&gt; grok_yaml(&quot;&quot;&quot;&lt;pre&gt;
... date: 2001-01-01
... tags: ['travel', 'humor']
... &lt;/pre&gt;&quot;&quot;&quot;, excludes=['&lt;'])
[('date', '2001-01-01'), ('tags', &quot;['travel', 'humor']&quot;)]
</pre>
<div class="note">
<p class="first admonition-title">Note</p>
<p class="last">TODO: handle continuation lines properly.</p>
</div>
<pre class="doctest-block">
&gt;&gt;&gt; grok_yaml(&quot;&quot;&quot;&lt;pre&gt;
... summary: What I did
...   this summer.
... &lt;/pre&gt;&quot;&quot;&quot;, excludes=['&lt;'])
[('summary', 'What I did'), ('  this summer.',)]
</pre>
</blockquote>
</div>

</div>

</div>
</div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Packages-from-apt-and-PyPI">Packages from apt and PyPI<a class="anchor-link" href="#Packages-from-apt-and-PyPI">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>The container doesn't have access to packages installed in the host system via pip or apt-get. But I can install from pypi within the container.</p>
<p>Installing from within the Dockerfile makes the package part of the container, but it involves killing and re-starting the container. And it feels less minimal/modular somehow.</p>
<p>Installing from within a notebook (e.g. <code>!pip install docutils</code>) is handy, but once the container is stopped, the installation goes away (unless the container is committed and the image kept handy somehow).</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="File-layout-limitations">File layout limitations<a class="anchor-link" href="#File-layout-limitations">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>The IPython notebook service can only see notebooks in one directory. I wish it were more web-like, i.e. it expected to be <a href="http://www.w3.org/DesignIssues/Principles.html#TOII">part of a larger whole</a>. I'd like to use it to edit <code>.ipynb</code> files under the various date-oriented subdirectories of my blog. Linking from a notebook to files elsewhere in the blog is also pretty awkward.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="References">References<a class="anchor-link" href="#References">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p><em>TODO: Zotero integration</em></p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<ul>
<li><a name="Perez07">Pérez, Fernando, and Brian E. Granger. 2007</a>. “IPython: a System for Interactive Scientific Computing.” Computing in Science &amp; Engineering 9 (3): 21–29. doi:10.1109/MCSE.2007.53. URL: http://ipython.org</li>
</ul>
</div>