title: 'M373K Notes'
date: 2014-01-06
tags: [logic, research]


<div class="text_cell_render border-box-sizing rendered_html">
<p>Mead purple notebook</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Dan Connolly<br />495-3497<br />M373K</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Preface:-Axioms">Preface: Axioms<a class="anchor-link" href="#Preface:-Axioms">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[1]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="k">def</span> <span class="nf">axiom</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">abbr</span><span class="p">,</span> <span class="n">fmla</span><span class="p">):</span>
    <span class="n">_rule_names</span> <span class="o">=</span> <span class="p">{</span><span class="n">abbr</span><span class="p">:</span> <span class="n">name</span><span class="p">}</span>
    <span class="n">_rules</span> <span class="o">=</span> <span class="p">{</span><span class="n">abbr</span><span class="p">:</span> <span class="p">[</span><span class="n">fmla</span><span class="p">]}</span>
    <span class="n">nd</span><span class="o">.</span><span class="n">add_rule_names</span><span class="p">(</span><span class="n">_rule_names</span><span class="p">)</span>
    <span class="n">nd</span><span class="o">.</span><span class="n">add_rules</span><span class="p">(</span><span class="n">_rules</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">abbr</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Preface:-Bidirectional-Inference-Rules">Preface: Bidirectional Inference Rules<a class="anchor-link" href="#Preface:-Bidirectional-Inference-Rules">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[2]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">from</span> <span class="nn">flip.logic</span> <span class="kn">import</span> <span class="n">nd</span>


<span class="k">def</span> <span class="nf">infer_bidir</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">abbr</span><span class="p">,</span> <span class="n">p</span><span class="p">,</span> <span class="n">q</span><span class="p">):</span>
    <span class="n">intro</span> <span class="o">=</span> <span class="n">abbr</span> <span class="o">+</span> <span class="s">&#39;I&#39;</span>
    <span class="n">elim</span> <span class="o">=</span> <span class="n">abbr</span> <span class="o">+</span> <span class="s">&#39;E&#39;</span>
    <span class="n">_rule_names</span> <span class="o">=</span> <span class="p">{</span>
               <span class="n">intro</span><span class="p">:</span> <span class="n">name</span> <span class="o">+</span> <span class="s">&#39; (intro)&#39;</span><span class="p">,</span>
               <span class="n">elim</span><span class="p">:</span> <span class="n">name</span> <span class="o">+</span> <span class="s">&#39; (elim)&#39;</span>
               <span class="p">}</span>
    <span class="n">_rules</span> <span class="o">=</span> <span class="p">{</span>
              <span class="n">elim</span><span class="p">:</span> <span class="p">[</span><span class="n">p</span><span class="p">,</span> <span class="n">q</span><span class="p">],</span>
              <span class="n">intro</span><span class="p">:</span> <span class="p">[</span><span class="n">q</span><span class="p">,</span> <span class="n">p</span><span class="p">]</span>
              <span class="p">}</span>
    <span class="n">nd</span><span class="o">.</span><span class="n">add_rule_names</span><span class="p">(</span><span class="n">_rule_names</span><span class="p">)</span>
    <span class="n">nd</span><span class="o">.</span><span class="n">add_rules</span><span class="p">(</span><span class="n">_rules</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">intro</span><span class="p">,</span> <span class="n">elim</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Preface:-Iff">Preface: Iff<a class="anchor-link" href="#Preface:-Iff">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[3]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">from</span> <span class="nn">flip.logic.formula</span> <span class="kn">import</span> <span class="p">(</span><span class="n">InfixRelation</span><span class="p">,</span> <span class="n">InfixLogical</span><span class="p">,</span>
                                <span class="n">Variable</span><span class="p">,</span> <span class="n">Function</span><span class="p">,</span> <span class="n">Infix</span><span class="p">,</span> <span class="n">TermPlaceholder</span><span class="p">)</span>
<span class="kn">from</span> <span class="nn">flip.logic.prop_common</span> <span class="kn">import</span> <span class="n">And</span><span class="p">,</span> <span class="n">Impl</span><span class="p">,</span> <span class="n">m1</span><span class="p">,</span> <span class="n">m2</span>

<span class="k">class</span> <span class="nc">Iff</span><span class="p">(</span><span class="n">InfixLogical</span><span class="p">):</span>
  <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">  Impl(a,b) means a &lt;=&gt;</span>
<span class="sd">  &quot;&quot;&quot;</span>
  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
    <span class="n">InfixLogical</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">symbol</span> <span class="o">=</span> <span class="s">&#39;&lt;=&gt;&#39;</span>


<span class="n">iffI</span><span class="p">,</span> <span class="n">iffE</span> <span class="o">=</span> <span class="n">infer_bidir</span><span class="p">(</span><span class="s">&#39;Iff&#39;</span><span class="p">,</span> <span class="s">&#39;iff&#39;</span><span class="p">,</span>
                         <span class="n">Iff</span><span class="p">(</span><span class="n">m1</span><span class="p">,</span> <span class="n">m2</span><span class="p">),</span>
                         <span class="n">And</span><span class="p">(</span><span class="n">Impl</span><span class="p">(</span><span class="n">m1</span><span class="p">,</span> <span class="n">m2</span><span class="p">),</span> <span class="n">Impl</span><span class="p">(</span><span class="n">m2</span><span class="p">,</span> <span class="n">m1</span><span class="p">)))</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Preamble:-Sets">Preamble: Sets<a class="anchor-link" href="#Preamble:-Sets">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[4]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">from</span> <span class="nn">flip.logic.prop_common</span> <span class="kn">import</span> <span class="n">Not</span>
<span class="kn">from</span> <span class="nn">flip.logic.fol</span> <span class="kn">import</span> <span class="n">Equal</span><span class="p">,</span> <span class="n">A</span><span class="p">,</span> <span class="n">E</span><span class="p">,</span> <span class="n">t1</span><span class="p">,</span> <span class="n">t2</span><span class="p">,</span> <span class="n">v1</span><span class="p">,</span> <span class="n">v2</span><span class="p">,</span> <span class="n">P1</span>

<span class="k">class</span> <span class="nc">elt</span><span class="p">(</span><span class="n">InfixRelation</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
        <span class="n">InfixRelation</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">symbol</span> <span class="o">=</span> <span class="s">&#39;.in.&#39;</span>  <span class="c"># borrow notation from R, somewhat arbitrarily</span>


<span class="n">phi</span> <span class="o">=</span> <span class="n">Variable</span><span class="p">(</span><span class="s">&#39;phi&#39;</span><span class="p">)</span>

<span class="n">emptySet</span> <span class="o">=</span> <span class="n">axiom</span><span class="p">(</span><span class="s">&#39;Empty Set&#39;</span><span class="p">,</span> <span class="s">&#39;emptySet&#39;</span><span class="p">,</span> <span class="n">Not</span><span class="p">(</span><span class="n">elt</span><span class="p">(</span><span class="n">t1</span><span class="p">,</span> <span class="n">phi</span><span class="p">)))</span>
<span class="c"># alternatively: E(x, A(y, Not(elt(y, x))))</span>

<span class="n">ext</span> <span class="o">=</span> <span class="n">infer_bidir</span><span class="p">(</span><span class="s">&#39;Extensionality&#39;</span><span class="p">,</span> <span class="s">&#39;ext&#39;</span><span class="p">,</span>
                  <span class="n">Equal</span><span class="p">(</span><span class="n">t1</span><span class="p">,</span> <span class="n">t2</span><span class="p">),</span>  <span class="c"># need a side-condition that t1 and t2 are sets?</span>
                  <span class="n">A</span><span class="p">(</span><span class="n">v1</span><span class="p">,</span> <span class="n">Iff</span><span class="p">(</span><span class="n">elt</span><span class="p">(</span><span class="n">v1</span><span class="p">,</span> <span class="n">t1</span><span class="p">),</span> <span class="n">elt</span><span class="p">(</span><span class="n">v1</span><span class="p">,</span> <span class="n">t2</span><span class="p">))))</span>

<span class="n">abst</span> <span class="o">=</span> <span class="n">axiom</span><span class="p">(</span><span class="s">&#39;Abstraction&#39;</span><span class="p">,</span> <span class="s">&#39;abst&#39;</span><span class="p">,</span> <span class="n">E</span><span class="p">(</span><span class="n">v1</span><span class="p">,</span> <span class="n">A</span><span class="p">(</span><span class="n">v2</span><span class="p">,</span> <span class="n">Iff</span><span class="p">(</span><span class="n">elt</span><span class="p">(</span><span class="n">v2</span><span class="p">,</span> <span class="n">v1</span><span class="p">),</span> <span class="n">P1</span><span class="p">(</span><span class="n">v2</span><span class="p">)))))</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Preamble:-Integers">Preamble: Integers<a class="anchor-link" href="#Preamble:-Integers">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[5]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">z</span> <span class="o">=</span> <span class="n">Variable</span><span class="p">(</span><span class="s">&#39;z&#39;</span><span class="p">)</span>

<span class="c"># TODO: infix functions?</span>

<span class="k">class</span> <span class="nc">plus</span><span class="p">(</span><span class="n">Function</span><span class="p">,</span> <span class="n">Infix</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
        <span class="n">Function</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
        <span class="n">Infix</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">symbol</span> <span class="o">=</span> <span class="s">&#39;+&#39;</span>

<span class="k">class</span> <span class="nc">times</span><span class="p">(</span><span class="n">Function</span><span class="p">,</span> <span class="n">Infix</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
        <span class="n">Function</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
        <span class="n">Infix</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">symbol</span> <span class="o">=</span> <span class="s">&#39;*&#39;</span>


<span class="k">class</span> <span class="nc">gt</span><span class="p">(</span><span class="n">InfixRelation</span><span class="p">):</span>
    <span class="n">symbol</span> <span class="o">=</span> <span class="s">&#39;&gt;&#39;</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Definition-of-\(a-|-b\)">Definition of \(a | b\)<a class="anchor-link" href="#Definition-of-\(a-|-b\)">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[6]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">from</span> <span class="nn">flip.logic.fol_session</span> <span class="kn">import</span> <span class="o">*</span>

<span class="k">class</span> <span class="nc">divides</span><span class="p">(</span><span class="n">InfixRelation</span><span class="p">):</span>
  <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">  divides(a,b) means a | b</span>
<span class="sd">  &quot;&quot;&quot;</span>
  <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
    <span class="n">InfixRelation</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">symbol</span> <span class="o">=</span> <span class="s">&#39;|&#39;</span>


<span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">d</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">TermPlaceholder</span><span class="p">,</span> <span class="s">&#39;a b d&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span class="n">k</span> <span class="o">=</span> <span class="n">Variable</span><span class="p">(</span><span class="s">&#39;k&#39;</span><span class="p">)</span>

<span class="n">divI</span><span class="p">,</span> <span class="n">divE</span> <span class="o">=</span> <span class="n">infer_bidir</span><span class="p">(</span><span class="s">&#39;Defn divides&#39;</span><span class="p">,</span> <span class="s">&#39;div&#39;</span><span class="p">,</span>
                         <span class="n">divides</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">),</span> <span class="n">E</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">Equal</span><span class="p">(</span><span class="n">b</span><span class="p">,</span> <span class="n">times</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">a</span><span class="p">))))</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Definition-of-\((a,-b)\)">Definition of \((a, b)\)<a class="anchor-link" href="#Definition-of-\((a,-b)\)">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[7]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="k">class</span> <span class="nc">gcf</span><span class="p">(</span><span class="n">Function</span><span class="p">):</span>
    <span class="k">pass</span>


<span class="k">def</span> <span class="nf">and_n</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">):</span>
    <span class="k">return</span> <span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">args</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span> <span class="k">else</span>
            <span class="n">And</span><span class="p">(</span><span class="n">args</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">and_n</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">[</span><span class="mi">1</span><span class="p">:])))</span>

<span class="n">gcfI</span><span class="p">,</span> <span class="n">gcfE</span> <span class="o">=</span> <span class="n">infer_bidir</span><span class="p">(</span><span class="s">&#39;Defn GCF&#39;</span><span class="p">,</span> <span class="s">&#39;gcf&#39;</span><span class="p">,</span>
                         <span class="n">Equal</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="n">gcf</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)),</span>
                         <span class="n">and_n</span><span class="p">(</span><span class="n">gt</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="n">z</span><span class="p">),</span>
                               <span class="n">divides</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="n">a</span><span class="p">),</span>
                               <span class="n">divides</span><span class="p">(</span><span class="n">d</span><span class="p">,</span> <span class="n">b</span><span class="p">),</span>
                               <span class="n">A</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="n">Impl</span><span class="p">(</span><span class="n">And</span><span class="p">(</span><span class="n">divides</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="n">a</span><span class="p">),</span>
                                             <span class="n">divides</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="n">b</span><span class="p">)),</span>
                                         <span class="n">divides</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="n">d</span><span class="p">)))))</span>
                         
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Thm-(Euclid)">Thm (Euclid)<a class="anchor-link" href="#Thm-(Euclid)">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[8]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="k">def</span> <span class="nf">nz</span><span class="p">(</span><span class="n">x</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">Not</span><span class="p">(</span><span class="n">Equal</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">z</span><span class="p">))</span>

