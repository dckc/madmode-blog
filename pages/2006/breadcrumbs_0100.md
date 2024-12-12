date: 2006-03-19
title: 'geocoding and hCards for airports from wikipedia'
published: True
tags: ['breadcrumbs', 'geo']

<p>Inspired by the <a href="http://austin.adactio.com/">SXSW hCard/google map mash-up</a>, I&#39;m geocoding some of my travel data.</p>  <p>In <a href="http://dev.w3.org/cvsweb/2001/palmagent/">palmagent</a>, I started on a module to get airport lat/long info from wikipedia; it grabs some other hCard info meanwhile:</p>  <pre>~/devcvs/2001/palmagent$ python aptdata.py LAX<br />getting list of airports contatining  LAX  in  http://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_L<br />looking for  LAX  in text<br />link path: /wiki/Los_Angeles_International_Airport<br />finding data in http://en.wikipedia.org/wiki/Los_Angeles_International_Airport<br />{&#39;url&#39;: &#39;http://en.wikipedia.org/wiki/Los_Angeles_International_Airport&#39;, &#39;org&#39;: &#39;Los Angeles International Airport&#39;, &#39;nickname&#39;: &#39;LAX&#39;, &#39;geo&#39;: {&#39;latitude&#39;: 33.942500000000003, &#39;longitude&#39;: -117.59194444444445}, &#39;tz&#39;: -8}<br /></pre>  <p>I don&#39;t have a kid template yet, but I hope you get the idea.</p>  <p>Along the way, I found a <a href="http://en.wikipedia.org/wiki/Wikipedia:WikiProject_Airports">wikipedia airport project</a> and this really cool <a href="http://www.nacgeo.com/nacsite/documents/nac.asp">NAC</a> coding system; basically, it&#39;s base 30 lat/long/altitue. Two 4-digit numerals get you down to a building, and with 5 digits, you get down to the square meter. Looks like a great <a href="http://esw.w3.org/topic/GeoOnion">GeoOnion</a> technique.</p>   <div>see also: <ul> <li><cite><a href="/breadcrumbs/node/99">using JSON and templates to produce microformat data</a></cite></li> <li><cite><a href="/breadcrumbs/node/91">Toward Semantic Web data from Wikipedia</a></cite></li> </ul> </div>  <div>tags: <a rel="tag" href="http://del.icio.us/connolly/geo">geo</a></div> 