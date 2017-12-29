date: 2006-05-19
title: 'webizing TaskJuggler'
published: True
tags: ['breadcrumbs', 'calendar']

<div>
<p>
Going over my <a rel="tag"href="http://del.icio.us/connolly/calendar">calendar</a> bookmarks
I rediscovered <a href="http://www.taskjuggler.org/">TaskJuggler</a>:</p>

  <blockquote>TaskJuggler provides an optimizing scheduler that computes your project time lines and resource assignments based on the project outline and the constrains that you have provided. The build-in resource balancer and consistency checker offload you from having to worry about irrelevant details and ring the alarm if the project gets out of hand.</blockquote>

<p>Sound like this tool might be applicable to the hard problem of scheduling meetings with various constraints.</p>

<p>It seems to have a declarative project description language:</p>

<pre>
flags team

resource dev "Developers" {
  resource dev1 "Paul Smith" { rate 330.0 }
  resource dev2 "Sebastien Bono"
  resource dev3 "Klaus Mueller" { vacation 2002-02-01 - 2002-02-05 }

  flags team
}
resource misc "The Others" {
  resource test "Peter Murphy" { limits { dailymax 6.4h } rate 240.0 }
  resource doc "Dim Sung" { rate 280.0 }

  flags team
}
</pre>

<p>What might that look like in <a href="http://www.w3.org/DesignIssues/Notation3">N3</a>, i.e. in RDF that the <a href="http://dig.csail.mit.edu/2005/ajar/ajaw/About.html">tabulator</a> could browse around? (See the
<a href="http://www.w3.org/2000/10/swap/Primer">N3 primer</a> to get a feel for RDF and N3.)
What would it take
to <a href="http://www.w3.org/DesignIssues/Webize">webize</a> the Taks Juggler?</p>

<p>Also... how does the taskjuggler consistency checker relate to OWL consistency
checkers like <a href="http://www.mindswap.org/2003/pellet/">pellet</a>?</p>