<span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">d</span><span class="p">,</span> <span class="n">m</span><span class="p">,</span> <span class="n">n</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">Variable</span><span class="p">,</span> <span class="s">&#39;a b d m n&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span class="n">s</span><span class="p">,</span> <span class="n">s1</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">Variable</span><span class="p">,</span> <span class="s">&#39;s s1&#39;</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>

<span class="n">thm_euclid</span> <span class="o">=</span> <span class="n">A</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">A</span><span class="p">(</span><span class="n">b</span><span class="p">,</span> <span class="n">Impl</span><span class="p">(</span><span class="n">Or</span><span class="p">(</span><span class="n">nz</span><span class="p">(</span><span class="n">a</span><span class="p">),</span> <span class="n">nz</span><span class="p">(</span><span class="n">b</span><span class="p">)),</span>
                            <span class="n">E</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">E</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">Equal</span><span class="p">(</span><span class="n">plus</span><span class="p">(</span><span class="n">times</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">a</span><span class="p">),</span> <span class="n">times</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">b</span><span class="p">)),</span>
                                            <span class="n">gcf</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)))))))</span>
<span class="n">checkp</span><span class="p">(</span><span class="n">thm_euclid</span><span class="p">,</span> <span class="n">given</span><span class="p">)</span>
</pre></div>

