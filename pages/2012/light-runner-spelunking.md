tags: ['coco', 'python', 'digial media', 'signal processing', 'ipython']
date: 2012-12-30
published: true
title: '"Light Runner", an exercise in digital preservation'
summary: In my teens, I wrote a Tron work-alike called Light Runner
         in assembly for the Color Computer; I even got Prickly Pear
         Software to release it commercially. I can't find my source code,
         but I have a copy of the product on cassette tape. I didn't
         quite get it restored to working order, but I had some fun trying.

<style type="text/css">

div.prompt {
    /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
    width: 11ex;
    /* This 0.4em is tuned to match the padding on the CodeMirror editor. */
    padding: 0.4em;
    margin: 0px;
    font-family: monospace;
    text-align:right;
}

div.input {
    page-break-inside: avoid;
}

/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
    color: black;
    border: 1px solid #ddd;
    border-radius: 3px;
    background: #f7f7f7;
}

div.input_prompt {
    color: navy;
    border-top: 1px solid transparent;
}

div.output_wrapper {
    /* This is a spacer between the input and output of each cell */
    margin-top: 5px;
    margin-left: 5px;
    /* FF needs explicit width to stretch */
    width: 100%;
    /* this position must be relative to enable descendents to be absolute within it */
    position: relative;
}

</style>
<meta charset="UTF-8">
<script src="https://c328740.ssl.cf1.rackcdn.com/mathjax/latest/MathJax.js?config=TeX-AMS_HTML" type="text/javascript">

</script>
<script type="text/javascript">
init_mathjax = function() {
    if (window.MathJax) {
        // MathJax loaded
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
            },
            displayAlign: 'left', // Change this to 'center' to center equations.
            "HTML-CSS": {
                styles: {'.MathJax_Display': {"margin": 0}}
            }
        });
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    }
}
init_mathjax();
</script>

<div class="text_cell_render border-box-sizing rendered_html">
<p>In my teens, I wrote a <a href="http://en.wikipedia.org/wiki/Tron_(video_game)">Tron</a> work-alike called <em>Light Runner</em> in
assembly for the Color Computer; I even got Prickly Pear Software to
release it commercially. I can't find my source code (<em>Grrr!</em>), but I have a
copy of the product on cassette tape. I didn't quite get it restored
to working order, but I had some fun trying.</p>
<figure>
  <img src='https://lh5.googleusercontent.com/-HfOBzwjRTB0/UN9ciuLvwzI/AAAAAAAAAkA/T89gPR2lWvQ/w497-h373/IMG_20121229_145634.jpg' />
  <figcaption>Light Runner and The Facts for the CoCo</figcaption>
</figure
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>The analog-to-digital-signal bit was only complicated by the fact that
the cassette player couldn't be connected to my desktop:</p>
<ol>
<li>Put the cassette in the boombox.</li>
<li>Hook the boombox to the netbook.</li>
<li>Use "Sound Recorder" to make <code>lr.wma</code>.</li>
<li>Move <code>lr.wma</code> to my desktop via a thumb drive.</li>
<li>Use Audacity to chop off the dead air and save in <code>.wav</code> format.</li>
</ol>
<figure>
  <img src='https://lh5.googleusercontent.com/-fOsav6xJGIs/UN9dyRBVMLI/AAAAAAAAAkc/FYLZAAs8Tec/s494/audacity-light-runner.png' />
  <figcaption>Audio cassette data in Audacity</figcaption>
</figure>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Processing the digital signal</strong> involved a steep learning curve. As
explained on pg. 10 of <em>The FACTS</em>:</p>
<blockquote>
<p>G. Cassette Interface - Cassette data is stored onto the tape
 using a format called Frequency Shift Keying (FSK). This means that
 two sine waves of differing frequency are used to zeroes and ones
 on the tape. A sine wave of 2400 hz is used to store a one, and a
 sine wave of 1200 Hertz is used to store a zero.</p>
