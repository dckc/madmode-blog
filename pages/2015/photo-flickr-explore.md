title: Syncing a 5 Year iPhoto Library with flickr
date: 2015-07-07
tags: [mac, photo, sysadmin]
published: true

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Yay! jawj's <a href="https://github.com/jawj/iphoto-flickr">iphoto-flickr</a> sync'd a 30GB iPhoto library flickr. Not only did it upload the images, but it made a map from iPhoto metadata to flickr metadata that lets me continue on with the flickr API, syncing dates and such, during and after the upload.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="OS-X-Yosemite-runs-iPhoto,-reluctantly">OS X Yosemite runs iPhoto, reluctantly<a class="anchor-link" href="#OS-X-Yosemite-runs-iPhoto,-reluctantly">&#182;</a></h2><p>Having replaced it with a newer model, I gave <strong>airbook</strong>, our late 2008 MacBook Air MB543LL/A, a complete labotomy and installed OS X Yosemite. When I tried to re-introduce it to our photo archive, Apple told me iPhoto is no longer; Photos is the new thing, complete with iCloud hip-ness.</p>
<p>So I'm faced with another "to Mac or not to Mac?" moment.</p>
<p>This time I figure no, I lead a multi-platform life and I want something more web-native.</p>
<p>I spent a bunch of time trying to downgrade to Mavericks. Just when I had given up trying to do it myself and ordered Mavericks on a USB flash drive via eBay, I learned that if you <a href="http://www.simplehelp.net/2015/05/01/how-to-install-iphoto-in-yosemite-os-x-10-10/#comment-2097851737">start iPhoto from a command prompt</a>, it runs on Yosemite after all.</p>
<p>The only complication was a dangling reference to <code>iLifeSlideshow.framework</code> in <code>/System/Library/PrivateFrameworks</code>. (Thank you <a href="https://bombich.com/">Carbon Copy Cloner</a> for a complete backup!)</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>it's time to take flickr up on the terabyte storage offer from they've been running since May 2013. My friends-and-family photo sharing community mostly uses facebook these days, but for curating an archive, flickr is a much better match:</p>
<ul>
<li>datetaken separate from date uploaded</li>
<li>easy access to original photo</li>
<li>archive by date taken</li>
<li>by place on map</li>
<li>by tag</li>
</ul>
<p>2004 flickr DanC (er... or was that when I created the affiliated yahoo account?)
2006-03: dckc on flickr: travel, kids, dogs, banff, roadtrip, ...
<a href="https://www.flickr.com/photos/dckc/archives/date-posted/2004/12/calendar/">https://www.flickr.com/photos/dckc/archives/date-posted/2004/12/calendar/</a> shows I posted in Dec 2004</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Home-directory-in-encrypted-sparsebundle">Home directory in encrypted sparsebundle<a class="anchor-link" href="#Home-directory-in-encrypted-sparsebundle">&#182;</a></h3><p>This photo library is on an external USB drive, in an encrypted sparsebundle. The <a href="https://discussions.apple.com/thread/2082558?tstart=0">sparsebundle support discussion</a> said all I have to do is double-click it, but it's hidden (filename starts with a dot). Command-line to the rescue, again: <code>open /Users/.maryc</code>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Flickr-is-the-web-photo-service-for-the-closet-librarian">Flickr is the web photo service for the closet librarian<a class="anchor-link" href="#Flickr-is-the-web-photo-service-for-the-closet-librarian">&#182;</a></h2><p>As an Android mobile user, Google's photo offerings were tempting. Then I discovered browsing photos of person X only works within one album. And to put a photo in multiple albums, you have to copy it, i.e. maintain the tags and such twice.</p>
<p>My friends-and-family photo sharing community mostly uses facebook these days, but for curating an archive, flickr is a much better match. Imagine my horror when I downloaded some of my photos from facebook and discovered they were only available at reduced resolution. Perhaps they've addressed that since, but I still haven't seen any support for date-taken as separate from date-uploaded on facebook. There's little, if any, support for quietly curating without notifications firing every which way.</p>
<p>My photostream on flickr goes back to <a href="https://www.flickr.com/photos/dckc/archives/date-posted/2004/12/calendar/">Dec 2004</a> when it was big in the open web community. I could never bring myself to go premium, but in May 2013 when they announced the terabyte storage offer, I dusted it off. Re-establishing my long lost yahoo credentials was no small feat, but I managed.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Flickr-Backup-from-Mac-App-Store-was-a-Bust">Flickr Backup from Mac App Store was a Bust<a class="anchor-link" href="#Flickr-Backup-from-Mac-App-Store-was-a-Bust">&#182;</a></h2><p>A quick search of the Mac App store turned up promising results:</p>
<ul>
<li><a href="https://itunes.apple.com/us/app/backup-to-flickr-for-iphoto/id733300407?mt=12">Backup to Flickr for iPhoto</a><br>
By Sonia Bohelay</li>
</ul>
<p>It was just a few bucks, so I went ahead. But oops: <strong>Your iPhoto library is either too old (iPhoto version &lt; 9.0) or no photo found</strong>. Indeed, my library is from 8.1.2. I might have been able to upgrade the library, but with Apple pushing Photos over iPhoto, I didn't want to bet on it.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="iPhoto--&gt;-Flickr-in-350-lines-of-code">iPhoto -&gt; Flickr in 350 lines of code<a class="anchor-link" href="#iPhoto--&gt;-Flickr-in-350-lines-of-code">&#182;</a></h2><p>I was thinking about rolling my own with the flickr API when I discovered a kindred spirit had already been down this path and come up with <a href="https://github.com/jawj/iphoto-flickr">iPhoto -&gt; Flickr</a>.</p>
<p>It worked in one go, so the incremental upload support wasn't necessary for the initial bulk upload, but to further sync the metadata, the resulting <code>uploaded-photo-ids-map.txt</code> is critical. In fact, I had to wrestle with iPhoto a bit to get ids that are useful without iPhoto running.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Just-Add-API-Key-and-Authorize-with-OAuth">Just Add API Key and Authorize with OAuth<a class="anchor-link" href="#Just-Add-API-Key-and-Authorize-with-OAuth">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>It works pretty much like it says on the tin. (<em>The <a href="https://github.com/jawj/iphoto-flickr/issues/22">colorize dependency issue</a> was easy enough to figure out.</em>)</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

<pre><code>airbook:src connolly$ git clone https://github.com/jawj/flickrbackup.git  # e339169212
airbook:flickrbackup connolly$ sudo gem install flickraw-cached colorize
Successfully installed flickraw-0.9.8
Successfully installed flickraw-cached-20120701
Successfully installed colorize-0.7.7

airbook:flickrbackup connolly$ ruby flickrbackup.rb 

Flickr API key: 0481...
Flickr API shared secret: 897...
Authorise access to your Flickr account: press [Return] when ready
Authorisation code: 162-...

2015-07-04 13:47:28 -0500  Authenticated as: DanC