</div>
</div>

<div class="vbox output_wrapper">
<div class="output vbox">


<div class="hbox output_area"><div class="prompt"></div>
<div class="box-flex1 output_subarea output_stream output_stdout">
<pre>
Aa.Ab.((~(a = z) v ~(b = z)) -&gt; Em.En.(((m * a) + (n * b)) = gcf(a,b)))  (0)  Given

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[9]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">clear</span><span class="p">()</span>
<span class="n">checkp</span><span class="p">(</span><span class="n">Or</span><span class="p">(</span><span class="n">nz</span><span class="p">(</span><span class="n">a</span><span class="p">),</span> <span class="n">nz</span><span class="p">(</span><span class="n">b</span><span class="p">)),</span> <span class="n">given</span><span class="p">)</span>
</pre></div>

</div>
</div>

<div class="vbox output_wrapper">
<div class="output vbox">


<div class="hbox output_area"><div class="prompt"></div>
<div class="box-flex1 output_subarea output_stream output_stdout">
<pre>
~(a = z) v ~(b = z)       (0)  Given

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[10]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="n">checkp</span><span class="p">(</span><span class="n">E</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">A</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">Iff</span><span class="p">(</span><span class="n">elt</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">s</span><span class="p">),</span>
              <span class="n">E</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">E</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">Equal</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">plus</span><span class="p">(</span><span class="n">times</span><span class="p">(</span><span class="n">m</span><span class="p">,</span> <span class="n">a</span><span class="p">),</span> <span class="n">times</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">b</span><span class="p">)))))))),</span> <span class="n">abst</span><span class="p">)</span>
