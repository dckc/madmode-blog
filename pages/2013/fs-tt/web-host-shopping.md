title: 'Web Host Shopping'
date: 2014-01-04
tags: [office, publishing, installation, vm, devops]


<div class="text_cell_render border-box-sizing rendered_html">
<p>The client I develop <a href="https://bitbucket.org/DanC/hh-office">hh-office</a> for is seeing poor performance, so I'm shopping for web hosting alternatives.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>It's an ordinary PHP/MySQL app with a few python bits and bobs. When I originally deployed it in last 2011, I knew:</p>
<ol style="list-style-type: decimal">
<li>Lots of people (including <a href="http://impressive.net/archives/fogo/20070109173322.GO5388@impressive.net">Gerald back in 2007</a>) used dreamhost.</li>
<li>Lots of people complain about dreamhost.</li>
</ol>
<p>But it's not clear that the complaints about dreamhost indicate anything other than popularity. After all, as the <a href="http://indiewebcamp.com/web_hosting">IndieWebCamp folks say</a>,</p>
<blockquote>
<p>Picking [a web hosting service] is in some ways like picking a cell phone provider - criteria may include things like: cost, levels of service, reliability, customer support.</p>
</blockquote>
<p>... and we all complain about our cell phone providers.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>The first performance remedy I tried was the $15/month <a href="http://www.dreamhost.com/servers/vps/">VPS hosting</a> upgrade, but it made little difference. I didn't read the documentation carefully enough to notice that <strong>the database is on a separate server</strong>. I think I saw some database-related upgrade options, but in <a href="https://drupal.org/node/120736">drupal performance discussion</a>, dreamhost seems to be somewhat notorious for poor MySQL architecture and hence performance. So I went shopping for alternatives.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>I tried cloud hosting with the <a href="http://bitnami.com/stack/lamp">LAMP Stack by bitnami</a> on Amazon EC2, but one VM is more than enough for this app and I guess I should have known that scalable <strong>cloud hosting isn't cost-effective if I'm not using the scalability</strong>.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>So I returned to exploring the overcrowded shared hosting marketplace. justhost and site5 were nominated in the drupal discussion, as was arvixe. I looked to see if any of them had free trials, and I was reminded of <a href="http://owncloud.org/providers/">ownCloud hosts</a> with free plans, one of which was arvixe. Based on that delightful sign-up experience and <a href="http://www.hostjury.com/reviews/arvixe">good reviews on hostjury</a>, I went ahead and bought a month's worth ($7) of shared hosting.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>I had a little hiccough getting shell access, but live chat support took care of it fast enough that I didn't really lose stride.</p>
<p>After <a href="http://www.arvixe.com/linux_web_hosting">claims</a> that they &quot;provide the latest Python version,&quot; I was a little disappointed to see that this means they let you <a href="http://blog.arvixe.com/create-your-own-python-enviroment-locally-in-your-shared-hosting-account/">build it from source</a>. Oh well; I had to do that on dreamhost too; it seems to be par for the course and it takes just a few minutes.</p>
<p>Bandwidth seemed OK, not that downloading on the server is relevant to my app:</p>
<pre><code>[~]# wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tgz
... 14,725,931  2.76M/s   in 9.5s </code></pre>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<hr />
<h2 id="fodder">Fodder</h2>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>dreamhost docs show a lot of legacy (reminds me of W3C)</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>services I use (or have used?)</p>
<ul>
<li>Shared hosting:</li>
<li>W3C server at MIT</li>
<li>dreamhost</li>
<li><p>arvixe</p></li>
<li>DNS mgmt:</li>
<li>zonedit.com</li>
<li>nearlyfreespeech.net</li>
<li><p>amazon Route5</p></li>
<li>blogging SAS:</li>
<li>wordpress</li>
<li><p>blogger</p></li>
<li>domain registrar:</li>
<li>gandi</li>
<li>namecheap</li>
<li><p>nearlyfreespeech.net</p></li>
<li>VPS:</li>
<li>AWS EC2</li>
<li><p>dreamhost</p></li>
</ul>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>tinytiny rss. it complained &quot;that folder is wrong and doesn't exist&quot; so I created it. then it (a similar page) complained that it exists.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>hope to chat with http://www.meetup.com/kcphpug/</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>hmmm mailing list hosting</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>Dec 26: make docker container for hh-office?</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>try hh-office oh Amazon Elastic Beanstalk?</p>
</div>