2015-07-04 13:47:44 -0500  8057 photos and 78 standard albums in iPhoto library
2015-07-04 13:47:44 -0500  8057 photos not yet uploaded to Flickr</code></pre>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Platform-Independent-Data">Platform Independent Data<a class="anchor-link" href="#Platform-Independent-Data">&#182;</a></h2><p>The kernel for this notebook is on my linux desktop, but iPhoto is running on <strong>airbook</strong>.</p>
<p><em>Since spaces in filenames are a royal pain over ssh, I made a convenient symlink.</em></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[190]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">!</span>ssh airbook.local ls -l Pictures/flickrbackup
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>lrwxr-xr-x  1 connolly  staff  57 Jul  5 09:34 Pictures/flickrbackup -&gt; /Users/connolly/Library/Application Support/flickrbackup/
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Upload-Map-DataFrame">Upload Map DataFrame<a class="anchor-link" href="#Upload-Map-DataFrame">&#182;</a></h2><p>It carefully logs the correspondence to support incremental update:</p>

<pre><code>2015-07-04 13:47:44 -0500  (1/8057)  Uploading '...2002/Sep 25, 2002/....jpg' ... 4294967334 -&gt; 19226418710</code></pre>
<p>Let's make sure we have redundant copies of the map. And let's use ordinary CSV rather than the funky <code>-&gt;</code> format.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[191]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">from</span> <span class="nn">IPython.display</span> <span class="kn">import</span> <span class="n">display</span><span class="p">,</span> <span class="n">Image</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="kn">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="kn">as</span> <span class="nn">np</span>
<span class="nb">dict</span><span class="p">(</span><span class="n">pandas</span><span class="o">=</span><span class="n">pd</span><span class="o">.</span><span class="n">__version__</span><span class="p">,</span> <span class="n">numpy</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[191]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>{&apos;numpy&apos;: &apos;1.9.2&apos;, &apos;pandas&apos;: &apos;0.14.1&apos;}</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[112]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">upload_map</span> <span class="o">=</span> <span class="o">!</span>ssh airbook.local cat Pictures/flickrbackup/uploaded-photo-ids-map.txt
<span class="n">upload_map</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="nb">dict</span><span class="p">(</span><span class="n">apple</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">a</span><span class="p">),</span> <span class="n">flickr</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">f</span><span class="p">))</span>
                          <span class="k">for</span> <span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">f</span><span class="p">)</span> <span class="ow">in</span> <span class="p">[</span><span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; -&gt; &#39;</span><span class="p">)</span> <span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">upload_map</span><span class="p">])</span>
<span class="n">upload_map</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[112]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>apple</th>
      <th>flickr</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 4294967334</td>
      <td> 19226418710</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 4294976544</td>
      <td> 18793385783</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 4294976530</td>
      <td> 18793388523</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4294976542</td>
      <td> 18791506174</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 4294971867</td>
      <td> 19414016905</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[187]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">upload_map</span><span class="o">.</span><span class="n">to_csv</span><span class="p">(</span><span class="s">&#39;uploaded-photo-ids-map.csv&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Flickr-metadata-access">Flickr metadata access<a class="anchor-link" href="#Flickr-metadata-access">&#182;</a></h2><p>Let's take a at the results on flickr. I experimented with python flickr apis; the main one seems to be <a href="http://stuvel.eu/media/flickrapi-docs/documentation/index.html">Python Flickr</a>. <a href="flickdata.py">flickdata.py</a> (in <a href="http://bitbucket.org/DanC/palmagent/">palmagent</a>) is a least-authority packaging of that API.</p>