</pre></div>

</div>
</div>

<div class="vbox output_wrapper">
<div class="output vbox">


<div class="hbox output_area"><div class="prompt"></div>
<div class="box-flex1 output_subarea output_stream output_stdout">
<pre>
Es.Ax.((x .in. s) &lt;=&gt; Em.En.(x = ((m * a) + (n * b))))  (1)  Abstraction

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="TODO:-Formatting-with-MathJax">TODO: Formatting with MathJax<a class="anchor-link" href="#TODO:-Formatting-with-MathJax">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[11]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="kn">from</span> <span class="nn">IPython.core.formatters</span> <span class="kn">import</span> <span class="n">HTMLFormatter</span>
<span class="n">rich</span> <span class="o">=</span> <span class="n">HTMLFormatter</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">TODO</span><span class="p">:</span>
  <span class="k">def</span> <span class="nf">_repr_html_</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
    <span class="k">return</span> <span class="s">&#39;&lt;span class=&quot;math&quot;&gt;</span><span class="si">%s</span><span class="s"> | </span><span class="si">%s</span><span class="s">&lt;/span&gt;&#39;</span> <span class="o">%</span> <span class="nb">tuple</span><span class="p">([</span><span class="n">rich</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">args</span><span class="p">[</span><span class="n">ix</span><span class="p">])</span> <span class="k">for</span> <span class="n">ix</span> <span class="ow">in</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]])</span>
</pre></div>

</div>
</div>

</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Appendix:-FLiP-Installation">Appendix: FLiP Installation<a class="anchor-link" href="#Appendix:-FLiP-Installation">&#182;</a></h2>
</div>

<div class="cell border-box-sizing code_cell vbox">
<div class="input hbox">
<div class="prompt input_prompt">
In&nbsp;[12]:
</div>
<div class="input_area box-flex1">
<div class="highlight"><pre><span class="o">!</span>pip install flip
</pre></div>

</div>
</div>

<div class="vbox output_wrapper">
<div class="output vbox">


<div class="hbox output_area"><div class="prompt"></div>
<div class="box-flex1 output_subarea output_stream output_stdout">
<pre>
Requirement already satisfied (use --upgrade to upgrade): flip in /usr/local/lib/python2.7/dist-packages
Cleaning up...

</pre>
</div>
</div>

</div>
</div>

</div>