</blockquote>
<p>I surfed around, wondering whether to make this an R project or a numpy project.
The clincher was a StackOverflow clue on <a href="http://stackoverflow.com/a/3843124">detecting zero crossings</a> by Jim Brissom Oct 1 2010:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="k">def</span> <span class="nf">zero_crossings</span><span class="p">(</span><span class="n">signal</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">numpy</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">numpy</span><span class="o">.</span><span class="n">diff</span><span class="p">(</span><span class="n">numpy</span><span class="o">.</span><span class="n">sign</span><span class="p">(</span><span class="n">signal</span><span class="p">)))[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">3</span><span class="p">,</span> <span class="o">-</span><span class="mi">4</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">7</span><span class="p">,</span> <span class="o">-</span><span class="mi">10</span><span class="p">]</span>
<span class="n">zero_crossings</span><span class="p">(</span><span class="n">a</span><span class="p">)</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt">Out[2]:</div>
<div class="output_subarea output_pyout">
<pre>array([ 3,  5,  9, 10, 11, 12, 15])</pre>
</div>
</div>
</div>
</div>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<h2>Aside/Colophon</h2>
<p>I'm trying out <a href="http://ipython.org/">IPython</a> as an authoring tool.
I'm fond of the interactive notebook idea.
The 0.12 version that comes with Ubuntu didn't support
inline plotting, and cell selection was glitchy.
But I'm using 0.14dev, and while it doesn't quite feel as
mature as RStudio, it's getting pretty close.</p>