<p><em>TODO: use a separate Photo object for setDates.</em></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[168]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">flickdata</span>
<span class="nb">reload</span><span class="p">(</span><span class="n">flickdata</span><span class="p">)</span>
<span class="n">flickdata</span><span class="o">.</span><span class="n">__version__</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[168]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>&apos;0.4&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To make a <code>flickdata.Account</code>, we use the privileged iPython notebook environment to get network access and the API key (<em>and OAuth credentials... where do they get squirrelled away?</em>) and pass it to <code>flickdata</code>:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[45]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">logging</span>
<span class="n">logger</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">()</span>
<span class="n">logger</span><span class="o">.</span><span class="n">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">INFO</span><span class="p">)</span>
<span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">(</span><span class="s">&#39;We try to log I/O.&#39;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>INFO:root:We try to log I/O.
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[75]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">myFlickrAcct</span><span class="p">(</span><span class="n">user_id</span><span class="o">=</span><span class="s">&#39;14874637@N00&#39;</span><span class="p">):</span>
    <span class="kn">import</span> <span class="nn">pathlib</span>
    <span class="kn">import</span> <span class="nn">flickrapi</span>
    <span class="n">api_secret</span> <span class="o">=</span> <span class="n">pathlib</span><span class="o">.</span><span class="n">Path</span><span class="p">(</span><span class="s">&#39;flickr_api_secret&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">open</span><span class="p">()</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">flickdata</span><span class="o">.</span><span class="n">Read</span><span class="o">.</span><span class="n">make</span><span class="p">(</span><span class="n">flickrapi</span><span class="p">,</span> <span class="n">api_secret</span><span class="p">,</span> <span class="n">user_id</span><span class="p">)</span>

<span class="n">myAcct</span> <span class="o">=</span> <span class="n">myFlickrAcct</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>INFO:flickdata:authenticating...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.auth.oauth.checkToken&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickrapi.core:REST Parser: using xml.etree.cElementTree
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Photostream-confused-about-recent-photos">Photostream confused about recent photos<a class="anchor-link" href="#Photostream-confused-about-recent-photos">&#182;</a></h3><p>A bunch of old photos and videos are showing up as recent in my photostream as the upload progresses.</p>
<p>Flickr seems to set datetaken = date uploaded when there's no EXIF date, so let's look at these supposedly recent photos.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[172]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">records</span> <span class="o">=</span> <span class="p">[</span>
    <span class="n">r</span>
    <span class="k">for</span> <span class="n">page</span> <span class="ow">in</span>
    <span class="n">myAcct</span><span class="o">.</span><span class="n">getPhotos</span><span class="p">(</span>
        <span class="n">min_taken_date</span><span class="o">=</span><span class="s">&#39;2015-07&#39;</span><span class="p">,</span>
        <span class="n">max_taken_date</span><span class="o">=</span><span class="s">&#39;2015-08&#39;</span><span class="p">,</span>
        <span class="n">sort</span><span class="o">=</span><span class="s">&#39;date-taken-asc&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">r</span> <span class="ow">in</span> <span class="n">page</span><span class="p">]</span>
<span class="n">photo</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">records</span><span class="p">)</span>
<span class="n">photo</span><span class="p">[</span><span class="s">&#39;id&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">photo</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>  <span class="c"># odd... even in JSON format, ids come back as strings</span>
<span class="n">photo</span> <span class="o">=</span> <span class="n">photo</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s">&#39;id&#39;</span><span class="p">)</span>
<span class="nb">len</span><span class="p">(</span><span class="n">photo</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>INFO:flickdata:getPhotos page 1 cirt: {&apos;sort&apos;: &apos;date-taken-asc&apos;, &apos;min_taken_date&apos;: &apos;2015-07&apos;, &apos;max_taken_date&apos;: &apos;2015-08&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.people.getPhotos&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:page 1 of 1
</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">Out[172]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>78</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Photo-URLs:-Thumbnail">Photo URLs: Thumbnail<a class="anchor-link" href="#Photo-URLs:-Thumbnail">&#182;</a></h3><p>Flickr's <a href="https://www.flickr.com/services/api/misc.urls.html">URLs API</a> uses "secrets" so they serve as nice tasty <a href="http://www.w3.org/TR/capability-urls/">capability URLs</a> for the photos. So we can see this thumbnail from this iPython notebook even though we're not logged in to flickr here.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[173]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">Image</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">photo</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">url_t</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[173]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<img src="https://farm1.staticflickr.com/540/19350464562_2ff03b551d_t.jpg"/>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Photo-info-fields">Photo info fields<a class="anchor-link" href="#Photo-info-fields">&#182;</a></h3><p><em>Note: this isn't all fields available from <a href="https://www.flickr.com/services/api/flickr.galleries.getPhotos.html">getPhotos</a></em>.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[174]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">photo</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[174]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>accuracy                                                               16
context                                                                 0
datetaken                                             2015-07-02 11:28:40
datetakengranularity                                                    0
datetakenunknown                                                        0
dateupload                                                     1435854531
description                                            {u&apos;_content&apos;: u&apos;&apos;}
farm                                                                    1
geo_is_contact                                                          0
geo_is_family                                                           0
geo_is_friend                                                           0
geo_is_public                                                           1
height_k                                                             1516
height_o                                                             2368
height_t                                                               74
height_z                                                              474
isfamily                                                                0
isfriend                                                                0
ispublic                                                                0
latitude                                                        39.054611
longitude                                                      -94.611264
machine_tags                                                             
owner                                                        14874637@N00
place_id                                               _zncmCVTVLmQsuBlEg
secret                                                         2ff03b551d
server                                                                540
tags                                                                     
title                                                 IMG_20150702_112835
url_k                   https://farm1.staticflickr.com/540/19350464562...
url_o                   https://farm1.staticflickr.com/540/19350464562...
url_t                   https://farm1.staticflickr.com/540/19350464562...
url_z                   https://farm1.staticflickr.com/540/19350464562...
width_k                                                              2048
width_o                                                              3200
width_t                                                               100
width_z                                                               640
woeid                                                            26342889
Name: 19350464562, dtype: object</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Ah. Good. When the display defaults date taken to upload date, the underlying data tells us so:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[176]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">datetime</span>

<span class="n">photo</span><span class="p">[</span><span class="s">&#39;upload_date&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">np</span><span class="o">.</span><span class="n">datetime64</span><span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="o">.</span><span class="n">fromtimestamp</span><span class="p">(</span><span class="nb">int</span><span class="p">(</span><span class="n">ts</span><span class="p">)))</span> <span class="k">for</span> <span class="n">ts</span> <span class="ow">in</span> <span class="n">photo</span><span class="o">.</span><span class="n">dateupload</span><span class="p">]</span>
<span class="n">photo</span><span class="p">[</span><span class="n">photo</span><span class="o">.</span><span class="n">datetakenunknown</span> <span class="o">==</span> <span class="s">&#39;1&#39;</span><span class="p">][[</span><span class="s">&#39;datetaken&#39;</span><span class="p">,</span> <span class="s">&#39;upload_date&#39;</span><span class="p">,</span> <span class="s">&#39;title&#39;</span><span class="p">,</span> <span class="s">&#39;width_o&#39;</span><span class="p">,</span> <span class="s">&#39;height_o&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[176]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datetaken</th>
      <th>upload_date</th>
      <th>title</th>
      <th>width_o</th>
      <th>height_o</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19426161436</th>
      <td> 2015-07-05 20:23:04</td>
      <td>2015-07-05 20:23:04</td>
      <td>  segway tour - 4</td>
      <td>  466</td>
      <td>  630</td>
    </tr>
    <tr>
      <th>19456508621</th>
      <td> 2015-07-05 20:23:10</td>
      <td>2015-07-05 20:23:10</td>
      <td> segway tour - 28</td>
      <td>  851</td>
      <td>  630</td>
    </tr>
    <tr>
      <th>19266094319</th>
      <td> 2015-07-05 20:23:12</td>
      <td>2015-07-05 20:23:12</td>
      <td>  segway tour - 2</td>
      <td>  466</td>
      <td>  630</td>
    </tr>
    <tr>
      <th>19264673498</th>
      <td> 2015-07-05 20:23:16</td>
      <td>2015-07-05 20:23:16</td>
      <td> segway tour - 33</td>
      <td>  466</td>
      <td>  630</td>
    </tr>
    <tr>
      <th>19445946592</th>
      <td> 2015-07-05 20:23:47</td>
      <td>2015-07-05 20:23:47</td>
      <td> Brennan baby tub</td>
      <td> 2351</td>
      <td> 2945</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>These were uploaded very soon after being taken; I suppose I turned on auto-upload on my phone:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[192]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">photo</span><span class="p">[</span><span class="n">photo</span><span class="o">.</span><span class="n">datetakenunknown</span> <span class="o">==</span> <span class="s">&#39;0&#39;</span><span class="p">][[</span><span class="s">&#39;datetaken&#39;</span><span class="p">,</span> <span class="s">&#39;upload_date&#39;</span><span class="p">,</span> <span class="s">&#39;title&#39;</span><span class="p">,</span> <span class="s">&#39;width_o&#39;</span><span class="p">,</span> <span class="s">&#39;height_o&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[192]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datetaken</th>
      <th>upload_date</th>
      <th>title</th>
      <th>width_o</th>
      <th>height_o</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19350464562</th>
      <td> 2015-07-02 11:28:40</td>
      <td>2015-07-02 11:28:51</td>
      <td> IMG_20150702_112835</td>
      <td> 3200</td>
      <td> 2368</td>
    </tr>
    <tr>
      <th>19425609241</th>
      <td> 2015-07-04 13:17:22</td>
      <td>2015-07-04 19:49:20</td>
      <td>                    </td>
      <td> 1122</td>
      <td>  712</td>
    </tr>
    <tr>
      <th>19235236159</th>
      <td> 2015-07-04 13:17:33</td>
      <td>2015-07-04 19:49:22</td>
      <td>                    </td>
      <td>  458</td>
      <td>   46</td>
    </tr>
    <tr>
      <th>18800793223</th>
      <td> 2015-07-04 13:17:43</td>
      <td>2015-07-04 19:49:23</td>
      <td>                    </td>
      <td>  546</td>
      <td>  100</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I verified the most recent upload dates against iphoto-flickr logs to be sure there were no timezone issues:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[177]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">photo</span><span class="p">[[</span><span class="s">&#39;datetaken&#39;</span><span class="p">,</span> <span class="s">&#39;upload_date&#39;</span><span class="p">,</span> <span class="s">&#39;title&#39;</span><span class="p">,</span> <span class="s">&#39;width_o&#39;</span><span class="p">,</span> <span class="s">&#39;height_o&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">sort</span><span class="p">(</span><span class="s">&#39;upload_date&#39;</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[177]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>datetaken</th>
      <th>upload_date</th>
      <th>title</th>
      <th>width_o</th>
      <th>height_o</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19453379905</th>
      <td> 2015-07-05 21:18:18</td>
      <td>2015-07-05 21:18:18</td>
      <td> 11223919_10103150053978467_4385673914430987089_n</td>
      <td> 960</td>
      <td> 639</td>
    </tr>
    <tr>
      <th>19457659531</th>
      <td> 2015-07-05 21:18:17</td>
      <td>2015-07-05 21:18:17</td>
      <td>                        Dining_Room_Turned_Office</td>
      <td> 550</td>
      <td> 400</td>
    </tr>
    <tr>
      <th>19447074092</th>
      <td> 2015-07-05 21:18:04</td>
      <td>2015-07-05 21:18:04</td>
      <td> 11261973_10103150053743937_5354724846552149885_n</td>
      <td> 960</td>
      <td> 639</td>
    </tr>
    <tr>
      <th>19447070902</th>
      <td> 2015-07-05 21:17:59</td>
      <td>2015-07-05 21:17:59</td>
      <td> 11143223_10103150052730967_2134381211714517553_n</td>
      <td> 960</td>
      <td> 639</td>
    </tr>
    <tr>
      <th>19457651521</th>
      <td> 2015-07-05 21:17:55</td>
      <td>2015-07-05 21:17:55</td>
      <td> 11265214_10103150052591247_2966764364887797640_n</td>
      <td> 960</td>
      <td> 639</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="iPhoto,-give-me-my-data-back!">iPhoto, give me my data back!<a class="anchor-link" href="#iPhoto,-give-me-my-data-back!">&#182;</a></h2><p>flickrbackup found the library I'm interested in even though it's not in the default path. Ah... it's using Applescript.</p>
<p>iPhoto uses fairly nice .xml and .db files with a nice, sturdy uuid for each photo. But the id <code>flickerbackup.rb</code> got via applescript is nowhere to be found in there!</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">!</span>ssh airbook.local grep <span class="o">{</span>photo.index<span class="o">[</span>0<span class="o">]}</span> Pictures/flickrbackup/uploaded-photo-ids-map.txt 
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>4294967334 -&gt; 19226418710
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">!</span>ssh airbook.local grep <span class="m">4294967334</span> Pictures/iphoto-maryc/AlbumData.xml
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">!</span>ssh airbook.local sqlite3 Pictures/iphoto-maryc/iPhotoMain.db .dump <span class="p">|</span> grep <span class="m">4294967334</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The <a href="http://www.mugginsoft.com/html/kosmictask/ASDictionaryDocs/Apple/iPhoto/OS-X-10.7/iPhoto-9.2.3/html/">iPhoto script dictionary</a> doesn't show a uid property. <strong>Darn.</strong> We'll have to use file paths or something.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="iPhoto-takes-orders-in-JavaScript">iPhoto takes orders in JavaScript<a class="anchor-link" href="#iPhoto-takes-orders-in-JavaScript">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Ooh! We can use <a href="https://developer.apple.com/library/mac/releasenotes/InterapplicationCommunication/RN-JavaScriptForAutomation/">JXA</a>, JavaScript for Automation. Somebody made a nice <a href="https://github.com/dtinth/JXA-Cookbook/wiki/Using-JavaScript-for-Automation">cookbook</a> on github.</p>
<p>The first API I found for writing a string to a file was this <code>$.NSString</code> objective-C bridge thing. Oh well. It works.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[39]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">export_keys</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span>
<span class="s">#!/usr/bin/env osascript -l JavaScript</span>

<span class="s">function save(info, where) {</span>
<span class="s">    console.log(&#39;saving to...&#39;, where)</span>
<span class="s">    var str = $.NSString.alloc.initWithUTF8String(JSON.stringify(info));</span>
<span class="s">    str.writeToFileAtomicallyEncodingError(where, true, $.NSUTF8StringEncoding, null);    </span>
<span class="s">}</span>

<span class="s">function getKeys(iPhoto) {</span>
<span class="s">    var photos = iPhoto.photoLibraryAlbum().photos;</span>

<span class="s">    return {</span>
<span class="s">        id: photos.id(),</span>
<span class="s">        date: photos.date(),</span>
<span class="s">        width: photos.width(),</span>
<span class="s">        height: photos.height(),</span>
<span class="s">        originalPath: photos.originalPath(),</span>
<span class="s">        imagePath: photos.imagePath()</span>
<span class="s">    };</span>
<span class="s">}</span>

<span class="s">function run(argv) {</span>
<span class="s">    out = argv[0];</span>
<span class="s">    iPhoto = Application(&#39;iPhoto&#39;);</span>
<span class="s">    save(getKeys(iPhoto), out)</span>
<span class="s">}</span>
<span class="s">&#39;&#39;&#39;</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's save it, <code>scp</code> it over, run it, and <code>scp</code> the results back:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[40]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">save_script</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span>
    <span class="kn">from</span> <span class="nn">pathlib</span> <span class="kn">import</span> <span class="n">Path</span>
    <span class="k">with</span> <span class="n">Path</span><span class="p">(</span><span class="s">&#39;photo_keys.js&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s">&#39;wb&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">out</span><span class="p">:</span>
        <span class="n">out</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">export_keys</span><span class="p">)</span>

<span class="n">save_script</span><span class="p">(</span><span class="s">&#39;photo_keys.js&#39;</span><span class="p">,</span> <span class="n">export_keys</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[41]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">!</span>scp photo_keys.js airbook.local:Pictures/
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>photo_keys.js                                 100%  687     0.7KB/s   00:00    
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[42]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">!</span>ssh airbook.local osascript -l JavaScript Pictures/photo_keys.js Pictures/keys.json
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>saving to... Pictures/keys.json

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[43]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="o">!</span>scp airbook.local:Pictures/keys.json .
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>keys.json                                     100% 1697KB 848.6KB/s   00:02    
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we can ground these ids in key information such as file paths, dates, and image sizes that we can join with other sources:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[47]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">pk</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">json</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="nb">open</span><span class="p">(</span><span class="s">&#39;keys.json&#39;</span><span class="p">)))</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s">&#39;id&#39;</span><span class="p">)</span>
<span class="n">pk</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[47]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>height</th>
      <th>imagePath</th>
      <th>originalPath</th>
      <th>width</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4294967334</th>
      <td> 2002-09-25T15:14:23.000Z</td>
      <td>  600</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td>  800</td>
    </tr>
    <tr>
      <th>4294976544</th>
      <td> 2003-07-21T03:52:05.000Z</td>
      <td> 1385</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 1332</td>
    </tr>
    <tr>
      <th>4294976530</th>
      <td> 2003-08-08T20:09:51.000Z</td>
      <td> 1459</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Modifie...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 1647</td>
    </tr>
    <tr>
      <th>4294976542</th>
      <td> 2003-08-08T20:09:51.000Z</td>
      <td> 1536</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 2048</td>
    </tr>
    <tr>
      <th>4294971867</th>
      <td> 2006-02-01T17:05:22.000Z</td>
      <td>  377</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td>  495</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Applescript reports the full image paths, but we'll need library-relative paths for our work below.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[62]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">libloc</span> <span class="o">=</span> <span class="s">&#39;/Volumes/maryc/Pictures/iPhoto Library/&#39;</span>  <span class="c"># TODO: get from applescript?</span>

<span class="n">pk</span><span class="p">[</span><span class="s">&#39;relativePath&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">p</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">libloc</span><span class="p">):]</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">pk</span><span class="o">.</span><span class="n">imagePath</span><span class="p">]</span>

<span class="n">pk</span><span class="p">[(</span><span class="n">pk</span><span class="o">.</span><span class="n">date</span> <span class="o">&gt;=</span> <span class="s">&#39;2002-09&#39;</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">pk</span><span class="o">.</span><span class="n">date</span> <span class="o">&lt;</span> <span class="s">&#39;2002-10&#39;</span><span class="p">)][[</span><span class="s">&#39;date&#39;</span><span class="p">,</span> <span class="s">&#39;height&#39;</span><span class="p">,</span> <span class="s">&#39;width&#39;</span><span class="p">,</span> <span class="s">&#39;relativePath&#39;</span><span class="p">]]</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[62]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>height</th>
      <th>width</th>
      <th>relativePath</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4294967334</th>
      <td> 2002-09-25T15:14:23.000Z</td>
      <td> 600</td>
      <td> 800</td>
      <td> Originals/2002/Sep 25, 2002/Santa Cecelia gran...</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="iPhoto-data-without-iPhoto">iPhoto data without iPhoto<a class="anchor-link" href="#iPhoto-data-without-iPhoto">&#182;</a></h2><p>iPhoto keeps nice sqlite3 databases.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[207]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">my_photo_db</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="s">&#39;maryc-airbook-iphoto-meta/iPhotoMain.db&#39;</span><span class="p">):</span>
    <span class="kn">import</span> <span class="nn">sqlite3</span>
    <span class="k">return</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>

<span class="n">db1</span> <span class="o">=</span> <span class="n">my_photo_db</span><span class="p">()</span>

<span class="n">q</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span>
<span class="s">select count(distinct uid) from SqPhotoInfo</span>
<span class="s">&#39;&#39;&#39;</span>
<span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="n">q</span><span class="p">,</span> <span class="n">db1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[207]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count(distinct uid)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 8607</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[212]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">q</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span>
<span class="s">select count(*) qty, year from (</span>
<span class="s">  select substr(datetime(photoDate +  julianday(&#39;2000-01-01 00:00:00&#39;)), 1, 4) year</span>
<span class="s">  from SqPhotoInfo</span>
<span class="s">) t</span>
<span class="s">group by year</span>
<span class="s">having count(*) &gt; 10</span>
<span class="s">&#39;&#39;&#39;</span>
<span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="n">q</span><span class="p">,</span> <span class="n">db1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[212]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>qty</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>  306</td>
      <td> 2011</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 4368</td>
      <td> 2012</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 1564</td>
      <td> 2013</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 2190</td>
      <td> 2014</td>
    </tr>
    <tr>
      <th>4</th>
      <td>  161</td>
      <td> 2015</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Cameras">Cameras<a class="anchor-link" href="#Cameras">&#182;</a></h3>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[195]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">q</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span>
<span class="s">select qty,</span>
<span class="s"> datetime(min_date +  julianday(&#39;2000-01-01 00:00:00&#39;)) min_date,</span>
<span class="s"> datetime(max_date +  julianday(&#39;2000-01-01 00:00:00&#39;)) max_date,</span>
<span class="s"> cameraModel from (</span>
<span class="s">select count(*) qty, min(photoDate) min_date, max(photoDate) max_date, cameraModel</span>
<span class="s"> from</span>
<span class="s">sqphotoinfo</span>
<span class="s">where photoDate &gt;  julianday(&#39;1993-01-01&#39;) - julianday(&#39;2000-01-01 00:00:00&#39;)</span>
<span class="s">group by cameraModel</span>
<span class="s">)</span>
<span class="s">where qty &gt;= 10</span>
<span class="s">order by 1 desc</span>
<span class="s">&#39;&#39;&#39;</span>
<span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="n">q</span><span class="p">,</span> <span class="n">db1</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[195]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>qty</th>
      <th>min_date</th>
      <th>max_date</th>
      <th>cameraModel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0 </th>
      <td> 5568</td>
      <td> 2009-11-25 17:28:32</td>
      <td> 2013-11-04 11:05:02</td>
      <td>   Canon PowerShot SD1100 IS</td>
    </tr>
    <tr>
      <th>1 </th>
      <td>  872</td>
      <td> 2013-12-04 07:02:10</td>
      <td> 2015-04-18 15:50:41</td>
      <td>               FinePix S4850</td>
    </tr>
    <tr>
      <th>2 </th>
      <td>  641</td>
      <td> 2006-02-01 11:05:22</td>
      <td> 2015-05-23 09:47:31</td>
      <td>                        None</td>
    </tr>
    <tr>
      <th>3 </th>
      <td>  401</td>
      <td> 2012-09-21 11:06:43</td>
      <td> 2015-01-02 09:22:16</td>
      <td>                Galaxy Nexus</td>
    </tr>
    <tr>
      <th>4 </th>
      <td>  399</td>
      <td> 2014-08-13 15:55:36</td>
      <td> 2014-08-19 11:15:30</td>
      <td>                  NIKON D800</td>
    </tr>
    <tr>
      <th>5 </th>
      <td>  273</td>
      <td> 2014-05-16 16:59:18</td>
      <td> 2014-06-28 14:09:51</td>
      <td>                 NIKON D3200</td>
    </tr>
    <tr>
      <th>6 </th>
      <td>  137</td>
      <td> 2012-11-14 17:35:19</td>
      <td> 2013-11-29 13:29:43</td>
      <td>             FinePix S5Pro  </td>
    </tr>
    <tr>
      <th>7 </th>
      <td>   90</td>
      <td> 2012-10-19 17:55:45</td>
      <td> 2015-03-12 11:37:07</td>
      <td>                   iPhone 4S</td>
    </tr>
    <tr>
      <th>8 </th>
      <td>   78</td>
      <td> 2012-09-15 18:21:05</td>
      <td> 2012-10-21 18:17:14</td>
      <td> Canon PowerShot ELPH 100 HS</td>
    </tr>
    <tr>
      <th>9 </th>
      <td>   65</td>
      <td> 2011-04-18 12:19:47</td>
      <td> 2012-05-05 15:40:20</td>
      <td>                   NIKON D90</td>
    </tr>
    <tr>
      <th>10</th>
      <td>   28</td>
      <td> 2014-06-27 22:17:35</td>
      <td> 2014-06-28 01:07:04</td>
      <td>   Canon PowerShot SD1200 IS</td>
    </tr>
    <tr>
      <th>11</th>
      <td>   28</td>
      <td> 2014-10-02 13:22:41</td>
      <td> 2014-10-02 15:31:08</td>
      <td>                    SGH-T999</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Photos-and-Images">Photos and Images<a class="anchor-link" href="#Photos-and-Images">&#182;</a></h3><p>The model is nice and clean, separating photos, relating any number of possibly-edited images to each photo-taking event, and issuing a uuid to the photo-taking event.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[139]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">q</span> <span class="o">=</span> <span class="s">&#39;&#39;&#39;</span>

<span class="s">select photo.primaryKey, photo.uid, datetime(photo.photoDate + julianday(&#39;2000-01-01 00:00:00&#39;)) as photoDate,</span>
<span class="s">       photo.cameraModel, photo.archiveFilename,</span>
<span class="s">       fi.imageWidth, fi.imageHeight, fi.fileSize, fi.imageType, fi.version,</span>
<span class="s">       fl.relativePath, fl.aliasPath</span>
<span class="s">       -- TODO: decode fl.format</span>
<span class="s">from SqPhotoInfo photo</span>
<span class="s">join SqFileImage fi on fi.photoKey = photo.primaryKey</span>
<span class="s">join SqFileInfo fl on fi.sqFileInfo = fl.primaryKey</span>

<span class="s">where fileSize &gt; 0</span>
<span class="s">order by photo.photoDate desc</span>
<span class="s">&#39;&#39;&#39;</span>
<span class="n">pdb</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_sql</span><span class="p">(</span><span class="n">q</span><span class="p">,</span> <span class="n">db1</span><span class="p">)</span>
<span class="n">pdb</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[139]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>primaryKey</th>
      <th>uid</th>
      <th>photoDate</th>
      <th>cameraModel</th>
      <th>archiveFilename</th>
      <th>imageWidth</th>
      <th>imageHeight</th>
      <th>fileSize</th>
      <th>imageType</th>
      <th>version</th>
      <th>relativePath</th>
      <th>aliasPath</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 9272</td>
      <td> 4BC69B9E-3AEF-4FA6-BFCC-5476CC6CAC0D</td>
      <td> 2015-05-23 09:47:31</td>
      <td> None</td>
      <td>                     Dining_Room_Turned_Office.jpg</td>
      <td> 550</td>
      <td> 400</td>
      <td>  34651</td>
      <td> 6</td>
      <td> 100</td>
      <td> Originals/2015/May 23, 2015/Dining_Room_Turned...</td>
      <td> None</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 9272</td>
      <td> 4BC69B9E-3AEF-4FA6-BFCC-5476CC6CAC0D</td>
      <td> 2015-05-23 09:47:31</td>
      <td> None</td>
      <td>                     Dining_Room_Turned_Office.jpg</td>
      <td> 360</td>
      <td> 262</td>
      <td>  52460</td>
      <td> 5</td>
      <td> 100</td>
      <td> Data/2015/May 23, 2015/Dining_Room_Turned_Offi...</td>
      <td> None</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 9282</td>
      <td> 11F6E0C9-90F8-43E3-8427-EFD1F98D5ECD</td>
      <td> 2015-05-20 09:24:50</td>
      <td> None</td>
      <td> 11223919_10103150053978467_4385673914430987089...</td>
      <td> 960</td>
      <td> 639</td>
      <td> 101115</td>
      <td> 6</td>
      <td> 100</td>
      <td> Originals/2015/May 20, 2015/11223919_101031500...</td>
      <td> None</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 9282</td>
      <td> 11F6E0C9-90F8-43E3-8427-EFD1F98D5ECD</td>
      <td> 2015-05-20 09:24:50</td>
      <td> None</td>
      <td> 11223919_10103150053978467_4385673914430987089...</td>
      <td> 360</td>
      <td> 240</td>
      <td>  67356</td>
      <td> 5</td>
      <td> 100</td>
      <td> Data/2015/May 20, 2015/11223919_10103150053978...</td>
      <td> None</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 9289</td>
      <td> 88DC7357-96A2-4C29-88CD-6DF9E39E4CBB</td>
      <td> 2015-05-20 09:24:41</td>
      <td> None</td>
      <td> 11261973_10103150053743937_5354724846552149885...</td>
      <td> 960</td>
      <td> 639</td>
      <td>  97108</td>
      <td> 6</td>
      <td> 100</td>
      <td> Originals/2015/May 20, 2015/11261973_101031500...</td>
      <td> None</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Joining-sqlite-data-with-flickr-via-applescript-key-info">Joining sqlite data with flickr via applescript key info<a class="anchor-link" href="#Joining-sqlite-data-with-flickr-via-applescript-key-info">&#182;</a></h2><p>Ah... excellent... even though there are more image files than photos, we get an exact 1-1 match when we join with our photo keys (implicitly on <code>relativePath</code>).</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[109]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="nb">len</span><span class="p">(</span><span class="n">pdb</span><span class="p">),</span> <span class="nb">len</span><span class="p">(</span><span class="n">pk</span><span class="p">),</span> <span class="nb">len</span><span class="p">(</span><span class="n">pdb</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">pk</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[109]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>(19127, 8057, 8057)</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[150]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">pkdb</span> <span class="o">=</span> <span class="n">pk</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">pdb</span><span class="p">)</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s">&#39;id&#39;</span><span class="p">)</span>
<span class="n">pkdb</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[150]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>height</th>
      <th>imagePath</th>
      <th>originalPath</th>
      <th>width</th>
      <th>relativePath</th>
      <th>primaryKey</th>
      <th>uid</th>
      <th>photoDate</th>
      <th>cameraModel</th>
      <th>archiveFilename</th>
      <th>imageWidth</th>
      <th>imageHeight</th>
      <th>fileSize</th>
      <th>imageType</th>
      <th>version</th>
      <th>aliasPath</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4294967334</th>
      <td> 2002-09-25T15:14:23.000Z</td>
      <td>  600</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td>  800</td>
      <td> Originals/2002/Sep 25, 2002/Santa Cecelia gran...</td>
      <td>   38</td>
      <td> 7281F4D1-E140-4832-B759-60D5B9DF78B1</td>
      <td> 2002-09-25 10:14:23</td>
      <td>          PDR-3320</td>
      <td>                Santa Cecelia granite.jpg</td>
      <td>  800</td>
      <td>  600</td>
      <td>  63092</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>4294976544</th>
      <td> 2003-07-21T03:52:05.000Z</td>
      <td> 1385</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 1332</td>
      <td>          Originals/2003/Jul 20, 2003/brothers.jpg</td>
      <td> 9248</td>
      <td> 7EFC6CF1-F3A5-42DD-ADBC-52561476CC50</td>
      <td> 2003-07-20 22:52:05</td>
      <td> hp photosmart 720</td>
      <td>                             brothers.jpg</td>
      <td> 1332</td>
      <td> 1385</td>
      <td> 615319</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>4294976530</th>
      <td> 2003-08-08T20:09:51.000Z</td>
      <td> 1459</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Modifie...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 1647</td>
      <td>          Modified/2003/Aug 8, 2003/justin car.jpg</td>
      <td> 9234</td>
      <td> E3D5AD74-7FC1-4916-A9DA-6C2CB47B5D16</td>
      <td> 2003-08-08 15:09:51</td>
      <td> hp photosmart 720</td>
      <td>                           justin car.jpg</td>
      <td> 1647</td>
      <td> 1459</td>
      <td> 828662</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>4294976542</th>
      <td> 2003-08-08T20:09:51.000Z</td>
      <td> 1536</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 2048</td>
      <td>       Originals/2003/Aug 8, 2003_2/justin car.jpg</td>
      <td> 9246</td>
      <td> CCD2008C-4CB5-46BF-B99D-4BAE8999D8AD</td>
      <td> 2003-08-08 15:09:51</td>
      <td> hp photosmart 720</td>
      <td>                           justin car.jpg</td>
      <td> 2048</td>
      <td> 1536</td>
      <td> 738791</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>4294971867</th>
      <td> 2006-02-01T17:05:22.000Z</td>
      <td>  377</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td>  495</td>
      <td> Originals/2006/Feb 1, 2006/NY-Skyline-new-york...</td>
      <td> 4571</td>
      <td> 5D1426FC-5F86-457D-9EB7-6F761607C8FA</td>
      <td> 2006-02-01 11:05:22</td>
      <td>              None</td>
      <td> NY-Skyline-new-york-1138029_495_377.jpeg</td>
      <td>  495</td>
      <td>  377</td>
      <td> 159106</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Merging with the <code>upload_map</code> gives us a clear correspondence between iPhoto applescript ids and flickr ids.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[151]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">upkdb</span> <span class="o">=</span> <span class="n">upload_map</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">pkdb</span><span class="p">,</span> <span class="n">left_on</span><span class="o">=</span><span class="s">&#39;apple&#39;</span><span class="p">,</span> <span class="n">right_index</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>

<span class="nb">len</span><span class="p">(</span><span class="n">upkdb</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[151]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>8057</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[152]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">upkdb</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[152]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>apple</th>
      <th>flickr</th>
      <th>date</th>
      <th>height</th>
      <th>imagePath</th>
      <th>originalPath</th>
      <th>width</th>
      <th>relativePath</th>
      <th>primaryKey</th>
      <th>uid</th>
      <th>photoDate</th>
      <th>cameraModel</th>
      <th>archiveFilename</th>
      <th>imageWidth</th>
      <th>imageHeight</th>
      <th>fileSize</th>
      <th>imageType</th>
      <th>version</th>
      <th>aliasPath</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td> 4294967334</td>
      <td> 19226418710</td>
      <td> 2002-09-25T15:14:23.000Z</td>
      <td>  600</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td>  800</td>
      <td> Originals/2002/Sep 25, 2002/Santa Cecelia gran...</td>
      <td>   38</td>
      <td> 7281F4D1-E140-4832-B759-60D5B9DF78B1</td>
      <td> 2002-09-25 10:14:23</td>
      <td>          PDR-3320</td>
      <td>                Santa Cecelia granite.jpg</td>
      <td>  800</td>
      <td>  600</td>
      <td>  63092</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>1</th>
      <td> 4294976544</td>
      <td> 18793385783</td>
      <td> 2003-07-21T03:52:05.000Z</td>
      <td> 1385</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 1332</td>
      <td>          Originals/2003/Jul 20, 2003/brothers.jpg</td>
      <td> 9248</td>
      <td> 7EFC6CF1-F3A5-42DD-ADBC-52561476CC50</td>
      <td> 2003-07-20 22:52:05</td>
      <td> hp photosmart 720</td>
      <td>                             brothers.jpg</td>
      <td> 1332</td>
      <td> 1385</td>
      <td> 615319</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>2</th>
      <td> 4294976530</td>
      <td> 18793388523</td>
      <td> 2003-08-08T20:09:51.000Z</td>
      <td> 1459</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Modifie...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 1647</td>
      <td>          Modified/2003/Aug 8, 2003/justin car.jpg</td>
      <td> 9234</td>
      <td> E3D5AD74-7FC1-4916-A9DA-6C2CB47B5D16</td>
      <td> 2003-08-08 15:09:51</td>
      <td> hp photosmart 720</td>
      <td>                           justin car.jpg</td>
      <td> 1647</td>
      <td> 1459</td>
      <td> 828662</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>3</th>
      <td> 4294976542</td>
      <td> 18791506174</td>
      <td> 2003-08-08T20:09:51.000Z</td>
      <td> 1536</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> 2048</td>
      <td>       Originals/2003/Aug 8, 2003_2/justin car.jpg</td>
      <td> 9246</td>
      <td> CCD2008C-4CB5-46BF-B99D-4BAE8999D8AD</td>
      <td> 2003-08-08 15:09:51</td>
      <td> hp photosmart 720</td>
      <td>                           justin car.jpg</td>
      <td> 2048</td>
      <td> 1536</td>
      <td> 738791</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
    <tr>
      <th>4</th>
      <td> 4294971867</td>
      <td> 19414016905</td>
      <td> 2006-02-01T17:05:22.000Z</td>
      <td>  377</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td> /Volumes/maryc/Pictures/iPhoto Library/Origina...</td>
      <td>  495</td>
      <td> Originals/2006/Feb 1, 2006/NY-Skyline-new-york...</td>
      <td> 4571</td>
      <td> 5D1426FC-5F86-457D-9EB7-6F761607C8FA</td>
      <td> 2006-02-01 11:05:22</td>
      <td>              None</td>
      <td> NY-Skyline-new-york-1138029_495_377.jpeg</td>
      <td>  495</td>
      <td>  377</td>
      <td> 159106</td>
      <td> 6</td>
      <td> 100</td>
      <td> None</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Fixing-Dates">Fixing Dates<a class="anchor-link" href="#Fixing-Dates">&#182;</a></h2><p>Let's grab flickr photos with unkonwn date taken (with upload date, title, and original size).</p>
<p>Then merge with the date information from the sqlite3 db.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[178]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">tofix</span> <span class="o">=</span> <span class="n">photo</span><span class="p">[</span><span class="n">photo</span><span class="o">.</span><span class="n">datetakenunknown</span> <span class="o">==</span> <span class="s">&#39;1&#39;</span><span class="p">][[</span><span class="s">&#39;datetaken&#39;</span><span class="p">,</span> <span class="s">&#39;upload_date&#39;</span><span class="p">,</span> <span class="s">&#39;title&#39;</span><span class="p">,</span> <span class="s">&#39;width_o&#39;</span><span class="p">,</span> <span class="s">&#39;height_o&#39;</span><span class="p">]]</span>
<span class="n">fixed</span> <span class="o">=</span> <span class="n">tofix</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">upkdb</span><span class="p">,</span> <span class="n">left_index</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">right_on</span><span class="o">=</span><span class="s">&#39;flickr&#39;</span><span class="p">)[</span>
    <span class="p">[</span><span class="s">&#39;date&#39;</span><span class="p">,</span> <span class="s">&#39;photoDate&#39;</span><span class="p">,</span> <span class="s">&#39;upload_date&#39;</span><span class="p">,</span> <span class="s">&#39;title&#39;</span><span class="p">,</span> <span class="s">&#39;archiveFilename&#39;</span><span class="p">,</span>
     <span class="s">&#39;width_o&#39;</span><span class="p">,</span> <span class="s">&#39;imageWidth&#39;</span><span class="p">,</span> <span class="s">&#39;height_o&#39;</span><span class="p">,</span> <span class="s">&#39;imageHeight&#39;</span><span class="p">,</span>
    <span class="s">&#39;flickr&#39;</span><span class="p">,</span> <span class="s">&#39;uid&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">set_index</span><span class="p">(</span><span class="s">&#39;flickr&#39;</span><span class="p">)</span>
<span class="k">print</span> <span class="nb">len</span><span class="p">(</span><span class="n">tofix</span><span class="p">),</span> <span class="nb">len</span><span class="p">(</span><span class="n">fixed</span><span class="p">)</span>
<span class="n">fixed</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stdout output_text">
<pre>74 74
</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">Out[178]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>photoDate</th>
      <th>upload_date</th>
      <th>title</th>
      <th>archiveFilename</th>
      <th>width_o</th>
      <th>imageWidth</th>
      <th>height_o</th>
      <th>imageHeight</th>
      <th>uid</th>
    </tr>
    <tr>
      <th>flickr</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>19426161436</th>
      <td> 2014-10-20T18:47:27.000Z</td>
      <td> 2014-10-20 13:47:27</td>
      <td>2015-07-05 20:23:04</td>
      <td>  segway tour - 4</td>
      <td>  segway tour - 4.jpg</td>
      <td>  466</td>
      <td>  466</td>
      <td>  630</td>
      <td>  630</td>
      <td> 93061866-7680-43EA-9D58-8DE25E554B43</td>
    </tr>
    <tr>
      <th>19456508621</th>
      <td> 2014-10-20T18:48:03.000Z</td>
      <td> 2014-10-20 13:48:03</td>
      <td>2015-07-05 20:23:10</td>
      <td> segway tour - 28</td>
      <td> segway tour - 28.jpg</td>
      <td>  851</td>
      <td>  851</td>
      <td>  630</td>
      <td>  630</td>
      <td> BFCD692A-52C7-4059-8A9F-F6264133C155</td>
    </tr>
    <tr>
      <th>19266094319</th>
      <td> 2014-10-20T18:52:50.000Z</td>
      <td> 2014-10-20 13:52:50</td>
      <td>2015-07-05 20:23:12</td>
      <td>  segway tour - 2</td>
      <td>  segway tour - 2.jpg</td>
      <td>  466</td>
      <td>  291</td>
      <td>  630</td>
      <td>  438</td>
      <td> B854FE26-841E-4968-BDF2-975C18AB3B05</td>
    </tr>
    <tr>
      <th>19264673498</th>
      <td> 2014-10-20T18:48:22.000Z</td>
      <td> 2014-10-20 13:48:22</td>
      <td>2015-07-05 20:23:16</td>
      <td> segway tour - 33</td>
      <td> segway tour - 33.jpg</td>
      <td>  466</td>
      <td>  338</td>
      <td>  630</td>
      <td>  519</td>
      <td> 8976E385-2BE0-46AB-8E9E-2FA573574ED4</td>
    </tr>
    <tr>
      <th>19445946592</th>
      <td> 2014-10-31T13:45:47.000Z</td>
      <td> 2014-10-31 08:45:47</td>
      <td>2015-07-05 20:23:47</td>
      <td> Brennan baby tub</td>
      <td> Brennan baby tub.jpg</td>
      <td> 2351</td>
      <td> 2351</td>
      <td> 2945</td>
      <td> 2945</td>
      <td> BA448463-3932-40C2-811C-B30017C68087</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>For this, we need write access.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[169]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">myFlickrEdit</span><span class="p">(</span><span class="n">user_id</span><span class="o">=</span><span class="s">&#39;14874637@N00&#39;</span><span class="p">):</span>
    <span class="kn">import</span> <span class="nn">pathlib</span>
    <span class="kn">import</span> <span class="nn">flickrapi</span>
    <span class="n">api_secret</span> <span class="o">=</span> <span class="n">pathlib</span><span class="o">.</span><span class="n">Path</span><span class="p">(</span><span class="s">&#39;flickr_api_secret&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">open</span><span class="p">()</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">flickdata</span><span class="o">.</span><span class="n">Write</span><span class="o">.</span><span class="n">make</span><span class="p">(</span><span class="n">flickrapi</span><span class="p">,</span> <span class="n">api_secret</span><span class="p">,</span> <span class="n">user_id</span><span class="p">)</span>

<span class="n">edit</span> <span class="o">=</span> <span class="n">myFlickrEdit</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>INFO:flickdata:authenticating...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.auth.oauth.checkToken&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickrapi.core:REST Parser: using xml.etree.cElementTree
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's work with one photo at first, verifying with the flickr web UI as we go.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[179]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">Image</span><span class="p">(</span><span class="n">url</span><span class="o">=</span><span class="n">photo</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="mi">19426161436</span><span class="p">]</span><span class="o">.</span><span class="n">url_t</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[179]:</div>

<div class="output_html rendered_html output_subarea output_execute_result">
<img src="https://farm1.staticflickr.com/308/19426161436_28c40cd67d_t.jpg"/>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[180]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">fixed</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="mi">19426161436</span><span class="p">]</span><span class="o">.</span><span class="n">photoDate</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt output_prompt">Out[180]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>u&apos;2014-10-20 13:47:27&apos;</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[181]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="n">edit</span><span class="o">.</span><span class="n">setDates</span><span class="p">(</span><span class="mi">19426161436</span><span class="p">,</span> <span class="n">date_taken</span><span class="o">=</span><span class="n">fixed</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="mi">19426161436</span><span class="p">]</span><span class="o">.</span><span class="n">photoDate</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-20 13:47:27&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
</pre>
</div>
</div>

<div class="output_area"><div class="prompt output_prompt">Out[181]:</div>


<div class="output_text output_subarea output_execute_result">
<pre>{u&apos;stat&apos;: u&apos;ok&apos;}</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we can iterate over all the fixes.</p>
<p>Incremental updates came in handy here. At first, I forgot to rate-limit my requests and flickr noticed after a few hundred. I went back and fetched metadata for recent photos in my photostream again and finished off the rest.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[182]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="kn">import</span> <span class="nn">time</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[185]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython2"><pre><span class="k">def</span> <span class="nf">do_fixes</span><span class="p">():</span>
    <span class="k">for</span> <span class="n">pid</span><span class="p">,</span> <span class="n">photo</span> <span class="ow">in</span> <span class="n">fixed</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>
        <span class="n">edit</span><span class="o">.</span><span class="n">setDates</span><span class="p">(</span><span class="n">pid</span><span class="p">,</span> <span class="n">date_taken</span><span class="o">=</span><span class="n">photo</span><span class="o">.</span><span class="n">photoDate</span><span class="p">)</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.5</span><span class="p">)</span>
<span class="n">do_fixes</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area"><div class="prompt"></div>
<div class="output_subarea output_stream output_stderr output_text">
<pre>INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-20 13:47:27&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-20 13:48:03&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-20 13:52:50&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-20 13:48:22&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-31 08:45:47&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-31 09:07:10&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-31 08:59:05&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-10-31 09:07:30&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-01 07:06:54&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:27:35&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:28:06&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:27:35&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:28:40&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:28:16&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:29:05&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:30:01&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:36:10&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:31:59&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:35:29&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:35:15&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 18:39:51&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:26:15&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:26:30&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:26:42&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:27:04&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:28:15&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:28:56&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:28:36&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:29:09&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:30:34&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:30:45&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:30:56&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:31:13&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:32:18&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:32:18&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:32:41&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:32:30&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:32:52&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:33:23&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:35:17&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:34:47&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:34:56&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:35:08&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:36:40&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:35:38&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 19:36:51&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 20:04:18&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 20:07:33&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 20:07:44&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-11-08 20:08:11&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-12-27 14:51:54&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-12-27 14:52:04&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-12-27 14:52:16&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-12-27 14:52:34&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2014-12-27 14:52:48&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-01-09 14:22:41&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-03-03 17:19:17&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-09 19:53:29&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-09 19:47:33&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-09 19:49:17&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-09 19:55:26&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-11 09:03:06&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-09 20:09:42&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-11 09:11:11&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-04-18 21:51:53&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:23:33&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:23:42&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:24:28&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:23:52&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:24:08&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:24:17&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:24:41&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-23 09:47:31&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
INFO:flickdata:setDates: {&apos;date_taken&apos;: u&apos;2015-05-20 09:24:50&apos;}...
INFO:flickrapi.core:Calling {&apos;nojsoncallback&apos;: 1, &apos;method&apos;: &apos;flickr.photos.setDates&apos;, &apos;format&apos;: &apos;parsed-json&apos;}
INFO:requests.packages.urllib3.connectionpool:Starting new HTTPS connection (1): api.flickr.com
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Future-Work">Future Work<a class="anchor-link" href="#Future-Work">&#182;</a></h2><ul>
<li>make an album of all the photos uploaded in this process?</li>
<li>tag flickr photos with uids<ul>
<li>don't lose "untagged" state, though! capture untagged-ness in an album or something.</li>
</ul>
</li>
<li>sync events... using photosets?</li>
<li>sync faces</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Additional notes bookmarked under: <a href="https://www.diigo.com/user/dckc-madmode/mac%20photos">mac photos</a>, <a href="https://www.diigo.com/user/dckc-madmode/mac%20sysadmin">mac sysadmin</a></p>

</div>
</div>
</div>
