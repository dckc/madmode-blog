title: 'Exploring the Web Hosting Marketplace'
date: 2014-01-04
tags: [office, publishing, installation, vm, devops]
summary: The client I develop hh-office for is seeing poor performance, so I'm shopping for web hosting alternatives.
published: True


<div class="text_cell_render border-box-sizing rendered_html">
<p>The client I develop <a href="https://bitbucket.org/DanC/hh-office">hh-office</a> for is seeing poor performance, so I'm shopping for web hosting alternatives.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="LAMP-on-Dreamhost:-it's-easier-than-thinking">LAMP on Dreamhost: it's easier than thinking<a class="anchor-link" href="#LAMP-on-Dreamhost:-it's-easier-than-thinking">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>The app is an ordinary PHP/MySQL app with a few python bits and bobs. When I originally deployed it in late 2011, I knew:</p>
<ol style="list-style-type: decimal">
<li>Lots of people used dreamhost
<ul>
<li>including <a href="http://impressive.net/archives/fogo/20070109173322.GO5388@impressive.net">Gerald, a world-class sysadmin, back in 2007</a></li>
</ul></li>
<li>Lots of people <em>complain</em> about dreamhost.</li>
</ol>
<p>But it's not clear that the complaints about dreamhost indicate anything other than popularity. After all, as the <a href="http://indiewebcamp.com/web_hosting">IndieWebCamp folks say</a>, picking a web hosting service is in some ways like picking a cell phone provider, and we all complain about our cell phone providers, don't we?</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Shared-Hosting,-VPS,-and-System-Administration">Shared Hosting, VPS, and System Administration<a class="anchor-link" href="#Shared-Hosting,-VPS,-and-System-Administration">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>The first performance remedy I tried was the dreamhost $15/month <a href="http://www.dreamhost.com/servers/vps/">VPS hosting</a> upgrade, but it made little difference. I didn't read the documentation carefully enough to notice that <strong>the database is on a separate server</strong>. I think I saw some database-related upgrade options, but in <a href="https://drupal.org/node/120736">drupal performance discussion</a>, dreamhost is notorious for poor MySQL architecture and hence performance. So I went shopping for alternatives.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>I tried the <a href="http://bitnami.com/stack/lamp">LAMP Stack by bitnami</a> on Amazon EC2, but the hourly fees stareted to add up. One VM is more than enough for this app and I guess I should have known that <strong>scalable cloud hosting isn't cost-effective if I'm not using the scalability</strong>.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>So I returned to exploring the overcrowded shared hosting marketplace. justhost and site5 were nominated in the drupal discussion, as was arvixe. I looked to see if any of them had free trials, and I was reminded of <a href="http://owncloud.org/providers/">ownCloud hosts</a> with free plans, one of which was arvixe. I might have liked to chat with <a href="http://www.meetup.com/kcphpug/">other KC PHP devs</a>, but I was too impatient to wait for the next meeting, so based on arvixe's delightful sign-up experience its hostjury reviews, I went ahead and paid a few dollars to experiment with their shared hosting for a month.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>What jumped out at me, after experimenting with a couple VPS platforms, is the economy of scale in <strong>system administration services</strong> with shared hosting. For just a few dollars a month, not only will they install wordpress or phpBB for a few clicks, but they will administer mailing lists, backups, log files, and databases.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>I suppose I could have tried NearlyFreeSpeech.Net. For less than a dollar a month, it works fine for static sites like this blog. But while but while they support everything this app needs (PHP, MySQL and installing python from source), I don't wouldn't expect performance to be better than dreamhost on their shoestring budget.</p>
<p>Plus, I could see my boys making good use of the one-click phpBB installer and such.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>In the long term, here's hoping <a href="http://www.docker.io/">docker</a> drives the price of PAAS services like Heroku down to this price range and diversifies their feature set to include mailing lists.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Arvixe-over-Dreamhost?">Arvixe over Dreamhost?<a class="anchor-link" href="#Arvixe-over-Dreamhost?">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>As I explored arvixe, I had a little hiccup getting shell access, but <strong>live chat support</strong> took care of it fast enough that I didn't really lose stride.</p>
<p>After <a href="http://www.arvixe.com/linux_web_hosting">claims</a> that they &quot;provide the latest Python version,&quot; I was a little disappointed to see that this means they let you <a href="http://blog.arvixe.com/create-your-own-python-enviroment-locally-in-your-shared-hosting-account/">build it from source</a>. Oh well; I had to do that on dreamhost too; it seems to be par for the course and it takes just a few minutes.</p>
<p>Bandwidth seemed OK, not that downloading on the server is relevant to my app:</p>
<pre><code>[~]# wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tgz
... 14,725,931  2.76M/s   in 9.5s </code></pre>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<p>After copying the ~120K records about ~10K clients, the app did seem to respond a little quicker on arvixe, though I don't have any hard data. I did see that PHP and the MySQL database were running on the same server.</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="A-Summary-of-My-Experience-with-Web-Hosting-Services">A Summary of My Experience with Web Hosting Services<a class="anchor-link" href="#A-Summary-of-My-Experience-with-Web-Hosting-Services">&#182;</a></h2>
</div>

<div class="text_cell_render border-box-sizing rendered_html">
<p>I missed out on the first ten or fifteen years of this marketplace, since I was in something of a bubble provided by the W3C systems team.</p>
<p>Since then, these are the services I have used, with the one I'd most likely use again on top:</p>
</div>
<div class="text_cell_render border-box-sizing rendered_html">
<ul>
<li>domain registrar:
<ul>
<li>namecheap</li>
<li>nearlyfreespeech.net
<ul>
<li>A consequence of their transparent pricing model is deposit fees. Namecheap's scale seems to hide such things.</li>
</ul></li>
<li>gandi
<ul>
<li>International credit card transactions are a little inconvenient.</li>
</ul></li>
</ul></li>
<li>DNS management (connecting domains to hosts)
<ul>
<li>namecheap</li>
<li>nearlyfreespeech.net</li>
<li>Amazon Route5</li>
<li>zonedit.com
<ul>
<li>Was great when the only alternative was <code>bind</code> config files!</li>
</ul></li>
</ul></li>
<li>Shared hosting:
<ul>
<li>arvixe</li>
<li>NearlyFreeSpeech.Net
<ul>
<li>Image bandwidth seems limited, for understandable reasons.</li>
</ul></li>
<li>dreamhost
<ul>
<li>Docs suggest a long, heavy legacy (reminds me of W3C in that way).</li>
</ul></li>
</ul></li>
<li>blogging SAS:
<ul>
<li>wordpress</li>
<li>blogger
<ul>
<li>Cheaper than blogger for bring-your-own-domain service, but you get what you pay for.</li>
</ul></li>
</ul></li>
<li>PAAS
<ul>
<li><a href="http://www.docker.io/">docker</a></li>
</ul></li>
<li>VPS:
<ul>
<li>AWS EC2</li>
<li>dreamhost</li>
</ul></li>
</ul>
</div>