<p>See <a href="cocogetblk/coco.ipynb">coco.ipynb</a> notebook source.</p>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="o">%</span><span class="k">pylab</span> <span class="n">inline</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt"></div>
<div class="output_subarea output_stream output_stdout">
<pre>
Welcome to pylab, a matplotlib-based Python environment [backend: module://IPython.zmq.pylab.backend_inline].
For more information, type &apos;help(pylab)&apos;.
</pre>
</div>
</div>
</div>
</div>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>Making a numpy array out of a <code>.wav</code> file is a piece of cake.
Scaling the amplitude to fit in an 8 bit DAC like the CoCo's
helps eliminate some high frequency noise:
(See <a href="cocogetblk/cloadm.py">cloadm.py</a> for full details.)</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">wave</span>
<span class="kn">import</span> <span class="nn">cloadm</span> <span class="kn">as</span> <span class="nn">c</span>
<span class="n">tape_fn</span> <span class="o">=</span> <span class="s">&#39;lr-cut.wav&#39;</span>
<span class="n">dest_fn</span> <span class="o">=</span> <span class="s">&#39;light-runner&#39;</span>
<span class="n">tape</span> <span class="o">=</span> <span class="n">wave</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tape_fn</span><span class="p">,</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
<span class="n">dest</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">dest_fn</span><span class="p">,</span> <span class="s">&#39;w&#39;</span><span class="p">)</span>
<span class="n">framerate</span><span class="p">,</span> <span class="n">signal</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">wavLoadMono</span><span class="p">(</span><span class="n">tape</span><span class="p">)</span>
<span class="n">amp_max</span> <span class="o">=</span> <span class="mi">128</span>  <span class="c"># 8 bit signed</span>
<span class="n">signal</span> <span class="o">=</span> <span class="n">signal</span> <span class="o">*</span> <span class="n">amp_max</span> <span class="o">/</span> <span class="nb">max</span><span class="p">(</span><span class="n">signal</span><span class="p">)</span>
<span class="n">framerate</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">signal</span><span class="p">),</span> <span class="n">signal</span><span class="p">[:</span><span class="mi">5</span><span class="p">]</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt">Out[3]:</div>
<div class="output_subarea output_pyout">
<pre>(44100, 1223945, array([16, 17, 17, 17, 17]))</pre>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>The next step is to find the long sequence of
alternating 0s and 1s that mark the beginning of a sequence of bytes.
In Audacity, I could hear the tone right around 2 seconds in.
The signal at this point looks about right:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">t</span> <span class="o">=</span> <span class="n">arange</span><span class="p">(</span><span class="mf">2.0</span><span class="p">,</span> <span class="mf">2.01</span><span class="p">,</span> <span class="mf">1.0</span><span class="o">/</span><span class="n">framerate</span><span class="p">)</span>
<span class="n">_</span> <span class="o">=</span> <span class="n">plot</span><span class="p">(</span><span class="n">t</span><span class="p">,</span>
         <span class="n">signal</span><span class="p">[</span><span class="n">t</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">framerate</span><span class="p">:</span><span class="n">t</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">*</span> <span class="n">framerate</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">t</span><span class="p">)])</span>
<span class="n">grid</span><span class="p">()</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt"></div>
<div class="output_subarea output_display_data">
<img src="data:image/png;base64,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
xf8Hfi3Ai3Y1rDkAAAAASUVORK5CYII=
"></img>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>The pattern of bits was close, but not quite there, no matter how I played with the threshold:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">freqs</span><span class="p">,</span> <span class="n">wave_ix</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">waves</span><span class="p">(</span><span class="n">zero_crossings</span><span class="p">(</span><span class="n">signal</span><span class="p">),</span> <span class="n">framerate</span><span class="p">)</span>
<span class="n">threshold</span> <span class="o">=</span> <span class="mi">1400</span>  <span class="c"># experimental; cf. (CoCo.rate0 + CoCo.rate1) / 2</span>
<span class="n">bits</span> <span class="o">=</span> <span class="p">(</span><span class="n">freqs</span> <span class="o">&gt;</span> <span class="n">threshold</span><span class="p">)</span> <span class="o">+</span> <span class="mi">0</span>
<span class="n">bits</span><span class="p">[</span><span class="n">wave_ix</span> <span class="o">&gt;</span> <span class="mf">2.0</span> <span class="o">*</span> <span class="n">framerate</span><span class="p">][:</span><span class="mi">40</span><span class="p">]</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt">Out[5]:</div>
<div class="output_subarea output_pyout">
<pre>array([1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0,
       1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>I pored over the disassembly from <em>The FACTS</em>, wondering what I'd missed:</p>
</div>

<pre>
*** LOOK FOR THE SYNC BYTES - RETURN WITH ACCA = 0 IF SYNC’ED
*** ON HI - LO TRANSITION, ACCA = $A0 IF SYNC’ED ON THE
*** LO - HI TRANSITION OF THE INPUT SIGNAL FROM THE CASSETTE.
CASON  ORCC   #$50      DISABLE IRQ,FIRQ
       BSR    LA7CA     TURN ON TAPE DECK MOTOR
       CLR    CPULWD    RESET UP TO SPEED COUNTER
LA782  BSR    LA763     WAIT FOR LO-HI TRANSITION
LA784  BSR    LA7AD     WAIT FOR HI-LO TRANSITION
       BHI    LA797     CASSETTE SPEED IN RANGE FOR 1200 HZ
LA788  BSR    LA7A7     WAIT FOR LO-HI TRANSITION
       BCS    LA79B     CASSETTE SPEED IN RANGE FOR 2400 HZ
       DEC    CPULWD    DECREMENT UP TO SPEED COUNTER IF SYNC’ED ON LO-HI
       LDA    CPULWD    GET IT
       CMPA   #-96      HAVE THERE BEEN 96 CONSECUTIVE 1-0-1-0 PATTERNS
LA792  BNE    LA782     NO
       STA    CBTPHA    SAVE WHICH TRANSITION (HI-LO OR LO-HI)
       RTS
</pre>

<div class="text_cell_render border-box-sizing rendered_html">
<p><em>Aside</em>: I haven't found <em>The FACTS</em> online, but the disassemblies
are also available in <a href="https://sites.google.com/a/aaronwolfe.com/cococoding/home/docs/color-basic-unravelled.pdf?attredirects=0&amp;d=1">Color Basic Unravelled</a>, also
by Spectral Associates, digitally restored by <a href="https://sites.google.com/a/aaronwolfe.com/cococoding/home/docs">Aaron Wolfe</a>.</p>
<p>I finally found the bug by</p>
<ul>
<li>focussing on an even smaller section of the signal,</li>
<li>together with the calculated frequencies and the derived bits: </li>
</ul>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">lo</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">framerate</span> <span class="o">*</span> <span class="mf">0.560</span><span class="p">)</span>
<span class="n">hi</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">framerate</span> <span class="o">*</span> <span class="mf">0.580</span><span class="p">)</span>
<span class="n">lo</span><span class="p">,</span> <span class="n">hi</span>

<span class="n">ix</span> <span class="o">=</span> <span class="n">intersect1d</span><span class="p">(</span><span class="n">where</span><span class="p">(</span><span class="n">wave_ix</span> <span class="o">&gt;</span> <span class="n">lo</span><span class="p">)[</span><span class="mi">0</span><span class="p">],</span> <span class="n">where</span><span class="p">(</span><span class="n">wave_ix</span> <span class="o">&lt;</span> <span class="n">hi</span><span class="p">)[</span><span class="mi">0</span><span class="p">])</span>

<span class="n">ones</span> <span class="o">=</span> <span class="n">ix</span><span class="p">[</span><span class="n">bits</span><span class="p">[</span><span class="n">ix</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">]</span>
<span class="n">zeros</span> <span class="o">=</span> <span class="n">ix</span><span class="p">[</span><span class="n">bits</span><span class="p">[</span><span class="n">ix</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">]</span>
<span class="n">_</span> <span class="o">=</span> <span class="n">plot</span><span class="p">(</span><span class="n">arange</span><span class="p">(</span><span class="n">lo</span><span class="p">,</span> <span class="n">hi</span><span class="p">),</span> <span class="n">signal</span><span class="p">[</span><span class="n">lo</span><span class="p">:</span><span class="n">hi</span><span class="p">],</span> <span class="s">&#39;b-&#39;</span><span class="p">,</span>
         <span class="n">wave_ix</span><span class="p">[</span><span class="n">ix</span><span class="p">],</span> <span class="p">(</span><span class="n">freqs</span><span class="o">/</span><span class="mi">20</span><span class="p">)[</span><span class="n">ix</span><span class="p">],</span> <span class="s">&#39;g*&#39;</span><span class="p">,</span>
         <span class="n">wave_ix</span><span class="p">[</span><span class="n">ones</span><span class="p">],</span> <span class="n">bits</span><span class="p">[</span><span class="n">ones</span><span class="p">],</span> <span class="s">&#39;r+&#39;</span><span class="p">,</span>
         <span class="n">wave_ix</span><span class="p">[</span><span class="n">zeros</span><span class="p">],</span> <span class="n">bits</span><span class="p">[</span><span class="n">zeros</span><span class="p">],</span> <span class="s">&#39;ro&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt"></div>
<div class="output_subarea output_display_data">
<img src="data:image/png;base64,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
"></img>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Do you see it?</p>
<p>The crossings start lo-hi for the first five bits, but somehow
the next bit is marked at a hi-lo transition.</p>
<p>I added a line of code to say that they should all go the same direction:</p>
<pre><code>    assert((numpy.sign(signal[z[::2]]) == numpy.sign(z[0])).all())
</code></pre>
<p>When the signal crossed zero by actually hitting zero, it threw things off.
So I tweaked <code>zero_crossings</code> algorithm to use <code>sign() &gt; 0</code> so that we
have just +/-, rather than +1/0/-1:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="k">def</span> <span class="nf">zero_crossings</span><span class="p">(</span><span class="n">signal</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">numpy</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">numpy</span><span class="o">.</span><span class="n">diff</span><span class="p">(</span><span class="n">numpy</span><span class="o">.</span><span class="n">sign</span><span class="p">(</span><span class="n">signal</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">))[</span><span class="mi">0</span><span class="p">]</span>
 
<span class="n">zero_crossings</span><span class="p">([</span><span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="o">-</span><span class="mi">4</span><span class="p">])</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt">Out[7]:</div>
<div class="output_subarea output_pyout">
<pre>array([1, 4, 6])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now the 1's and 0's alternate nicely:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">freqs</span><span class="p">,</span> <span class="n">wave_ix</span> <span class="o">=</span> <span class="n">c</span><span class="o">.</span><span class="n">waves</span><span class="p">(</span><span class="n">zero_crossings</span><span class="p">(</span><span class="n">signal</span><span class="p">),</span> <span class="n">framerate</span><span class="p">)</span>
<span class="n">threshold</span> <span class="o">=</span> <span class="mi">1400</span>  <span class="c"># experimental; cf. (CoCo.rate0 + CoCo.rate1) / 2</span>
<span class="n">bits</span> <span class="o">=</span> <span class="p">(</span><span class="n">freqs</span> <span class="o">&gt;</span> <span class="n">threshold</span><span class="p">)</span> <span class="o">+</span> <span class="mi">0</span>
<span class="n">bits</span><span class="p">[</span><span class="n">wave_ix</span> <span class="o">&gt;</span> <span class="mf">2.0</span> <span class="o">*</span> <span class="n">framerate</span><span class="p">][:</span><span class="mi">40</span><span class="p">]</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt">Out[8]:</div>
<div class="output_subarea output_pyout">
<pre>array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
       0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])</pre>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>This allows us to find the sync pattern:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">c</span><span class="o">.</span><span class="n">find_sync</span><span class="p">(</span><span class="n">bits</span><span class="p">)</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt">Out[9]:</div>
<div class="output_subarea output_pyout">
<pre>1145</pre>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Putting it all together, we see that we get a certain distance before falling out of sync:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">)</span>
<span class="kn">import</span> <span class="nn">StringIO</span>
<span class="n">tape</span> <span class="o">=</span> <span class="n">wave</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">tape_fn</span><span class="p">,</span> <span class="s">&#39;r&#39;</span><span class="p">)</span>
<span class="n">dest</span> <span class="o">=</span> <span class="n">StringIO</span><span class="o">.</span><span class="n">StringIO</span><span class="p">()</span>
<span class="k">try</span><span class="p">:</span>
    <span class="n">c</span><span class="o">.</span><span class="n">decode</span><span class="p">(</span><span class="n">tape</span><span class="p">,</span> <span class="n">dest</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
    <span class="k">print</span> <span class="s">&quot;oops!&quot;</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt"></div>
<div class="output_subarea output_stream output_stderr">
<pre>INFO:cloadm:block type: 0 length: 15
INFO:cloadm:block type: 1 length: 255
WARNING:cloadm:expected check $88 does not match found $8
INFO:cloadm:block type: 1 length: 255
WARNING:cloadm:expected check $6d does not match found $ed
INFO:cloadm:block type: 1 length: 255
INFO:cloadm:block type: 1 length: 255
INFO:cloadm:block type: 1 length: 255
INFO:cloadm:block type: 1 length: 255
INFO:cloadm:block type: 1 length: 255
WARNING:cloadm:expected check $f0 does not match found $70
INFO:cloadm:block type: 1 length: 255
WARNING:cloadm:expected check $6 does not match found $86
WARNING:cloadm:expected block start $55 does not match found $ab
WARNING:cloadm:expected block start $3c does not match found $78
INFO:cloadm:block type: 2 length: 254
</pre>
</div>
</div>
<div class="hbox output_area">
<div class="prompt output_prompt"></div>
<div class="output_subarea output_stream output_stdout">
<pre>oops!
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>The filename and copyright statement confirm that we're on the right track:</p>
</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">content</span> <span class="o">=</span> <span class="n">dest</span><span class="o">.</span><span class="n">getvalue</span><span class="p">()</span>
<span class="k">print</span> <span class="s">&quot;filename:&quot;</span><span class="p">,</span> <span class="n">content</span><span class="p">[:</span><span class="mi">8</span><span class="p">]</span>
<span class="k">print</span>
<span class="k">print</span> <span class="n">content</span><span class="p">[</span><span class="mi">229</span><span class="p">:</span><span class="mi">298</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x00</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
<div class="vbox output_wrapper">
<div class="output vbox">
<div class="hbox output_area">
<div class="prompt output_prompt"></div>
<div class="output_subarea output_stream output_stdout">
<pre>filename: RUNNER  

LIGHT RUNNER
COPR(C) 1983 BY CO&amp;CO SOFTWARE
WRITTEN BY: DAN CONNOLLY

</pre>
</div>
</div>
</div>
</div>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2>Related Work</h2>
<p>Browsing around the <a href="http://five.pairlist.net/pipermail/coco/">coco mailing list</a>
I found a <code>CASIN.EXE</code> program by Jeff Vavasour circa 1994;
I got it running under dosbox; the first thing it said was:</p>
<pre><code>This .WAV file is not a 11025Hz/mono/8-bit sample.
</code></pre>
<p>So sox to the rescue:</p>
<pre><code>$ `sox ../../lr-cut.wav -r 11025 -b 8 lr8.wav`
</code></pre>
<p>Then <code>CASIN</code> made some progress, but didn't get very far.
It decoded even less data than my code did. I might have felt
a little silly poring over all the low-level details if
there was a well-known solution that worked out of the box.
But data analysis and signal processing is a growing part
of my day job, and learning the scientific python toolset
has been on my todo list for quite some time, so I'm glad I did.</p>
</div>
