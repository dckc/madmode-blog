<!DOCTYPE html>
<!-- saved from url=(0109)https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps -->
<html ng-app="codementor" ng-class="{&quot;phone-only&quot;: Viewport.phoneOnly, &quot;tablet-up&quot;: Viewport.tabletUp}" class="ng-scope tablet-up skrollr skrollr-desktop"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">@charset "UTF-8";[ng\:cloak],[ng-cloak],[data-ng-cloak],[x-ng-cloak],.ng-cloak,.x-ng-cloak,.ng-hide:not(.ng-hide-animate){display:none !important;}ng\:form{display:block;}.ng-animate-shim{visibility:hidden;}.ng-anchor{position:absolute;}</style>

<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/nr-1118.min.js"></script><script type="text/javascript" async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/f.txt"></script><script type="text/javascript" async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/analytics.js"></script><script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/bat.js" async=""></script><script async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/fbevents.js"></script><script async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/qevents.js"></script><script type="text/javascript" async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/analytics.js"></script><script type="text/javascript" async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/5230ba2b3f55731e15000057.js"></script><script async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/analytics.js"></script><script async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/gtm.js"></script><script type="text/javascript" async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/amplitude-4.5.2-min.gz.js"></script><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"af0bef5486","applicationID":"2355903","transactionName":"c1tbTUBYXlgHRBoLVFxEalVbREZdDFFGTEJYW0I=","queueTime":1,"applicationTime":115,"agent":""}</script>
<script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(3),u=e(4),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],t),e}finally{f.emit("fn-end",[c.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){if(!o)return!1;if(e!==o)return!1;if(!n)return!0;if(!i)return!1;for(var t=i.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var u=navigator.userAgent,f=u.match(a);f&&u.indexOf("Chrome")===-1&&u.indexOf("Chromium")===-1&&(o="Safari",i=f[1])}n.exports={agent:o,version:i,match:r}},{}],3:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],4:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],5:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=v(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||o(t)}function w(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:l,addEventListener:l,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(3),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!E++){var e=x.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+x.offset],null,"api");var t=l.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===l.readyState&&i()}function i(){f("mark",["domContent",a()+x.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-x.offset}var u=(new Date).getTime(),f=e("handle"),c=e(3),s=e("ee"),p=e(2),d=window,l=d.document,m="addEventListener",v="attachEvent",g=d.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:g,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var h=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1118.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),x=n.exports={offset:u,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),l[m]?(l[m]("DOMContentLoaded",i,!1),d[m]("load",r,!1)):(l[v]("onreadystatechange",o),d[v]("onload",r)),f("mark",["firstbyte",u],null,"api");var E=0,O=e(5)},{}]},{},["loader"]);</script>
<title>
Learning to make stuff with computers: from CPUs to Haskell Web Apps Quick Tips | Codementor
</title>
<link href="https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps" rel="canonical">
<meta content="https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps" property="og:url">
<link href="https://www.codementor.io/manifest.json" rel="manifest">
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<meta content="We have multi-core, gigahertz processors on our wrists. Games are developed like Hollywood blockbusters, with hundreds of ..." name="description">
<meta content="Codementor" name="author">
<meta content="Code Mentor, Coding Help, Pair Programming, Software Expert, Top Developer, " name="keywords">
<meta content="website" property="og:type">
<meta content="Learning to make stuff with computers: from CPUs to Haskell Web Apps Quick Tips | Codementor" property="og:title">
<meta content="We have multi-core, gigahertz processors on our wrists. Games are developed like Hollywood blockbusters, with hundreds of ..." property="og:description">
<meta content="https://cdn.codementor.io/assets/codementor-logo-square-56b62392c1c2ddb72e012424b2e0d5ca282859ae66c912788d66429e879d7fc3.png" property="og:image">
<meta content="website" name="og:type">
<meta content="summary" name="twitter:card">
<meta content="We have multi-core, gigahertz processors on our wrists. Games are developed like Hollywood blockbusters, with hundreds of ..." name="twitter:description">
<meta content="@codementorio" name="twitter:site">
<meta content="Learning to make stuff with computers: from CPUs to Haskell Web Apps Quick Tips | Codementor" name="twitter:title">
<meta content="https://cdn.codementor.io/assets/codementor-logo-square-56b62392c1c2ddb72e012424b2e0d5ca282859ae66c912788d66429e879d7fc3.png" name="twitter:image">
<meta content="Learning to make stuff with computers: from CPUs to Haskell Web Apps Quick Tips | Codementor" name="twitter:image:alt">
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="TQDk5iTH34RJ999F4U6Xy0wi48qKK3AxlSwugtU7W5Dwvd3ChA1M19JRyzPuKwCTdNj7gY8ocFaSJzE5dDVX9Q==">
<link href="https://assets.codementor.io/icons/favicon-16x16.png" rel="icon" sizes="16x16" type="image/png">
<link href="https://assets.codementor.io/icons/favicon-32x32.png" rel="icon" sizes="32x32" type="image/png">
<link href="https://assets.codementor.io/icons/favicon-96x96.png" rel="icon" sizes="96x96" type="image/png">
<link href="https://assets.codementor.io/icons/favicon-128x128.png" rel="icon" sizes="128x128" type="image/png">
<link href="https://assets.codementor.io/icons/favicon-196x196.png" rel="icon" sizes="196x196" type="image/png">
<link rel="stylesheet" media="screen" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/bootstrap.min-905eae7ba4149cf543f3366d08256839f6d80173f0500658f47735953a70865a.css">
<link rel="stylesheet" media="screen" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/layout_wide-3221c4b17e5e5445f45f77c940813891a78d6fd327ea509d565bdf964654dca7.css">

<style>
.alert.flash-message{width:100%;box-sizing:border-box;-moz-box-sizing:border-box;border-radius: 0;-webkit-border-radius: 0px;-moz-border-radius: 0px;margin-bottom:0px;}
</style>
<script>
//<![CDATA[
window.gon={};gon.api_host="https://api.codementor.io";gon.firebase_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI0OTc5NzcsInYiOjAsImlhdCI6MTU1MjQxMTU3NywiZCI6eyJjb2RlbWVudG9yX3VzZXJuYW1lIjoiY21UYWl3YW4yMDEzISIsInV1aWQiOiIiLCJ1aWQiOiIifX0.Zm5wY6sM10Mg0--xvrld-cmTT2WqccHE9SwZgl5OSKw";gon.firebase_path="https://codementor.firebaseio.com/";gon.stripe_publishable_key="pk_live_4xo7T4dk6S3FLB0AU5U3MluV";gon.perfect_audience_order_id="";gon.agoliaAPIKey="7c36eb43e38ceee5bfa9cbfd641b9d92";gon.agoliaAPPID="XIMRNVJLQ7";gon.agoliaCategoryURL="https://XIMRNVJLQ7.algolia.net/1/indexes/Category_production";gon.agoliaMentorURL="https://XIMRNVJLQ7.algolia.net/1/indexes/Mentor_production";gon.agoliaMentorIndex="Mentor_production";gon.mode="production";gon.data_init={"firebase":{"path":"https://codementor.firebaseio.com/","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI0OTc5NzcsInYiOjAsImlhdCI6MTU1MjQxMTU3NywiZCI6eyJjb2RlbWVudG9yX3VzZXJuYW1lIjoiY21UYWl3YW4yMDEzISIsInV1aWQiOiIiLCJ1aWQiOiIifX0.Zm5wY6sM10Mg0--xvrld-cmTT2WqccHE9SwZgl5OSKw"}};gon.one_signal_app_id="f52dab00-90d2-4657-9003-12006de62b66";gon.cdn_root="https://cdn.codementor.io/assets";gon.CKEDITOR_BASEPATH="https://cdn.codementor.io/assets/lib/ckeditor/";gon.minimize_chat_side_bar=true;gon.helpListingContent="&lt;p&gt;We have multi-core, gigahertz processors on our wrists. Games are developed like Hollywood blockbusters, with hundreds of creative and technical people working together for years. As a new developer, where do you even start?! I have a few gems for you:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;a href=&quot;http://www.codeworld.info/&quot;&gt;CodeWorld&lt;/a&gt;:&amp;nbsp;&lt;span style=&quot;color:rgb(95, 99, 102); font-family:lato,sans-serif&quot;&gt;create your own pictures, animations, and games on the Web&lt;/span&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;https://www.youtube.com/watch?v=yF5-6AcohQw&quot;&gt;How The Web Just Happened&lt;/a&gt;&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;http://www.cs.colby.edu/djskrien/CPUSim/&quot;&gt;CpuSim&lt;/a&gt;:&amp;nbsp;An Interactive CPU Simulator&lt;/li&gt;&lt;li&gt;&lt;a href=&quot;http://www.nand2tetris.org/&quot;&gt;From NAND to Tetris&lt;/a&gt;: Building a Modern Computer from First Principles&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;&lt;a href=&quot;http://www.codeworld.info/&quot;&gt;CodeWorld&lt;/a&gt;, by Chris Smith,&amp;nbsp;was designed to teach math to teenagers. &lt;span style=&quot;color:rgb(95, 99, 102); font-family:lato,sans-serif&quot;&gt;It lets b&lt;/span&gt;rand new developers, with just a few hours of instruction,&amp;nbsp;build haskell web apps right in your browser, without the hassle of text editors, compilers, etc.&lt;/p&gt;&lt;p&gt;Computer Science degree programs typically start students with Java or the like, but consider&lt;/p&gt;&lt;pre&gt;&lt;code class=&quot;language-java&quot;&gt;x = x + 1&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;&amp;nbsp;from the perspective of the typical high school algebra student. That&amp;#39;s nonsense!&lt;/p&gt;&lt;p&gt;Then consider&lt;/p&gt;&lt;pre&gt;&lt;code&gt;main      = animationOf(design)\r\ndesign(t) = rotate(slot, 60 * t) &amp;amp; middle &amp;amp; outside\r\nslot      = solidRectangle(4, 0.4)\r\nmiddle    = solidCircle(1.2)\r\noutside   = circle(2)&lt;/code&gt;&lt;/pre&gt;&lt;p&gt;versus the mish-mash of concepts and code typical graphics and animation frameworks&amp;nbsp;require. And while CodeWorld looks a bit like a toy, haskell is not. Haskell will take you a long way in the world of computing.&lt;/p&gt;&lt;p&gt;&lt;a href=&quot;https://www.youtube.com/watch?v=yF5-6AcohQw&quot;&gt;How The Web Just Happened&lt;/a&gt;&amp;nbsp;is an hour talk by&amp;nbsp;Tim Berners-Lee, inventor of the Web, explaining how he started by building magnets, and just as he mastered those, transistors became available to hobbyists. And just as he mastered transitors, integrated circuits came along. And so on, until he had a Next machine and the Internet at his disposal. My own career followed a similar path, just a few years behind his. I didn&amp;#39;t build my own display, but with a Radio Shack Color Computer, I learned the principles of Unix from OS/9, and I built my own printer interface and wrote my own disk driver. Tim and I met in 1991 and worked together building the Web for the next&amp;nbsp;20 years.&lt;/p&gt;&lt;p&gt;&lt;a href=&quot;http://www.cs.colby.edu/djskrien/CPUSim/&quot;&gt;CpuSim&lt;/a&gt;, &lt;span style=&quot;color:rgb(95, 99, 102); font-family:lato,sans-serif&quot;&gt;by Dale Skrien at&amp;nbsp;&lt;/span&gt;Colby College, lets you really see how CPUs work, with registers and memory and assembly language and machine language. While it&amp;#39;s great to know haskell and other high level programming languges, it&amp;#39;s still important to know what&amp;#39;s going on underneath. This one you have to download and install to run, but it took me just a few minutes, and as a Java app, it runs on lots of platforms.&lt;/p&gt;&lt;p&gt;&lt;a href=&quot;http://www.nand2tetris.org/&quot;&gt;From NAND to Tetris&lt;/a&gt;, b&lt;span style=&quot;color:rgb(95, 99, 102); font-family:lato,sans-serif&quot;&gt;y Noam Nisan and Shimon Schocken, covers the parts in between: operating systems, compilers, and all that. It&amp;#39;s a course of many weeks, and I haven&amp;#39;t done it, personally. But if you&amp;#39;re willing to spend the time, it lets you walk the path that Tim and I did, even though the giga-scale technology is all ready rolled out everywhere.&lt;/span&gt;&lt;/p&gt;";
//]]>
</script><style>@media print {#ghostery-purple-box {display:none !important}}</style>
<script>
  var CKEDITOR_BASEPATH = gon.CKEDITOR_BASEPATH;
</script>
<script crossorigin="anonymous" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/bundle.min.js"></script>
<script>
  Sentry.init({
    dsn: 'https://cc570a38e3514aa9a85bf5bcf072d9e8@sentry.io/1392970',
    environment: "production"
  })
</script>
<!-- / cm tracker -->
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/bundled.js"></script>
<script>
  var _t = window.__CmTracker__({
    mode: "production",
    amplitudeEnabled: true,
    gtmEnabled: true
  })
</script>
<!-- Google Analytics -->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
</script>
<script>
  ga('create', 'UA-38879567-3'), 'auto', {'allowLinker': true};
  ga('require', 'linker')
  ga('linker:autoLink', ['hire.codementor.io'] )
</script>
<script>
  ga('require', 'displayfeatures');
</script>
<script>
  (function() {
    window._pa = window._pa || {};
    _pa.orderId = gon.perfect_audience_order_id; // OPTIONAL: attach user email or order ID to conversions
    // _pa.revenue = "19.99"; // OPTIONAL: attach dynamic purchase values to conversions
    var pa = document.createElement('script'); pa.type = 'text/javascript'; pa.async = true;
    pa.src = ('https:' == document.location.protocol ? 'https:' : 'http:') + "//tag.perfectaudience.com/serve/5230ba2b3f55731e15000057.js";
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(pa, s);
  })();
</script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/598270338.js"></script>
<!-- ///////////// Start SteelHouse Tracking Pixel -->
<script type="text/javascript" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/spx"></script><script>
  (function(){"use strict";var e=null,b="4.0.0",
  n="11828",
  additional="",
  t,r,i;try{t=top.document.referer!==""?encodeURIComponent(top.document.referrer.substring(0,2048)):""}catch(o){t=document.referrer!==null?document.referrer.toString().substring(0,2048):""}try{r=window&&window.top&&document.location&&window.top.location===document.location?document.location:window&&window.top&&window.top.location&&""!==window.top.location?window.top.location:document.location}catch(u){r=document.location}try{i=parent.location.href!==""?encodeURIComponent(parent.location.href.toString().substring(0,2048)):""}catch(a){try{i=r!==null?encodeURIComponent(r.toString().substring(0,2048)):""}catch(f){i=""}}var l,c=document.createElement("script"),h=null,p=document.getElementsByTagName("script"),d=Number(p.length)-1,v=document.getElementsByTagName("script")[d];if(typeof l==="undefined"){l=Math.floor(Math.random()*1e17)}h="dx.steelhousemedia.com/spx?"+"dxver="+b+"&shaid="+n+"&tdr="+t+"&plh="+i+"&cb="+l+additional+"";c.type="text/javascript";c.src=("https:"===document.location.protocol?"https://":"http://")+h;v.parentNode.insertBefore(c,v)})()
</script>
<!-- ///////////// End of SteelHouse Tracking Pixel -->

<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/application-28061e5d7d7ce04fbc5d369683a20f091487aeae38f7e5ebf0848411c3d504aa.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/parsley-14a51879e0288da756b1536e5edbfb4241d02ed377d49457e948d327d1e068e1.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/parsley.extend-70e143baa7cc98140f2b0e5b16a67abcb5d6fd1971425784e16ebec249a08333.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/jquery.session-963aae79fa1e5c55f527edcf9ed0ee8c5dab73ec6ca8b7500187f23dbad068e1.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/bootstrap-datepicker-89b958c53e1cdc5d4195b1a7b9c5ed092fbfc5b67474d2bbfd8d1962003558e1.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/purl-cee77264b6bc0445d4ea0c1870879a0fe77590f4fe109cad2a2202ec7f9108a5.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/md5-be1141a482c805387f86a4ca004517177112abfd31150a172df037a5e6250f9b.js"></script>
<link rel="stylesheet" media="screen" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/show_new-59d388f42e2b748b8a94f85af90774e1b35347bbf9ce9fbaad6eee248d9aa41e.css">
<link rel="stylesheet" media="screen" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/show-7dc05d6bbb285977209593b4f242ad9df40def91b02c192167cd2e9067689e84.css">
<link rel="stylesheet" media="screen" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/css">
<link rel="stylesheet" media="screen" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/prism-4eb79518de6cff4ea7b96eee320c735c1e6c88be664d3a435b2bc0298a02122a.css">
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/skrollr.min-8d1dbfc0596df5a2ec517170c70caa449beda5238fcb5e1baea4b863343667b5.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/addthis_widget.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/ckeditor-674517844ad5a7ab30abcf781ff6f7f01fd0d6bddc5cced25c1223625aefcb02.js"></script><style>.cke{visibility:hidden;}</style>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/prism-cf96d3bf15bcca028ac82fd85b2f6ec5a9d0c09ceddf600ddf977bbc21530449.js"></script>
<script>
  (function() {
    var ckeditor;
  
    ckeditor = new CKEDITOR.editor;
  
    ckeditor.on('loaded', function() {
      return setTimeout(function() {
        var filtered, fragment, writer;
        writer = new CKEDITOR.htmlParser.basicWriter();
        fragment = CKEDITOR.htmlParser.fragment.fromHtml($('<div/>').html(gon.helpListingContent).text());
        ckeditor.filter.applyTo(fragment);
        fragment.writeHtml(writer);
        filtered = writer.getHtml();
        $('.help-listing-content').html(filtered);
        return Prism.highlightAll();
      });
    });
  
  }).call(this);
</script>
<link rel="stylesheet" media="screen" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/right_side_bar-0f354fa9d1816c5516152b387785e513e051c5f0c92561e7654f1c7c66fad844.css">

<script type="text/javascript" async="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/embed.js"></script><script type="text/javascript" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/config.js"></script><link rel="stylesheet" type="text/css" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/editor.css"><script type="text/javascript" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/en.js"></script><style type="text/css"></style><style type="text/css">.fp__btn{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;display:inline-block;height:34px;padding:4px 30px 5px 40px;position:relative;margin-bottom:0;vertical-align:middle;-ms-touch-action:manipulation;touch-action:manipulation;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;font-family:"Open Sans", sans-serif;font-size:12px;font-weight:600;line-height:1.42857143;color:#fff;text-align:center;white-space:nowrap;background:#ef4925;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAVCAYAAABLy77vAAAABGdBTUEAALGPC/xhBQAAAJRJREFUOBHNUcEWgCAIy14fbl9egK5MRarHQS7ocANmOCgWh1gdNERig1CgwPlLxkZuE80ndHlU+4Lda1zz0m01dSKtcz0h7qpQb7WR+HyrqRPxahzwwMqqkEVs6qnv+86NQAbcJlK/X+vMeMe7XcBOYaRzcbItUR7/8QgcykmElQrQPErnmxNxl2yyiwcgEvQUocIJaE6yERwqXDIAAAAASUVORK5CYII=");background-repeat:no-repeat;background-position:15px 6px;border:1px solid transparent;border-radius:17px}.fp__btn:hover{background-color:#d64533}.fp__btn::after{position:absolute;content:"";top:15px;right:14px;width:7px;height:4px;background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAICAYAAAA1BOUGAAAABGdBTUEAALGPC/xhBQAAAGlJREFUCB1j/P//vw4DA4MiEKOD+0xAkatA/AJNBsS/ysTIyPgfyDgHxO+hCkD0Oag4RAhoPDsQm4NoqCIGBiBnAhBjAxNAkkxAvBZNFsQHuQesmxPIOQZVAKI54UZDFYgABbcBsQhMAgDIVGYSqZsn6wAAAABJRU5ErkJggg==");}.fp__btn:hover::after{background-position:0 -4px;}.fp__btn:active,.fp__btn:focus{outline:none}@media only screen and (min--moz-device-pixel-ratio: 2), only screen and (-o-min-device-pixel-ratio: 2 / 1), only screen and (-webkit-min-device-pixel-ratio: 2), only screen and (min-device-pixel-ratio: 2){.fp__btn{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAqCAYAAADbCvnoAAAABGdBTUEAALGPC/xhBQAAAQFJREFUWAntWEESwjAIbBwfHl+upNoRNjKUJhk5kIvZQGG7bHOwPGltgdYtEJedShKyJnLHhEILz1Zi9HCOzFI7FUqFLAWseDgPdfeQ9QZ4b1j53nstnEJJyBqx20NeT1gEMB5uZG6Fzn5lV5UMp1ASQhMjdnvoqjewsYbDjcytEH5lsxULp1AS0sx8nJfVnjganf3NkVlKhVPIfQ9Zb6jF0atK3mNriXwpicPHvIeyr3sTDA53VgpgH8BvMu1ZCCz7ew/7MPwlE4CQJPNnQj2ZX4SYlEPbVpsvKFZ5TOwhcRoUTQiwwhVjArPEqVvRhMCneMXzDk9lwYphIwrZZOihF32oehMAa1qSAAAAAElFTkSuQmCC");background-size:18px 21px}.fp__btn::after{background:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAQCAYAAAAmlE46AAAABGdBTUEAALGPC/xhBQAAANpJREFUKBWVkU8KglAYxJ/u3HuBwmUX8BqepKN4ka4RguDOVYu2QVCrhIJ6/caekqLiGxi+PzPD58PAWrszxmygD84h7hpePFLy1mEQBJamgvcVYXkqZXTR0LwpJWw0z0Ba6bymDcrI4kkp4EvzCNoVztNKfVATwoOiyx/NDup1SVqPQVBbDDeK3txBb9JuHfhNW3HWjZhDX+SGRAgPHkl5f0+kieBxRVieaPD5LGJ4WghLiwehbkBI4HUirF3S+SYrhhQ2f2H16aR5vMSYwbdjNtYXZ0J7cc70BXnFMHIGznzEAAAAAElFTkSuQmCC");background-size:7px 8px;}}</style><style type="text/css" id="diigolet-chrome-css">body#skrollr-body .diigolet,body#skrollr-body .diigolet a,body#skrollr-body .diigolet em,body#skrollr-body .diigolet span,body#skrollr-body .diigolet div,body#skrollr-body .diigolet dl,body#skrollr-body .diigolet dt,body#skrollr-body .diigolet dd,body#skrollr-body .diigolet ul,body#skrollr-body .diigolet ol,body#skrollr-body .diigolet li,body#skrollr-body .diigolet h1,body#skrollr-body .diigolet h2,body#skrollr-body .diigolet h3,body#skrollr-body .diigolet h4,body#skrollr-body .diigolet h5,body#skrollr-body .diigolet h6,body#skrollr-body .diigolet pre,body#skrollr-body .diigolet form,body#skrollr-body .diigolet fieldset,body#skrollr-body .diigolet p,body#skrollr-body .diigolet blockquote,body#skrollr-body .diigolet th,body#skrollr-body .diigolet td,body#skrollr-body .diigolet input,body#skrollr-body .diigolet textarea,body#skrollr-body .diigolet select,body#skrollr-body .diigolet *{background:transparent none;padding:0;margin:0;flex-direction:row;border:#000 0 solid;text-align:left;text-decoration:none;text-transform:none;text-indent:0;line-height:normal;word-break:normal;word-wrap:normal;width:auto;height:auto;color:inherit;font:inherit;float:none;cursor:default;position:static;overflow:visible;max-width:none;box-shadow:none;opacity:1;border-radius:0;}
body#skrollr-body .diigolet{color:#000;font:normal normal normal 13px arial,helvetica,clean,sans-serif;}
body#skrollr-body .diigolet input[type=text],body#skrollr-body .diigolet textarea,body#skrollr-body .diigolet select,body#skrollr-body .diigolet fieldset{background-color:#FFF;border:1px #999 solid;padding:1px;font-size:12px;display:inline;border-radius:2px;-webkit-transition:border linear .2s,box-shadow linear .2s;}
body#skrollr-body .diigolet select{padding:0;height:20px;}
body#skrollr-body .diigolet input[type=text],body#skrollr-body .diigolet textarea{cursor:text;}
body#skrollr-body .diigolet input[type=text]{height:20px;}
body#skrollr-body .diigolet input[type="button"],body#skrollr-body .diigolet input[type="submit"],body#skrollr-body .diigolet input[type="reset"],body#skrollr-body .diigolet input[type="file"]{color:buttontext;cursor:default;padding:2px 5px;text-align:center;border:1px solid #ccc;background:#fff;border-radius:2px;background-image:-webkit-gradient(linear,0% 0,0% 100%,from(#f8f8f8),to(#d2d2d2));}
body#skrollr-body .diigolet input[type="button"]:active,body#skrollr-body .diigolet input[type="submit"]:active,body#skrollr-body .diigolet input[type="reset"]:active,body#skrollr-body .diigolet input[type="file"]:active{background:#ddd;}
body#skrollr-body .diigolet textarea{white-space:normal!important;resize:vertical!important;padding:2px!important;}
body#skrollr-body .diigolet input.diigo-check{border:none;vertical-align:middle;}
body#skrollr-body .diigolet input.diigo-button{font-size:12px!important;font-weight:bold;padding:4px 8px;cursor:pointer;border-radius:4px;}
body#skrollr-body .diigolet input.diigo-button#diigolet-dlgBm-btnSave{width:56px;color:white;height:25px;-webkit-border-radius:4px;background-color:rgba(237,237,237,0);-webkit-box-shadow:0 1px 1px rgba(0,0,0,.15);border:solid 1px #0388dc;background-image:-webkit-linear-gradient(top,#4eaffa,#0492f5);}
body#skrollr-body .diigolet input.diigo-button#diigolet-dlgBm-btnSave:hover{background-image:-webkit-linear-gradient(top,#349ef0,#0580d6);}
body#skrollr-body .diigolet input.diigo-button#diigolet-dlgBm-btnSave:active{background-image:-webkit-linear-gradient(bottom,#4eaffa,#0492f5);}
body#skrollr-body .diigolet input.diigo-downlist{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/arrow-down.png) 50% 50% no-repeat,-webkit-gradient(linear,0% 0,0% 100%,from(#f8f8f8),to(#d2d2d2));width:12px;margin-left:-16px;}
body#skrollr-body .diigolet input.diigo-downlist:active{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/arrow-down.png) 50% 50% no-repeat,#ddd;}
body#skrollr-body .diigolet div.diigo-buttonswitchlist{padding:4px 2px;border:1px solid #ccc;position:absolute;right:72px;background:#fff;z-index:100000;}
body#skrollr-body .diigolet div.diigo-buttonswitchlist ul li{padding:2px 6px;}
body#skrollr-body .diigolet div.diigo-buttonswitchlist ul li:hover{background:#43658F;color:#fff;cursor:pointer;}
body#skrollr-body #diigoletFNSubmit{width:50px;}
body#skrollr-body .diigolet table{border-collapse:collapse;border-spacing:0;width:auto;}
body#skrollr-body .diigolet label{cursor:pointer!important;display:inline;vertical-align:middle;}
body#skrollr-body .diigolet fieldset,body#skrollr-body .diigolet img{border:0;}
body#skrollr-body .diigolet address,body#skrollr-body .diigolet caption,body#skrollr-body .diigolet cite,body#skrollr-body .diigolet code,body#skrollr-body .diigolet dfn,body#skrollr-body .diigolet em,body#skrollr-body .diigolet strong,body#skrollr-body .diigolet th,body#skrollr-body .diigolet var{font-style:normal;font-weight:bold;}
body#skrollr-body .diigolet ol,body#skrollr-body .diigolet ul,body#skrollr-body .diigolet li{list-style:none;display:block;}
body#skrollr-body .diigolet caption,body#skrollr-body .diigolet th{text-align:left;}
body#skrollr-body .diigolet h1,body#skrollr-body .diigolet h2,body#skrollr-body .diigolet h3,body#skrollr-body .diigolet h4,body#skrollr-body .diigolet h5,body#skrollr-body .diigolet h6{font-weight:bold;}
body#skrollr-body .diigolet q:before,body#skrollr-body .diigolet q:after{content:'';}
body#skrollr-body .diigolet abbr,body#skrollr-body .diigolet acronym{border:0;}
body#skrollr-body .diigolet a:link,body#skrollr-body .diigolet a:visited,body#skrollr-body .diigolet a:hover,body#skrollr-body .diigolet a:active{text-decoration:none;color:#00F;cursor:pointer!important;}
body#skrollr-body .diigolet a:hover{text-decoration:underline;}
body#skrollr-body .diigolet a *{cursor:inherit;}
body#skrollr-body #diigolet-tray{position:fixed;top:0;left:10;width:16px;height:16px;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv3.gif") no-repeat left -4px;z-index:2147483646;}
body#skrollr-body .diigolet a.diigolet-Help:link,body#skrollr-body .diigolet a.diigolet-Help:visited{color:#06F;}
body#skrollr-body .diigolet a.diigolet-Help:hover,body#skrollr-body .diigo a.diigolet-Help:active{color:#00F;}
body#skrollr-body .diigolet label{margin-left:3px;}
body#skrollr-body .diigolet span.noComments{color:#AAA;font-size:10px;}
body#skrollr-body #diigolet-toolbar{border:none;width:100%;position:absolute;top:0;left:0;z-index:2147483647;color:#333;}
body#skrollr-body #diigolet-tb-content{padding:3px 5px;background:#EFEDDE url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigolet-toolbar-bg2.gif) repeat scroll 0;}
body#skrollr-body #diigolet-tb-bar span,body#skrollr-body #diigolet-tb-bar div,body#skrollr-body #diigolet-tb-bar a,body#skrollr-body #diigolet-tb-bar em{line-height:24px;}
body#skrollr-body #diigolet-tb-shadow{height:5px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigolet-toolbar-shadow.png) repeat-x left top;}
* html body#skrollr-body #diigolet-tb-shadow.ie6{filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=scale,src="chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigolet-toolbar-shadow.png");overflow:hidden;background:none;}
body#skrollr-body #diigolet-help{display:none;position:absolute;top:29px;right:10px;width:200px;border:1px #ccc solid;background-color:#FFC;padding:6px 16px 6px 6px;}
body#skrollr-body .diigolet a.diigoletButton{height:24px;float:left;padding-right:4px;cursor:pointer!important;}
body#skrollr-body .diigolet a.diigoletButton:hover{text-decoration:none;color:#000;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3_r.png") no-repeat right top;}
body#skrollr-body .diigolet a.diigoletButton:active{background-position:right bottom;}
body#skrollr-body .diigolet a.diigoletButton b{font-weight:normal;color:#000;line-height:24px;float:left;padding-left:4px;height:24px;}
body#skrollr-body #diigolet-button-highlight-dropdown{width:8px;height:16px;margin-right:4px;background:transparent url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/down_arrow.gif') no-repeat scroll left 2px;}
body#skrollr-body #diigolet-button-highlight-dropdown.mouseovered{border-left:1px solid #888;margin-right:0;text-decoration:none;width:11px;height:24px;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn4.png") no-repeat left top!important;}
body#skrollr-body #diigolet-button-highlight-dropdown.mouseoveredIe{border-left:1px solid #888;margin-right:1px;text-decoration:none;width:11px;height:24px;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn4.png") no-repeat left top!important;}
body#skrollr-body #diigolet-button-highlight-dropdown.checked{border-left:1px solid #888;margin-right:0;text-decoration:none;width:11px;height:24px;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn4_s.png") no-repeat left top!important;}
body#skrollr-body #diigolet-button-highlight.mouseovered{text-decoration:none;color:#000;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3_r.png") no-repeat right top!important;}
body#skrollr-body #diigolet-button-highlight.mouseoveredIe{text-decoration:none;color:#000;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3_r.png") no-repeat right top!important;}
body#skrollr-body #diigolet-button-highlight.mouseovered b.outer{background:transparent url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3.png') no-repeat left top;}
body#skrollr-body #diigolet-button-highlight.mouseoveredIe b.outer{background:transparent url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3.png') no-repeat left top;}
body#skrollr-body a#diigolet-button-highlight b.outer{padding-right:5px;}
body#skrollr-body a#diigolet-button-highlight{padding-right:0!important;}
body#skrollr-body a.diigoletButton:hover b.outer{background:transparent url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3.png') no-repeat left top;}
body#skrollr-body a.diigoletButton:active b.outer{background-position:left bottom;}
body#skrollr-body .diigolet a.diigoletButton b b{font-size:12px;padding-left:20px;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv3.gif") no-repeat left 50%;}
body#skrollr-body .diigolet a.diigoletButton:active b b{position:relative;top:1px;left:1px;}
body#skrollr-body .diigolet a.diigoletButton.diigoletDisabled{cursor:default;}
body#skrollr-body .diigolet a.diigoletButton.diigoletDisabled b b{color:#999;position:static;}
body#skrollr-body .diigolet a.diigoletButton.diigoletDisabled:hover{background:none transparent;}
body#skrollr-body .diigolet a.diigoletButton.diigoletDisabled:hover b.outer{background:none transparent;}
body#skrollr-body .diigolet a.diigoletButton.checked{background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3_r.png") no-repeat right top;background-position:right bottom;}
body#skrollr-body .diigolet a.diigoletButton.checked b.outer{background:transparent url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletBtn3.png') no-repeat left top;background-position:left bottom;}
body#skrollr-body .diigolet a.diigoletButton.checked b b{position:relative;top:1px;left:1px;}
body#skrollr-body #diigolet-tb-btnSidebar b b{background-position:left -24px;}
body#skrollr-body #diigolet-tb-btnSidebar.toClose b b{background-position:left -48px;}
body#skrollr-body #diigolet-tb-btnBookmark b b{background-position:left -144px;}
body#skrollr-body #diigolet-tb-btnBookmark.saved b b{background-position:left -120px;}
body#skrollr-body #diigolet-button-highlight b b{background-position:left -72px;}
body#skrollr-body #diigolet-button-highlight.dontShow b b{background-position:left -96px;}
body#skrollr-body #diigolet-button-highlight.yellow b b{background-position:left -355px;}
body#skrollr-body #diigolet-button-highlight.blue b b{background-position:left -375px;}
body#skrollr-body #diigolet-button-highlight.green b b{background-position:left -395px;}
body#skrollr-body #diigolet-button-highlight.pink b b{background-position:left -415px;}
body#skrollr-body .diigolet .colorItem{padding-left:20px;height:16px;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv3.gif") no-repeat left -440px;}
body#skrollr-body #diigolet-context-yellow b,body#skrollr-body #diigolet-colorMenu-yellow b{background-position:left -440px;}
body#skrollr-body #diigolet-context-blue b,body#skrollr-body #diigolet-colorMenu-blue b{background-position:left -460px;}
body#skrollr-body #diigolet-context-green b,body#skrollr-body #diigolet-colorMenu-green b{background-position:left -480px;}
body#skrollr-body #diigolet-context-pink b,body#skrollr-body #diigolet-colorMenu-pink b{background-position:left -500px;}
body#skrollr-body #diigolet-context-yellow.colorchecked b,body#skrollr-body #diigolet-colorMenu-yellow.colorchecked b{background-position:left -520px;}
body#skrollr-body #diigolet-context-blue.colorchecked b,body#skrollr-body #diigolet-colorMenu-blue.colorchecked b{background-position:left -540px;}
body#skrollr-body #diigolet-context-green.colorchecked b,body#skrollr-body #diigolet-colorMenu-green.colorchecked b{background-position:left -560px;}
body#skrollr-body #diigolet-context-pink.colorchecked b,body#skrollr-body #diigolet-colorMenu-pink.colorchecked b{background-position:left -580px;}
body#skrollr-body #diigolet-tb-btnFloatNote b b{background-position:left -167px;}
body#skrollr-body #diigolet-tb-btnTwitter b b{background:transparent url("http://twitter.com/favicon.ico") no-repeat left 50%;}
body#skrollr-body #diigolet-tb-btnComment b b{background-position:left -192px;}
body#skrollr-body #diigolet-tb-btnComment.commented b b{background-position:left -192px;}
body#skrollr-body #diigolet-tb-btnMore b b{background-position:left 0;}
body#skrollr-body #diigolet-tb-btnSignIn b b{background-position:left -264px;}
body#skrollr-body #diigolet-tb-btnHide{float:right;height:24px;width:16px;background:transparent url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv3.gif") no-repeat left -240px;}
body#skrollr-body div.diigoIcon{cursor:pointer!important;margin:0;padding:0;position:absolute;display:none;width:24px!important;z-index:2147483643;height:23px!important;background:transparent url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/edit-highlight.png') no-repeat left;-webkit-transition:-webkit-transform 150ms ease;vertical-align:text-bottom;}
body#skrollr-body span.diigoHighlightCommentLocator{vertical-align:text-bottom;line-height:0;}
body#skrollr-body div.diigoIcon span{color:#000;display:block;font-family:Helvetica,Arial,sans-serif;font-size:13px;font-weight:700;line-height:18px;text-align:center;text-shadow:0 1px 1px #FFF;text-decoration:none;text-indent:0;display:none;}
body#skrollr-body div.diigoHighlightcommented{display:inline-block!important;}
body#skrollr-body div.ImageIcon{background-color:transparent!important;}
body#skrollr-body div.diigoIcon:hover{background-color:transparent!important;background-repeat:no-repeat!important;-webkit-transform:translate(0px,-2px);}
body#skrollr-body div.diigoHighlightcommented.TextIcon{bottom:0;}
body#skrollr-body div.diigoHighlightcommented.public{background:#FFF url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/public-annotation.png') no-repeat left;}
body#skrollr-body div.diigoHighlightcommented.private.yellow{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 0 no-repeat;}
body#skrollr-body div.diigoHighlightcommented.private.blue{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 -46px no-repeat;}
body#skrollr-body div.diigoHighlightcommented.private.green{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 -92px no-repeat;}
body#skrollr-body div.diigoHighlightcommented.private.pink{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 -138px no-repeat;}
body#skrollr-body div.diigoHighlightcommented.group.yellow{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 -23px no-repeat;}
body#skrollr-body div.diigoHighlightcommented.group.blue{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 -69px no-repeat;}
body#skrollr-body div.diigoHighlightcommented.group.green{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 -115px no-repeat;}
body#skrollr-body div.diigoHighlightcommented.group.pink{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/annotation-icon.png') 0 -161px no-repeat;}
body#skrollr-body #diigolet-toolbar .dropdownMenu{display:none;border:1px solid #999;font:12px arial,helvetica,clean,sans-serif;background-color:Menu;padding:2px 0;z-index:2147483647;position:absolute;top:30px;width:140px;}
body#skrollr-body #diigolet-toolbar .dropdownMenu a,body#skrollr-body #diigolet-toolbar .dropdownMenu a:link,body#skrollr-body #diigolet-toolbar .dropdownMenu a:visited,body#skrollr-body #diigolet-toolbar .dropdownMenu a:hover,body#skrollr-body #diigolet-toolbar .dropdownMenu a:active{display:block;padding:2px 12px;font-weight:normal;text-decoration:none;color:#000;background:#fff;cursor:default;}
body#skrollr-body #diigolet-toolbar .dropdownMenu a:hover,body#skrollr-body #diigolet-toolbar .dropdownMenu a:active{color:#fff;background:#09f;}
body#skrollr-body #diigolet-notify{display:none;position:absolute;top:33px;left:0;border:1px #ccc solid;background-color:#FFC;padding:6px 16px 6px 6px;z-index:2147483647;}
body#skrollr-body #diigolet-notify.right{left:auto;right:0;text-align:right;}
body#skrollr-body .diigolet .tagList{margin:2px 0;float:left;}
body#skrollr-body .diigolet .diigo-su-tag .tagButton{display:inline-block;height:16px;padding:0 5px;line-height:16px;background-color:#f2f2f2;border-top:1px solid rgba(0,0,0,0);border-left:1px solid rgba(0,0,0,0);border-right:1px solid #C9D7F1;border-bottom:1px solid #C9D7F1;color:#858585;border-radius:1px;cursor:pointer;margin-right:3px;}
body#skrollr-body .diigolet .diigo-su-tag .tagButton:hover{border-color:#82b3f8;}
body#skrollr-body .diigolet .diigo-su-tag .tagButton.inused{color:#3f99a1;}
body#skrollr-body .diigolet .diigo-su-tag .tagButton.selected{border-color:#82b3f8;}
body#skrollr-body .diigolet .tagLoading a{display:none;margin-bottom:10px;}
body#skrollr-body .diigolet .tagList.tagLoading .loading{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/indicator.gif) no-repeat left top;height:16px;padding-left:22px;display:block;}
body#skrollr-body .diigolet .tagLoading .tagListHeader{display:none;}
body#skrollr-body .diigolet .tagListHeader{cursor:pointer;float:left;width:100px;line-height:23px;}
body#skrollr-body .diigolet .tagListHeader:hover{text-decoration:underline;}
body#skrollr-body .diigolet .tagList div{color:#666!important;font-size:12px!important;font-weight:bold!important;padding-right:5px!important;text-align:left!important;}
body#skrollr-body #diigolet-twitter{background-color:threedface;font-family:Arial,sans-serif;font-size:13px;color:windowtext;padding:5px 5px;margin:0;left:0;top:30px;z-index:2147483646;width:380px;position:static;border:1px #09F solid;border-left-width:0;}
body#skrollr-body #diigolet-twitter input{vertical-align:middle;}
body#skrollr-body .diigolet .twitterlogo{width:210px;height:49px;FILTER:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=scale,src="http://assets3.twitter.com/images/twitter.png");}
body#skrollr-body #diigolet-tagForward{background-color:white;width:460px;font-family:Arial,Helvetica,sans-serif;-webkit-border-radius:0;cursor:default;position:static;right:5px;top:75px;z-index:2147483646;border:1px solid rgba(0,0,0,.25);box-shadow:0 1px 5px rgba(0,0,0,.3);-webkit-user-select:none;background-clip:content-box;-webkit-animation:fadeinScale 200ms ease;}
body#skrollr-body #diigolet-tagForward.show{-webkit-animation:fadeinScale 200ms ease;}
body#skrollr-body #diigolet-tagForward.hide{-webkit-animation:fadeoutScale 200ms ease;}
body#skrollr-body #diigolet-tagForward *{-webkit-box-sizing:content-box!important;box-sizing:content-box!important;}
body#skrollr-body #diigolet-tagForward-topBar{height:38px;vertical-align:middle;background-color:#f5f5f5;border-bottom:1px solid #ddd;}
body#skrollr-body #diigolet-tagForward-topBar>span{line-height:38px;display:inline-block;margin-left:15px;color:#4B4B4B;font-size:16px;cursor:move;}
body#skrollr-body #diigolet-tagForward-topBar .focus-research-tip{margin-left:3px;font-size:12px;display:none;}
body#skrollr-body #diigolet-tagForward .tabContainer{text-align:center;margin:5px;}
body#skrollr-body #diigolet-tagForward .tab{margin-right:8px;margin-left:8px;padding:0 8px 2px 8px;font-weight:bold;}
body#skrollr-body #diigolet-tagForward .tabContainer a:link,body#skrollr-body #diigolet-tagForward .tabContainer a:visited{padding:4px;border:1px #fff solid;font-weight:bold;color:#06c;text-decoration:none;}
body#skrollr-body #diigolet-tagForward .tabContainer a.active:link,body#skrollr-body #diigolet-tagForward .tabContainer a.active:visited{border:none;background-color:#09f;color:#fff;padding:5px;}
body#skrollr-body #diigolet-tagForward .tabContainer a:hover,body#skrollr-body #diigolet-tagForward .tabContainer a:active{border:1px #09f solid;}
body#skrollr-body #diigolet-tagForward div.tabContent{display:none;}
body#skrollr-body #diigolet-tagForward div.tabContent.active{display:block;}
body#skrollr-body #diigolet-tagForward-caption{text-align:center;line-height:30px;font-size:14px;font-weight:bold;}
body#skrollr-body #diigolet-tagForward-remove{float:right;color:#f00;background:-webkit-linear-gradient(bottom,#ebebeb,#f5f5f5);margin-top:6px;margin-right:15px;cursor:pointer;height:24px;width:27px;border:1px solid #c4c4c4;border-radius:4px;box-shadow:0 1px 0 #fff;}
body#skrollr-body #diigolet-tagForward-remove:active{background:-webkit-linear-gradient(top,#ebebeb,#f5f5f5);}
body#skrollr-body #diigolet-tagForward-remove>span{float:left;background-image:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/remove.png');height:14px;width:11px;margin-top:5px;margin-left:8px;cursor:pointer;}
body#skrollr-body #diigolet-tagForward-remove:hover>span{background-position:0 -14px;}
body#skrollr-body #diigolet-Bookmark-Form{padding:20px 15px 0 15px;}
body#skrollr-body #diigolet-Bookmark-Form input[type="text"],body#skrollr-body #diigolet-Bookmark-Form textarea{outline:none;border:none;background-color:white;-webkit-transition:height .1s ease-in-out;}
body#skrollr-body #diigolet-Bookmark-Form input[type="text"]{line-height:20px;min-height:20px;}
body#skrollr-body #diigolet-tagForward .diigo-hr{width:426px;border-top:1px #ccc solid;margin:0 auto;height:1px;overflow:hidden;}
body#skrollr-body .diigolet .diigo-table{margin:10px 20px;}
body#skrollr-body .diigolet .diigo-table td{padding:2px 0;}
body#skrollr-body .diigolet .diigo-table th{color:#666;font-weight:bold;padding-right:5px;width:62px;text-align:left;font-size:12px!important;}
body#skrollr-body .diigolet .diigolet-input{width:350px;padding:1px;font-size:12px!important;height:16px!important;padding-left:3px!important;line-height:16px!important;outline:none!important;}
body#skrollr-body .diigolet .diigolet-input:focus{border:solid 1px #3996ed;-webkit-box-shadow:0 0 1px rgba(77,144,254,.55);}
body#skrollr-body #Diigo-Bookmark-Description,body#skrollr-body #Diigo-Forward-PS{border:1px solid #d7d7d7;background-color:white;-webkit-transition:border 400ms ease;min-height:56px;}
body#skrollr-body #Diigo-Bookmark-Description.focus{border:1px solid #aaa;}
body#skrollr-body #Diigo-Bookmark-Description-Input{width:413px;max-width:413px;font-family:Arial;height:45px;margin-left:6px;margin-top:3px;font-size:12px;padding:2px;}
body#skrollr-body #Diigo-Bookmark-Url{border-left:1px solid #DCDCDC;border-right:1px solid #DCDCDC;background-color:white;position:relative;-webkit-transform:rotateX(-90deg);height:0;position:relative;}
body#skrollr-body #Diigo-Bookmark-Url.fold{-webkit-animation:fold 400ms ease both;-webkit-animation-play-state:running;}
body#skrollr-body #Diigo-Bookmark-Url.unfold{-webkit-animation:unfold 400ms ease both;-webkit-animation-play-state:running;border-bottom:1px solid #DCDCDC;}
body#skrollr-body #Diigo-Bookmark-Url>div#url-arrow{height:6px;width:13px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/dp-arrow.png");position:absolute;left:11px;top:-6px;}
body#skrollr-body #Diigo-Bookmark-Url-Input{margin-top:3px;width:412px;margin-left:5px;}
body#skrollr-body #Diigo-Bookmark-Title{height:30px;border:1px solid #d7d7d7;background-color:white;-webkit-transition:border 400ms ease;position:relative;}
body#skrollr-body .diigolet .diigo-alert-tip{background-color:rgba(255,0,0,0.8);position:absolute;left:117px;top:-29px;padding:4px 6px;display:block;font-size:12px;font-weight:bold;pointer-events:none;font-family:arial,sans-serif;color:white;display:none;line-height:16px;}
body#skrollr-body .diigolet .diigo-alert-tip span{background:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/alert.png') -6px -4px no-repeat;text-indent:17px;display:inline-block;vertical-align:middle;}
body#skrollr-body .diigolet .diigo-alert-tip .diigo-alert-tip-arrow{position:absolute;border:5px solid;border-top-color:transparent;border-right-color:transparent;border-bottom-color:rgba(255,0,0,0.8);border-left-color:transparent;top:24px;height:0;width:0;line-height:0;-webkit-transform:rotate(180deg);left:91px;}
body#skrollr-body .diigolet #Diigo-Bookmark-Url .diigo-alert-tip{left:136px;}
body#skrollr-body .diigolet #Diigo-Bookmark-Url .diigo-alert-tip-arrow{left:71px;}
body#skrollr-body #Diigo-Bookmark-Title.focus{border:1px solid #aaa;}
body#skrollr-body #Diigo-Bookmark-Title-Input{margin:4px 0 0 0;width:392px;border:none;outline:none;font-size:14px;}
body#skrollr-body #Diigo-Bookmark-Title #link-icon{float:left;height:30px;width:30px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/URL.png") 4px 0 no-repeat;cursor:pointer;}
body#skrollr-body #Diigo-Bookmark-Title #link-icon:hover{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/URL.png") 4px -30px no-repeat;}
body#skrollr-body #Diigo-Bookmark-Title #link-icon.unfold{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/URL.png") 4px -30px no-repeat;}
body#skrollr-body #Diigo-Bookmark-Options .diigo-option{font-size:12px;height:inherit;width:120px;display:inline-block;padding:13px 0 15px 0;color:#555;}
body#skrollr-body .diigo-option:hover{background-position:0 -20px;}
body#skrollr-body .diigo-option:active{background-position:0 -40px;}
body#skrollr-body .diigo-option.active{background-position:0 -40px;}
body#skrollr-body .diigo-option .op-checkbox,body#skrollr-body #Diigo-Bookmark-checkShareExisting .op-checkbox{height:13px;width:15px;display:inline-block;vertical-align:middle;position:relative;cursor:pointer;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/checkbox.png");}
body#skrollr-body .diigo-option .op-label{margin-left:7px;text-indent:20px;display:inline-block;vertical-align:middle;cursor:pointer;}
body#skrollr-body #Diigo-Bookmark-checkShareExisting{display:none;}
body#skrollr-body #Diigo-Bookmark-checkShareExisting .op-label{margin-left:7px;text-indent:-6px;display:inline-block;vertical-align:middle;cursor:pointer;}
body#skrollr-body #Diigo-Bookmark-Options .op-checkbox-container{display:inline;cursor:pointer;}
body#skrollr-body #Diigo-Bookmark-uploadCache{margin-left:20px;}
body#skrollr-body .diigolet .op-checkbox-container:hover>.op-checkbox{background-position:0 -13px;}
body#skrollr-body .diigolet .op-checkbox-container.checked .op-checkbox{background-position:0 -26px;}
body#skrollr-body #Diigo-Bookmark-Privacy .op-label{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/private.png");background-repeat:no-repeat;}
body#skrollr-body #Diigo-Bookmark-Unread .op-label{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/op-readlater.png");background-repeat:no-repeat;}
body#skrollr-body #Diigo-Bookmark-uploadCache .op-label{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/cache.png");background-repeat:no-repeat;}
body#skrollr-body #Diigo-Bookmark-Url.invalid{border:1px solid #f00;margin-top:-1px;}
body#skrollr-body #Diigo-Bookmark-Url.invalid div{background-position:0 -6px;}
body#skrollr-body #Diigo-Bookmark-Title.invalid{border:1px solid #f00;}
body#skrollr-body #Diigo-Bookmark-Tag-Wrapper{min-height:24px;border:1px solid #d7d7d7;background-color:white;margin-top:15px;position:relative;-webkit-transition:border 400ms ease;height:30px;}
body#skrollr-body #Diigo-Bookmark-Tag-Wrapper.focus{border:1px solid #aaa;}
body#skrollr-body #Diigo-Bookmark-Tag-Input{margin-top:4px;margin-left:2px;width:389px;}
body#skrollr-body #Diigo-Bookmark-Tag{height:30px;}
body#skrollr-body .diigolet #Diigo-Bookmark-Tag{box-shadow:none;}
body#skrollr-body #Diigo-Bookmark-Tag-Wrapper.active{border:solid 1px #3996ed;-webkit-box-shadow:0 0 1px rgba(77,144,254,.55);}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud{border:1px solid #d7d7d7;border-bottom-right-radius:3px;border-bottom-left-radius:3px;display:none;background-color:white;font-size:12px;margin-top:-1px;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud>div:first-child{height:25px;width:100%;line-height:25px;font-weight:bold;border-bottom:1px solid #ccc;text-indent:2px;clear:both;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud>div:first-child a{float:right;margin-right:3px;text-decoration:none;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud>div:first-child a:hover{text-decoration:underline;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud-Container{max-height:180px;overflow:auto;width:421px;padding:3px 5px 5px 0;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud-Container::-webkit-scrollbar{width:6px;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud-Container::-webkit-scrollbar-track-piece{background-color:transparent;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud-Container::-webkit-scrollbar-thumb:vertical{height:20px;background-color:#CCC;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud-Container::-webkit-scrollbar-thumb:hover{background-color:#aaa;}
body#skrollr-body #Diigo-Bookmark-Tag-Wrapper.opened+#Diigo-Bookmark-Tag-Cloud{visibility:visible;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud ul li{display:inline-block;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud .Diigo-Bookmark-Tag-item{margin-left:3px;text-decoration:none;color:#04c;line-height:normal;display:inline-block;line-height:140%;cursor:pointer;padding:0 2px;}
body#skrollr-body #Diigo-Bookmark-checkShare{display:none;}
body#skrollr-body #Diigo-Bookmark-checkShareExisting{margin-right:3px;}
body#skrollr-body #Diigo-Bookmark-checkShare input[type=checkbox]{width:14px;height:14px;margin:0;cursor:pointer;vertical-align:middle;background:#fff;border:1px solid #dcdcdc;-webkit-border-radius:1px;-moz-border-radius:1px;border-radius:1px;-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box;position:relative!important;}
body#skrollr-body #Diigo-Bookmark-checkShare input[type=checkbox]:hover{border-color:#c6c6c6;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,0.1);-moz-box-shadow:inset 0 1px 1px rgba(0,0,0,0.1);box-shadow:inset 0 1px 1px rgba(0,0,0,0.1);}
body#skrollr-body #Diigo-Bookmark-checkShare input[type=checkbox]:active{border-color:#c6c6c6;background:#ebebeb;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud .Diigo-Bookmark-Tag-item.selected{background-color:#09f;color:white;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud>div:first-child{height:20px;width:100%;line-height:20px;font-weight:bold;border-bottom:1px solid #ccc;text-indent:2px;}
body#skrollr-body #Diigo-Bookmark-Tag-Cloud .Diigo-Bookmark-Tag-item:hover{text-decoration:underline;}
body#skrollr-body #Diigo-Bookmark-Tag-Eidt{float:right;margin-right:3px;}
body#skrollr-body #Diigo-Bookmark-Tag-suggestion{margin-top:7px;}
body#skrollr-body #diigolet-bm-tagListContainer-recommend{margin-top:3px;display:none;}
body#skrollr-body #Diigo-Bookmark-Tag-suggestion .diigo-su-tag{line-height:26px;font-size:12px;min-height:26px;margin-top:5px;}
body#skrollr-body #Diigo-Bookmark-Tag-suggestion .diigo-su-tag a{display:inline-block;text-decoration:none;color:#555;width:93px;}
body#skrollr-body #Diigo-Bookmark-Tag-suggestion .loading{display:inline-block;height:10px;width:120px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/loading.gif");}
body#skrollr-body #Diigo-Bookmark-Tag-suggestion .diigo-su-tag a:hover{text-decoration:underline;}
body#skrollr-body #Diigo-Bookmark-Tag-dropdown{height:30px;width:28px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/dropdown.png");float:left;cursor:pointer;}
body#skrollr-body #Diigo-Bookmark-Tag-dropdown:hover{background-position:0 -30px;}
body#skrollr-body .diigo-table .diigo-invalid-input{display:none;height:16px;width:16px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/icons.png");background-position:-16px -80px;margin-left:4px;}
body#skrollr-body #diigo-list-group{margin-top:17px;width:430px;height:24px;}
body#skrollr-body #diigolet-Bookmark-Form #Diigo-outliner #diigo-list-addInput{width:309px;height:26px;border:1px solid #d7d7d7;-webkit-transition:border 400ms ease;padding:0 3px;}
body#skrollr-body #Diigo-outliner{height:30px;margin-bottom:15px;}
body#skrollr-body #Diigo-outliner>div{float:left;height:20px;font-size:12px;color:#04c;font-weight:bold;line-height:20px;}
body#skrollr-body #diigo-list-group>div{float:left;height:20px;font-size:12px;color:#04c;width:200px;font-weight:bold;line-height:20px;}
body#skrollr-body #Diigo-outliner #diigo-list-add-tip{border-radius:4px;padding:5px 14px 5px 14px;font-size:12px;text-shadow:0 1px 0 rgba(255,255,255,0.5);background-color:#f2dede;border:1px solid #eed3d7;color:#b94a48;font-weight:normal;width:399px;display:none;}
body#skrollr-body #Diigo-outliner #diigo-list-add-tip a{float:right;margin:0 5px;color:b94a48;text-decoration:none;}
body#skrollr-body #Diigo-outliner #diigo-list-add-tip a:hover{text-decoration:underline;}
body#skrollr-body #Diigo-outliner #diigo-list-add{position:relative;display:none;}
body#skrollr-body #diigo-list-add .diigo-alert-tip{left:7px;top:-29px;}
body#skrollr-body #Diigo-outliner .diigo-alert-tip .diigo-alert-tip-arrow{left:43px;}
body#skrollr-body #diigo-list-group #diigo-list-addInput{width:102px;height:26px;border:1px solid #d7d7d7;-webkit-transition:border 400ms ease;padding:0 3px;font-weight:normal;color:#000;border-radius:0;}
body#skrollr-body #diigo-list-group #diigo-list-addInput:focus{border:1px solid #aaa;}
body#skrollr-body #diigo-list-add>*{float:left;}
body#skrollr-body #diigo-list-addBtn{height:26px;min-width:38px;background-image:-webkit-linear-gradient(top,#53aaf0,#118cef);border:1px solid #066ec1;color:#fff;border-radius:2px;line-height:26px;font-weight:normal;margin-left:6px;cursor:pointer;-webkit-transition:.3s cubic-bezier(0.175,0.885,0.32,1.275) all;text-align:center;}
body#skrollr-body #diigo-list-addBtn:not(.processing):hover{background-image:-webkit-linear-gradient(top,#45a2ee,#037bdb);}
body#skrollr-body #diigo-list-addBtn:not(.processing):active{background-image:-webkit-linear-gradient(bottom,#53aaf0,#118cef);}
body#skrollr-body #diigo-list-addBtn .label{margin:8px;cursor:pointer;-webkit-transition:.3s cubic-bezier(0.175,0.885,0.320,1.275) all;}
body#skrollr-body #diigo-list-addBtn .spinner{left:8px;margin-left:-16px;opacity:0;height:16px;width:16px;-webkit-transition:.3s cubic-bezier(0.175,0.885,0.320,1.275) all;display:inline-block;position:relative;top:3px;visibility:hidden;}
body#skrollr-body #diigo-list-addBtn.processing+a{display:none;}
body#skrollr-body #diigo-list-addBtn.processing .spinner{opacity:1;margin-left:12px;left:-7px;visibility:visible;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/addlist-processing.gif");}
body#skrollr-body #diigo-list-addCancel{color:#999;cursor:pointer;font-weight:normal;line-height:26px;margin-left:5px;font-size:12px;margin-top:2px;}
body#skrollr-body #diigo-list-addCancel:hover{text-decoration:underline;}
body#skrollr-body #diigo-list-group>div>select:hover{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/select-arrow-hover.png"),-webkit-linear-gradient(top,#fbfbfb,#f3f3f3);}
body#skrollr-body #diigo-list-group>div>select.processing{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/loading5.gif"),-webkit-linear-gradient(top,#f5f5f5,#fff);}
body#skrollr-body #diigo-list-group>div>select:active{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/select-arrow-hover.png"),-webkit-linear-gradient(top,#f5f5f5,#fff);}
body#skrollr-body #diigolet-bm-tagListContainer-group{display:none;}
body#skrollr-body #diigo-list-group>div>select,body#skrollr-body #Diigo-outliner>div>select{height:28px;width:430px;display:block;-webkit-appearance:none!important;border:1px solid #d7d7d7;background-position:right;background-repeat:no-repeat;color:#333;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/popup-image/select-arrow.png"),-webkit-linear-gradient(top,#fff,#f5f5f5);outline:none;cursor:pointer;font-size:12px;padding-right:22px;border-radius:0;font-weight:normal;box-sizing:border-box!important;}
body#skrollr-body #Diigo-Bookmark-bottom{height:49px;padding-top:24px;}
body#skrollr-body #Diigo-Bookmark-bottom>div:first-child{float:left;margin-top:3px;margin-left:15px;}
body#skrollr-body #diigolet-dlgBm-btnSave{display:inline-block;height:28px;width:82px;line-height:28px;background-image:-webkit-linear-gradient(top,#53aaf0,#118cef);float:right;cursor:pointer;margin-right:15px;text-align:center;color:white;border-radius:2px;border:1px solid #066ec1;font-size:14px;}
body#skrollr-body #diigolet-dlgBm-btnSave:hover{background-image:-webkit-linear-gradient(top,#45a2ee,#037bdb);}
body#skrollr-body #diigolet-dlgBm-btnSave:active{background-image:-webkit-linear-gradient(bottom,#53aaf0,#118cef);}
body#skrollr-body #diigolet-dlgBm-btnCancel{display:inline-block;float:right;font-size:14px;color:#999;height:12px;cursor:pointer;margin-top:8px;margin-right:19px;}
body#skrollr-body #diigolet-dlgBm-btnCancel:hover{text-decoration:underline;}
body#skrollr-body .diigolet .diigolet-submit{width:140px;height:25px;text-align:center;}
body#skrollr-body #diigolet-txtPermalink{background-color:#eee;padding:3px;font-size:13px;}
body#skrollr-body #diigolet-cross-promotion{font-family:arial,helvetica,sans-serif;font-size:12px;padding:10px;}
body#skrollr-body #diigolet-cross-promotion a{background:whiteSmoke;border:1px solid #CCC;color:#06C;display:block;padding:3px 10px;text-align:center;text-decoration:none;-webkit-box-shadow:rgba(255,255,255,0.6) 0 1px 0;-webkit-border-radius:10px;-webkit-transition:all .25s linear;}
body#skrollr-body #diigolet-cross-promotion a:hover{background:white;text-decoration:none;color:#04c;}
body#skrollr-body .diigoletContexMenu{font:12px arial,helvetica,clean,sans-serif;z-index:2147483645;}
body#skrollr-body #diigolet-csm #diigolet-csm-research-mode{width:18px;height:18px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/focus-research-csm.png");position:absolute;top:-8px;left:-9px;z-index:1;display:none;}
body#skrollr-body #diigolet-csm.diigo-researchMode #diigolet-csm-research-mode{display:block;}
body#skrollr-body #diigolet-csm .csm-action{display:block;height:22px!important;width:27px!important;border:1px solid rgba(0,0,0,.15);border-radius:1px 0 0 1px;opacity:.9;z-index:100000;float:left;margin:0!important;}
body#skrollr-body #diigolet-csm #diigolet-csm-highlight{background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/highlight-csm.png),-webkit-linear-gradient(#fff,#f5f5f5);}
body#skrollr-body #diigolet-csm #diigolet-csm-highlight:active{background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/highlight-csm.png),-webkit-linear-gradient(#f2f2f2,#fff);}
body#skrollr-body #diigolet-csm #diigolet-csm-highlightAndComment{border-width:1px 1px 1px 0;border-style:solid;border-color:rgba(0,0,0,.15);border-radius:1px 0 0 1px;background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/stickynote-csm.png),-webkit-linear-gradient(#fff,#f5f5f5);}
body#skrollr-body #diigolet-csm #diigolet-csm-highlightAndComment:active{background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/stickynote-csm.png),-webkit-linear-gradient(#f2f2f2,#fff);}
body#skrollr-body #diigolet-csm #diigolet-csm-search{border-width:1px 1px 1px 0;border-style:solid;border-color:rgba(0,0,0,.15);border-radius:1px 0 0 1px;background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/search-csm.png),-webkit-linear-gradient(#fff,#f5f5f5);}
body#skrollr-body #diigolet-csm #diigolet-csm-search:active{background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/search-csm.png),-webkit-linear-gradient(#f2f2f2,#fff);}
body#skrollr-body #diigolet-csm.yellow #diigolet-csm-highlight{background-position:0 0;}
body#skrollr-body #diigolet-csm.blue #diigolet-csm-highlight{background-position:0 -22px;}
body#skrollr-body #diigolet-csm.green #diigolet-csm-highlight{background-position:0 -44px;}
body#skrollr-body #diigolet-csm.pink #diigolet-csm-highlight{background-position:0 -66px;}
body#skrollr-body #diigolet-csm.yellow #diigolet-csm-highlightAndComment{background-position:0 0;}
body#skrollr-body #diigolet-csm.blue #diigolet-csm-highlightAndComment{background-position:0 -22px;}
body#skrollr-body #diigolet-csm.green #diigolet-csm-highlightAndComment{background-position:0 -44px;}
body#skrollr-body #diigolet-csm.pink #diigolet-csm-highlightAndComment{background-position:0 -66px;}
body#skrollr-body #diigolet-csm .csm-action:not(#diigolet-csm-search).editing{opacity:1!important;}
body#skrollr-body #diigolet-csm a:visited,body#skrollr-body #diigolet-csm a:link{padding:0!important;}
body#skrollr-body #diigolet-csm{z-index:100000;height:22px!important;flex-direction:row;}
body#skrollr-body #diigolet-csm>div{float:left;position:relative;}
body#skrollr-body #diigolet-csm a:hover{opacity:1!important;}
body#skrollr-body #diigolet-csm #diigolet-csm-dropdown:hover{background-position:0 -44px;}
body#skrollr-body #diigolet-csm #diigolet-csm-highlight:hover+a#diigolet-csm-dropdown{background-position:0 -22px;}
body#skrollr-body #diigolet-csm #diigolet-csm-dropdown:active{background-position:0 -66px;}
body#skrollr-body #diigolet-csm .diigolet-csm-color{position:absolute;top:23px;left:1px;background-color:white;-webkit-box-shadow:0 1px 2px rgba(0,0,0,.35);line-height:13px;overflow:hidden;height:0;visibility:visible!important;z-index:-1;display:block!important;}
body#skrollr-body #diigolet-csm-highlightAndComment-wrapper .diigolet-csm-color{left:0;}
body#skrollr-body #diigolet-csm .diigolet-csm-color.hidden{height:0;}
body#skrollr-body #diigolet-csm .diigolet-csm-color.small{height:0;width:27px;display:block;}
body#skrollr-body #diigolet-csm .diigolet-csm-coloritem{float:left;display:block;cursor:pointer;padding:0;margin:0;}
body#skrollr-body .diigolet-csm-color.small .diigolet-csm-coloritem{height:7px;width:10px;}
body#skrollr-body #diigolet-csm .diigolet-csm-coloritem.yellow{background-color:#fc6;border:1px solid #fc6;margin-right:1px;margin-bottom:1px;margin-left:1px;margin-top:1px;}
body#skrollr-body #diigolet-csm .diigolet-csm-coloritem.blue{background-color:#7ccce5;border:1px solid #7ccce5;margin-bottom:1px;margin-top:1px;}
body#skrollr-body #diigolet-csm .diigolet-csm-coloritem.green{background-color:#b4db66;border:1px solid #b4db66;margin-right:1px;margin-left:1px;margin-bottom:1px;}
body#skrollr-body #diigolet-csm .diigolet-csm-coloritem.pink{background-color:#f98baf;border:1px solid #f98baf;margin-right:0!important;margin-bottom:1px;}
body#skrollr-body #diigolet-csm .diigolet-csm-color .diigolet-csm-coloritem:hover{border-color:#36c;}
body#skrollr-body #diigolet-annMenu{height:26px;border-top:2px solid #43B4EA;border-radius:2px;background-color:#fff;padding:1px;position:absolute;box-shadow:-1px 0 0 rgba(0,0,0,0.1),1px 0 0 rgba(0,0,0,0.1),0px 1px 1px rgba(0,0,0,0.2);-webkit-user-select:none;-webkit-animation:fadeIn 130ms ease-in;box-sizing:content-box!important;}
body#skrollr-body #diigolet-annMenu .diigolet-annMenu-item{height:20px;width:20px;float:left;padding:1px;position:relative;cursor:pointer;-webkit-transition:background-color 200ms ease;border-radius:3px;padding:3px;box-sizing:content-box!important;}
body#skrollr-body #diigolet-annMenu .diigolet-annMenu-item *{box-sizing:content-box!important;}
body#skrollr-body #diigolet-annMenu .diigolet-annMenu-item>b{cursor:pointer;}
body#skrollr-body #diigolet-annMenu .diigolet-annMenu-item:hover{background-color:#d8f2ff;}
body#skrollr-body #diigolet-annMenu #diigolet-annMenu-currentColor{height:12px;width:12px;border:1px solid #289FE4;margin:3px 0 0 2px;}
body#skrollr-body #diigolet-annMenu #diigolet-annMenu-currentColor>b{height:10px;width:10px;border:1px solid #fff;display:block;background-color:#fc6;cursor:pointer;}
body#skrollr-body #diigolet-annMenu #diigolet-annMenu-currentColor.yellow>b{background-color:#fc6;}
body#skrollr-body #diigolet-annMenu #diigolet-annMenu-currentColor.blue>b{background-color:#7ccce5;}
body#skrollr-body #diigolet-annMenu #diigolet-annMenu-currentColor.green>b{background-color:#b4db66;}
body#skrollr-body #diigolet-annMenu #diigolet-annMenu-currentColor.pink>b{background-color:#f98baf;}
body#skrollr-body #diigolet-annMenu .diigolet-annMenu-item>b{display:block;height:20px;width:20px;}
body#skrollr-body #diigolet-annMenu-add>b{background-image:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/ann-add.png');}
body#skrollr-body #diigolet-annMenu-share>b{background-image:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/ann-share.png');}
body#skrollr-body #diigolet-annMenu-del>b{background-image:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/ann-del.png');}
body#skrollr-body #diigolet-annMenu-more>b{background-image:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/ann-more.png');}
body#skrollr-body #diigolet-annMenu-colorPicker{height:62px;width:14px;border:1px solid #96bbd5;padding:3px 2px;background-color:#fff;position:relative;top:3px;left:-1px;display:none;-webkit-animation:diigo-dropdown .15s ease-in 1;flex-direction:column;}
body#skrollr-body #diigolet-annMenu-colorPicker .ann-colorItem{height:12px;width:12px;border-width:1px;border-style:solid;display:block;margin-bottom:2px;}
body#skrollr-body #diigolet-annMenu-colorPicker .ann-colorItem:hover{border-color:#06f!important;}
body#skrollr-body #diigolet-annMenu-colorPicker .ann-colorItem.colorchecked b{width:4px;height:4px;background:#666;margin-top:4px;margin-left:4px;display:block;}
body#skrollr-body .ann-colorItem#diigolet-context-yellow{border-color:#e9a110;background-color:#fc6;}
body#skrollr-body .ann-colorItem#diigolet-context-blue{border-color:#33a5c9;background-color:#7ccce5;}
body#skrollr-body .ann-colorItem#diigolet-context-green{border-color:#9ac83b;background-color:#b4db66;}
body#skrollr-body .ann-colorItem#diigolet-context-pink{border-color:#da376c;background-color:#f98baf;}
body#skrollr-body #diigolet-annMenu-arrow{position:absolute;top:100%;left:33px;height:8px;width:14px;background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/ann-arrow.png);}
body#skrollr-body #diigolet-annMenu.onlyMy #diigolet-annMenu-arrow{left:59px;}
body#skrollr-body #diigolet-annMenu-tip{padding-left:4px;border-top:1px solid #eee;margin-top:1px;color:#999;}
body#skrollr-body #diigolet-annMenu-moreThings{display:none;position:absolute;top:110%;left:77%;min-width:236px;max-width:236px;padding:3px;border:1px solid #94bcd6;box-shadow:0 1px 2px rgba(0,0,0,.15);background-color:#fff;border-radius:3px;font:12px/18px arial;color:#333;}
body#skrollr-body .diigoletContexMenu a:link,body#skrollr-body .diigoletContexMenu a:visited{display:block;padding:2px 3px;text-decoration:none;color:#000;cursor:default;white-space:nowrap;}
body#skrollr-body .diigoletContexMenu a:hover:not(.colorItem),body#skrollr-body .diigoletContexMenu a:active{color:#fff;background:#09f;}
body#skrollr-body .diigoletContexMenu div.sep{line-height:0;border-top:1px solid #AAA;margin:3px 0;}
body#skrollr-body *html .diigoletContexMenu ._selection a{width:45px;}
body#skrollr-body *html .diigoletContexMenu ._highlight a{width:90px;}
body#skrollr-body .diigolet.diigoletFN{z-index:2147483644;width:300px;-webkit-user-select:none;}
body#skrollr-body .diigolet.diigoletFN *{flex-direction:row;}
body#skrollr-body #diigolet-dlg-sticky.groupNew #FN-post-form{display:block;}
body#skrollr-body #diigolet-dlg-sticky.groupNew #FN-group-content-nav{display:none;}
body#skrollr-body #diigolet-dlg-sticky.groupNew #FN-group-content{display:none;}
body#skrollr-body .diigolet.diigoletFN.onlyPrivate #diigolet-dlg-sticky-switcher{margin-left:29px;}
body#skrollr-body .diigolet.diigoletFN.onlyGroup #diigolet-dlg-sticky-switcher{margin-left:29px;}
body#skrollr-body #diigolet-dlg-sticky-top{height:30px;border-radius:2px 2px 0 0;position:relative;z-index:2;-webkit-transition:background-color 200ms ease;padding-right:5px;display:block;}
body#skrollr-body #diigolet-dlg-sticky.yellow #diigolet-dlg-sticky-top{background:#f1c40f;}
body#skrollr-body #diigolet-dlg-sticky.blue #diigolet-dlg-sticky-top{background:#5cc7ff;}
body#skrollr-body #diigolet-dlg-sticky.green #diigolet-dlg-sticky-top{background:#47bf87;}
body#skrollr-body #diigolet-dlg-sticky.pink #diigolet-dlg-sticky-top{background:#fe97bc;}
body#skrollr-body #diigolet-dlg-sticky-content{background-color:#fcfbf7;border-radius:0 0 2px 2px;border-width:0 1px 1px 1px;border-color:rgba(0,0,0,.08);border-style:solid;box-shadow:0 1px 3px rgba(0,0,0,.08);position:relative;}
body#skrollr-body #diigolet-dlg-sticky-logo{float:left;height:20px;width:20px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/FN-logo.png") 50% 50% no-repeat;margin:4px 5px 0 4px;}
body#skrollr-body #diigolet-dlg-sticky-top>span{vertical-align:middle;line-height:28px;font-size:14px;color:#bb6602;}
body#skrollr-body #diigolet-dlg-sticky-close{float:right;height:20px;width:20px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/FN-close.png") 50% 50% no-repeat;margin:5px 4px 0 0;cursor:pointer;display:none;}
body#skrollr-body #diigolet-dlg-sticky-color{position:relative;float:right;margin:9px 4px 0 0;cursor:pointer;z-index:2;}
body#skrollr-body #diigolet-dlg-sticky-addTab{height:12px;width:21px;margin:9px 7px 0 0;display:none;float:right;cursor:pointer;}
body#skrollr-body #diigolet-dlg-sticky.onlyPrivate #diigolet-dlg-sticky-addTab{display:block;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/add-tab.png") 0 0 no-repeat;}
body#skrollr-body #diigolet-dlg-sticky.onlyGroup #diigolet-dlg-sticky-addTab{display:block;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/add-tab.png") 0 -12px no-repeat;}
body#skrollr-body #diigolet-dlg-sticky-currentColor{height:12px;width:12px;border:1px solid #fff;cursor:pointer;border-radius:1px;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker{height:62px;width:13px;padding:3px 3px 3px 2px;background-color:#fff;position:absolute;top:122%;display:none;-webkit-animation:diigo-dropdown .15s ease-in 1;box-shadow:0 1px 1px rgba(0,0,0,0.25);z-index:3;flex-direction:column;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker .dlg-colorItem{height:12px;width:12px;border-width:1px;border-style:solid;display:block;margin-bottom:2px;margin-left:-1px;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker .dlg-colorItem[color="yellow"]{border-color:#e9a110;background-color:#fc6;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker .dlg-colorItem[color="blue"]{border-color:#33a5c9;background-color:#7ccce5;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker .dlg-colorItem[color="green"]{border-color:#9ac83b;background-color:#b4db66;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker .dlg-colorItem[color="pink"]{border-color:#da376c;background-color:#f98baf;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker .dlg-colorItem.colorchecked b{width:4px;height:4px;background:#666;margin-top:3px;margin-left:3px;display:block;}
body#skrollr-body #diigolet-dlg-sticky-colorPicker .dlg-colorItem:hover{border-color:#06f!important;}
body#skrollr-body .FN-content-wrapper{display:none;opacity:0;-webkit-animation:fadeIn .2s ease-out;}
body#skrollr-body 0%{opacity:0;}
body#skrollr-body 100%{opacity:1;}
body#skrollr-body .FN-content-wrapper.private{min-height:120px;}
body#skrollr-body #diigolet-dlg-sticky-content .FN-content-wrapper.private textarea{margin:6px 6px 0 6px;min-height:104px;width:282px;background-color:#fcfbf7;border:none;outline:none;overflow-y:visible;resize:none!important;font-size:12px;line-height:18px;word-wrap:break-word;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer{text-align:right;margin-top:-5px;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer #editing{height:30px;border-top:1px solid #ECECE7;display:none;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer #editing a{float:right;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer #editing #FN-private-saveBtn{height:20px;width:50px;border-radius:2px;border:1px solid #85a0a6;color:#85a0a6;font-size:12px;text-align:center;line-height:20px;margin:4px 4px 4px 10px;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer #editing #FN-private-saveBtn:active{background:#85a0a6;color:#fff;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer #editing #FN-private-cancelBtn{text-decoration:none;color:#A3A39E;font-size:12px;line-height:30px;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer #editing #FN-private-cancelBtn:hover{text-decoration:underline;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-content-footer #editDone{height:22px;}
body#skrollr-body #FN-private-saveBtn.notify{-webkit-animation:borderNotice 600ms ease both;-webkit-animation-iteration-count:2;}
body#skrollr-body #FN-content-footer #FN-private-datetime{font-family:Arial,Helvetica;font-size:12px;color:#999;line-height:22px;margin-right:10px;float:right;}
body#skrollr-body #FN-content-footer #FN-private-delete{display:none;float:left;vertical-align:middle;line-height:22px;margin-left:8px;color:#999;cursor:pointer;-webkit-transition:color 200ms ease;}
body#skrollr-body #FN-content-footer #FN-private-delete b{display:block;float:left;height:12px;width:11px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/private-del.png");background-repeat:no-repeat;margin:5px 3px 0 0;cursor:pointer;}
body#skrollr-body #FN-content-footer #FN-private-delete:hover{color:red;}
body#skrollr-body #FN-content-footer #FN-private-delete:hover b{background-position:0 -12px;}
body#skrollr-body .FN-content-wrapper.group{min-height:50px;}
body#skrollr-body .FN-radio{display:none;}
body#skrollr-body #diigolet-dlg-sticky-switcher{position:absolute;left:82px;top:-25px;z-index:2;}
body#skrollr-body #diigolet-dlg-sticky-switcher.onlyOneTab span{margin-left:28px;}
body#skrollr-body #diigolet-dlg-sticky-switcher .FN-switcher{float:left;height:18px;text-align:center;font-size:12px;cursor:pointer;padding:3px 8px;color:#fff;line-height:14px;-webkit-transition:background-color 200ms ease;border-radius:2px;}
body#skrollr-body #diigolet-dlg-sticky-switcher .FN-switcher b{height:12px;width:13px;float:left;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/tab-logo.png");background-repeat:no-repeat;margin:1px 1px 0 0;cursor:pointer;}
body#skrollr-body #diigolet-dlg-sticky-content.private #FN-switcher-private{background-color:rgba(0,0,0,.12);}
body#skrollr-body #diigolet-dlg-sticky-content #FN-switcher-private b{background-position:0 0;}
body#skrollr-body #diigolet-dlg-sticky-content #FN-switcher-group b{background-position:0 -12px;}
body#skrollr-body #diigolet-dlg-sticky-content.group #FN-switcher-group{background-color:rgba(0,0,0,.12);}
body#skrollr-body #diigolet-dlg-sticky.onlyPrivate #FN-switcher-group{display:none;}
body#skrollr-body #diigolet-dlg-sticky.onlyGroup #FN-switcher-private{display:none;}
body#skrollr-body #diigolet-dlg-sticky-content.private .FN-content-wrapper.private{opacity:1;display:block;}
body#skrollr-body #diigolet-dlg-sticky-content.group .FN-content-wrapper.group{opacity:1;-webkit-transition:opacity ease-out .2s .1s;display:block;}
body#skrollr-body #FN-post-form{padding:10px;display:none;}
body#skrollr-body #FN-post-form>div:last-child{margin-top:6px;}
body#skrollr-body #FN-post-form textarea{width:272px;max-width:272px;height:54px;outline:none;line-height:18px;border:1px solid #ddd;}
body#skrollr-body #FN-post-form textarea.notify,body#skrollr-body #FN-post-form select.notify{-webkit-animation:borderNotice 600ms ease both;-webkit-animation-iteration-count:2;}
body#skrollr-body #FN-post-form button{float:right;margin:0;height:24px;width:50px;text-align:center;background-image:-webkit-linear-gradient(top,#fff,#f5f5f5);border:1px solid #ccc;font-size:14px;border-radius:2px;cursor:pointer;-webkit-transition:.3s cubic-bezier(0.175,0.885,0.32,1.275) all,10ms ease background-color;overflow:hidden;position:relative;}
body#skrollr-body #FN-post-form .button-label{-webkit-transition:.3s cubic-bezier(0.175,0.885,0.32,1.275) all;position:relative;cursor:pointer;z-index:3;}
body#skrollr-body #FN-post-form .button-spinner{position:absolute;z-index:2;display:inline-block;width:18px;height:18px;opacity:0;-webkit-transition:.3s cubic-bezier(0.175,0.885,0.32,1.275) all;left:31px;margin-left:-16px;margin-top:-10px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/uploading.gif");}
body#skrollr-body #FN-post-form textarea:disabled{color:#999;background-color:#eee;}
body#skrollr-body #FN-post-form button:disabled{background-color:#ddd;background-image:none;cursor:default;}
body#skrollr-body #FN-post-form button:disabled .button-label{opacity:0;top:16px;}
body#skrollr-body #FN-post-form button:disabled .button-spinner{opacity:1;top:12px;}
body#skrollr-body #FN-post-form a{float:right;font-size:12px;text-decoration:none;color:#aaa;margin:5px 12px 5px 5px;}
body#skrollr-body #FN-post-form a:hover{text-decoration:underline;}
body#skrollr-body #FN-post-form.notEdit #FN-group-share{margin-left:67px;}
body#skrollr-body #FN-post-form.notEdit div:first-child{display:none;}
body#skrollr-body #FN-post-form.notEdit button,body#skrollr-body #FN-post-form.notEdit a{display:none;}
body#skrollr-body #FN-group-content-nav{width:100%;height:25px;border-bottom:1px solid #eee;color:#333;font-size:12px;text-align:center;position:relative;z-index:1;}
body#skrollr-body #FN-current-group{line-height:25px;padding:2px 10px;cursor:pointer;}
body#skrollr-body #FN-current-group b{height:0;width:0;border-width:5px;border-style:solid;border-bottom-color:transparent;border-left-color:transparent;border-right-color:transparent;border-top-color:#666;display:inline-block;margin:2px 2px 0 6px;vertical-align:middle;cursor:pointer;}
body#skrollr-body #FN-current-group span{cursor:pointer;}
body#skrollr-body #FN-group-menu{margin:0;position:absolute;width:196px;top:90%;left:50px;background-color:#fff;border:1px solid rgba(0,0,0,.12);text-align:left;box-shadow:0 1px 2px rgba(0,0,0,.1);-webkit-animation:diigo-dropdown .15s ease-in 1;padding:2px;display:none;}
body#skrollr-body #FN-group-content-nav li{list-style:none;height:20px;width:100%;line-height:20px;font-size:12px;color:#333;cursor:pointer;text-indent:9px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
body#skrollr-body #FN-group-share-new-ul{margin-top:2px;padding-top:2px;border-top:1px solid #ccc;}
body#skrollr-body #FN-group-content-nav li:hover{background-color:#aaa;color:#fff;}
body#skrollr-body #FN-group-content-container{min-height:80px;max-height:200px;overflow-y:auto;padding:0 10px 10px 10px;margin-top:-1px;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item{border-top:1px solid #eee;padding:5px 0;position:relative;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item-tbar{position:relative;font-size:12px;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item-content{font-size:12px;line-height:18px;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item-tbar .FN-group-comment-name{text-decoration:none;margin-right:3px;color:#0072d6;float:left;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item-time{font-size:12px;color:#777;}
body#skrollr-body #FN-group-content-postform{padding:10px;position:relative;}
body#skrollr-body #FN-group-content-postform textarea{height:18px;width:204px;max-width:208px;border:1px solid #d7d7d7;outline:none;line-height:18px;vertical-align:bottom;-webkit-transition:background-color .1s ease-in-out;}
body#skrollr-body #FN-group-content-postform.active textarea{height:36px;border-color:#aaa;}
body#skrollr-body #FN-group-content-postform textarea.notify{-webkit-animation:borderNotice 600ms ease both;-webkit-animation-iteration-count:2;}
body#skrollr-body #FN-group-content-postform textarea:disabled{color:#999;background-color:#eee;}
body#skrollr-body #FN-group-content-postform .post-action{vertical-align:bottom;display:inline-block;width:50px;padding:0 0 0 14px;}
body#skrollr-body #FN-group-content-postform .post-action a{position:relative;left:4px;top:2px;color:#aaa;display:none;}
body#skrollr-body #FN-group-content-postform.active .post-action a{display:block;}
body#skrollr-body #FN-group-content-postform .post-action a:hover{text-decoration:underline;}
body#skrollr-body #FN-group-content-postform button{margin:0;height:24px;width:50px;text-align:center;background-image:-webkit-linear-gradient(top,#fff,#f5f5f5);border:1px solid #ccc;font-size:14px;cursor:pointer;-webkit-transition:.3s cubic-bezier(0.175,0.885,0.32,1.275) all,10ms ease background-color;overflow:hidden;position:relative;}
body#skrollr-body #FN-group-content-postform .button-label{-webkit-transition:.3s cubic-bezier(0.175,0.885,0.32,1.275) all;position:relative;cursor:pointer;z-index:3;}
body#skrollr-body #FN-group-content-postform .button-spinner{position:absolute;z-index:2;display:inline-block;width:18px;height:18px;opacity:0;-webkit-transition:.3s cubic-bezier(0.175,0.885,0.32,1.275) all;left:31px;margin-left:-16px;margin-top:-10px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/uploading.gif");}
body#skrollr-body #FN-group-content-postform button:disabled{background-color:#ddd;background-image:none;cursor:default;}
body#skrollr-body #FN-group-content-postform button:disabled .button-label{opacity:0;top:16px;}
body#skrollr-body #FN-group-content-postform button:disabled .button-spinner{opacity:1;top:12px;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item-delete{text-decoration:none;font-size:12px;color:#999;cursor:pointer;visibility:hidden;float:right;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item:hover .FN-group-comment-item-delete{visibility:visible;}
body#skrollr-body #FN-group-content-container .FN-group-comment-item-delete:hover{color:red;}
body#skrollr-body #diigolet-dlg-sticky-content ::-webkit-scrollbar{width:8px;}
body#skrollr-body #diigolet-dlg-sticky-content ::-webkit-scrollbar-track-piece{background-color:transparent;}
body#skrollr-body #diigolet-dlg-sticky-content ::-webkit-scrollbar-thumb:vertical{height:20px;background-color:#CCC;}
body#skrollr-body #diigolet-dlg-sticky-content ::-webkit-scrollbar-thumb:hover{background-color:#aaa;}
body#skrollr-body #diigolet-dlg-sticky-content select{-webkit-appearance:none;width:150px;height:24px;border:1px solid #ccc;background-position:right;background-repeat:no-repeat;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/FN-select-arrow.png"),-webkit-linear-gradient(top,#fff,#fafafa);outline:none;cursor:pointer;font-size:12px;border-radius:2px;padding-right:14px;}
body#skrollr-body .diigolet.diigoletFN a:link,body#skrollr-body .diigolet.diigoletFN a:visited{color:#06c;}
body#skrollr-body .diigolet.diigoletFN a:hover,body#skrollr-body .diigolet.diigoletFN a:active{color:#333;text-decoration:none;}
body#skrollr-body .diigolet .diigoletFNL{width:23px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_l.png) no-repeat left top;}
body#skrollr-body .diigolet .diigoletFNT{height:32px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_t.png) no-repeat right top;cursor:move!important;}
body#skrollr-body .diigolet .diigoletFNR{width:16px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_r.png) no-repeat left bottom;overflow:hidden;vertical-align:bottom;}
body#skrollr-body .diigolet .diigoletFNB{height:34px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_b.png) no-repeat left bottom;}
body#skrollr-body .diigolet .diigoletFNTH{vertical-align:top;width:12px;}
body#skrollr-body .diigolet .diigoletFNTH div{width:12px;height:12px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_h_rt.gif) no-repeat right top;position:relative;top:5px;left:-22px;overflow:hidden;cursor:ne-resize!important;}
body#skrollr-body .diigolet .diigoletFNB{vertical-align:top;overflow:hidden;}
body#skrollr-body .diigolet .diigoletFNPosN .diigoletFNXjjR,body#skrollr-body .diigolet .diigoletFNPosN .diigoletFNXjjT,body#skrollr-body .diigolet .diigoletFNPosN .diigoletFNXjjB,body#skrollr-body .diigolet .diigoletFNPosN .diigoletFNTH div,body#skrollr-body .diigolet .diigoletFNPosN .diigoletFNB div{display:none;}
body#skrollr-body .diigolet .diigoletFNT h1{font:12px/19px Arial,Helvetica,sans-serif;font-weight:bold;color:#666;margin:4px 0 0 5px;padding:0;}
body#skrollr-body .diigolet .diigoletFNT div.menu{margin:3px 21px 10px 0;background-color:#fff9a4;border-right:1px solid #f2e984;border-left:1px solid #c9b822;}
body#skrollr-body .diigolet .diigoletFNT div.menu a{display:block;line-height:19px;float:left;color:#666;padding:0 5px;border-right:1px solid #c9b822;text-decoration:none;}
body#skrollr-body .diigolet .diigoletFNT div.menu a:hover,body#skrollr-body .diigolet .diigoletFNT div.menu a:active{background-color:#fff587;color:#333;}
body#skrollr-body .diigolet .diigoletFNT div.menu a.diigoletFNOpt{background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_downdot.gif) no-repeat right top;padding-right:14px;}
body#skrollr-body .diigolet .diigoletFNT{font:12px/32px Arial,Helvetica,sans-serif;}
body#skrollr-body .diigolet .diigoletFNContent,body#skrollr-body .diigolet .diigoletFNComment{background-color:#fff89f;color:#666;font-family:Arial,Helvetica,sans-serif;font-size:11px;overflow:auto;width:355px;zoom:1;border-bottom:1px solid #E0DB9D;}
body#skrollr-body .diigolet .diigoletFNContent .diigoletFNAuthorP{font-size:10px;font-weight:normal;color:#666;margin:0 11px 5px 0;padding:2px 5px;line-height:100%;}
body#skrollr-body .diigolet .diigoletFNContent .diigoletFNAuthorP .diigoletFNAuthor{border-bottom:1px dotted #ccc;color:#06c;}
body#skrollr-body .diigolet .diigoletFNContent .diigoletFNAuthorP .diigoletFNAuthor:hover,body#skrollr-body .diigoletFNContent .diigoletFNAuthorP .diigoletFNAuthor:active{border-bottom:1px solid #ccc;color:#333;}
body#skrollr-body .diigolet .diigoletFNContent .diigoletFNAuthorP a{color:#999;}
body#skrollr-body .diigolet .diigoletFNContent .diigoletFNAuthorP a:hover,body#skrollr-body .diigoletFNContent .diigoletFNAuthorP a:active{color:#666;}
body#skrollr-body .diigolet.diigoletFN blockquote{display:inline-block;}
body#skrollr-body .diigolet .diigoletFNComment select,body#skrollr-body .diigolet .diigoletFNComment input,body#skrollr-body .diigolet .diigoletFNComment textarea{font:11px/15px Verdana,Arial,Helvetica,sans-serif;max-width:345px;}
body#skrollr-body .diigolet .diigoletFNComment p{margin:5px 0;}
body#skrollr-body .diigolet .diigoletFNTDiv{height:32px;overflow:hidden;}
body#skrollr-body .diigolet.diigoletFN .menu{float:right;height:19px;overflow:hidden;}
body#skrollr-body .diigolet .labelList label{margin-right:2px;background-color:#eee;color:#666;white-space:nowrap;font-weight:normal;font-size:9px;}
body#skrollr-body .diigolet .labelList span{padding:0 2px;}
body#skrollr-body .diigolet .labelList a{padding:0 2px;background-color:#ffe76a;}
body#skrollr-body .diigolet .labelList a:hover{color:#fef5c7;text-decoration:none;}
body#skrollr-body .diigolet .labelList a.del{border:none;padding-right:2px;font-weight:normal;}
body#skrollr-body .diigolet a.del{cursor:pointer;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv3.gif") no-repeat left -343px;}
body#skrollr-body .diigolet a.del:hover{filter:alpha(opacity=100);-moz-opacity:1;background-position:1px -342px;text-decoration:none;}
body#skrollr-body .diigolet ul.diigoletFNDropdown{position:absolute;display:none;left:10px;background-color:#fff89f;border:1px solid #c9b822;z-index:2147483647;}
body#skrollr-body .diigolet ul.diigoletFNDropdown li{padding-left:25px;}
body#skrollr-body .diigolet ul.diigoletFNDropdown a:link,body#skrollr-body .diigolet ul.diigoletFNDropdown a:visited{color:#666;display:block;width:85px;font:11px Arial,Helvetica,sans-serif;}
body#skrollr-body .diigolet ul.diigoletFNDropdown a:hover,body#skrollr-body .diigolet ul.diigoletFNDropdown a:active{background-color:#fff567;color:#333;}
body#skrollr-body .diigolet.diigoletFNIEPatch .diigoletFNL{background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_l.gif) no-repeat left top;}
body#skrollr-body .diigolet.diigoletFNIEPatch .diigoletFNT{background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_t.gif) no-repeat right top;}
body#skrollr-body .diigolet.diigoletFNIEPatch .diigoletFNR{background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_r.gif) no-repeat left bottom;}
body#skrollr-body .diigolet.diigoletFNIEPatch .diigoletFNB{background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_b.gif) no-repeat left bottom;}
body#skrollr-body .diigolet.diigoletFNIEPatch .diigoletFNT{height:23px;}
body#skrollr-body .diigolet.diigoletFNIEPatch .diigoletFNTDiv{height:23px;}
body#skrollr-body .diigoletFN.editing .diigoletFNComment{display:block;}
body#skrollr-body .personalText{color:#555!important;font-size:10px!important;display:inline-block;overflow:hidden!important;text-overflow:ellipsis!important;white-space:nowrap!important;width:343px!important;margin-top:4px!important;}
body#skrollr-body .IconFeild{float:left!important;margin-left:8px!important;margin-top:5px!important;}
body#skrollr-body .IconFeild:hover .editIcon{background-position:right!important;}
body#skrollr-body .multipalCol{padding-top:0!important;}
body#skrollr-body .singleCol{padding-top:7px!important;}
body#skrollr-body .myCommentSpan{margin-left:35px!important;}
body#skrollr-body .notMyCommentSpan{margin-left:15px!important;}
body#skrollr-body .footText{line-height:1.5;width:343px!important;}
body#skrollr-body div.floatNote{position:absolute!important;width:34px;height:34px;text-align:center;background-image:url('chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_icon.png')!important;background-repeat:no-repeat;z-index:2147483643;}
body#skrollr-body div.floatNote.private.yellow{background-position:0 0;}
body#skrollr-body div.floatNote.private.blue{background-position:0 -68px;}
body#skrollr-body div.floatNote.private.green{background-position:0 -136px;}
body#skrollr-body div.floatNote.private.pink{background-position:0 -204px;}
body#skrollr-body div.floatNote.group.yellow{background-position:0 -34px;}
body#skrollr-body div.floatNote.group.blue{background-position:0 -102px;}
body#skrollr-body div.floatNote.group.green{background-position:0 -170px;}
body#skrollr-body div.floatNote.group.pink{background-position:0 -238px;}
body#skrollr-body div.floatNote.diigoshow{-webkit-animation:bounceIn 400ms ease both;-webkit-animation-play-state:running;}
body#skrollr-body div.floatNote.diigoadd{-webkit-animation:flipInY 600ms ease both;-webkit-animation-play-state:running;}
body#skrollr-body div.floatNote span{position:absolute;left:-4px;top:-3px;display:block;border-radius:15px;background-color:#666;padding:2px 3px;border:1px solid #fff;height:8px;font-size:11px;color:#fff;line-height:8px;}
html body#skrollr-body div.floatNote{filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,sizingMethod=scale,src="chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_icon.png");overflow:hidden;background:none;overflow:visible;}
body#skrollr-body em.diigoHighlight{text-align:inherit;text-decoration:inherit;line-height:inherit;font:inherit;color:inherit;display:inline;position:relative;zoom:1;margin:0;padding:0;}
body#skrollr-body em.diigoHighlight.hover{cursor:move;}
body#skrollr-body em.diigoHighlight.hover.yellow{background-color:#F5F548;}
body#skrollr-body em.diigoHighlight.hover.blue{background-color:#84B9EF;}
body#skrollr-body em.diigoHighlight.hover.green{background-color:#A0DE60;}
body#skrollr-body em.diigoHighlight.hover.pink{background-color:#F9B0B0;}
body#skrollr-body em.diigoHighlight.diigoHighlightcommented{margin-right:25px;}
body#skrollr-body em.diigoHighlight.mouseOvered{background-color:#ffc62a!important;}
body#skrollr-body em.diigoHighlight.yellow{background-color:#FF9;}
body#skrollr-body img.diigoHighlight.yellow{cursor:pointer;outline:2px solid #FF9!important;}
body#skrollr-body em.diigoHighlight.blue{background-color:#ABD5FF;}
body#skrollr-body img.diigoHighlight.blue{cursor:pointer;outline:2px solid #ABD5FF!important;}
body#skrollr-body em.diigoHighlight.green{background-color:#B2E57E;}
body#skrollr-body img.diigoHighlight.green{cursor:pointer;outline:2px solid #B2E57E!important;}
body#skrollr-body em.diigoHighlight.pink{background-color:#fcc;}
body#skrollr-body img.diigoHighlight.pink{cursor:pointer;outline:2px solid #fcc!important;}
body#skrollr-body img.diigoHighlight.mouseOvered{cursor:pointer;outline:2px solid #ffc62a!important;}
body#skrollr-body .diigolet .diigolet-closeBtn{position:absolute;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/close1.gif);width:14px;height:14px;top:2px;right:2px;cursor:pointer!important;}
body#skrollr-body .ac_results{border:1px solid #ddd;background:#fff none repeat scroll 0;cursor:pointer!important;font-size:11px!important;left:0;position:absolute;width:392px;z-index:2147483647;border-radius:1px;}
body#skrollr-body .ac_results ul{margin:0;padding:0;}
body#skrollr-body .ac_results li{list-style-image:none;list-style-position:outside;list-style-type:none;padding:2px 5px;border-radius:1px;}
body#skrollr-body .ac_results a{width:100%;}
body#skrollr-body .ac_results li.over{color:white;background:#09f none repeat scroll 0;}
body#skrollr-body #gtooltip{background-color:#2a2a2a;border:1px solid #fff;color:#fff;display:block;font-size:12px!important;font-weight:bold!important;opacity:0;padding:4px 6px!important;pointer-events:none;position:absolute!important;-webkit-transition:visibility .13s,opacity .13s ease-out,left 0 linear .13s,top 0 linear .13s;-moz-transition:visibility .13s,opacity .13s ease-out,left 0 linear .13s,top 0 linear .13s;-o-transition:visibility .13s,opacity .13s ease-out,left 0 linear .13s,top 0 linear .13s;transition:visibility .13s,opacity .13s ease-out,left 0 linear .13s,top 0 linear .13s;visibility:hidden;font-family:arial,sans-serif!important;z-index:2147483647;top:-100px;left:-100px;line-height:15px!important;}
body#skrollr-body #gtooltip.show{visibility:visible;opacity:1;-webkit-transition:visibility 0,opacity .13s ease-in;}
body#skrollr-body #gtooltip #gtooltip-arrow{position:absolute!important;border:5px solid!important;border-top-color:transparent!important;border-right-color:transparent!important;border-bottom-color:#2a2a2a!important;border-left-color:transparent!important;height:0!important;width:0!important;line-height:0!important;}
body#skrollr-body #gtooltip #gtooltip-content{white-space:nowrap!important;}
body#skrollr-body .diigo-scrollmarker{height:10px;width:10px;cursor:pointer;overflow:hidden;font-size:12px;z-index:1000000;}
body#skrollr-body .diigo-scrollmarker .inner{height:0;width:0;border-width:5px;border-style:solid;position:relative;right:-4px;}
body#skrollr-body .diigo-scrollmarker.yellow .inner{border-color:transparent transparent transparent #ffb000;}
body#skrollr-body .diigo-scrollmarker.blue .inner{border-color:transparent transparent transparent #0087f7;}
body#skrollr-body .diigo-scrollmarker.green .inner{border-color:transparent transparent transparent #00a256;}
body#skrollr-body .diigo-scrollmarker.pink .inner{border-color:transparent transparent transparent #f39;}
body#skrollr-body #diigolet-highlight-share{background-color:#fcfbf7;width:402px;font-family:Arial,Helvetica,sans-serif;-webkit-border-radius:0;cursor:default;position:absolute;z-index:2147483646;box-shadow:0 1px 3px rgba(0,0,0,.08);background-clip:content-box;visibility:hidden;opacity:0;border-radius:2px;display:block;}
body#skrollr-body #diigolet-highlight-share.show{opacity:1;visibility:visible;}
body#skrollr-body #diigolet-highlight-share-top{height:30px;vertical-align:middle;background-color:#39baf6;line-height:30px;padding:0 10px;font-size:14px;color:white;text-align:left;border-radius:2px 2px 0 0;}
body#skrollr-body .diigolet-question-mark{height:12px;width:12px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/q-mark.png");cursor:pointer;position:relative;display:inline-block;margin:9px 7px 0 6px;}
body#skrollr-body .diigolet-question-mark-tip{padding:5px;position:absolute;bottom:139%;left:-82px;display:none;width:180px;color:#7f8d99;border-radius:2px;box-shadow:0 0 0 2px rgba(0,0,0,.2);background:#fff;font:normal 12px/14px Arial,helvetica,sans-serif;}
body#skrollr-body #diigolet-highlight-share-close{float:right;height:16px;width:16px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/win-close.png") 50% 50% no-repeat;margin-top:7px;opacity:.5;cursor:pointer;}
body#skrollr-body #diigolet-highlight-share-close:hover{opacity:1;}
body#skrollr-body #diigolet-highlight-container{border-radius:0 0 2px 2px;border-width:0 1px 1px 1px;border-color:rgba(0,0,0,.08);border-style:solid;display:block;}
body#skrollr-body #diigolet-highlight-main{padding:10px 10px;}
body#skrollr-body #diigolet-highlight-share-textarea{border:1px solid #d7d7d7;outline:none;width:372px;height:42px;max-width:374px;line-height:18px;-webkit-transition:border-color 200ms ease;font:12px/14px Arial;min-height:42px;padding:3px 3px;resize:vertical;box-sizing:content-box;}
body#skrollr-body #diigolet-highlight-share-textarea:disabled{background-color:#eee;}
body#skrollr-body #diigolet-highlight-share-textarea:focus{border:1px solid #AAA;}
body#skrollr-body .clearfloat:after{display:block;clear:both;content:"";visibility:hidden;height:0;}
body#skrollr-body .clearfloat{zoom:1;}
body#skrollr-body #diigolet-highlight-footer{padding:0 10px 10px 10px;position:relative;display:block;}
body#skrollr-body #diigolet-highlight-footer a{float:right;}
body#skrollr-body #diigolet-highlight-share-copybtn{height:24px;width:60px;line-height:24px;cursor:pointer;text-align:center;color:white;border-radius:2px;border:1px solid #066ec1;font-size:12px;text-decoration:none;border-radius:2px;border:1px solid #85a0a6;color:#85a0a6;font-size:12px;text-align:center;}
body#skrollr-body #diigolet-highlight-share-copybtn:active{background:#85a0a6;color:#fff;}
body#skrollr-body #diigolet-highlight-share-cancelbtn{color:#999;height:12px;font-size:12px;margin:6px 14px 0 0;text-decoration:none;border:none!important;}
body#skrollr-body #diigolet-highlight-share-cancelbtn:hover{text-decoration:underline;}
body#skrollr-body #diigolet-highlight-footer .diigolet-highlight-social-btn{float:left!important;height:26px;width:26px;margin-right:12px;}
body#skrollr-body #diigolet-highlight-share-twitter{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/highlight-share.png");}
body#skrollr-body #diigolet-highlight-share-facebook{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/highlight-share.png");background-position:-26px 0;}
body#skrollr-body #diigolet-highlight-share-copySuccess{position:absolute;top:0;right:85px;padding:5px 10px;background:#FFF1A8;color:black;border-radius:3px;line-height:18px;font-size:12px;-webkit-transition:all .3s;opacity:0;-webkit-transform-style:preserve-3d;-webkit-transform:rotateY(-70deg);}
body#skrollr-body #diigolet-highlight-share-copySuccess.show{-webkit-transform:rotateY(0deg);opacity:1;}
body#skrollr-body #diigo-annotationList{background-color:#fff;width:423px;font-family:Arial,Helvetica,sans-serif;-webkit-border-radius:0;cursor:default;z-index:2147483646;box-shadow:0 1px 3px rgba(0,0,0,0.08);background-clip:content-box;border-radius:2px;position:fixed;top:52px;left:0;-webkit-animation:slideInRight 200ms ease;}
body#skrollr-body #diigo-annotationList-btn{height:20px;width:20px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/warning-orphanHighlight.png");position:fixed;right:0;top:55px;cursor:pointer;z-index:1000001;}
body#skrollr-body #diigo-annotationList-top{height:30px;vertical-align:middle;background-color:#39BAF6;line-height:30px;padding:0 10px;font-size:14px;color:#FFF;text-align:left;border-radius:2px 2px 0 0;text-indent:5px;display:block;}
body#skrollr-body #diigo-annotationList-top b{height:12px;width:14px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/list-icon.png");float:left;margin-top:10px;margin-left:-4px;display:block;}
body#skrollr-body #diigo-annotationList-close{float:right;height:16px;width:16px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/win-close.png") 50% 50% no-repeat;margin-top:7px;opacity:.5;cursor:pointer;}
body#skrollr-body #diigo-annotationList-close:hover{opacity:1;}
body#skrollr-body #diigo-annotationList-toolbar{height:30px;font:normal 12px/30px arial,Helvetica;display:block;}
body#skrollr-body #diigo-annotationList-toolbar span{float:left;color:#333;margin-left:10px;}
body#skrollr-body #diigo-annotationList-toolbar a{float:right;margin-right:10px;text-decoration:none;color:#0072d6;}
body#skrollr-body #diigo-annotationList-box{border-radius:0 0 2px 2px;border-width:0 1px 1px 1px;border-color:rgba(0,0,0,0.08);border-style:solid;padding:5px 6px 0 6px;position:relative;max-height:300px;overflow:auto;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item{margin-bottom:8px;position:relative;background-color:#f9f9f9;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-orphan .diigo-annotationList-highlight,body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-orphan .diigo-annotationList-sticky{padding-right:19px;}
body#skrollr-body .diigo-annotationList-item .diigo-annotationList-orphan-warning{height:19px;width:19px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/orphan-warning.png");position:absolute;top:0;right:0;opacity:.65;}
body#skrollr-body .diigo-orphan-warning{height:15px;width:15px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/orphan-warning-small.png");float:left;opacity:.65;margin-right:4px;margin-top:7px;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-highlight{padding:6px 6px;font:normal 12px/14px arial,Helvetica;color:#333;border-left-style:solid;border-left-width:4px;border-bottom:1px solid #eee;position:relative;word-wrap:break-word;white-space:normal;word-break:break-all;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-yellow .diigo-annotationList-highlight{border-left-color:#FFBA01;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-blue .diigo-annotationList-highlight{border-left-color:#6EAAF5;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-green .diigo-annotationList-highlight{border-left-color:#7BBD3F;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-pink .diigo-annotationList-highlight{border-left-color:#FF9C9C;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-sticky{padding:6px 6px 6px 26px;font:normal 12px/14px arial,Helvetica;color:#333;background-color:#f9f9f9;border-left-style:solid;border-left-width:4px;border-left-color:#DDD;border-bottom:1px solid #eee;position:relative;word-wrap:break-word;white-space:normal;word-break:break-all;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-yellow .diigo-annotationList-sticky .diigo-anntationList-floatIcon{background-position:0 -16px;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-blue .diigo-annotationList-sticky .diigo-anntationList-floatIcon{background-position:0 -32px;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-green .diigo-annotationList-sticky .diigo-anntationList-floatIcon{background-position:0 -48px;}
body#skrollr-body #diigo-annotationList-box .diigo-annotationList-item.diigo-pink .diigo-annotationList-sticky .diigo-anntationList-floatIcon{background-position:0 -64px;}
body#skrollr-body .diigo-annotationList-item .diigo-annotationList-item-action{position:absolute;right:1px;bottom:1px;font:normal 10px/12px arial,Helvetica;display:none;z-index:10000;}
body#skrollr-body .diigo-annotationList-item .diigo-annotationList-item-btn{background-color:rgba(0,0,0,0.3);padding:2px;color:#fff;cursor:pointer;z-index:1;opacity:.8;float:left;margin-left:5px;}
body#skrollr-body .diigo-annotationList-item .diigo-annotationList-item-btn:hover{opacity:1;}
body#skrollr-body .diigo-annotationList-commentItem{padding:5px 6px;background-color:#f9f9f9;word-break:break-all;border-left-style:solid;border-left-width:4px;border-left-color:#DDD;border-bottom:1px solid #eee;font:normal 12px/14px arial,Helvetica;}
body#skrollr-body .diigo-annotationList-item:hover .diigo-annotationList-item-action{display:block;}
body#skrollr-body .diigo-anntationList-floatIcon{background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/float_note_icon.png");height:16px;width:16px;position:absolute;left:5px;top:5px;}
body#skrollr-body #diigo-annotationList-main{position:relative;}
body#skrollr-body #diigo-annotationList-notification{height:30px;width:150px;border:2px solid rgba(0,0,0,.15);position:absolute;left:50%;top:50%;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/success.png") 5px 50% no-repeat;text-indent:26px;font:normal 12px/30px arial,Helvetica;background-color:#fff;border-radius:2px;-webkit-transform:translate(-50%,-50%);background-clip:content-box;z-index:1;display:none;}
body#skrollr-body #diigo-annotationList-noItem{padding:10px;font-weight:bold;}
body#skrollr-body .diigo-customize-scrollbar::-webkit-scrollbar{width:6px;}
body#skrollr-body .diigo-customize-scrollbar::-webkit-scrollbar-track-piece{background-color:transparent;}
body#skrollr-body .diigo-customize-scrollbar::-webkit-scrollbar-thumb:vertical{height:20px;background-color:#CCC;}
body#skrollr-body .diigo-customize-scrollbar::-webkit-scrollbar-thumb:hover{background-color:#aaa;}
body#skrollr-body .diigolet-highlight-selected{-webkit-animation:highlight 800ms ease-in-out;}
body#skrollr-body #diigo-ext-tutorial-wrapper{position:fixed;bottom:0;right:0;left:0;top:0;background:rgba(0,0,0,.8);text-align:center;font-family:arial,Helvetica;z-index:10000;font-size:16px!important;visibility:hidden;opacity:0;transition:opacity .2s linear;}
body#skrollr-body #diigo-ext-tutorial-wrapper.active{visibility:visible;opacity:1;}
body#skrollr-body #diigo-ext-tutorial-panel{display:inline-block;width:805px;height:664px;border-radius:5px;background:white;vertical-align:middle;position:relative;transform:scale(0.95);transition:transform .2s linear;}
body#skrollr-body #diigo-ext-tutorial-wrapper.active #diigo-ext-tutorial-panel{transform:scale(1);}
body#skrollr-body #diigo-ext-tutorial-panel .diigo-ext-tutorial-btn{display:block;height:36px;width:36px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/back_icon.png");position:absolute;top:300px;transition:transfrom 200ms ease;}
body#skrollr-body #diigo-ext-tutorial-panel .diigo-ext-tutorial-btn:active{transform:scale(0.95);}
body#skrollr-body #diigo-ext-tutorial-panel #diigo-ext-tutorial-prev{left:-64px;display:none;}
body#skrollr-body #diigo-ext-tutorial-panel #diigo-ext-tutorial-next{-webkit-transform:rotate(180deg);right:-64px;}
body#skrollr-body #diigo-ext-tutorial-panel #diigo-ext-tutorial-next:active{transform:scale(0.95) rotate(180deg);}
body#skrollr-body #diigo-ext-tutorial-panel #diigo-ext-tutorial-close{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/close_icon.png");right:-64px;display:none;}
body#skrollr-body #diigo-ext-tutorial-banner{height:169px;border-radius:5px 5px 0 0;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/bg.png"),#4e8df7;color:white;position:relative;overflow:hidden;}
body#skrollr-body #diigo-ext-tutorial-banner-text{height:65px;position:relative;top:38px;transform:translate3d(0,-80px,0);opacity:0;transition:transform .5s cubic-bezier(0.77,0,0.175,1) .2s,opacity .5s cubic-bezier(0.77,0,0.175,1) .2s;}
body#skrollr-body #diigo-ext-tutorial-banner-text>div{font-size:19px;}
body#skrollr-body #diigo-ext-tutorial-banner-text span{line-height:47px;font-size:24px;font-weight:600;}
body#skrollr-body #diigo-ext-tutorial-wrapper::after{display:inline-block;height:100%;margin-left:-.05em;content:'';vertical-align:middle;}
body#skrollr-body #diigo-ext-tutorial-container{height:495px;border-radius:0 0 5px 5px;position:relative;}
body#skrollr-body .diigo-ext-tutorial-slide{visibility:hidden;opacity:0;position:absolute;left:0;right:0;transition:opacity 600ms ease-in-out;}
body#skrollr-body #diigo-ext-tutorial-wrapper.active .diigo-ext-tutorial-slide.active{visibility:visible;opacity:1;}
body#skrollr-body .diigo-ext-tutorial-slide .left,body#skrollr-body .diigo-ext-tutorial-slide .right{float:left;}
body#skrollr-body .diigo-ext-tutorial-slide .left{width:350px;}
body#skrollr-body .diigo-ext-tutorial-slide .right{width:400px;text-align:left;color:#757575;}
body#skrollr-body .diigo-ext-tutorial-slide .right>div{width:360px;line-height:20px;}
body#skrollr-body #diigo-tutorial-image1{height:347px;width:297px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/save.png");margin:22px 0 0 83px;}
body#skrollr-body #diigo-tutorial-image2{height:421px;width:186px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/screenshot.png");margin:22px 0 0 83px;}
body#skrollr-body #diigo-tutorial-image3{height:312px;width:537px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/highlighted.png");margin:75px 0 0 25px;}
body#skrollr-body .diigo-ext-tutorial-3 .left{width:581px;}
body#skrollr-body .diigo-ext-tutorial-3 .right{width:auto;}
body#skrollr-body .diigo-ext-tutorial-3 .right>div{width:194px;}
body#skrollr-body #diigo-tutorial-image4{height:302px;width:261px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/outliner.png");margin:83px 0 0 62px;}
body#skrollr-body .diigo-ext-tutorial-4 .left{width:350px;}
body#skrollr-body .diigo-ext-tutorial-4 .right{width:auto;}
body#skrollr-body .diigo-ext-tutorial-4 .right>div{width:375px;}
body#skrollr-body #diigo-ext-tutorial-elem1{position:absolute;left:138px;bottom:0;height:80px;width:74px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/spaceman.png");transform:translate3d(0,80px,0);transition:transform 600ms cubic-bezier(0.77,0,0.175,1);}
body#skrollr-body #diigo-ext-tutorial-elem2{position:absolute;right:97px;bottom:79px;height:48px;width:48px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/moon.png");transform:scale(0);transition:transform .5s cubic-bezier(0.77,0,0.175,1);}
body#skrollr-body #diigo-ext-tutorial-elem3{position:absolute;right:97px;bottom:-34px;height:118px;width:125px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/img/tutorial/rocket.png");transform:translate3d(100px,84px,0);transition:transform .5s cubic-bezier(0.77,0,0.175,1);}
body#skrollr-body #diigo-ext-tutorial-wrapper.active.step4 #diigo-ext-tutorial-elem1,body#skrollr-body #diigo-ext-tutorial-wrapper.active.step4 #diigo-ext-tutorial-elem2,body#skrollr-body #diigo-ext-tutorial-wrapper.active.step4 #diigo-ext-tutorial-elem3{transform:translate3d(0,0,0);transform:scale(1);}
body#skrollr-body #diigo-ext-tutorial-wrapper.active.step2 #diigo-ext-tutorial-elem1{transform:translate3d(0,0,0);}
body#skrollr-body #diigo-ext-tutorial-wrapper.active.step3 #diigo-ext-tutorial-elem2,body#skrollr-body #diigo-ext-tutorial-wrapper.active.step3 #diigo-ext-tutorial-elem1{transform:translate3d(0,0,0);}
body#skrollr-body #diigo-ext-tutorial-wrapper.active #diigo-ext-tutorial-banner-text{transform:translate3d(0,0,0);opacity:1;}
body#skrollr-body #diigo-code-clipper{height:24px;width:24px;background:red;position:absolute;opacity:.5;cursor:pointer;}
body#skrollr-body #diigo-code-clipped{position:absolute;display:inline-block;padding:0 4px;font-size:12px;border-radius:2px;text-align:center;color:white;background:rgba(0,0,0,.5);}
body#skrollr-body #diigo-code-clipper .clipped-area{display:none;}
body#skrollr-body #diigo-code-clipper.clipped{pointer-events:none;font-size:12px;display:inline-block;width:auto;}
body#skrollr-body #diigo-code-clipper.clipped .clipped-area{display:block;}
body#skrollr-body #diigo-code-clipper:hover{opacity:1;}
body#skrollr-body #d3df-sidebar{border:1px #ccc solid;z-index:99997;}
body#skrollr-body #d3df-sidebar div.heading{padding:3px;font-size:13px;border-top:1px #E8EEF7 solid;font-weight:bold;zoom:1;}
body#skrollr-body #d3df-sidebar div.popOut{width:16px;height:16px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/popout.gif) no-repeat scroll left top;cursor:pointer;}
body#skrollr-body #d3df-sidebar div.popOut.popIn{background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/popin.gif);}
body#skrollr-body #d3df-sidebar div.popOut.close{background-image:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/close1.gif);}
body#skrollr-body #d3df-sidebar div.heading a.add{background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv1.gif) no-repeat scroll left -172px;padding-left:18px;display:block;float:right;font-weight:normal;}
body#skrollr-body #d3df-sidebar a.togglePanel{background:transparent url(http://www.diigo.com/images/v2/eoc.gif) no-repeat scroll left top;display:block;float:right;width:16px;height:16px;}
body#skrollr-body #d3df-sidebar a.togglePanel.collapsed{background-position:left bottom;}
body#skrollr-body #d3df-sidebar ul,body#skrollr-body #d3df-sidebar ul li{list-style:none;overflow:hidden;zoom:1;}
body#skrollr-body #d3df-sidebar li.highlight a.highlight{overflow:hidden;height:24px;zoom:1;}
body#skrollr-body #d3df-sidebar ul.highlights li{margin:1px;}
body#skrollr-body #d3df-sidebar ul.comments li{margin:1px;padding:2px;}
body#skrollr-body #d3df-sidebar div.noComments{font-size:11px;text-align:center;padding:15px 5px;}
body#skrollr-body #d3df-sidebar p.commentBody,body#skrollr-body #d3df-sidebar p.commentBody a{font-size:11px;}
body#skrollr-body #d3df-sidebar a.avatar{float:left;margin-right:3px;}
body#skrollr-body #d3df-sidebar a.avatar img{padding:1px;border:1px #CCC solid;width:32px;height:32px;}
body#skrollr-body #d3df-sidebar .commentInfo{font-size:12px;}
body#skrollr-body #d3df-sidebar .commentInfo a{border-bottom:1px dotted #999;}
body#skrollr-body #d3df-sidebar a.highlight{line-height:24px;padding-left:18px;display:block;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv1.gif) no-repeat scroll left -192px;}
body#skrollr-body #d3df-sidebar a.floatNote{padding-left:16px;background:transparent url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/diigoletIconv1.gif) no-repeat scroll left -144px;}
body#skrollr-body #d3df-sidebar a.highlight .jumpTo{line-height:24px;padding-left:5px;font-size:12px;font-style:italic;}
body#skrollr-body #d3df-sidebar.themeDefault .bgColor1{background-color:#C3D9FF;}
body#skrollr-body #d3df-sidebar.themeDefault .bgColor2{background-color:#E8EEF7;}
body#skrollr-body #d3df-sidebar.themeDefault .bgColor3{background-color:#FFF;}
body#skrollr-body #d3df-sidebar.themeDefault .color1{color:#999;}
body#skrollr-body #d3df-sidebar.themeDefault .color2{color:#333;}
body#skrollr-body.diigoHiPen-yellow{cursor:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/highlighter-orange.cur) 4 15,text!important;}
body#skrollr-body.diigoHiPen-blue{cursor:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/highlighter-blue.cur) 4 15,auto!important;}
body#skrollr-body.diigoHiPen-green{cursor:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/highlighter-green.cur) 4 15,text!important;}
body#skrollr-body.diigoHiPen-pink{cursor:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/ietoolbar-images/highlighter-pink.cur) 4 15,text!important;}
body#skrollr-body .diigolet.notice{font:bold 13px/1.5 Helvetica,Arial,sans-serif;position:fixed;top:5px;left:0;width:100%;text-align:center;z-index:2147483647;height:1px;-webkit-animation:fadeIn 400ms ease;}
body#skrollr-body .diigolet.notice>div{border:1px solid #fad42e;background:#fea;border-radius:5px;color:#000;display:inline-block;padding:5px 10px 5px 5px;-webkit-box-shadow:rgba(0,0,0,0.3) 0 1px 1px;}
body#skrollr-body .diigolet.notice>div>b{display:inline-block;height:16px;width:16px;margin:2px 3px 0 0;background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) 0 -80px no-repeat;float:left;}
body#skrollr-body .diigolet.notice>div>p>a{font-size:12px;}
body#skrollr-body .diigolet.notice>div>p{float:left;max-width:420px;}
body#skrollr-body .diigolet.notice>div.alert{background:#fef6f3;border-color:#cd0a0a;}
body#skrollr-body .diigolet.notice>div.alert p #retry{margin-left:3px;text-decoration:underline;}
body#skrollr-body .diigolet.notice>div.alert>b{background-position:-16px -80px;}
body#skrollr-body .diigolet.notice>div.info>b{background-position:-32px -80px;}
body#skrollr-body .diigolet.notice>div.wait>b{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/processing.gif) no-repeat scroll left 0 transparent;}
body#skrollr-body .diigolet.notice div #close{display:block;height:12px;width:12px;background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/close.png);float:right;margin-left:10px;margin-top:3px;}
body#skrollr-body .diigolet.notice div #close:hover{background-position:0 -12px;}
body#skrollr-body #diigolet-panel-panel{z-index:2147483641;}
body#skrollr-body #diigolet-panel-panel.notSignedIn .signedIn{display:none;}
body#skrollr-body #diigolet-panel-panel.signedIn .notSignedIn{display:none;}
body#skrollr-body #diigolet-panel-panel{height:36px;border-top-left-radius:19px;border-bottom-left-radius:19px;font:normal 12px/1.5 Helvetica,Arial,sans-serif;position:fixed;left:5px;top:5px;background-color:#fff;white-space:nowrap;border:1px solid #ccc;-webkit-user-select:none;background-clip:content-box;box-shadow:0 2px 10px rgba(0,0,0,.2);}
body#skrollr-body #diigolet-panel-panel:hover #diigolet-panel-space{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -379px 0 no-repeat;opacity:.4;}
body#skrollr-body #diigolet-panel-panel.fold #diigolet-panel-logo{opacity:1;width:28px;}
body#skrollr-body #diigolet-panel-panel.fold #diigolet-panel-main{width:0;border-radius:0;}
body#skrollr-body #diigolet-panel-panel.orphanHighlight.fold #diigolet-panel-logo{background-position:-84px 0;}
body#skrollr-body #diigolet-panel-panel.orphanHighlight.fold #diigolet-panel-logo:hover{background-position:-112px 0;}
body#skrollr-body .clearfloat:after{display:block;clear:both;content:"";visibility:hidden;height:0;}
body#skrollr-body .clearfloat{zoom:1;}
body#skrollr-body #diigolet-panel-main{height:36px;display:inline-block;background-color:rgba(255,255,255,1);border-radius:19px 0 0 19px;overflow:hidden;-webkit-transition:left 100ms ease-in-out;}
body#skrollr-body #diigolet-panel-logo{display:inline-block;width:0;height:36px;border-top-left-radius:19px;border-bottom-left-radius:19px;background-image:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/di.png");background-position:0 0;background-color:#fff;opacity:0;cursor:pointer;}
body#skrollr-body #diigolet-panel-logo:hover{background-position:-28px 0;}
body#skrollr-body #diigolet-panel-space{width:12px;height:36px;display:inline-block;background-color:#fff;}
body#skrollr-body #diigolet-panel-panel .diigolet-panel-btn{height:36px;float:left;}
body#skrollr-body #diigolet-panel-panel .diigolet-panel-btn>b{height:36px;width:36px;display:block;cursor:pointer;margin:0 auto;-webkit-transition:background-color 200ms ease;}
body#skrollr-body #diigolet-panel-panel .diigolet-panel-btn>b:hover{background-color:#E7F0FF;}
body#skrollr-body #diigolet-panel-panel .diigolet-panel-btn>b:active{-webkit-transform:scale(.9);}
body#skrollr-body #diigolet-panel-fold{height:36px;float:left;cursor:pointer;width:19px;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") 0 0 no-repeat;}
body#skrollr-body #diigolet-panel-fold:hover{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -38px 0 no-repeat;}
body#skrollr-body #diigolet-panel-Highlight{width:48px;}
body#skrollr-body #diigolet-panel-btnHighlight{width:34px;height:36px;float:right;}
body#skrollr-body #diigolet-panel-btnHighlight>b{height:36px;width:36px;display:block;cursor:pointer;-webkit-transition:background-color 200ms ease,border-radius 200ms ease;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -105px 0 no-repeat;}
body#skrollr-body #diigolet-panel-Highlight.pen #diigolet-panel-btnHighlight>b{height:36px;width:36px;margin:0;}
body#skrollr-body #diigolet-panel-Highlight:not(.pen) #diigolet-panel-btnHighlight>b:hover{background-color:#E7F0FF!important;}
body#skrollr-body #diigolet-panel-btnHighlight>b:active{-webkit-transform:scale(.9);}
body#skrollr-body #diigolet-panel-Highlight.pen #diigolet-panel-btnHighlight>b{background-color:#E7F0FF;-webkit-transform:scale(0.9);}
body#skrollr-body #diigolet-panel-btnHighlight.yellow>b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -73px 0 no-repeat;}
body#skrollr-body #diigolet-panel-btnHighlight.blue>b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -105px 0 no-repeat;}
body#skrollr-body #diigolet-panel-btnHighlight.green>b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -137px 0 no-repeat;}
body#skrollr-body #diigolet-panel-btnHighlight.pink>b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -169px 0 no-repeat;}
body#skrollr-body #diigolet-panel-hightlight-dropdown.yellow>b{background-color:#ffb000;}
body#skrollr-body #diigolet-panel-hightlight-dropdown.blue>b{background-color:#39abed;}
body#skrollr-body #diigolet-panel-hightlight-dropdown.green>b{background-color:#7c0;}
body#skrollr-body #diigolet-panel-hightlight-dropdown.pink>b{background-color:#f6b;}
body#skrollr-body #diigolet-panel-hightlight-dropdown{width:14px;height:36px;float:right;background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -360px 0 no-repeat;cursor:pointer;}
body#skrollr-body #diigolet-panel-hightlight-dropdown:hover{background-color:#E7F0FF;}
body#skrollr-body #diigolet-panel-hightlight-dropdown>b{height:5px;width:5px;border-radius:12px;display:block;margin-top:16px;margin-left:5px;cursor:pointer;}
body#skrollr-body #diigolet-panel-btnStickyNote{width:42px;}
body#skrollr-body #diigolet-panel-btnStickyNote b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -234px -1px no-repeat;}
body#skrollr-body #diigolet-panel-btnBookmark{width:42px;}
body#skrollr-body #diigolet-panel-btnBookmark b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -296px -1px no-repeat;}
body#skrollr-body #diigolet-panel-btnBookmark.diigo-research-mode b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -485x -1px no-repeat;}
body#skrollr-body #diigolet-panel-btnBookmark.saved b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -328px -1px no-repeat;}
body#skrollr-body #diigolet-panel-btnAnnotationList b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -419px -1px no-repeat;}
body#skrollr-body #diigolet-panel-panel.orphanHighlight #diigolet-panel-btnAnnotationList b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -451px -1px no-repeat;}
body#skrollr-body #diigolet-panel-orphanHighlight{width:46px;}
body#skrollr-body #diigolet-panel-orphanHighlight b{background:url("chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/toolbar-icon.png") -266px -1px no-repeat;}
body#skrollr-body #diigolet-panel-colorPicker{display:none;position:absolute;left:15px;top:41px;width:91px;background-color:#fff;box-shadow:0 1px 4px rgba(0,0,0,.35);border-radius:2px;padding:5px 0;-webkit-animation:diigo-dropdown .15s ease-in 1;}
body#skrollr-body #diigolet-panel-colorPicker.dropdownShown{display:block;}
body#skrollr-body #diigolet-panel-colorPicker-arrow{border:5px solid;border-top-color:transparent;border-right-color:transparent;border-bottom-color:#fff;border-left-color:transparent;position:absolute;left:40px;top:-9px;}
body#skrollr-body #diigolet-panel-colorPicker li{font-weight:normal;display:block;padding-right:10px!important;padding-left:10px!important;text-decoration:none!important;line-height:26px;height:26px;color:#434343;min-width:60px;width:71px;background:none!important;border:none!important;-webkit-transition:background-color 200ms ease;}
body#skrollr-body #diigolet-panel-colorPicker li:hover{background-color:#e8e8e8!important;color:#434343!important;text-decoration:none!important;}
body#skrollr-body #diigolet-panel-colorPicker li span{display:inline-block;width:12px;height:12px;border-radius:7px;margin-right:5px;vertical-align:middle;margin-bottom:3px;}
body#skrollr-body #diigolet-panel-colorPicker li span b{width:4px;height:4px;background:#606060;margin-top:4px;margin-left:4px;border-radius:2px;}
body#skrollr-body #diigolet-panel-colorPicker li.selected span b{display:block;}
body#skrollr-body #diigolet-panel-colorPicker li.yellow span{background:#fde200;border:1px solid #b0a224;}
body#skrollr-body #diigolet-panel-colorPicker li.blue span{background:#7db3f9;border:1px solid #63799a;}
body#skrollr-body #diigolet-panel-colorPicker li.green span{background:#86ca25;border:1px solid #718b49;}
body#skrollr-body #diigolet-panel-colorPicker li.pink span{background:#ff9b9a;border:1px solid #ae657a;}
body#skrollr-body .diigolet .moreActionShare b{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) 0 -96px no-repeat;}
body#skrollr-body #diigolet-dialog-share{background-color:#fcfbf7;border-radius:2px;font:normal 13px/1.5 Helvetica,Arial,sans-serif;position:fixed;left:5px;top:7px;box-shadow:0 1px 3px rgba(0,0,0,.08);white-space:nowrap;width:520px;z-index:2147483646;display:block;}
body#skrollr-body #diigolet-dialog-share *{white-space:normal;}
body#skrollr-body #diigolet-dialog-share-title{height:30px;vertical-align:middle;background-color:#39baf6;line-height:30px;padding:0 10px;font-size:14px;color:white;text-align:left;border-radius:2px 2px 0 0;display:block;}
body#skrollr-body #diigolet-dialog-share-closeBtn{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/images/win-close.png) 50% 50% no-repeat;float:right;height:16px;margin-left:10px;width:16px;margin-top:7px;}
body#skrollr-body #diigolet-dialog-share-content{border-radius:0 0 2px 2px;border-width:1px 1px 1px 1px;border-color:rgba(0,0,0,.08);border-style:solid;display:block;}
body#skrollr-body #diigolet-dialog-share-social{padding:10px;}
body#skrollr-body #diigolet-dialog-share-social .social-item{height:50px;width:100px;border-radius:3px;background:red;margin:10px 20px 10px 0;display:block;float:left;}
body#skrollr-body #diigolet-share-shareToTabs{background-color:#fcfbf7;list-style-type:none;padding:0 5px;margin:0;height:30px;line-height:30px;border-left:1px solid rgba(0,0,0,.08);border-right:1px solid rgba(0,0,0,.08);}
body#skrollr-body #diigolet-share-shareToTabs li{display:inline-block;line-height:22px;height:24px;margin-top:6px;}
body#skrollr-body #diigolet-share-shareToTabs li a{text-decoration:none;border-bottom-color:#3669a8;border-top-left-radius:5px;border-top-right-radius:5px;color:#000;opacity:.8;display:block;padding:0 5px;}
body#skrollr-body #diigolet-share-shareToTabs a:hover{opacity:1;}
body#skrollr-body #diigolet-share-shareToTabs a.current{border-radius:2px 2px 0 0;border-width:1px 1px 0 1px;border-color:rgba(0,0,0,.08);border-style:solid;border-bottom:1px solid #fcfbf7;color:#000;opacity:1;z-index:0;position:relative;top:1px;}
body#skrollr-body #diigolet-share-shareToTabs a.current:hover{color:#222;}
body#skrollr-body #diigolet-share-shareToTabs li b{display:inline-block;width:16px;height:16px;vertical-align:text-bottom;margin-right:3px;}
body#skrollr-body .diigolet .shareToTwitter b{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) -16px -96px no-repeat;}
body#skrollr-body .diigolet .shareToFacebook b{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) -32px -96px no-repeat;}
body#skrollr-body .diigolet .shareToGplus b{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) -48px -96px no-repeat;}
body#skrollr-body .diigolet .shareToEmail b{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) 0 -112px no-repeat;}
body#skrollr-body .diigolet .getAnnotatedLink b{background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) -16px -112px no-repeat;}
body#skrollr-body .diigolet .twitterDesc{color:#777;font-size:13px;line-height:20px;}
body#skrollr-body #diigolet-twitter-saveBtn{display:block;line-height:24px;cursor:pointer;text-align:center;color:white;border-radius:2px;border:1px solid #066ec1;font-size:12px;text-decoration:none;border-radius:2px;border:1px solid #85a0a6;color:#85a0a6;font-size:12px;text-align:center;height:20px;width:50px;line-height:20px;float:right;}
body#skrollr-body #diigolet-twitter-saveBtn:active{background:#85a0a6;color:#fff;}
body#skrollr-body #diigolet-twitter-cancelBtn{color:#999;height:12px;font-size:12px;margin:1px 8px 0 6px;text-decoration:none;float:right;}
body#skrollr-body #diigolet-twitter-cancelBtn:hover{text-decoration:underline;}
body#skrollr-body #diigolet-email-saveBtn{display:block;line-height:24px;cursor:pointer;text-align:center;color:white;border-radius:2px;border:1px solid #066ec1;font-size:12px;text-decoration:none;border-radius:2px;border:1px solid #85a0a6;color:#85a0a6;font-size:12px;text-align:center;height:20px;width:50px;line-height:20px;float:right;margin-top:4px;}
body#skrollr-body #diigolet-email-saveBtn:active{background:#85a0a6;color:#fff;}
body#skrollr-body #diigolet-email-cancelBtn{color:#999;height:12px;font-size:12px;margin:6px 14px 0 0;text-decoration:none;float:right;}
body#skrollr-body #diigolet-email-cancelBtn:hover{text-decoration:underline;}
body#skrollr-body #diigolet-annotatedLink-saveBtn{display:block;line-height:24px;cursor:pointer;text-align:center;color:white;border-radius:2px;border:1px solid #066ec1;font-size:12px;text-decoration:none;border-radius:2px;border:1px solid #85a0a6;color:#85a0a6;font-size:12px;text-align:center;height:20px;width:50px;line-height:20px;float:right;}
body#skrollr-body #diigolet-annotatedLink-saveBtn:active{background:#85a0a6;color:#fff;}
body#skrollr-body #diigolet-annotatedLink-cancelBtn{color:#999;height:12px;font-size:12px;margin:2px 8px 0 6px;text-decoration:none;float:right;}
body#skrollr-body #diigolet-annotatedLink-cancelBtn:hover{text-decoration:underline;}
body#skrollr-body #diigolet-share-twitterLeftChars{color:#999;float:right;font-size:20px;font-weight:700;line-height:20px;}
body#skrollr-body #diigolet-share-twitterLeftChars.full{color:#F00;}
body#skrollr-body #diigolet-dialog-share .inputTxt{border:1px solid #7F9DB9;font:normal 12px/1.5 Arial,Helvetica,sans-serif;border:1px solid #d7d7d7;-webkit-transition:border-color 200ms ease;outline:none;}
body#skrollr-body #diigolet-dialog-share .inputTxt:focus{border:1px solid #AAA;}
body#skrollr-body #diigolet-dialog-share-twitterMsg{height:54px;width:492px;}
body#skrollr-body #diigolet-dialog-share .buttonRow{margin-top:5px;text-align:right;display:block;}
body#skrollr-body #diigolet-dialog-share .buttonRow input{margin-left:5px;padding:1px 6px;}
body#skrollr-body #diigolet-dialog-share input.defaultAction{font-weight:700;}
body#skrollr-body #diigolet-dialog-share-twitter{padding:10px;display:block;}
body#skrollr-body #diigolet-dialog-share-facebook{padding:5px;font-size:20px;height:100px;line-height:100px;text-align:center;}
body#skrollr-body #diigolet-dialog-share-gPlus{padding:5px;font-size:20px;height:100px;line-height:100px;text-align:center;}
body#skrollr-body #diigolet-dialog-share-gBuzz iframe{border:none;height:340px;width:100%;overflow:hidden;}
body#skrollr-body #diigolet-dialog-share-email{padding:10px;display:block;}
body#skrollr-body #diigolet-dialog-share-email>table{width:100%;border-width:0;margin-bottom:5px;}
body#skrollr-body #diigolet-dialog-share-email>table td{padding:2px 0;}
body#skrollr-body #diigolet-dialog-share-email label{font-weight:700;}
body#skrollr-body #diigolet-dialog-share-email-to,body#skrollr-body #diigolet-dialog-share-email-subject{width:100%;}
body#skrollr-body #diigolet-dialog-share-email-message{height:72px;width:100%;}
body#skrollr-body #diigolet-dialog-share-email-quotes-checker{font-weight:400!important;float:right;}
body#skrollr-body #diigolet-dialog-share-email-quotes-checker input{margin-right:2px;vertical-align:text-bottom;}
body#skrollr-body #diigolet-dialog-share-email-quotes{border:1px solid #bbb;border-radius:3px;width:100%;max-height:150px;overflow-y:scroll;}
body#skrollr-body #diigolet-aidlog-share-email-quotes-content{margin:5px 10px 10px 10px;}
body#skrollr-body #diigolet-dialog-share-annotatedLink{padding:10px;display:block;}
body#skrollr-body .diigolet .annotatedLinkInfo{border:1px solid #fad42e;background:#fea;border-radius:5px;color:#000;display:inline-block;padding:0 0 0 20px!important;position:relative;margin-bottom:10px!important;}
body#skrollr-body .diigolet .annotatedLinkInfo b{display:inline-block;height:16px;width:16px;margin-right:3px;background:url(chrome-extension://pnhplgjpclknigjpccbcnmicgcieojbh/diigolet/chrome-panel-images/icons.png) -32px -80px no-repeat;position:absolute;left:1px;top:1px;}
body#skrollr-body #diigolet-dialog-share-annotatedLink-value{font-weight:700!important;font-size:13px!important;padding:2px;width:496px;}
body#skrollr-body #diigolet-dialog-share-annotatedLink-value.loading{color:#ccc;font-style:italic;}
body#skrollr-body #diigolet-dialog-share-annotatedLink-optLinks{float:left;}
body#skrollr-body .diigolet .autocompleteContacts{border:1px solid #d9d9d9;border-top-color:#999;border-left-color:#999;width:380px;}
body#skrollr-body .diigolet .recInput{font:12px verdana;border-width:0;float:left;margin:2px;padding-top:2px;}
body#skrollr-body .diigolet .recItem{border:1px solid #7B9EBD;padding:0 2px;background-color:#F0F5FE;float:left;margin:2px 2px 0 0;}
body#skrollr-body .diigolet .recInputSizer{position:absolute;visibility:hidden;left:0;bottom:0;font:11px verdana;}
body#skrollr-body .diigolet .accTip{position:absolute;border:1px solid #ddd;border-top:none;background-color:#f5f5f5;font-size:11px;color:#777;text-align:left;padding:2px 0;text-indent:5px;z-index:8998;}
body#skrollr-body .diigolet .accNotice{position:absolute;border:1px solid #ffd324;border-top:none;background-color:#fff6bf;font-size:11px;color:#600;text-align:left;padding:2px 0;text-indent:5px;z-index:8999;}
body#skrollr-body .diigolet .accList{position:absolute;border:1px solid #999;border-top:none;background-color:#fff;font:10px verdana;color:#777;text-align:left;z-index:9000;line-height:18px;}
body#skrollr-body .diigolet .accList .cItem{border-bottom:1px solid #ddd;background-color:#fff;cursor:pointer;padding:2px;color:#333;}
body#skrollr-body .diigolet .accList .cItem b{font-size:11px;font-weight:normal;color:#000;}
body#skrollr-body .diigolet .accList .cItem i,body#skrollr-body .recItem i{font-size:7pt;color:#090;font-style:normal;margin-right:2px;}
body#skrollr-body .diigolet .accList div strong{background-color:#FFFADB;padding:0 2px;}
body#skrollr-body .diigolet .accList div.hover{background-color:#E0ECFF;text-decoration:none;}
body#skrollr-body .diigolet .recItem a{color:#999;font-family:Verdana,Arial,Helvetica,sans-serif;font-size:12px;font-weight:bold;line-height:16px;margin:0 1px 0 3px;}
body#skrollr-body .diigolet .recItem a:hover{color:#333;text-decoration:none;}
body#skrollr-body .diigolet .cItem span.extraDesc{float:none;font-weight:normal;color:#777;margin-left:10px;font-style:italic;}
body#skrollr-body .diigolet .cItem span.extraDesc .keywordStrong{color:#000;font-style:italic;background-color:#fff;}
body#skrollr-body .diigolet .cItem span.keywordStrong{float:none;font-weight:bold;}
</style><link rel="preload" as="style" href="https://c.disquscdn.com/next/embed/styles/lounge.9974049bf7b0591e5d4f055cb67f3ee3.css"><link rel="preload" as="script" href="https://c.disquscdn.com/next/embed/common.bundle.880980e048a2432334f13013030456ac.js"><link rel="preload" as="script" href="https://c.disquscdn.com/next/embed/lounge.bundle.7ca5005d1897180d07d928e89d2628be.js"><link rel="preload" as="script" href="https://disqus.com/next/config.js"><style type="text/css" id="cliqz-adblokcer-css-rules"> :root .adsbox {display:none !important;}</style><script type="text/javascript" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/styles.js"></script><script type="text/javascript" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/highlight.pack.js"></script></head>
<body class="minibar ng-scope" ng-controller="MainCtrl" id="skrollr-body">
<div id="fb-root"></div>

<!-- we only need webapp_component when request by login user -->

<div class="navbar menu_new_v2" id="main-header" style="margin-bottom:0px;">
<div class="navbar-inner">
<div class="container">
<div class="btn btn-navbar" data-target=".nav-collapse" data-toggle="collapse">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</div>
<a class="brand" href="https://www.codementor.io/">
<img width="140" height="19" alt="Codementor" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/codementor-logo-eea4ea58e817c09d61c9a97a536ea2fd2c683e9430d83908c4c0df3f9e99a10b.png">
</a>
<!-- Unsign Up User -->
<div class="nav-collapse collapse">
  <ul class="nav" itemscope="" itemtype="http://www.schema.org/SiteNavigationElement">
<li class="showMobile" itemprop="name">
<a href="https://www.codementor.io/experts" itemprop="url">Find a mentor</a>
</li>
<li class="learnTopMenu hideMobile" itemprop="name">
<a class="learnTopLink" href="https://www.codementor.io/experts" itemprop="url">
Find a mentor
<b class="caret"></b>
</a>
<ul aria-labelledby="dropdownMenu" class="learnSecondMenu expert-second-menu" role="menu">
<li class="item subMenuItem">
<a class="sublink secondItem" href="https://www.codementor.io/experts/web-programming" tabindex="-1">
Web Programming
</a>
<div class="learnThirdMenu expert-third-menu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/experts/web-programming" tabindex="-1">
Web Programming
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/ruby-experts" tabindex="-1">
Ruby
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/javascript-experts" tabindex="-1">
JavaScript
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/angularjs-experts" tabindex="-1">
AngularJS
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/python-experts" tabindex="-1">
Python
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/php-experts" tabindex="-1">
PHP
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/html_css-experts" tabindex="-1">
HTML/CSS
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/jquery-experts" tabindex="-1">
jQuery
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/ruby-on-rails-experts" tabindex="-1">
Ruby on Rails
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/django-experts" tabindex="-1">
Django
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/nodejs-experts" tabindex="-1">
Node.js
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/coffeescript-experts" tabindex="-1">
CoffeeScript
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/emberjs-experts" tabindex="-1">
Ember.js
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/backbonejs-experts" tabindex="-1">
Backbone.js
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/meteor-experts" tabindex="-1">
Meteor
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/flask-experts" tabindex="-1">
Flask
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/scala-experts" tabindex="-1">
Scala
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/reactjs-experts" tabindex="-1">
React
</a>
</div>
</div>
</div>
</div>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem" href="https://www.codementor.io/experts/coding" tabindex="-1">
Code
</a>
<div class="learnThirdMenu expert-third-menu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/experts/coding" tabindex="-1">
Code
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/ruby-experts" tabindex="-1">
Ruby
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/javascript-experts" tabindex="-1">
JavaScript
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/php-experts" tabindex="-1">
PHP
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/python-experts" tabindex="-1">
Python
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/java-experts" tabindex="-1">
Java
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/c_sharp-experts" tabindex="-1">
C#
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/c_plus_plus-experts" tabindex="-1">
C++
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/go-experts" tabindex="-1">
Go
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/c-experts" tabindex="-1">
C
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/dot_net-experts" tabindex="-1">
.Net
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/haskell-experts" tabindex="-1">
Haskell
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/perl-experts" tabindex="-1">
Perl
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/erlang-experts" tabindex="-1">
Erlang
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/matlab-experts" tabindex="-1">
Matlab
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/debugging-experts" tabindex="-1">
Debugging
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/crystal-experts" tabindex="-1">
Crystal
</a>
</div>
</div>
</div>
</div>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem" href="https://www.codementor.io/experts/mobile-app-programming" tabindex="-1">
Mobile App Programming
</a>
<div class="learnThirdMenu expert-third-menu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/experts/mobile-app-programming" tabindex="-1">
Mobile App Programming
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/ios-experts" tabindex="-1">
iOS
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/android-experts" tabindex="-1">
Android
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/swift-experts" tabindex="-1">
Swift
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/phonegap-experts" tabindex="-1">
PhoneGap
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/cordova-experts" tabindex="-1">
Cordova
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/ionic-experts" tabindex="-1">
Ionic
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/titanium-experts" tabindex="-1">
Titanium
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/sencha-experts" tabindex="-1">
Sencha
</a>
</div>
</div>
</div>
</div>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem" href="https://www.codementor.io/experts/design" tabindex="-1">
Design/UX
</a>
<div class="learnThirdMenu expert-third-menu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/experts/design" tabindex="-1">
Design/UX
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/html_css-experts" tabindex="-1">
HTML/CSS
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/css-experts" tabindex="-1">
CSS
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/sass-experts" tabindex="-1">
Sass
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/twitter-experts" tabindex="-1">
Twitter
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/famous-experts" tabindex="-1">
Famo.us
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/kendo-ui-experts" tabindex="-1">
Kendo UI
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/responsive-experts" tabindex="-1">
Responsive
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/foundation-experts" tabindex="-1">
Foundation
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/photoshop-experts" tabindex="-1">
Photoshop
</a>
</div>
</div>
</div>
</div>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem" href="https://www.codementor.io/experts/devops" tabindex="-1">
Database/Operations
</a>
<div class="learnThirdMenu expert-third-menu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/experts/devops" tabindex="-1">
Database/Operations
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/server-experts" tabindex="-1">
Server
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/devops-experts" tabindex="-1">
DevOps
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/mysql-experts" tabindex="-1">
MySQL
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/sql-experts" tabindex="-1">
SQL
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/mongodb-experts" tabindex="-1">
MongoDB
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/hadoop-experts" tabindex="-1">
Hadoop
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/apache-experts" tabindex="-1">
Apache
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/linux-experts" tabindex="-1">
Linux
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/aws-experts" tabindex="-1">
AWS
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/heroku-experts" tabindex="-1">
Heroku
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/database-experts" tabindex="-1">
Database
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/security-experts" tabindex="-1">
Security
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/azure-experts" tabindex="-1">
Azure
</a>
</div>
</div>
</div>
</div>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem" href="https://www.codementor.io/experts/development-process" tabindex="-1">
Development Process/Tools
</a>
<div class="learnThirdMenu expert-third-menu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/experts/devops" tabindex="-1">
Development Process/Tools
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/git-experts" tabindex="-1">
Git
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/devops-experts" tabindex="-1">
DevOps
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/wordpress-experts" tabindex="-1">
Wordpress
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/drupal-experts" tabindex="-1">
Drupal
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/joomla-experts" tabindex="-1">
Joomla
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/seo-experts" tabindex="-1">
SEO
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/vim-experts" tabindex="-1">
Vim
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/bower-experts" tabindex="-1">
Bower
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/machine-learning-experts" tabindex="-1">
Machine Learning
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/xcode-experts" tabindex="-1">
Xcode
</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/jenkins-experts" tabindex="-1">
Jenkins
</a>
</div>
</div>
</div>
</div>
</li>

<li class="divider"></li>
<li class="item subMenuItem">
<a class="sublink secondItem">
Programming Tutors
</a>
<div class="learnThirdMenu expert-third-menu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/tutors" tabindex="-1">
Programming Tutors
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span6">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/tutors/java-tutors" tabindex="-1">
Java
</a>
</div>
</div>
<div class="span6">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/tutors/c-sharp-tutors" tabindex="-1">
C#
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span6">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/tutors/python-tutors" tabindex="-1">
Python
</a>
</div>
</div>
<div class="span6">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/tutors/computer-science-tutors" tabindex="-1">
Computer Science
</a>
</div>
</div>
</div>
</div>
</li>

</ul>
</li>

<li class="showMobile" itemprop="name">
<a href="https://www.codementor.io/developers" itemprop="url">
Find a freelancer
</a>
</li>
<li class="learnTopMenu hideMobile" itemprop="name">
<a class="learnTopLink" href="https://www.codementor.io/developers" itemprop="url">
Find a freelancer
<b class="caret"></b>
</a>
<ul aria-labelledby="dropdownMenu" class="learnSecondMenu codementorx-second-menu" role="menu">
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/java-developers" tabindex="-1">
Java Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/python-developers" tabindex="-1">
Python Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/android-developers" tabindex="-1">
Android Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/ios-developers" tabindex="-1">
iOS Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/php-developers" tabindex="-1">
PHP Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/frontend-developers" tabindex="-1">
Frontend Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/backend-developers" tabindex="-1">
Backend Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/web-developers" tabindex="-1">
Web Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/software-developers" tabindex="-1">
Software Developers
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/wordpress-developers" tabindex="-1">
Wordpress Developers
</a>
</li>
</ul>
</li>

<li class="showMobile" itemprop="name">
<a href="https://www.codementor.io/community" itemprop="url">Community</a>
</li>
<li class="learnTopMenu hideMobile" itemprop="name">
<a class="learnTopLink" href="https://www.codementor.io/community" itemprop="url" style="cursor:pointer">
Community
<b class="caret"></b>
</a>
<ul aria-labelledby="dropdownMenu" class="learnSecondMenu learn-to-code-second-menu" role="menu" style="height:300px">
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/collections" tabindex="-1">
Collections
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/community" tabindex="-1">
Trending Posts
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/community/editors-choice" tabindex="-1">
Editors' Choice
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem individual-link" href="https://www.codementor.io/community/new" tabindex="-1">
New Posts
</a>
</li>
<li class="item subMenuItem">
<a class="sublink secondItem" href="https://www.codementor.io/community" tabindex="-1">
Topics
</a>
<div class="learnThirdMenu">
<div class="row-fluid">
<div class="span12">
<div class="header-item">
<a class="topic-btn" href="https://www.codementor.io/community" tabindex="-1">
Topics
</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/javascript">JavaScript</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/python">Python</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/ios">iOS</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/swift">Swift</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/reactjs">React</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/angularjs">Angular</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/nodejs">NodeJs</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/ruby-on-rails">Ruby on Rails</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/data-science">Data Science</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/devops">DevOps</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/php">PHP</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/java">Java</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/android">Android</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/ruby">Ruby</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/c_sharp">C#</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/apache-spark">Spark</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/css">CSS</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/c_plus_plus">C++</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/testing">Testing</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/go">GO</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/sql">SQL</a>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/docker">Docker</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/meteor">Meteor</a>
</div>
</div>
<div class="span4">
<div class="item subMenuItem">
<a class="thirdlink" href="https://www.codementor.io/community/topic/django">Django</a>
</div>
</div>
</div>
</div>
</li>
</ul>
</li>

<li itemprop="name">
<a href="https://www.codementor.io/howitworks" itemprop="url">How it Works</a>
</li>
<li class="hideTablet" itemprop="name">
<a href="https://www.codementor.io/mentor/apply" itemprop="url">
<b>Become a Codementor</b>
</a>
</li>
</ul>

  <ul class="nav pull-right">
<li>
<a class="highlight red-btn" data-target="#signup-modal" data-toggle="modal" id="headerSignUpBtn">Sign Up</a>
</li>
<li itemprop="name">
<a href="https://www.codementor.io/login" itemprop="url">Log In</a>
</li>
</ul>


</div>
</div>
</div>
</div>



<div id="main" role="main" style="margin-top:0px;">

<div class="alerts ng-scope" ng-controller="AlertCtrl as alertCtrl">
<!-- ngRepeat: alert in Alert.alerts -->
</div>

<div class="helpListing ng-scope" ng-controller="helpListingShowCtrl as helpListingShow">
<div class="signUpTab skrollable skrollable-between" data--51-top="display:block;" data-bottom-top="display:none;position:fixed;" data-emit-events="" style="display: none; position: fixed;">
<div class="customizeContainer">
<div class="row-fluid">
<div class="span10 offset1">
<div class="tabTitle">
<span class="hideMobile">
Get notified about new tutorials
</span>
<a class="actionLink" href="https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps#signup-modal" id="headerSignUpBtn" ng-click="popReceiveTutorialForm()">
RECEIVE NEW TUTORIALS
</a>
</div>
</div>
</div>
</div>
</div>
<div class="firstPart">
<div class="customizeContainer">
<div class="row-fluid topRow">
<div class="span8">
<div class="pageBreadCrumb">
<div :xmlns:v="http://rdf.data-vocabulary.org/#" class="innerBreadcrumb">
<span typeof="v:Breadcrumb">
<a class="breadLink" href="https://www.codementor.io/learn" property="v:title" rel="v:url">
Learning Center
</a>
</span>
<span class="sign">
&nbsp;›&nbsp;
</span>
<span typeof="v:Breadcrumb">
<a class="breadLink" href="https://www.codementor.io/tips">
Quick Tips
</a>
</span>
<span class="sign">
&nbsp;›&nbsp;
</span>
<span typeof="v:Breadcrumb">
<a class="breadLink" href="https://www.codementor.io/dckc/tips">
Dan Connolly's Quick Tips
</a>
</span>
<span class="sign">
&nbsp;›&nbsp;
</span>
<span class="lastLink">
Learning to make stuff with...
</span>
</div>
</div>
<h1 class="helpTitle">
Learning to make stuff with computers: from CPUs to Haskell Web Apps
</h1>
<div class="row-fluid">
<div class="span12">
<div class="content">
<div class="expertise">
<a class="badge customizeBadge" href="https://www.codementor.io/haskell-experts">
Haskell
</a>
<a class="badge customizeBadge" href="https://www.codementor.io/animation-experts">
Animation
</a>
<a class="badge customizeBadge" href="https://www.codementor.io/assembly-experts">
Assembly
</a>
<a class="badge customizeBadge" href="https://www.codementor.io/canvas-experts">
Canvas
</a>
<a class="badge customizeBadge" href="https://www.codementor.io/computer-graphics-experts">
Computer graphics
</a>
</div>
</div>
</div>
</div>
</div>
<div class="span4 rightSideBar">
<div class="help-listing rightSideBarWapper ng-scope" ng-controller="rightSideBarCtrl as rsbc" side-bar-stick-at-bottom="" style="position: fixed; top: 137px; z-index: 4;">
<a class="free-trial-badge" href="https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps#">
First 15 Minutes Free
</a>
<div class="actionCard">
<div class="topCard">
<img class="img-circle" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/photo.jpg" alt="Nk5o2i1aqu2grrdrvd4m">
<a class="display-name" href="https://www.codementor.io/dckc">
Dan Connolly
</a>
<div class="rating">
<span> ★ </span>  <span> ★ </span>  <span> ★ </span>  <span> ★ </span>  <span> ★ </span> 
</div>
<a class="btn btn-success messageBtn" href="https://www.codementor.io/dckc">
View Profile
</a>
</div>
</div>
<div class="restInfo">
<div class="sessionGiven info-block">
121 sessions given
<br>
since Nov 15, 2014
</div>
<div class="info-block">
<div class="mentor-response wide clearfix">
<div class="rate">
Likelihood of Reply:
<span class="num">
50%
</span>
</div>
<div class="avg-time">
Response Time:
<span class="num">
within a day
</span>
</div>
</div>

</div>
</div>
</div>

</div>
</div>
</div>
</div>
<div class="secondPart">
<div class="customizeContainer">
<div class="row-fluid">
<div class="span8">
<div class="row-fluid">
<div class="span12">
<div class="infoBlock">
<img class="img-circle headImg" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/photo.jpg">
<a class="name" href="https://www.codementor.io/dckc">
Dan Connolly
</a>
<div class="viewsInfo pull-right muted">
<small>
Dec 06, 2014
</small>
</div>
</div>
</div>
</div>
<div class="row-fluid">
<div class="well span12">
<div class="help-listing-content" ng-non-bindable=""><p>We have multi-core, gigahertz processors on our wrists. Games are developed like Hollywood blockbusters, with hundreds of creative and technical people working together for years. As a new developer, where do you even start?! I have a few gems for you:</p><ul><li><a href="http://www.codeworld.info/">CodeWorld</a>:&nbsp;<span style="color:rgb(95, 99, 102)">create your own pictures, animations, and games on the Web</span></li><li><a href="https://www.youtube.com/watch?v=yF5-6AcohQw">How The Web Just Happened</a></li><li><a href="http://www.cs.colby.edu/djskrien/CPUSim/">CpuSim</a>:&nbsp;An Interactive CPU Simulator</li><li><a href="http://www.nand2tetris.org/">From NAND to Tetris</a>: Building a Modern Computer from First Principles</li></ul><p><a href="http://www.codeworld.info/">CodeWorld</a>, by Chris Smith,&nbsp;was designed to teach math to teenagers. <span style="color:rgb(95, 99, 102)">It lets b</span>rand new developers, with just a few hours of instruction,&nbsp;build haskell web apps right in your browser, without the hassle of text editors, compilers, etc.</p><p>Computer Science degree programs typically start students with Java or the like, but consider</p><pre class=" language-java"><code class=" language-java">x <span class="token operator">=</span> x <span class="token operator">+</span> <span class="token number">1</span></code></pre><p>&nbsp;from the perspective of the typical high school algebra student. That's nonsense!</p><p>Then consider</p><pre><code>main      = animationOf(design)
design(t) = rotate(slot, 60 * t) &amp; middle &amp; outside
slot      = solidRectangle(4, 0.4)
middle    = solidCircle(1.2)
outside   = circle(2)</code></pre><p>versus the mish-mash of concepts and code typical graphics and animation frameworks&nbsp;require. And while CodeWorld looks a bit like a toy, haskell is not. Haskell will take you a long way in the world of computing.</p><p><a href="https://www.youtube.com/watch?v=yF5-6AcohQw">How The Web Just Happened</a>&nbsp;is an hour talk by&nbsp;Tim Berners-Lee, inventor of the Web, explaining how he started by building magnets, and just as he mastered those, transistors became available to hobbyists. And just as he mastered transitors, integrated circuits came along. And so on, until he had a Next machine and the Internet at his disposal. My own career followed a similar path, just a few years behind his. I didn't build my own display, but with a Radio Shack Color Computer, I learned the principles of Unix from OS/9, and I built my own printer interface and wrote my own disk driver. Tim and I met in 1991 and worked together building the Web for the next&nbsp;20 years.</p><p><a href="http://www.cs.colby.edu/djskrien/CPUSim/">CpuSim</a>, <span style="color:rgb(95, 99, 102)">by Dale Skrien at&nbsp;</span>Colby College, lets you really see how CPUs work, with registers and memory and assembly language and machine language. While it's great to know haskell and other high level programming languges, it's still important to know what's going on underneath. This one you have to download and install to run, but it took me just a few minutes, and as a Java app, it runs on lots of platforms.</p><p><a href="http://www.nand2tetris.org/">From NAND to Tetris</a>, b<span style="color:rgb(95, 99, 102)">y Noam Nisan and Shimon Schocken, covers the parts in between: operating systems, compilers, and all that. It's a course of many weeks, and I haven't done it, personally. But if you're willing to spend the time, it lets you walk the path that Tim and I did, even though the giga-scale technology is all ready rolled out everywhere.</span></p></div>
<div class="share">
<h4>
Share this
</h4>
<div class="addthis_sharing_toolbox"></div>
</div>
<div class="related-help-listings">
<h4>Related Tips</h4>
<div class="row-fluid">
<div class="span6">
<div class="lModule">
<span>
<a class="relatedLink" href="https://www.codementor.io/tips/7712934628/haskell-foldl-lambda-set-empty">
Haskell - foldl $ lambda Set.empty
</a>
</span>
<span class="mentorLink">
<img class="mentorIcon img-circle" src="https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps">
<a href="https://www.codementor.io/6d11c469eecb8b67d4fe.ckoenig">
Removed User
</a>
</span>
</div>
</div>
<div class="span6">
<div class="lModule">
<span>
<a class="relatedLink" href="https://www.codementor.io/tips/8377241790/be-quick-to-respond-always-">
be quick to respond always.
</a>
</span>
<span class="mentorLink">
<img class="mentorIcon img-circle" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/IMG_1331.JPG">
<a href="https://www.codementor.io/ashish1dev">
Ashish
</a>
</span>
</div>
</div>
</div>
<div class="row-fluid">
<div class="span6">
<div class="lModule">
<span>
<a class="relatedLink" href="https://www.codementor.io/tips/4917782736/operations-with-user-defined-datatype">
Operations with user defined Datatype
</a>
</span>
<span class="mentorLink">
<img class="mentorIcon img-circle" src="https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps">
<a href="https://www.codementor.io/6d11c469eecb8b67d4fe.ckoenig">
Removed User
</a>
</span>
</div>
</div>
<div class="span6">
<div class="lModule">
<span>
<a class="relatedLink" href="https://www.codementor.io/tips/6748713284/haskell-when-declaring-a-class-how-can-i-use-a-type-variable-that-is-not-immediately-in-the-constructors">
Haskell: When declaring a class, how can I use a type variable that is not immediately in the constructors?
</a>
</span>
<span class="mentorLink">
<img class="mentorIcon img-circle" src="https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps">
<a href="https://www.codementor.io/6d11c469eecb8b67d4fe.ckoenig">
Removed User
</a>
</span>
</div>
</div>
</div>
</div>
<!-- ////////// DISQUS ///////////////// -->
<!-- ////////// DISQUS ///////////////// -->
<div class="discussContent">
<div id="disqus_thread" style="display: inline-block;"><iframe style="display: inline-block; width: 100%; border: 1px solid rgb(204, 204, 204); height: 80px; background: rgb(255, 255, 255);" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/saved_resource.html"></iframe></div>
<script>
  /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
  var disqus_shortname = "codementorio"; // required: replace example with your forum shortname
  
  /* * * DON'T EDIT BELOW THIS LINE * * */
  (function() {
      var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
      dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
      (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
  })();
</script>
<script>
  var disqus_config = function() {
    this.callbacks.onNewComment = [function(comment) {
      var url = "/api/disqus_comment_callback/tips"
      var data ={
        'post': comment.id,
        'text': comment.text,
        'page': window.location.pathname
      }
      $.ajax({
          type: "POST",
          url: url,
          data: data,
          dataType: 'json'
        });
    }];
  };
</script>
<noscript>
Please enable JavaScript to view the
<a href='http://disqus.com/?ref_noscript'>comments powered by Disqus.</a>
</noscript>

<!-- ////////// DISQUS ///////////////// -->
</div>

<!-- ////////// DISQUS ///////////////// -->
</div>
</div>
</div>
</div>
</div>
</div>
</div>

</div>
  <footer class="show  footer-block">
    <div class="footer-container" ng-class="{&#39;text-center&#39;: Viewport.phoneOnly}">
      <div class="footer-block__link-block">
        <div class="row-fluid">
          <div class="span4">
            <div>
              <div class="footer-block__header">
                Expert
              </div>
            </div>
            <div class="row-fluid">
              <div class="span6">
                <div class="footer-block__subheader">
                  TOPICS
                </div>
                <a class="footer-block__link" href="https://www.codementor.io/experts/web-programming">
                  Web Programming
                </a>
                <a class="footer-block__link" href="https://www.codementor.io/experts/coding">
                  Code
                </a>
                <a class="footer-block__link" href="https://www.codementor.io/experts/mobile-app-programming">
                  Mobile App Programming
                </a>
                <a class="footer-block__link" href="https://www.codementor.io/experts/design">
                  Design/UX
                </a>
                <a class="footer-block__link" href="https://www.codementor.io/experts/devops">
                  Database/Operations
                </a>
                <a class="footer-block__link" href="https://www.codementor.io/experts/development-process">
                  Development Process/Tools
                </a>
                <a class="footer-block__link" href="https://www.codementor.io/experts">View All</a>
              </div>
              <div class="span6">
                <div class="footer-block__subheader">
                  POPULAR CATEGORIES
                </div>
                <a class="footer-block__link" href="https://www.codementor.io/javascript-experts">JavaScript Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/angularjs-experts">AngularJS Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/ruby-on-rails-experts">RoR Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/java-experts">Java Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/ios-experts">iOS Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/c_sharp-experts">C# Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/python-experts">Python Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/android-experts">Android Expert Help</a>
                <a class="footer-block__link" href="https://www.codementor.io/php-experts">PHP Expert Help</a>
              </div>
            </div>
          </div>
          <div class="span4">
            <div>
              <div class="footer-block__header">
                Learning Center
              </div>
            </div>
            <div class="row-fluid">
              <div class="span6">
                <div class="footer-block__subheader">
                  TOPICS
                </div>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-ruby-on-rails-online-bwc75wpyu">Learn RoR Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-angularjs-online-bwban7j0d">Learn AngularJS Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-reactjs-online-bwc6wg9jg">Learn React Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-python-online-bwbc63ulz">Learn Python Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-android-development-online-bwba0mlle">Learn Android Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-reactjs-online-bwc6wg9jg">Learn JavaScript Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-c-sharp-online-bwbavow0y">Learn C# Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections/learn-java-online-bwbbwjibt">Learn Java Online</a>
                <a class="footer-block__link" href="https://www.codementor.io/learn/blockchain">Learn Blockchain</a>

              </div>
              <div class="span6">
                <div class="footer-block__subheader">
                  RESOURCES
                </div>
                <a class="footer-block__link" href="https://www.codementor.io/community">Community</a>
                <a class="footer-block__link" href="https://www.codementor.io/collections">Collections</a>
                <a class="footer-block__link" href="https://www.codementor.io/pair-programming">Pair Programming</a>
                <a class="footer-block__link" href="https://www.codementor.io/requests">Solved Requests</a>
                <a class="footer-block__link" href="https://www.codementor.io/tutors">Programming Tutors</a>
                <a class="footer-block__link" href="https://www.codementor.io/developers">Freelance Developers</a>
                <a class="footer-block__link" href="https://www.codementor.io/freelance-jobs">Freelance Job</a>
              </div>
            </div>
          </div>
          <div class="span4">
            <div>
              <div class="footer-block__header">
                Company
              </div>
            </div>
            <div class="row-fluid">
              <div class="span6">
                <div class="footer-block__subheader">
                  INFO
                </div>
                <a class="footer-block__link" href="https://www.codementor.io/mentor/apply">Become a Codementor</a>
                <a class="footer-block__link" href="https://www.codementor.io/howitworks/mentorship">How It Works</a>
                <a class="footer-block__link" href="https://www.codementor.io/success-stories">Codementor Reviews</a>
                <a class="footer-block__link" href="http://www.bestprogramminglanguagefor.me/" target="_blank">What Language to Learn</a>
                <a class="footer-block__link" href="https://hire.codementor.io/">CodementorX</a>
              </div>
              <div class="span6">
                <div class="footer-block__subheader">
                  &nbsp;
                </div>
                <a class="footer-block__link" href="https://support.codementor.io/">Support</a>
                <a class="footer-block__link" title="Codementor Jobs" href="https://www.codementor.io/careers">Careers</a>
                <a class="footer-block__link" href="https://www.codementor.io/blog">Blog</a>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="footer-block__company-info">
        <div class="row-fluid">
          <div class="span8">
            <div class="pull-left footer-block__company-info__left">
              <div class="footer-block__company-info__company-name">
                Codementor
              </div>
              <div class="footer-block__company-info__slogan">
                On-demand Marketplace for Software Developers
              </div>
            </div>
            <div class="pull-left footer-block__company-info__right">
              <a href="http://www.facebook.com/codementor" title="Codementor on Facebook">
                <div class="social-icon">
                  <i class="fa fa-facebook"></i>
                </div>
              </a>
              <a href="http://www.twitter.com/codementorIO" title="Codementor on Twitter">
                <div class="social-icon">
                  <i class="fa fa-twitter"></i>
                </div>
              </a>
               <a href="https://plus.google.com/102580007686679046547" title="Codementor on Google+">
                <div class="social-icon">
                  <i class="fa fa-google-plus"></i>
                </div>
              </a>
              <a href="https://mixpanel.com/f/partner">
                <img class="mixpanel" alt="Mobile Analytics" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/badge_blue.png">
              </a>
            </div>
          </div>
          <div class="span4">
            <div class="footer-block__company-info__copy-right">
              <span>
                © Copyright 2019 Codementor
              </span>
            </div>
            <div class="footer-block__company-info__term-of-service">
              <a href="https://www.codementor.io/terms">Terms of Service</a>
            </div>
          </div>
        </div>
      </div>
      </div>
    
  </footer>
<script>

  $(document).ready(function(){
    function getheight() {
      var myWidth = 0,
          myHeight = 0,
          element = document.getElementById("email_collection_footer").firstElementChild;

      if (typeof(window.innerWidth) == 'number') {
          //Non-IE
          myWidth = window.innerWidth;
          myHeight = window.innerHeight;
      }
      else if (document.documentElement && (document.documentElement.clientWidth || document.documentElement.clientHeight)) {
          //IE 6+ in 'standards compliant mode'
          myWidth = document.documentElement.clientWidth;
          myHeight = document.documentElement.clientHeight;
      }
      else if (document.body && (document.body.clientWidth || document.body.clientHeight)) {
          //IE 4 compatible
          myWidth = document.body.clientWidth;
          myHeight = document.body.clientHeight;
      }

      var scrolledtonum = window.pageYOffset + myHeight + 2;
      var heightofbody = document.body.offsetHeight;

      if (myWidth < 980){
        if(element.className.indexOf("disable") == -1){
          element.className = element.className + " disable"
        }
      }
      else {
        if (scrolledtonum >= heightofbody/2 || scrolledtonum > 1700){
          setTimeout(function(){
            element.className = element.className.replace(" disable", "");
          }, 5000);
        }
      }

      if (scrolledtonum >= heightofbody) {
        if(element.className.indexOf("trigger_fadeOut_event") == -1){
          element.className = element.className + " trigger_fadeOut_event";
        }
      }
      else{
        element.className = element.className.replace(" trigger_fadeOut_event","");
      }
    }
    if(document.getElementById("email_collection_footer") != null){
      window.onscroll = getheight;
      $("#email_collection_footer .closeBtn").on("click", function(){
        $("#email_collection_footer").hide();
      });
    }
  });

</script>

<app-sound><audio data-effect="notify"><source ng-src="https://cdn.codementor.io/assets/notify.ogg" type="audio/ogg" src="https://cdn.codementor.io/assets/notify.ogg"><source ng-src="https://cdn.codementor.io/assets/notify.mp3" type="audio/mpeg" src="https://cdn.codementor.io/assets/notify.mp3"></audio></app-sound>
<div aria-hidden="true" class="modal hide fade" id="signup-modal" menu-sign-up-form="" role="dialog" tabindex="-1">
<div class="modal-header clearfix">
<h3>
<img class="codementor-logo" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/codementor-logo-white-45322e5e8f84a4405caad6cd593627ea057edf7e57b7278f1abbd1597da70ff0.png">
<img class="codementor-text" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/codementor-logo-eea4ea58e817c09d61c9a97a536ea2fd2c683e9430d83908c4c0df3f9e99a10b.png">
<div class="signin muted">
<a href="https://www.codementor.io/users/sign_in">Sign In</a>
</div>
</h3>
</div>
<div class="modal-body" style="max-height: none;">

<div class="extra-info alert alert-success ng-binding ng-hide" ng-show="sf.extraInfo">

</div>
<div class="row-fluid">
<div class="span12">
<h3>Sign Up and Get Help Now</h3>
<a class="social-auth social-auth--twitter" href="https://api.codementor.io/api/v2/auth/twitter?origin=https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps&amp;to=https://www.codementor.io/user-onboarding">
<i class="fa fa-twitter" style="margin-right:12px;"></i>
Continue with twitter
</a>
<a class="social-auth social-auth--google" href="https://api.codementor.io/api/v2/auth/google?origin=https://www.codementor.io/tips/4919482737/learning-to-make-stuff-with-computers-from-cpus-to-haskell-web-apps&amp;to=https://www.codementor.io/user-onboarding">
<i class="fa fa-google" style="margin-right:12px;"></i>
Continue with google
</a>
<div class="separator">
or
</div>
<form class="form-inline signup-form signup-form-normal ng-pristine ng-scope ng-invalid ng-invalid-required ng-valid-minlength ng-valid-email" name="signupForm" ng-controller="signupFormCtrl as sfCtrl" id="new_user" action="https://www.codementor.io/expert_page_signup" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓" autocomplete="off"><input type="hidden" name="authenticity_token" value="TQDk5iTH34RJ999F4U6Xy0wi48qKK3AxlSwugtU7W5Dwvd3ChA1M19JRyzPuKwCTdNj7gY8ocFaSJzE5dDVX9Q==" autocomplete="off"><input placeholder="Full name" minlength="2" required="required" ng-model="user.name" type="text" name="user[name]" id="user_name" class="ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required ng-valid-minlength">
<input placeholder="Email address" required="required" ng-model="user.email" type="email" name="user[email]" id="user_email" class="ng-pristine ng-untouched ng-empty ng-valid-email ng-invalid ng-invalid-required">
<input placeholder="New password" minlength="8" required="required" ng-model="user.password" type="password" name="user[password]" id="user_password" class="ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required ng-valid-minlength">
<input ng-value="sfCtrl.user.timeZoneText" value="-05:00, DST" type="hidden" name="user[time_zone]" id="user_time_zone" autocomplete="off">
<input value="" type="hidden" name="user[pending_msg_content]" id="user_pending_msg_content" autocomplete="off">
<input value="" type="hidden" name="user[pending_msg_mentor]" id="user_pending_msg_mentor" autocomplete="off">
<input type="hidden" name="user[office_hour]" id="user_office_hour" autocomplete="off">
<input type="hidden" name="user[after_sign_in_url]" id="user_after_sign_in_url" autocomplete="off">
<input type="hidden" name="is_offers" id="is_offers" value="false" autocomplete="off">
<input type="hidden" name="is_refferral" id="is_refferral" value="false" autocomplete="off">
<input type="hidden" name="is_promotion" id="is_promotion" value="false" autocomplete="off">
<input type="hidden" name="promo_code" id="promo_code" value="" autocomplete="off">
<input type="hidden" name="promotion_type" id="promotion_type" autocomplete="off">
<input type="hidden" name="utm_seo" id="utm_seo" value="" autocomplete="off">
<input type="hidden" name="utm_form" id="utm_form" value="menu_new_form" autocomplete="off">
<button name="button" type="submit" style="width:100%;margin-bottom:8px;font-weight:bold;" class="btn btn-primary" data-disable-with="Loading... &lt;i class=&quot;icon-spin icon-refresh&quot;&gt;&lt;/i&gt;" ng-click="onSignup(signupForm.$valid)">Sign up for free</button>
<div style="color:#666;font-size:12px;line-height:1.5;margin-top:8px;">
By signing up, I agree to Codementor's
<a href="https://www.codementor.io/terms">Terms of Service</a>
and
<a href="https://www.codementor.io/privacy">Privacy Policy.</a>
</div>
</form>
<hr>
<div class="become-codementor">
<a href="https://www.codementor.io/mentor/apply">Want to become a Codementor?</a>
</div>
</div>
</div>
</div>
</div>
<script>
  $(function(){
    $('#signup-modal').on('shown', function(){
      $('#signup-modal input#user_name').focus();
    });
  });
</script>



<!-- // detect user timezone -->
<script>
  (function(){
    try{
      var time_zone_input = document.getElementById("user_time_zone");
      if(time_zone_input){
        time_zone_input.value = new Date().currentTimeZoneText();
      }
    }catch(e){}
  })();
</script>
<script type="text/ng-template" id="/template/timezoneTool.html">
  <div class="appChatbox-timezone-tool animate-show">
    <div class="timezone-tool-title">
      SUGGEST A SCHEDULE IN CHAT
    </div>
    <div class="timezone-tool-month">
      <div class="choose-prev" ng-click="vm.prevMonth()"></div>
      <div class="month-value">{{ vm.timeSelected.month }}</div>
      <div class="choose-next" ng-click="vm.nextMonth()"></div>
    </div>
    <div class="timezone-tool-dates">
      <div class="choose-prev" ng-click="vm.prevNDays(7)"></div>
      <div class="dates-container">
        <div class="date-box" ng-repeat="dateInfo in vm.timeOptions.datesInfo"
          ng-class="{'date-box-selected': vm.timeSelected.date == dateInfo.date,
          'date-box-holiday': dateInfo.day == 'Sat' || dateInfo.day == 'Sun'}"
          ng-click="vm.selectDate($index)">
            <span class="date-value"> {{ dateInfo.date }} </span>
            <small class="day-value"> {{ dateInfo.day.substr(0, 3).toUpperCase() }} </small>
            <span class="selected-light"></span>
        </div>
      </div>
      <div class="choose-next" ng-click="vm.nextNDays(7);flip=1"></div>
    </div>
    <div class="timezone-tool-time">
      <div class="btn-group time-selection-hour">
        <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
          <span class="time-selected">{{ vm.timeSelected.hour }}</span>
          <span class="caret"></span>
        </a>
        <ul class="dropdown-menu">
          <li ng-repeat="(value, disabled) in vm.timeOptions.hours" ng-click="vm.selectHour($index)"
          value="{{ value }}" ng-class="{'disabled': disabled}"><a href="#">{{ value }}</a></li>
        </ul>
      </div>
      <span class="colon">&#58;</span>
      <div class="btn-group time-selection-minute">
        <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
          <span class="time-selected">{{ vm.timeSelected.minute }}</span>
          <span class="caret"></span>
        </a>
        <ul class="dropdown-menu">
          <li ng-repeat="(value, disabled) in vm.timeOptions.minutes" ng-click="vm.selectMinute($index)"
          value="{{ value }}" ng-class="{'disabled': disabled}"><a href="#">{{ value }}</a></li>
        </ul>
      </div>
      <div class="time-utc-offset">
        UTC {{ vm.timeSelected.utc }}
      </div>
    </div>
    <div class="timezone-tool-info">
      <div class="opposite-info">
        <p>{{ vm.oppositeDetail.name }}'s Time</p>
        <div class="opposite-time">
          <p class="pull-left">{{ vm.oppositeUserTimeFormat }}</p>
          <div class="clearfix"></div>
        </div>
      </div>
      <form>
        <a class="btn btn-primary pull-left" ng-click="vm.send()">Send</a>
        <a class="btn btn-default pull-right cancel" ng-click="vm.dismiss()">Cancel</a>
        <div class="clearfix"></div>
      </form>
    </div>
  </div>
</script>

<script id="/templates/appChatList.html" type="text/ng-template">
  <div class='appChatList clearfix'>
    <div class='appChatbox-title clearfix' ng-click='Chat.chatList.isMinimized = !Chat.chatList.isMinimized'>
      <span class='appChatbox-contact-name'>Chat List</span>
      <span class='appChatbox-toggle-min'></span>
      <a class='action-btn pull-right' ng-click='Chat.chatBarMaximize();$event.stopPropagation();' ng-if='Chat.chatList.isMinimized'>
        <i class='icon-chevron-up' ng-show='Viewport.width<1280'></i>
        <i class='fi-arrows-expand' ng-show='Viewport.width>=1280'></i>
      </a>
      <a class='action-btn pull-right' ng-click='Chat.chatBarMinimize();$event.stopPropagation();' ng-if='!Chat.chatList.isMinimized'>
        <i class='icon-chevron-down'></i>
      </a>
    </div>
    <div class='searchContact' ng-hide='Chat.chatList.isMinimized'>
      <input ng-model="chatList.searchQuery" ng-change="chatList.search(chatList.searchQuery)" placeholder="Search" name="searchContact" type="text">
      <span ng-show="!chatList.searchQuery" class="search-icon fa fa-search ng-cloak"></span>
      <span ng-click="chatList.searchQuery='';chatList.searchResults=null;" ng-show="chatList.searchQuery.length>0" class="search-icon fa fa-remove ng-cloak"></span>
    </div>
    <div class='appChatList-action top' ng-hide='chatList.searchQuery && (chatList.searchResults || chatList.searching)'>
      <a class='tab' ng-class="{active:chatList.tab=='category'||!User.isMember, 'the-one':!User.isMember}" ng-click="chatList.tab='category'">
        {{ (!User.isMember)?'Expert Mentors': (User.isMentor ? 'My Clients' : 'Experts')}}
      </a>
      <a class='tab' ng-class="{active:chatList.tab=='recent'}" ng-click="chatList.tab='recent'" ng-if='User.isMember'>
        Recent Chats
      </a>
      <a class='action-btn minimize' ng-click='Chat.chatBarMinimize()'>
        <i class='icon-chevron-down'></i>
      </a>
    </div>
    <div class='appChatList-action top' style="line-height: 35px;padding: 0 10px;" ng-if="chatList.searchQuery && (chatList.searchResults || chatList.searching)">
      Search Results
    </div>
    <div class='appChatbox-dialog ng-cloak' ng-if='!Chat.chatList.isMinimized && chatList.searchQuery && (chatList.searchResults || chatList.searching)' prevent-body-scroll>
      <div class='appChatList-loading' ng-if='chatList.searching'>
        <i class='icon-spin icon-spinner'></i>
        <span>Loading...</span>
      </div>
      <div class='appChatList-empty ng-cloak' ng-if='chatList.searchResults.length == 0'>
        <h4>No Results</h4>
      </div>
      <div class='appChatList-ul'>
        <div class='appChatList-li ng-cloak' ng-class="{'hide-presence':(!u.presence||u.presence=='offline')}" ng-click='chatList.openChat(u)' ng-repeat='u in chatList.searchResults' placement='left' popover-profile='{{chatList.oppositeUser(u).username}}'>
          <div class='appChatList-avatar'>
            <img ng-src='{{chatList.oppositeUser(u).small_avatar_url}}'>
            <presence status='u.presence' un='{{ chatList.oppositeUser(u).username }}'></presence>
          </div>
          <div class='info'>
            <div class='display-name'>
              {{ chatList.oppositeUser(u).name }}
            </div>
          </div>
          <span class='user-local-time'>
            <current-time offset='{{chatList.oppositeUser(u).timezone_offset}}'></current-time>
          </span>
          <div class="favorited" ng-if="chatList.isFavorited(chatList.oppositeUser(u))">
            <i class="icon-star"></i>
          </div>
        </div>
      </div>
    </div>
    <div class='appChatbox-dialog ng-cloak' ng-hide='Chat.chatList.isMinimized' ng-if="chatList.tab=='category' && !(chatList.searchQuery && (chatList.searchResults || chatList.searching))" prevent-body-scroll>
      <div class='appChatList-loading' ng-if='chatList.loading'>
        <i class='icon-spin icon-spinner'></i>
        <span>Loading...</span>
      </div>
      <div class='appChatList-empty ng-cloak' ng-if='!(chatList.list.longterm.length + chatList.list.category_chats.length + chatList.list.my.length) && !chatList.loading'>
        <h4>No messages here.</h4>
        <p class='ng-cloak' ng-if='!User.isMentor'>
          Want to connect with a Codementor?
        </p>
        <p class='ng-cloak' ng-if='User.isMentor'>
          Share your Codementor profile to receive more requests.
        </p>
        <a class='btn btn-highlight ng-cloak' href='#' onclick='showGetHelpNow()' ng-if='!User.isMentor&&User.isMember'>
          GET HELP NOW
        </a>
        <a class='btn btn-highlight ng-cloak' ng-click='chatList.signup()' ng-if='!User.isMentor&&!User.isMember'>
          SIGNUP NOW
        </a>
        <a class='btn btn-primary' href='/users/public_profile' ng-if='User.isMentor'>
          GET MORE REQUESTS
        </a>
      </div>
      <div class='appChatList-my' ng-if='!!chatList.list.my.length'>
        <h4 class='appChatList-title' ng-if='!User.isMentor'>
          My Expert Mentors
        </h4>
        <h4 class='appChatList-title' ng-if='User.isMentor && chatList.list.longterm.length>0'>
          My Client{{ (chatList.list.my.length>1)?'s':'' }}
        </h4>
        <div class='appChatList-ul'>
          <div class='appChatList-li ng-cloak' ng-class="{'hide-presence':(!u.presence||u.presence=='offline')}" ng-click='chatList.openChat(u)' ng-repeat='u in chatList.list.my | orderBy : chatList.sortByStatusAndFavorite : true | limitTo: chatList.myListLimit' placement='left' popover-profile='{{chatList.oppositeUser(u).username}}'>
            <div class='appChatList-avatar'>
              <img ng-src='{{chatList.oppositeUser(u).small_avatar_url}}'>
              <presence status='u.presence' un='{{ chatList.oppositeUser(u).username }}'></presence>
            </div>
            <div class='info'>
              <div class='display-name'>
                {{ chatList.oppositeUser(u).name }}
              </div>
            </div>
            <span class='user-local-time'>
              <current-time offset='{{chatList.oppositeUser(u).timezone_offset}}'></current-time>
            </span>
            <div class="favorited" ng-if="chatList.isFavorited(chatList.oppositeUser(u))">
              <i class="icon-star"></i>
            </div>
          </div>
        </div>
        <a class='load-more' href='#' ng-click='chatList.loadMoreMy()' ng-if='!chatList.noMoreMy'>
          Load More
        </a>
      </div>
      <div class='category-list' ng-if='!!chatList.list.category_chats.length'>
        <div class='appChatList-categories' ng-if='category.chat_list.length' ng-repeat='category in chatList.list.category_chats'>
          <h4 class='appChatList-title'>
            <a ng-href='{{category.experts_url}}'>
              {{category.category_name}}
            </a>
          </h4>
          <div class='appChatList-ul'>
            <div class='appChatList-li ng-cloak' ng-class="{'hide-presence':(!cc.presence||cc.presence=='offline')}" ng-click='chatList.openChat(cc)' ng-repeat='cc in category.chat_list | orderBy : chatList.sortByStatus : true' placement='left' popover-profile='{{chatList.oppositeUser(cc).username}}'>
              <div class='appChatList-avatar'>
                <img ng-src='{{chatList.oppositeUser(cc).small_avatar_url}}'>
                <presence status='cc.presence' un='{{ chatList.oppositeUser(cc).username }}'></presence>
              </div>
              <div class='info' ng-class="{'has-rating':chatList.oppositeUser(cc).rating>0}">
                <div class='display-name'>
                  {{ chatList.oppositeUser(cc).name }}
                </div>
                <div class='rating' ng-if='chatList.oppositeUser(cc).rating>0'>
                  {{chatList.oppositeUser(cc).rating | number:1}}<span class='star' ng-repeat='i in Rating.genRateRange(chatList.oppositeUser(cc).rating)'>★</span><span class='empty star' ng-repeat='i in Rating.genEmptyRateRange(chatList.oppositeUser(cc).rating)'>★</span>
                </div>
              </div>
              <div class="favorited" ng-if="chatList.isFavorited(chatList.oppositeUser(cc))">
                <i class="icon-star"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class='appChatbox-dialog ng-cloak' ng-hide='Chat.chatList.isMinimized' ng-if="chatList.tab=='recent' && !(chatList.searchQuery && (chatList.searchResults || chatList.searching))" prevent-body-scroll>
      <div class='appChatList-loading' ng-show='chatList.loading'>
        <i class='icon-spin icon-spinner'></i>
        <span>Loading...</span>
      </div>
      <div class='appChatList-empty ng-cloak' ng-if='!(chatList.list.recent_chats.length) && !chatList.loading'>
        <h4>No messages here.</h4>
        <p class='ng-cloak' ng-if='!User.isMentor'>
          Want to connect with a Codementor?
        </p>
        <p class='ng-cloak' ng-if='User.isMentor'>
          Share your Codementor profile to receive more requests.
        </p>
        <a class='btn btn-highlight ng-cloak' href='#' onclick='showGetHelpNow()' ng-if='!User.isMentor&&User.isMember'>
          GET HELP NOW
        </a>
        <a class='btn btn-highlight ng-cloak' ng-click='chatList.signup()' ng-if='!User.isMentor&&!User.isMember'>
          SIGNUP NOW
        </a>
        <a class='btn btn-primary' href='/users/public_profile' ng-if='User.isMentor'>
          GET MORE REQUESTS
        </a>
      </div>
      <div class='appChatList-recent-chats' ng-show='!!chatList.list.recent_chats.length'>
        <div class='appChatList-ul'>
          <div class='appChatList-li ng-cloak' ng-class="{'hide-presence':(!m.presence||m.presence=='offline')}" ng-click='chatList.openChat(m)' ng-repeat='m in chatList.list.recent_chats | orderBy : chatList.sortByCreatedAt : true | limitTo: chatList.recentChatLimit' placement='left' popover-profile='{{chatList.oppositeUser(m).username}}'>
            <div class='appChatList-avatar'>
              <img ng-src='{{chatList.oppositeUser(m).small_avatar_url}}'>
              <presence status='m.presence' un='{{ chatList.oppositeUser(m).username }}'></presence>
            </div>
            <div class='info'>
              <div class='display-name'>
                {{ chatList.oppositeUser(m).name }}
              </div>
            </div>
            <span class='user-local-time'>
              <current-time offset='{{chatList.oppositeUser(m).timezone_offset}}'></current-time>
            </span>
            <div class="favorited" ng-if="chatList.isFavorited(chatList.oppositeUser(m))">
              <i class="icon-star"></i>
            </div>
          </div>
        </div>
        <a class='load-more' href='#' ng-click='chatList.loadMoreList()' ng-if='!chatList.noMoreList'>
          Load More
        </a>
      </div>
    </div>
  </div>
</script>

<script type="text/ng-template" id="/template/appChatbox.html">
  <div class="appChatbox" ng-mouseenter="chatbox.read()">
    <div class="appChatbox-title clearfix">
      <presence status="chatroom.presence" un="{{chatroom.contact.username}}" style="margin:0 5px 0 3px;">
      </presence>
      <a class="appChatbox-contact-name" ng-href="{{'/' + chatroom.contact.username}}" ng-class="{'is-mentor': !User.isMentor}">{{chatroom.contact.name}}</a>
      <span class="appChatbox-toggle-min" ng-click="chatroom.isMinimized = !chatroom.isMinimized"></span>
      <span>
        <i class="appChatbox-button" ng-class="{'icon-external-link-sign':!chatbox.expanded, 'icon-chevron-down':chatbox.expanded}" ng-hide="chatbox.expanded||!User.isMember" ng-click="chatbox.toggleExpand()"></i>
        <!-- Dropdown toggle for user. -->
        <i class="appChatbox-button appChatbox-button-toolbox icon-reorder" ng-class="{active: chatroom.showToolbox}" ng-click="chatbox.toggleToolbox(!chatroom.showToolbox, $event)" ng-show="User.isMember && !User.isMentor"></i>

        <!-- Dropdown toggle for mentor. Show warning if the opposite user is suspended or suspicious. -->
        <i class="appChatbox-button appChatbox-button-toolbox icon-reorder" ng-class="{active: chatroom.showToolbox, success: (chatbox.newToService && !chatbox.suspicious && !chatbox.suspended), error: (chatbox.suspended || chatbox.suspicious)}" ng-click="chatbox.toggleToolbox(!chatroom.showToolbox, $event)" ng-show="User.isMentor"></i>
        <i class="appChatbox-button icon-remove" ng-click="chatbox.close()"></i>
      </span>
    </div>

    <!-- Toolbox -->
    <div class="appChatbox-toolbox ng-hide" ng-show="chatroom.showToolbox">
      <i class="appChatbox-button icon-lock" style="margin-left:6px;" ng-click="chatbox.block($event)" ng-if="!chatroom.contact.blocked">
        <span class="appChatbox-tip">Block {{chatroom.contact.name}}</span>
      </i>
      <i class="appChatbox-button icon-unlock-alt" style="margin-left:6px;" ng-click="chatbox.unblock($event)" ng-if="chatroom.contact.blocked">
        <span class="appChatbox-tip">Unblock {{chatroom.contact.name}}</span>
      </i>
      <i class="appChatbox-button icon-warning-sign" style="margin-left:6px;" ng-click="chatbox.openReportModal($event)">
        <span class="appChatbox-tip">Report {{chatroom.contact.name}}</span>
      </i>
      <i class="appChatbox-button icon-question-sign" style="margin-left:6px;" ng-click="chatbox.showLatestReq=true" ng-if="User.isMentor && chatbox.latestReq">
        <span class="appChatbox-tip">View latest request</span>
      </i>

      <hr ng-if="User.isMentor && (chatbox.suspicious || chatbox.suspended || chatbox.newToService)"/>

      <!-- New-to-service account -->
      <i class="appChatbox-button appChatbox-button-success icon-n" style="margin-left:6px;" ng-if="User.isMentor && chatbox.newToService && !(chatbox.suspicious || chatbox.suspended)">
        <span class="appChatbox-tip">New User</span>
        <br />
        <small class="appChatbox-tip">This user hasn't had any sessions yet</small>
      </i>

      <!-- Suspicious account -->
      <i class="appChatbox-button appChatbox-button-error icon-exclamation-sign" style="margin-left:6px;" ng-if="User.isMentor && chatbox.suspicious">
        <span class="appChatbox-tip">Suspicious Activity</span>
        <br />
        <small class="appChatbox-tip">We’ve asked this user to contact Codementor support. Please refrain from assisting this user until this has been resolved.</small>
      </i>

      <!-- Suspended account -->
      <i class="appChatbox-button appChatbox-button-error icon-exclamation-sign" style="margin-left:6px;" ng-if="User.isMentor && chatbox.suspended">
        <span class="appChatbox-tip">Suspended Account</span>
        <br />
        <small class="appChatbox-tip">Suspended for fraudulent activity</small>
      </i>

      <hr ng-if="chatroom.oppositeTimezoneOffsetText"/>
      <i class="appChatbox-button disable icon-time" style="margin-left:6px;" ng-if="chatroom.oppositeTimezoneOffsetText">
        <span class="appChatbox-tip">{{chatroom.oppositeTimezoneOffsetText}}</span>
      </i>
    </div>
    <!-- End Toolbox -->

    <timezone-tool ng-show="chatbox.timezoneToolToggled" vm-chat="chatbox" opposite-detail="chatroom.contact"></timezone-tool>

    <div class="appChatbox-toolbar" ng-hide="(chatroom.isMinimized && !chatbox.expanded) || User.isMentor || chatroom.isFake || chatroom.contact.blocked || onVacation || chatbox.findScheduleCluster()">
      <i class="appChatbox-button icon-play" ng-click="chatbox.connect(chatroom.contact)" ng-class="{disable:!chatbox.userOnline}">
        <span class="appChatbox-tip">Start Session</span>
      </i>
      <i class="appChatbox-button appChatbox-button-icon icon-calendar"
        ng-class="{disable: onVacation}"
        ng-click="chatbox.schedule(chatroom.contact)"
        ng-mouseenter="chatbox.showToolbarButtonInfo('Schedule a Session', chatbox.schedule,$event)"
        ng-mouseleave="chatbox.showToolbarButtonInfo(false)">
      </i>
      <i class="appChatbox-button appChatbox-button-icon icon-offline-help" ng-click="chatbox.openOfflineHelpModal($event)"
        ng-show="!User.isMentor" ng-class="{disable: chatroom.contact.blocked || onVacation}"
        ng-mouseenter="chatbox.showToolbarButtonInfo('Pay for Offline Help', chatbox.openOfflineHelpModal,$event)"
        ng-mouseleave="chatbox.showToolbarButtonInfo(false)">
      </i>
      <i class="appChatbox-button appChatbox-button-icon icon-star-empty" ng-click="chatbox.favorite($event)"
        ng-if="!User.isMentor && !chatroom.contact.favorited"
        ng-mouseenter="chatbox.showToolbarButtonInfo('Favorite ' + chatroom.contact.name, chatbox.favorite,$event)"
        ng-mouseleave="chatbox.showToolbarButtonInfo(false)">
      </i>
      <i class="appChatbox-button appChatbox-button-icon icon-star" style="color:#FCAB2E" ng-click="chatbox.unfavorite($event)"
        ng-if="!User.isMentor && chatroom.contact.favorited"
        ng-mouseenter="chatbox.showToolbarButtonInfo('Unfavorite ' + chatroom.contact.name, chatbox.favorite,$event)"
        ng-mouseleave="chatbox.showToolbarButtonInfo(false)">
      </i>
    </div>


    <!-- Toolbar for Codementor Monthly users -->
    <div class="appChatbox-toolbar" ng-hide="(chatroom.isMinimized && !chatbox.expanded) || User.isMentor || chatroom.isFake || chatroom.contact.blocked || !chatbox.findScheduleCluster()">
      <a class="appChatbox-button icon-play" ng-class="{disable:!chatbox.userOnline}" ng-href="{{chatbox.getStartScheduleClusterSessionPath()}}" ng-click="chatbox.checkConnectionForMonthly($event)" data-method="post">
        <span class="appChatbox-tip">Start Session</span>
      </a>
      <i class="appChatbox-button appChatbox-button-icon icon-calendar" ng-click="chatbox.goToScheduleCluster()"
        ng-show="!User.isMentor"
        ng-mouseenter="chatbox.showToolbarButtonInfo('Go to Codementor Monthly', chatbox.goToScheduleCluster, $event)"
        ng-mouseleave="chatbox.showToolbarButtonInfo(false)">
      </i>
      <i class="appChatbox-button appChatbox-button-icon icon-offline-help" ng-click="chatbox.openOfflineHelpModal()"
        ng-show="!User.isMentor" ng-class="{disable: chatroom.contact.blocked}"
        ng-mouseenter="chatbox.showToolbarButtonInfo('Pay for Extra Offline Help', chatbox.openOfflineHelpModal, $event)"
        ng-mouseleave="chatbox.showToolbarButtonInfo(false)">
      </i>
    </div>

    <!-- Fake toolbar for mentee that shows up when the contacted user is on vacation -->
    <div class="appChatbox-toolbar" ng-if="onVacation && !chatroom.contact.blocked">
      <div style="line-height:36px;padding:0 10px;color:#777;font-size: 12px;box-sizing:border-box;">{{chatroom.contact.name}} is away for vacation</div>
    </div>

    <!-- Fake toolbar for mentee that shows up when the contacted user is blocked -->
    <div class="appChatbox-toolbar" ng-if="!User.isMentor && chatroom.contact.blocked">
      <div style="line-height:36px;padding:0 10px;color:#777;font-size: 12px;box-sizing:border-box;">{{chatroom.contact.name}} has been blocked</div>
    </div>
    <div class="appChatbox-toolbar" style="line-height: 36px;" ng-hide="(chatroom.isMinimized && !chatbox.expanded) || !User.isMentor">
      <i class="appChatbox-button ask-start-session icon-play" ng-show="User.isMentor"  ng-click="chatbox.toggleMentorAskSession(!chatroom.mentorAskSession)">
        <span class="appChatbox-tip">Ask to start session</span>
      </i>
      <rate-for-client un="{{chatroom.contact.username}}" id-key="{{contactKey}}" mentee="{{chatroom.contact}}" is-disabled="chatroom.contact.blocked" style="{{(!!chatbox.findScheduleCluster() ? '' : 'margin: 6px 6px 6px 8px;')}}display:flex;display:-webkit-flex;" is-monthly-client="!!chatbox.findScheduleCluster()"></rate-for-client>
      <i class="appChatbox-button appChatbox-button-icon icon-calendar pull-right" ng-click="chatbox.goToScheduleCluster()"
        ng-show="chatbox.findScheduleCluster()"
        ng-mouseenter="chatbox.showToolbarButtonInfo('Go to Codementor Monthly', chatbox.goToScheduleCluster, $event)"
        ng-mouseleave="chatbox.showToolbarButtonInfo(false)">
      </i>
    </div>

    <div ng-show="toolbarButtonInfo" class="appChatbox-extra-info from-toolbar center muted" ng-click="chatbox.onExtraInfoClick($event)"
      ng-mouseenter="chatbox.showToolbarButtonInfo(true)"
      ng-mouseleave="chatbox.showToolbarButtonInfo(false)">{{toolbarButtonInfo}}</div>
    <div ng-show="!onVacation&&showNotResponsiveMsg&&!showNoReplyMsg&&User.isUser" class="appChatbox-msg-warning">
      <i class="icon-info-sign"></i>
      {{chatroom.contact.name}} hasn't been very responsive lately.  If you're looking for more immediate support, you can
      <a href="#" class="get-help-now" ng-click='chatbox.getHelpNow($event, "chatbox-not-responsive-msg")'>get help now here</a>.
      <a ng-click="showNotResponsiveMsg=false" href="#" class="close">
        <i class="icon-remove"></i>
      </a>
    </div>
    <div ng-show="showOnVacationMsg&&User.isUser&&!showNoReplyMsg" class="appChatbox-msg-warning">
      <i class="icon-info-sign"></i>
      {{chatroom.contact.name}} is away for vacation and not available for incoming requests.
      <a href="#" class="get-help-now" ng-click='chatbox.getHelpNow($event, "chatbox-not-responsive-msg")'>Get help from other mentors now</a>.
      <a ng-click="showOnVacationMsg=false" href="#" class="close">
        <i class="icon-remove"></i>
      </a>
    </div>
    <div ng-show="chatroom.infoMsg" class="appChatbox-msg-alert"> {{chatroom.infoMsg}} <a ng-click="chatroom.infoMsg='';" href="#" class="close"><i class="icon-remove"></i></a></div>
    <div ng-show="alertMsg" class="appChatbox-msg-alert text-error"><i class="icon-exclamation"></i> {{alertMsg}} <a ng-click="alertMsg='';" href="#" class="close"><i class="icon-remove"></i></a></div>

    <!-- Toolbar for Mentor to ask for a session -->
    <div ng-show="chatroom.mentorAskSession" class="appChatbox-askSession">
      <div class="appChatbox-askSession__block">
        <div class="appChatbox-askSession__block__link"  ng-click="chatbox.startSession()">
          {{ chatbox.findScheduleCluster() ? 'Start a monthly session' : 'Start a paid session' }}
        </div>
        <div class="appChatbox-askSession__block__link" ng-click="chatbox.startFreeSession()">
          <!-- <i class="icon-circle appChatbox-askSession__block__link--icon"/> -->
          Start a free info session
        </div>
        <div class="appChatbox-askSession__block__link voice_call" ng-click="chatbox.startFreeCall()">
          <div>
            <span>Start a free voice call</span><sup class="beta">Beta</sup>
          </div>
          <div  class="hint">
            <i class="fa fa-info-circle"/>
            <span>What is this?</span>
          </div>
        </div>
      </div>
    </div>

    <div class="appChatbox-latestRequest" ng-if="chatbox.showLatestReq && !chatroom.infoMsg">
      <div class="latestRequest-head">Latest request:</div>
      <p class="latestRequest-title">
        <span ng-if="chatbox.latestReq.request_type=='one_on_one'">
          [One on one]
        </span>
        <span ng-if="chatbox.latestReq.request_type=='longterm'">
          [Long-term]
        </span>
        <span ng-if="chatbox.latestReq.request_type=='offline_help'">
          [Offline Help]
        </span>
        {{ chatbox.latestReq.title | truncate:190 }}
      </p>
      <a ng-href="{{ chatbox.latestReq.url }}" ng-click="chatbox.viewLatestReqDetails()" class="latestRequest-view-details" target="_blank" rel="noreferrer">View details</a>
      <a href="#" class="latestRequest-close" ng-click="chatbox.closeLatestReq()"><i class="icon-remove"></i></a>
    </div>

    <div class="appChatbox-dialog" ng-click="chatbox.actSheet=false" ng-hide="(chatroom.isMinimized && !chatbox.expanded)" prevent-body-scroll>
      <a class="appChatbox-show-more" href="#" ng-click="chatbox.more()" ng-show="showMore"><i class="icon-caret-up"></i> Load Earlier Messages</a>
      <app-chatbox-message scroll-bottom app-chatbox-object="self" contact-username="contactUsername" var-message="message" var-last-read-message-id="lastReadMessageId" ng-repeat="message in messages | orderObjectBy: 'created_at'"></app-chatbox-message>
      <div ng-show="showNoReplyMsg&&User.isUser" class="appChatbox-system-msg">
        We've noticed it may take {{responseTimeDisplay}} for {{chatroom.contact.name}} to reply to your messages.
        If you're looking for more immediate support, you can
        <a href="#" class="get-help-now" ng-click='chatbox.getHelpNow($event, "chatbox-no-reply-msg")'>get help now here</a>.
      </div>
    </div>
    <div class="appChatbox-action" ng-hide="(chatroom.isMinimized && !chatbox.expanded)">
      <div class="appChatbox-action-sheet-position">
        <div class="appChatbox-action-sheet-ul" ng-class="{'active':chatbox.actSheet}">
          <div ng-hide="User.isMentor" class="action-sheet-li" ng-click="chatbox.sendNda();chatbox.actSheet=false;"><i class="icon-file"></i> Send NDA Request</div>
          <div ng-hide="User.isMentor" class="action-sheet-li" ng-click="chatbox.attachRequest();chatbox.actSheet=false;"><i class="icon-plus-sign-alt"></i> Attach request</div>
          <div ng-hide="User.isUser" class="action-sheet-li" ng-click="chatbox.requestOfflineHelp();chatbox.actSheet=false;"><i class="icon-offline-help-request"></i> Offline Help: Request Payment</div>
          <div class="action-sheet-li" ng-click="chatbox.uploadFile();chatbox.actSheet=false;"><i class="icon-cloud-upload"></i> Upload a file</div>
        </div>
      </div>
      <i class="appChatbox-button open-action-sheet" ng-class="{'icon-circle-arrow-up':!chatbox.actSheet, 'icon-remove':chatbox.actSheet}" ng-click="chatbox.actSheet=!chatbox.actSheet" ng-hide="chatroom.isFake" ng-if="!chatroom.contact.blocked"></i>
      <i class="appChatbox-icon-blocked icon-ban-circle" ng-if="chatroom.contact.blocked"></i>
      <textarea class="appChatbox-input" ng-click="chatbox.actSheet=false" placeholder="Send a message..." msd-elastic ng-model="chatroom.input" ng-focus="chatbox.read();" ui-keydown="{
        'enter': 'chatbox.send(chatroom.input); $event.preventDefault()'
      }" ng-disabled="chatroom.contact.blocked || !chatroom.ready"></textarea>
      <i class="icon-time appChatbox-timezone-button" ng-class="{'hide': chatroom.contact.blocked || !User.isMember}" ng-click="chatbox.toggleTimezoneTool()"></i>
    </div>
  </div>
</script>

<script type="text/ng-template" id="/template/appSysChatbox.html">
  <div class="appChatbox" ng-hide="chatroom.isClosed">
    <div class="appChatbox-title clearfix">
      <a class="appChatbox-contact-name" ng-href="{{'/'}}">System Message</a>
      <span class="appChatbox-toggle-min" ng-click="chatroom.isMinimized = !chatroom.isMinimized"></span>
      <span>
        <i class="appChatbox-button icon-minimize-{{chatroom.isMinimized ? 'up' : 'down'}}" ng-click="chatroom.isMinimized = !chatroom.isMinimized"></i>
        <i class="appChatbox-button icon-remove" ng-click="chatbox.close()"></i>
      </span>
    </div>
    <div ng-show="alertMsg" class="appChatbox-extra-info red"><i class="icon-exclamation"></i> {{alertMsg}} <a ng-click="alertMsg=''" href="#" class="close"><i class="icon-remove"></i></a></div>
    <div class="appChatbox-dialog" ng-hide="(chatroom.isMinimized && !chatbox.expanded)">
      <a class="appChatbox-show-more" href="#" ng-click="chatbox.more()" ng-show="showMore"><i class="icon-caret-up"></i> Load Earlier Messages</a>
      <app-chatbox-message scroll-bottom var-message="message" var-is-last="$last" sender-img-list="senderImgList" ng-repeat="message in messages"></app-chatbox-message>
    </div>
  </div>
</script>

<script type="text/ng-template" id="modal/mentee-recent-requests.html">
  <div class="modal-header">
      <h3 class="modal-title">{{modal.config.mentee.name}}&#39;s Recent Requests</h3>
  </div>
  <div class="modal-body recent-requests">
    <div ng-if="modal.loading" style="padding: 15px 26px;"><i class="icon-spin icon-spinner"></i> Loading..</div>
    <div ng-if="!modal.loading && modal.requests.length==0" style="padding: 15px 26px;">No recent request.</div>
    <div ng-if="!modal.loading">
      <a class="recent-request row-fluid" ng-href="/questions/{{request.id}}" ng-repeat="request in modal.requests">
        <span class="span9">
          <span class="title">{{request.title}}</span>
          <span class="cates">
            <span ng-repeat="category in request.categories" class="category badget muted">{{category.name}}</span>
          </span>
        </span>
        <span class="span3">
          <span class="muted datetime text-right">
            {{request.created_at | date:'mediumDate'}}
          </span>
          <span class="budget text-right" ng-if="request.estimated_budget">
            ${{request.estimated_budget*4}}/hr
          </span>
        </span>
      </a>
    </div>
  </div>
  <hr />
  <div class="modal-footer">
    <button class="btn btn-success" ng-click="$close()">Okay</button>
  </div>
</script>

<script type="text/ng-template" id="modal/report-user.html">
  <div class="modal-body">
    <div class="row-fluid">
      <h3>Help Us Understand What&apos;s Happening</h3>
      <hr>
      <h4>This {{modal.config.isMentor ? 'mentor ...' : 'user has been:'}}</h4>

      <!-- Report user -->
      <form ng-hide="modal.config.isMentor">
        <label class="radio">
          <input type="radio" ng-model="reason" value="offensive">
          Offensive or disrespectful
        </label>
        <label class="radio">
          <input type="radio" ng-model="reason" value="ask_for_free_help">
          Asking for free help
        </label>
        <label class="radio">
          <input type="radio" ng-model="reason" value="spam">
          Posting spam
        </label>

        <label class="radio">
          <input type="radio" ng-model="reason" value="other">
          <textarea ng-model="other_reason" ng-focus="reason = 'other'" placeholder="Other reasons"></textarea>
        </label>
      </form>

      <!-- Report mentor -->
      <form ng-show="modal.config.isMentor">
        <label class="radio">
          <input type="radio" ng-model="reason" value="late">
          Was late to a session
        </label>
        <label class="radio">
          <input type="radio" ng-model="reason" value="not_show_up">
          Failed to show up for a scheduled session
        </label>
        <label class="radio">
          <input type="radio" ng-model="reason" value="harassment">
          Harassed me about ratings
        </label>

        <label class="radio">
          <input type="radio" ng-model="reason" value="other">
          <textarea ng-model="other_reason" ng-focus="reason = 'other'" placeholder="Other reasons"></textarea>
        </label>
      </form>
    </div>
  </div>
  <div class="modal-footer">
    <button class="btn btn-default" ng-click="$dismiss()">
      Cancel
    </button>
    <button class="btn btn-success" ng-click="$close({ reason: reason, other_reason: other_reason||'' })">
      Submit
    </button>
  </div>
</script>

<script type="text/ng-template" id="/template/appChatboxMessage.html">
  <div>
    <div class="appChatboxMessage clearfix" ng-class="{
      'from-self': message.sender.username == User.username,
      'showTime': message.showTime
    }">
      <div class="row-fluid gray">
        <time class="span12 show-time" ng-if='!!message.showTime'>{{message.showTime}}</time>
      </div>
      <img class="appChatboxMessage-avatar" ng-src="{{'/users/avatar/'+message.sender.username}}">
      <div title="{{message.hoverTime}}" ng-class="(message.type != 'suggestTime') ? 'appChatboxMessage-content' : 'appChatboxMessage-suggest-time-content'">
        <div class='triangle-left' ng-if="message.sender.username !== User.username"></div>
        <div class='triangle-right' ng-if="message.sender.username === User.username"></div>
        <ng-switch on="message.type">
          <p ng-switch-when="file">[File]<br><a target="_blank" ng-href="{{message.request.url}}"><b>{{message.request.filename}}</b></a><br>{{ message.request.size | fileSize }}</p>
          <p ng-switch-when="connect">Please click <a ng-click="$parent.$parent.chatbox.connect(message.sender)" href="#">Start Session</a> to start a session with me.</p>
          <p ng-switch-when="freeConnect">Let’s start a free info session by <a ng-href="/session?sid={{appChatboxObject.getChatroomID()}}">clicking here</a>.
          <p ng-switch-when="sessionLink">Please click <a ng-click="$parent.$parent.chatbox.startSessionFromLinkInChat(message.request.sessionLink)" href="#">Start Session</a> to start a session with me.</p>
          <p ng-switch-when="schedule_cluster_connect">Please click <a data-method="{{User.isMentor ? '' : 'post'}}" ng-href="{{User.isMentor ? '#' : appChatboxObject.getStartScheduleClusterSessionPath()}}">Start Session</a> to start a Codementor Monthly session with me.</p>
          <p ng-switch-when="request_offline_help">[Offline Help Request] Please create an <a ng-click="$parent.$parent.chatbox.createOfflineHelp(message.sender)" href="#">OFFLINE HELP</a> payment on Codementor.<br><a ng-click="$parent.$parent.chatbox.openOfflineHelpLearnMore()" href="#">Learn more</a></p>
          <p ng-switch-when="request">[Request]<br><a {{(User.isMentor)?'target="_blank"':''}} ng-href="/questions/{{message.request.id}}"><strong>{{message.request.title}}</strong><br><small class="muted">{{message.request.description | limitTo : 30}}{{(message.request.description.length>30)?"...":""}}</small></a></p>
          <p ng-switch-when="signature">[NDA Request]<br><span ng-show="message.request.general">{{message.request.msg}}</span><span ng-show="!message.request.general">I have initiated a Non-Disclosure Agreement request. <a ng-click="mentorStartSign(message.request.signUrl, message.request.clientId, message.request.fromUser, message.request.signatureRequestId)" href="#">CLICK HERE</a> to see how it works.</span></p>
          <div ng-switch-when="suggestTime" class="suggest-time-box">
            <div class="date-box pull-left">
              <h3>{{ timeObj.date }}</h3>
              <span>{{ timeObj.month.substr(0, 3).toUpperCase() }}</span>
            </div>
            <div class="time-box pull-right">
              <p>
                {{ timeObj.day }}
              </p>
              <p>
                {{ timeObj.hour12 }}:{{ timeObj.minute }}{{ timeObj.ampm }}
                <small>UTC {{ timeObj.utc }}</small>
              </p>
            </div>
            <div class="clearfix"></div>
            <p class="opposite-time" ng-init="oppositeAction=(User.username!=message.sender.username)?'sender':'receiver'">
              {{ message[oppositeAction].name }}: {{ opposite_timeObj.day.substr(0, 3) }}
              {{ opposite_timeObj.hour12 }}:{{ opposite_timeObj.minute }}{{ opposite_timeObj.ampm }}
              (UTC {{ opposite_timeObj.utc }})
            </p>
          </div>
          <p ng-switch-default ng-bind-html="message.content | linky: '_blank' | newLine"></p>
        </ng-switch>
        <img class="appChatboxMessage-avatar lastSeen" ng-src="{{'/users/avatar/'+message.receiver.username}}" ng-if="lastReadMessageId === message.id">
      </div>
    </div>
  </div>
</script>


<link rel="stylesheet" type="text/css" href="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/appOfflineHelp.css">
<script type="text/ng-template" id="/template/offline-help-modal.html">
  <form method="POST" action="/offline-helps" ng-submit="modal.submit($event)" style="margin-bottom:0px;">
    <form-authenticity-token></form-authenticity-token>
    <div class="modal-header">
      <h3>Pay {{modal.config.mentorName}} for Additional Offline Help</h3>
    </div>
    <div class="modal-body">
      <div class="row-fluid">
        <div class="span12">
          <input name="mentor_username" type="hidden" value="{{modal.config.mentorUsername}}">
          <p class="modal-description">Has {{modal.config.mentorName}} helped you outside of Codementor sessions? Send payment directly to {{modal.config.mentorName}} for additional offline help.</p>
        </div>
      </div>
      <div class="row-fluid">
        <div class="span2">
          <div class="colName pull-right">
            Title
          </div>
        </div>
        <div class="span10">
          <input type="text" ng-class="{inputError:modal.requiredMsgTitle}" class="offlineTitle span12" name="title" ng-model="modal.title" placeholder="What is this for?"></input>
        </div>
      </div>
      <div class="row-fluid" style="margin-bottom:10px;">
        <div class="span2">
          <div class="colName pull-right">
            Description
          </div>
        </div>
        <div class="span10">
          <textarea rows="4" class="offlineContent span12" name="content" ng-model="modal.content" placeholder="(Optional)"></textarea>
        </div>
      </div>
      <div class="row-fluid">
        <div class="span2">
          <div class="colName pull-right">
            Amount
          </div>
        </div>
        <div class="span10">
          <div class="input-prepend input-append">
            <span class="add-on"> $ </span>
            <input class="cost" name="cost" ng-blur="modal.amountBlur()" ng-model="modal.cost"></input>
            <span class="add-on"> USD </span>
          </div>
          <div class="red" ng-show="modal.errorMsg">{{modal.errorMsg}}</div>
        </div>
      </div>
      <div class="row-fluid">
        <div class="span2">
          <div class="colName pull-right">
          </div>
        </div>
        <div class="span10">
          <label class="checkbox">
            <input type="checkbox" name="delay_payment" value="true" ng-model="modal.delay_payment"></input>
            Hold payout until {{modal.config.mentorName}} confirms completion of request
          </label>
        </div>
      </div>
      <div ng-show="modal.creditCardIssue" class="row-fluid">
        <div class="span10 offset2">
          <span class="red">{{modal.creditCardIssue}}</span>&nbsp;
          Please <a href="/settings/payment">modify payment setting</a>.
          <br>
          If this issue persists, please contact us:
          <a href="mailto:support@codementor.io">
            support@codementor.io
          </a>
        </div>
      </div>
    </div>
    <div class="modal-footer text-center">
      <small class="red" ng-show="modal.requiredMsgTitle || modal.requiredMsgContent">* required field &nbsp;&nbsp;</small>
      <button class="btn" type="button" ng-disabled="modal.loading" ng-click="$dismiss()">
        <i class="icon-remove"></i>
        Cancel
      </button>
      <button type="submit" ng-class="{'btn-primary':!modal.loading}" ng-disabled="modal.loading" class="btn submit">
        <i ng-hide="modal.loading" class="icon-ok"></i>
        <img ng-show="modal.loading" src="/assets/loading_w_l.gif" style="width:16px;">
        <span>Send Payment</span>
      </button>
    </div>
  </form>
</script>

<!-- /////////// Google Code for Remarketing Tag -->
<!--
------------------------------------------------
Remarketing tags may not be associated with personally identifiable information or placed on pages related to sensitive categories. See more information and instructions on how to setup the tag on: http://google.com/ads/remarketingsetup
-------------------------------------------------
-->
<script>
  /* <![CDATA[ */
  var google_conversion_id = 996301096;
  var google_custom_params = window.google_tag_params;
  var google_remarketing_only = true;
  /* ]]> */
</script>
<div style="display:none">
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/f(1).txt" type="text/javascript"></script>
<!--[CDATA[
]]-->
</div>
<noscript>
<div style='display:inline;'>
<img alt='' height='1' src='//googleads.g.doubleclick.net/pagead/viewthroughconversion/996301096/?value=0&amp;guid=ON&amp;script=0' style='border-style:none;' width='1'>
</div>
</noscript>
<!-- /////////// End of Google Code for Remarketing Tag -->
<!-- /////////// Hellosign API -->
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/embedded.js"></script>
<script type="text/javascript" id="">!function(d,e,f,a,b,c){d.qp||(a=d.qp=function(){a.qp?a.qp.apply(a,arguments):a.queue.push(arguments)},a.queue=[],b=document.createElement(e),b.async=!0,b.src=f,c=document.getElementsByTagName(e)[0],c.parentNode.insertBefore(b,c))}(window,"script","https://a.quora.com/qevents.js");qp("init","c010797c9de84ce696f5fb046d483ab0");qp("track","ViewContent");</script>
<noscript><img height="1" width="1" style="display:none" src="https://q.quora.com/_/ad/c010797c9de84ce696f5fb046d483ab0/pixel?tag=ViewContent&amp;noscript=1"></noscript>
<script type="text/javascript" id="">window.cmTracker("event",{name:"PageView",url:google_tag_manager["GTM-MWM4HC"].macro(2),path:google_tag_manager["GTM-MWM4HC"].macro(3),referrer:google_tag_manager["GTM-MWM4HC"].macro(4),userAgent:google_tag_manager["GTM-MWM4HC"].macro(5)});"undefined"!==typeof amplitude&&amplitude.logEvent("PageView",{url:google_tag_manager["GTM-MWM4HC"].macro(6)});</script>
<script type="text/javascript" id="hs-script-loader" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/2437237.js"></script><script type="text/javascript" id="">var _hsq=window._hsq=window._hsq||[];_hsq.push(["setPath",google_tag_manager["GTM-MWM4HC"].macro(7)]);_hsq.push(["trackPageView"]);</script>
<script type="text/javascript" id="" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/js"></script>
<script type="text/javascript" id="">!function(b,e,f,g,a,c,d){b.fbq||(a=b.fbq=function(){a.callMethod?a.callMethod.apply(a,arguments):a.queue.push(arguments)},b._fbq||(b._fbq=a),a.push=a,a.loaded=!0,a.version="2.0",a.queue=[],c=e.createElement(f),c.async=!0,c.src=g,d=e.getElementsByTagName(f)[0],d.parentNode.insertBefore(c,d))}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init","159823411022603");fbq("set","agent","tmgoogletagmanager","159823411022603");fbq("track","PageView");</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=159823411022603&amp;ev=PageView&amp;noscript=1"></noscript>
<script type="text/javascript" id="">(function(b,c,e,f,d){b[d]=b[d]||[];var g=function(){var a={ti:"20081573"};a.q=b[d];b[d]=new UET(a);b[d].push("pageLoad")};var a=c.createElement(e);a.src=f;a.async=1;a.onload=a.onreadystatechange=function(){var b=this.readyState;b&&"loaded"!==b&&"complete"!==b||(g(),a.onload=a.onreadystatechange=null)};c=c.getElementsByTagName(e)[0];c.parentNode.insertBefore(a,c)})(window,document,"script","//bat.bing.com/bat.js","uetq");</script><script type="text/javascript" id="">window.cmTracker||(window.cmTracker=function(){console.log("using legacy cm_tracker")});</script>
<!-- //////////////// Twitter - site visit -->
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/oct.js" type="text/javascript"></script>
<script>
  if(typeof twttr !== 'undefined' && typeof twttr.conversion.trackPid == 'function') {
    twttr.conversion.trackPid('l4ifd');
  }
</script>
<noscript>
<img alt='' height='1' src='https://analytics.twitter.com/i/adsct?txn_id=l4ifd&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0' style='display:none;' width='1'>
<img alt='' height='1' src='//t.co/i/adsct?txn_id=l4ifd&amp;p_id=Twitter&amp;tw_sale_amount=0&amp;tw_order_quantity=0' style='display:none;' width='1'>
</noscript>
<!-- //////////////// End of Twitter -->

<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/ng_general-749d45377bb57c69b541a01b51e376654607502d58b04b2b8277809e5f373397.js"></script>
<script type="text/javascript" id="">window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date);gtag("config","AW-996301096");</script>


<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/filestack.js"></script>
<script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/ng_codementor-a9b4c573a8b3e1b15a284627f30c86792c7551ff447c3480b1bf47541b8f4ec3.js"></script>
<div class="cookie-consent ng-scope ng-hide" ng-controller="CookieConsentCtrl as cookieConsentCtrl" ng-show="show">
<div class="cookie-consent__container">
<h3>Please accept our cookies! 🍪</h3>
<i class="fa fa-times close" ng-click="close()"></i>
<p>
Codementor and its third-party tools use cookies to gather statistics and offer you personalized content and experience. Read about how we use cookies and how to withdraw your consent in our Cookie Policy. If you continue to use this site, you consent to our use of cookies.
</p>
<p class="mini">
Please accept our cookies! Read
<a href="https://www.codementor.io/cookies" target="_blank">
Cookie Policy
</a>
 🍪
</p>
<div class="actions">
<a href="https://www.codementor.io/cookies" target="_blank">
Cookie Policy
</a>
<div class="highlight-btn" ng-click="accept()">
accept cookies
</div>
</div>
<div class="bg">
<svg height="145" viewBox="0 0 148 145" width="148" xmlns="http://www.w3.org/2000/svg">
<g fill-rule="nonzero" fill="#E6E6E6" opacity=".5">
<path d="M87.725 143.445c-.432 1.019-2.194 1.285-2.947.444a94.205 94.205 0 0 1-3.396-4.79c-2.092-.091-4.17-.324-6.217-.488-1.15-.155-1.688-1.385-.812-2.266a84.907 84.907 0 0 0 3.964-4.489 198.224 198.224 0 0 1-1.264-5.905c-.238-1.142.774-2.03 1.631-1.438 1.492.855 3.022 1.411 4.642 2.127.657-.561 1.3-1.081 1.91-1.667l1.757-1.855c.643-.703 1.907-.152 2.033.896.29 1.978.55 3.967.777 5.96 1.672 1.067 3.442 2.122 5.237 2.948 1.002.533 1.02 1.866.01 2.443-1.84.938-3.798 1.592-5.729 2.399-.458 1.92-.983 3.854-1.596 5.68zM60.115 1.114C60.546.092 62.306-.172 63.059.67a94.273 94.273 0 0 1 3.399 4.79c2.09.088 4.17.323 6.217.488 1.146.154 1.685 1.385.809 2.263a88.253 88.253 0 0 0-3.962 4.49c.453 1.967.873 3.934 1.264 5.907.239 1.142-.776 2.03-1.63 1.435-1.496-.852-3.022-1.409-4.646-2.127-.653.564-1.296 1.084-1.91 1.67l-1.754 1.852c-.643.706-1.907.152-2.033-.894-.29-1.978-.549-3.966-.78-5.962-1.668-1.064-3.439-2.122-5.233-2.945-1.002-.536-1.02-1.866-.011-2.446 1.838-.936 3.796-1.589 5.73-2.396.455-1.923.98-3.855 1.596-5.681zm86.754 57.698c1.047.42 1.318 2.138.455 2.872a93.927 93.927 0 0 1-4.91 3.316c-.09 2.038-.332 4.068-.5 6.062-.158 1.121-1.417 1.646-2.32.792a89.235 89.235 0 0 0-4.602-3.865c-2.017.442-4.036.852-6.056 1.23-1.17.236-2.079-.754-1.473-1.588.876-1.458 1.446-2.947 2.183-4.53-.579-.638-1.11-1.268-1.712-1.861l-1.902-1.714c-.717-.628-.152-1.86.922-1.984 2.028-.282 4.063-.535 6.107-.757 1.093-1.631 2.178-3.36 3.021-5.109.547-.977 1.913-.996 2.508-.01.958 1.792 1.628 3.702 2.458 5.589 1.97.444 3.949.956 5.821 1.557zm-2.888 37.371c.7.878.086 2.511-1.028 2.73a68.248 68.248 0 0 1-5.992.463c-1.179 1.701-2.264 3.423-3.501 5.033-.78.857-2.175.677-2.462-.473-.48-1.868-1.264-3.794-1.982-5.579a205.976 205.976 0 0 1-5.858-1.879c-1.128-.365-1.438-1.674-.504-2.11.718-.43 1.487-.858 2.189-1.333l2.044-1.513c-.394-1.68-.657-3.246-1.283-4.85-.322-.896.776-1.696 1.775-1.28 1.908.744 3.807 1.518 5.7 2.32 1.728-.894 3.563-1.86 5.27-2.948.945-.588 2.19.07 2.16 1.207l-.709 6.047c1.454 1.338 2.81 2.712 4.181 4.165zm-21.635 30.971c.193 1.142-1.168 2.26-2.288 1.853a99.832 99.832 0 0 1-5.456-2.548c-.924.48-1.803 1.011-2.75 1.432l-2.861 1.21c-1.09.4-2.197-.413-1.878-1.581.477-1.96.881-3.854 1.181-5.73a210.748 210.748 0 0 1-4.138-4.508c-.79-.87-.343-2.09.64-2.082a119.49 119.49 0 0 0 5.161-.374c.501-1.678.949-3.303 1.35-4.876.255-.865 1.549-1.09 2.21-.23a215.42 215.42 0 0 1 3.77 4.818 88.9 88.9 0 0 0 5.991-.057c1.165-.008 1.848 1.126 1.24 2.093-1.154 1.672-2.322 3.368-3.712 4.881a94.202 94.202 0 0 1 1.54 5.7zm-72.93 13.471c-.9.685-2.574.084-2.799-1a64.368 64.368 0 0 1-.476-5.846c-1.742-1.152-3.507-2.21-5.16-3.418-.875-.76-.693-2.12.488-2.401 1.915-.465 3.89-1.231 5.716-1.934a202.062 202.062 0 0 1 1.926-5.712c.378-1.1 1.72-1.406 2.167-.494.44.7.879 1.453 1.366 2.138l1.548 1.99c1.725-.38 3.33-.64 4.972-1.248.921-.314 1.74.757 1.312 1.73a194.2 194.2 0 0 1-2.376 5.563c.914 1.682 1.907 3.475 3.022 5.137.6.925-.075 2.137-1.238 2.111l-6.2-.695c-1.37 1.419-2.778 2.741-4.268 4.079zm-31.75-21.103c-1.17.185-2.315-1.142-1.9-2.232.828-1.829 1.699-3.6 2.612-5.325-.49-.899-1.036-1.756-1.468-2.684l-1.24-2.788c-.41-1.066.426-2.145 1.623-1.832 2.01.463 3.949.86 5.875 1.153a199.199 199.199 0 0 1 4.62-4.037c.892-.774 2.143-.337 2.135.622.09 1.617.206 3.305.383 5.037 1.72.49 3.386.925 4.995 1.315.89.25 1.117 1.513.236 2.156a206.283 206.283 0 0 1-4.936 3.676 82.609 82.609 0 0 0 .058 5.848c.006 1.134-1.157 1.8-2.145 1.207-1.714-1.126-3.453-2.265-5.006-3.619-1.902.552-3.85 1.05-5.842 1.503zM.969 85.746c-1.045-.42-1.318-2.137-.455-2.874a95.524 95.524 0 0 1 4.91-3.313c.093-2.039.332-4.069.5-6.065.158-1.119 1.42-1.644 2.32-.79a89.235 89.235 0 0 0 4.602 3.865c2.017-.441 4.037-.852 6.056-1.233 1.17-.233 2.079.755 1.473 1.591-.876 1.458-1.446 2.948-2.183 4.529.579.64 1.11 1.267 1.712 1.863l1.902 1.714c.72.627.152 1.858-.919 1.98-2.03.285-4.066.536-6.11.761-1.093 1.63-2.178 3.358-3.021 5.108-.547.975-1.913.996-2.507.01-.96-1.794-1.629-3.704-2.457-5.588-1.968-.445-3.95-.96-5.823-1.558zm2.89-37.37c-.702-.878-.086-2.514 1.025-2.731a69.246 69.246 0 0 1 5.995-.465c1.179-1.699 2.263-3.42 3.5-5.03.78-.857 2.176-.677 2.463.473.479 1.868 1.261 3.791 1.982 5.578 1.966.596 3.918 1.226 5.855 1.88 1.128.365 1.438 1.674.506 2.108-.718.431-1.489.86-2.19 1.335l-2.042 1.51c.394 1.683.656 3.249 1.28 4.853.322.896-.776 1.696-1.773 1.28a204.623 204.623 0 0 1-5.7-2.323c-1.727.894-3.565 1.86-5.268 2.95-.946.586-2.192-.073-2.165-1.207l.713-6.049c-1.457-1.335-2.81-2.71-4.182-4.162zm21.633-30.974c-.193-1.142 1.168-2.258 2.288-1.853a99.85 99.85 0 0 1 5.456 2.55c.924-.48 1.803-1.01 2.75-1.431l2.862-1.21c1.092-.4 2.196.413 1.877 1.58-.474 1.96-.881 3.855-1.181 5.731a192.206 192.206 0 0 1 4.138 4.508c.79.87.343 2.09-.64 2.082a119.49 119.49 0 0 0-5.161.374 127.36 127.36 0 0 0-1.35 4.873c-.255.868-1.549 1.09-2.21.23a204.077 204.077 0 0 1-3.769-4.818 90.715 90.715 0 0 0-5.992.06c-1.162.005-1.848-1.126-1.24-2.093 1.157-1.675 2.322-3.368 3.712-4.881a94.812 94.812 0 0 1-1.54-5.702zm72.931-13.47c.9-.683 2.574-.082 2.8 1.002.238 1.94.412 3.85.474 5.846 1.743 1.152 3.508 2.208 5.158 3.418.879.76.694 2.119-.484 2.401-1.918.465-3.89 1.23-5.72 1.934a196.48 196.48 0 0 1-1.925 5.712c-.375 1.1-1.717 1.403-2.164.494-.442-.703-.879-1.456-1.37-2.138l-1.547-1.994c-1.723.385-3.33.643-4.972 1.25-.918.313-1.74-.756-1.312-1.73.763-1.86 1.556-3.713 2.378-5.56-.913-1.686-1.907-3.476-3.024-5.14-.6-.923.075-2.138 1.238-2.11l6.203.693c1.37-1.419 2.778-2.738 4.267-4.079zm31.75 21.105c1.17-.188 2.314 1.142 1.899 2.231a95.288 95.288 0 0 1-2.612 5.323c.49.902 1.037 1.759 1.468 2.686l1.24 2.788c.41 1.066-.426 2.146-1.623 1.832-2.01-.462-3.948-.86-5.874-1.152a193.686 193.686 0 0 1-4.62 4.034c-.893.774-2.144.34-2.136-.622a110.737 110.737 0 0 0-.383-5.035c-1.72-.489-3.385-.925-4.995-1.317-.89-.248-1.117-1.51-.236-2.153a206.378 206.378 0 0 1 4.937-3.68 82.55 82.55 0 0 0-.06-5.845c-.005-1.134 1.158-1.803 2.146-1.21 1.717 1.127 3.453 2.269 5.006 3.622a99.94 99.94 0 0 1 5.842-1.502zM90.34 64.365c4.973 1.633 8.59 6.174 8.59 11.573v14.021c0 6.76-5.64 12.258-12.569 12.258H61.477c-6.929 0-12.567-5.498-12.567-12.258V75.938c0-5.399 3.616-9.94 8.59-11.573v-6.008c0-8.832 7.366-16.018 16.42-16.018 9.053 0 16.42 7.186 16.42 16.018v6.008zm3.232 25.594V75.938c0-3.88-3.236-7.037-7.21-7.037H61.477c-3.978 0-7.211 3.156-7.211 7.037v14.021c0 3.878 3.233 7.032 7.21 7.032h24.884c3.975 0 7.211-3.154 7.211-7.032zM73.92 47.565c-6.099 0-11.062 4.842-11.062 10.792v5.318h22.125v-5.318c0-5.95-4.963-10.792-11.063-10.792zm4.7 33.614c0 1.829-1.104 3.394-2.69 4.128v6.499h-4.017v-6.499c-1.589-.734-2.692-2.302-2.692-4.128 0-2.532 2.103-4.586 4.7-4.586 2.594 0 4.699 2.054 4.699 4.586z"></path>
</g>
</svg>
</div>
</div>
</div>




<iframe name="filepicker_comm_iframe" id="filepicker_comm_iframe" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/saved_resource(1).html" style="display: none;"></iframe><iframe name="fpapi_comm_iframe" id="fpapi_comm_iframe" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/saved_resource(2).html" style="display: none;"></iframe><div id="diigo-video-capture" style="display: none;"><div id="diigo-video-capture-container"><div id="diigo-video-capture-logo"></div>Capture</div></div><div id="diigo-video-capture-wrapper"><div id="diigo-video-capture-wrapper-tip">Drag to outliner or <span id="diigo-video-capture-upload">Upload</span></div><div id="diigo-video-capture-wrapper-close">Close</div></div><div class="diigolet notice" id="diigolet-notice" style="display: none;"><div><b>&nbsp;</b><p>Ok, done!</p><span id="close"></span></div></div><div id="diigolet-dlg-sticky" style="position: absolute; left: 100px; top: 100px; display: none;" class="diigolet diigoletFN yellow"><div id="diigolet-dlg-sticky-top" class="_dragHandle" style="cursor: move;"><span id="diigolet-dlg-sticky-close"></span><span id="diigolet-dlg-sticky-color"><div id="diigolet-dlg-sticky-currentColor" title="change color"></div><div id="diigolet-dlg-sticky-colorPicker" style="display: none;"><b color="yellow" id="diigolet-dlg-yellow" class="dlg-colorItem colorchecked"><b></b></b><b color="blue" id="diigolet-dlg-blue" class="dlg-colorItem"><b></b></b><b color="green" id="diigolet-dlg-green" class="dlg-colorItem"><b></b></b><b color="pink" id="diigolet-dlg-pink" class="dlg-colorItem"><b></b></b></div></span><span id="diigolet-dlg-sticky-addTab"></span></div><div id="diigolet-dlg-sticky-content" class="private"><div id="diigolet-dlg-sticky-switcher"><span class="FN-switcher" id="FN-switcher-private"><b></b>Private</span><span class="FN-switcher" id="FN-switcher-group"><b></b>Group</span></div><div class="FN-content-wrapper private"><textarea id="FN-private-editor" placeholder="Input here..."></textarea><div id="FN-content-footer"><div id="editDone"><span id="FN-private-delete"><b></b></span><span id="FN-private-datetime"></span></div><div id="editing"><a href="javascript:void(0)" id="FN-private-saveBtn">Save</a><a href="javascript:void(0)" id="FN-private-cancelBtn">Cancel</a></div></div></div><div class="FN-content-wrapper group"><div><div id="FN-group-content-nav"><span id="FN-current-group"><span>+Share to a new group</span><b></b></span><div id="FN-group-menu" style="display: none;"><ul id="FN-group-ul"></ul><ul id="FN-group-share-new-ul"><li id="FN-group-share-new">+Share to a new group</li></ul></div></div><div id="FN-post-form" class=""><div><textarea id="FN-group-post" placeholder="write a comment..."></textarea></div><div><select id="FN-group-share"></select><button><span class="button-label">Post</span><span class="button-spinner"></span></button><a href="javascript:void(0)">Cancel</a></div></div><div id="FN-group-content"><div id="FN-group-content-container"></div><div id="FN-group-content-postform"><textarea placeholder="Write a comment..."></textarea><div class="post-action"><button><span class="button-label">Post</span><span class="button-spinner"></span></button><a href="javascript:void(0)">Cancel</a></div></div></div></div></div></div></div><div id="diigolet-csm" class="yellow" style="position: absolute; left: 532px; top: 481px; display: none;"><div id="diigolet-csm-research-mode"></div><div id="diigolet-csm-highlight-wrapper" class="csm-btn"><a id="diigolet-csm-highlight" class="csm-action" title="Highlight" href="javascript:void(0);"></a><div class="diigolet-csm-color small hidden" style="height: 0px;"><a class="diigolet-csm-coloritem yellow" data-color="yellow" style="height: 0px;"></a><a class="diigolet-csm-coloritem blue" data-color="blue" style="height: 0px;"></a><a class="diigolet-csm-coloritem green" data-color="green" style="height: 0px;"></a><a class="diigolet-csm-coloritem pink" data-color="pink" style="height: 0px;"></a></div></div><div id="diigolet-csm-highlightAndComment-wrapper" class="csm-btn"><a id="diigolet-csm-highlightAndComment" class="csm-action" title="Highlight &amp; Sticky note" href="javascript:void(0);"></a><div class="diigolet-csm-color small hidden" style="height: 0px;"><a class="diigolet-csm-coloritem yellow" data-color="yellow" style="height: 0px;"></a><a class="diigolet-csm-coloritem blue" data-color="blue" style="height: 0px;"></a><a class="diigolet-csm-coloritem green" data-color="green" style="height: 0px;"></a><a class="diigolet-csm-coloritem pink" data-color="pink" style="height: 0px;"></a></div></div><a id="diigolet-csm-search" class="csm-action" title="Search in Google" href="javascript:void(0);"></a></div><div id="diigo-chrome-installed" style="display: none;"></div><iframe style="display: none;" src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/saved_resource(3).html"></iframe><div id="cke_editor1" class="cke cke_1 cke_reset_all cke_chrome cke_editor_editor1 cke_float cke_ltr cke_browser_webkit" dir="ltr" title="" lang="en" role="application" style="display: none; z-index: 9999; user-select: none;" aria-labelledby="cke_editor1_arialbl"><span id="cke_editor1_arialbl" class="cke_voice_label">Rich Text Editor, editor1</span><div class="cke_inner"><div id="cke_1_top" class="cke_top" role="presentation"><span id="cke_9" class="cke_voice_label">Editor toolbars</span><span id="cke_1_toolbox" class="cke_toolbox" role="group" aria-labelledby="cke_9" onmousedown="return false;"><span id="cke_12" class="cke_toolbar" aria-labelledby="cke_12_label" role="toolbar"><span id="cke_12_label" class="cke_voice_label">Clipboard/Undo</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_13" class="cke_button cke_button__cut cke_button_disabled " href="javascript:void(&#39;Cut&#39;)" title="Cut" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_13_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(2,event);" onfocus="return CKEDITOR.tools.callFunction(3,event);" onclick="CKEDITOR.tools.callFunction(4,this);return false;"><span class="cke_button_icon cke_button__cut_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -264px;background-size:auto;">&nbsp;</span><span id="cke_13_label" class="cke_button_label cke_button__cut_label" aria-hidden="false">Cut</span></a><a id="cke_14" class="cke_button cke_button__copy cke_button_disabled " href="javascript:void(&#39;Copy&#39;)" title="Copy" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_14_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(5,event);" onfocus="return CKEDITOR.tools.callFunction(6,event);" onclick="CKEDITOR.tools.callFunction(7,this);return false;"><span class="cke_button_icon cke_button__copy_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -216px;background-size:auto;">&nbsp;</span><span id="cke_14_label" class="cke_button_label cke_button__copy_label" aria-hidden="false">Copy</span></a><a id="cke_15" class="cke_button cke_button__paste cke_button_disabled " href="javascript:void(&#39;Paste&#39;)" title="Paste" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_15_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(8,event);" onfocus="return CKEDITOR.tools.callFunction(9,event);" onclick="CKEDITOR.tools.callFunction(10,this);return false;"><span class="cke_button_icon cke_button__paste_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -312px;background-size:auto;">&nbsp;</span><span id="cke_15_label" class="cke_button_label cke_button__paste_label" aria-hidden="false">Paste</span></a><a id="cke_16" class="cke_button cke_button__pastetext cke_button_disabled " href="javascript:void(&#39;Paste as plain text&#39;)" title="Paste as plain text" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_16_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(11,event);" onfocus="return CKEDITOR.tools.callFunction(12,event);" onclick="CKEDITOR.tools.callFunction(13,this);return false;"><span class="cke_button_icon cke_button__pastetext_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -720px;background-size:auto;">&nbsp;</span><span id="cke_16_label" class="cke_button_label cke_button__pastetext_label" aria-hidden="false">Paste as plain text</span></a><a id="cke_17" class="cke_button cke_button__pastefromword cke_button_disabled " href="javascript:void(&#39;Paste from Word&#39;)" title="Paste from Word" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_17_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(14,event);" onfocus="return CKEDITOR.tools.callFunction(15,event);" onclick="CKEDITOR.tools.callFunction(16,this);return false;"><span class="cke_button_icon cke_button__pastefromword_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -768px;background-size:auto;">&nbsp;</span><span id="cke_17_label" class="cke_button_label cke_button__pastefromword_label" aria-hidden="false">Paste from Word</span></a><span class="cke_toolbar_separator" role="separator"></span><a id="cke_18" class="cke_button cke_button__undo cke_button_disabled " href="javascript:void(&#39;Undo&#39;)" title="Undo" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_18_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(17,event);" onfocus="return CKEDITOR.tools.callFunction(18,event);" onclick="CKEDITOR.tools.callFunction(19,this);return false;"><span class="cke_button_icon cke_button__undo_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -1008px;background-size:auto;">&nbsp;</span><span id="cke_18_label" class="cke_button_label cke_button__undo_label" aria-hidden="false">Undo</span></a><a id="cke_19" class="cke_button cke_button__redo cke_button_disabled " href="javascript:void(&#39;Redo&#39;)" title="Redo" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_19_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(20,event);" onfocus="return CKEDITOR.tools.callFunction(21,event);" onclick="CKEDITOR.tools.callFunction(22,this);return false;"><span class="cke_button_icon cke_button__redo_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -960px;background-size:auto;">&nbsp;</span><span id="cke_19_label" class="cke_button_label cke_button__redo_label" aria-hidden="false">Redo</span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_20" class="cke_toolbar" aria-labelledby="cke_20_label" role="toolbar"><span id="cke_20_label" class="cke_voice_label">Editing</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_21" class="cke_button cke_button__scayt cke_button_off " href="javascript:void(&#39;Spell Checker&#39;)" title="Spell Checker" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_21_label" aria-haspopup="true" aria-disabled="false" onkeydown="return CKEDITOR.tools.callFunction(23,event);" onfocus="return CKEDITOR.tools.callFunction(24,event);" onclick="CKEDITOR.tools.callFunction(25,this);return false;"><span class="cke_button_icon cke_button__scayt_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -888px;background-size:auto;">&nbsp;</span><span id="cke_21_label" class="cke_button_label cke_button__scayt_label" aria-hidden="false">Spell Check As You Type</span><span class="cke_button_arrow"></span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_22" class="cke_toolbar" aria-labelledby="cke_22_label" role="toolbar"><span id="cke_22_label" class="cke_voice_label">Links</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_23" class="cke_button cke_button__link cke_button_disabled " href="javascript:void(&#39;Link&#39;)" title="Link" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_23_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(26,event);" onfocus="return CKEDITOR.tools.callFunction(27,event);" onclick="CKEDITOR.tools.callFunction(28,this);return false;"><span class="cke_button_icon cke_button__link_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -528px;background-size:auto;">&nbsp;</span><span id="cke_23_label" class="cke_button_label cke_button__link_label" aria-hidden="false">Link</span></a><a id="cke_24" class="cke_button cke_button__unlink cke_button_disabled " href="javascript:void(&#39;Unlink&#39;)" title="Unlink" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_24_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(29,event);" onfocus="return CKEDITOR.tools.callFunction(30,event);" onclick="CKEDITOR.tools.callFunction(31,this);return false;"><span class="cke_button_icon cke_button__unlink_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -552px;background-size:auto;">&nbsp;</span><span id="cke_24_label" class="cke_button_label cke_button__unlink_label" aria-hidden="false">Unlink</span></a><a id="cke_25" class="cke_button cke_button__anchor cke_button_disabled " href="javascript:void(&#39;Anchor&#39;)" title="Anchor" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_25_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(32,event);" onfocus="return CKEDITOR.tools.callFunction(33,event);" onclick="CKEDITOR.tools.callFunction(34,this);return false;"><span class="cke_button_icon cke_button__anchor_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -504px;background-size:auto;">&nbsp;</span><span id="cke_25_label" class="cke_button_label cke_button__anchor_label" aria-hidden="false">Anchor</span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_26" class="cke_toolbar" aria-labelledby="cke_26_label" role="toolbar"><span id="cke_26_label" class="cke_voice_label">Insert</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_27" class="cke_button cke_button__image cke_button_disabled " href="javascript:void(&#39;Image&#39;)" title="Image" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_27_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(35,event);" onfocus="return CKEDITOR.tools.callFunction(36,event);" onclick="CKEDITOR.tools.callFunction(37,this);return false;"><span class="cke_button_icon cke_button__image_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -360px;background-size:auto;">&nbsp;</span><span id="cke_27_label" class="cke_button_label cke_button__image_label" aria-hidden="false">Image</span></a><a id="cke_28" class="cke_button cke_button__codesnippet cke_button_disabled " href="javascript:void(&#39;Insert Code Snippet&#39;)" title="Insert Code Snippet" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_28_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(38,event);" onfocus="return CKEDITOR.tools.callFunction(39,event);" onclick="CKEDITOR.tools.callFunction(40,this);return false;"><span class="cke_button_icon cke_button__codesnippet_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -1056px;background-size:auto;">&nbsp;</span><span id="cke_28_label" class="cke_button_label cke_button__codesnippet_label" aria-hidden="false">Insert Code Snippet</span></a><a id="cke_29" class="cke_button cke_button__table cke_button_disabled " href="javascript:void(&#39;Table&#39;)" title="Table" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_29_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(41,event);" onfocus="return CKEDITOR.tools.callFunction(42,event);" onclick="CKEDITOR.tools.callFunction(43,this);return false;"><span class="cke_button_icon cke_button__table_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -912px;background-size:auto;">&nbsp;</span><span id="cke_29_label" class="cke_button_label cke_button__table_label" aria-hidden="false">Table</span></a><a id="cke_30" class="cke_button cke_button__horizontalrule cke_button_disabled " href="javascript:void(&#39;Insert Horizontal Line&#39;)" title="Insert Horizontal Line" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_30_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(44,event);" onfocus="return CKEDITOR.tools.callFunction(45,event);" onclick="CKEDITOR.tools.callFunction(46,this);return false;"><span class="cke_button_icon cke_button__horizontalrule_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -336px;background-size:auto;">&nbsp;</span><span id="cke_30_label" class="cke_button_label cke_button__horizontalrule_label" aria-hidden="false">Insert Horizontal Line</span></a><a id="cke_31" class="cke_button cke_button__specialchar cke_button_disabled " href="javascript:void(&#39;Insert Special Character&#39;)" title="Insert Special Character" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_31_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(47,event);" onfocus="return CKEDITOR.tools.callFunction(48,event);" onclick="CKEDITOR.tools.callFunction(49,this);return false;"><span class="cke_button_icon cke_button__specialchar_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -864px;background-size:auto;">&nbsp;</span><span id="cke_31_label" class="cke_button_label cke_button__specialchar_label" aria-hidden="false">Insert Special Character</span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_32" class="cke_toolbar" aria-labelledby="cke_32_label" role="toolbar"><span id="cke_32_label" class="cke_voice_label">Tools</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_33" class="cke_button cke_button__maximize cke_button_disabled " href="javascript:void(&#39;Maximize&#39;)" title="Maximize" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_33_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(50,event);" onfocus="return CKEDITOR.tools.callFunction(51,event);" onclick="CKEDITOR.tools.callFunction(52,this);return false;"><span class="cke_button_icon cke_button__maximize_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -672px;background-size:auto;">&nbsp;</span><span id="cke_33_label" class="cke_button_label cke_button__maximize_label" aria-hidden="false">Maximize</span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_34" class="cke_toolbar" aria-labelledby="cke_34_label" role="toolbar"><span id="cke_34_label" class="cke_voice_label">Document</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_35" class="cke_button cke_button__source cke_button_disabled " href="javascript:void(&#39;Source&#39;)" title="Source" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_35_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(53,event);" onfocus="return CKEDITOR.tools.callFunction(54,event);" onclick="CKEDITOR.tools.callFunction(55,this);return false;"><span class="cke_button_icon cke_button__source_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -840px;background-size:auto;">&nbsp;</span><span id="cke_35_label" class="cke_button_label cke_button__source_label" aria-hidden="false">Source</span></a></span><span class="cke_toolbar_end"></span></span><span class="cke_toolbar_break"></span><span id="cke_36" class="cke_toolbar" aria-labelledby="cke_36_label" role="toolbar"><span id="cke_36_label" class="cke_voice_label">Basic Styles</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_37" class="cke_button cke_button__bold cke_button_disabled " href="javascript:void(&#39;Bold&#39;)" title="Bold" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_37_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(56,event);" onfocus="return CKEDITOR.tools.callFunction(57,event);" onclick="CKEDITOR.tools.callFunction(58,this);return false;"><span class="cke_button_icon cke_button__bold_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -24px;background-size:auto;">&nbsp;</span><span id="cke_37_label" class="cke_button_label cke_button__bold_label" aria-hidden="false">Bold</span></a><a id="cke_38" class="cke_button cke_button__italic cke_button_disabled " href="javascript:void(&#39;Italic&#39;)" title="Italic" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_38_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(59,event);" onfocus="return CKEDITOR.tools.callFunction(60,event);" onclick="CKEDITOR.tools.callFunction(61,this);return false;"><span class="cke_button_icon cke_button__italic_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -48px;background-size:auto;">&nbsp;</span><span id="cke_38_label" class="cke_button_label cke_button__italic_label" aria-hidden="false">Italic</span></a><a id="cke_39" class="cke_button cke_button__strike cke_button_disabled " href="javascript:void(&#39;Strikethrough&#39;)" title="Strikethrough" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_39_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(62,event);" onfocus="return CKEDITOR.tools.callFunction(63,event);" onclick="CKEDITOR.tools.callFunction(64,this);return false;"><span class="cke_button_icon cke_button__strike_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -72px;background-size:auto;">&nbsp;</span><span id="cke_39_label" class="cke_button_label cke_button__strike_label" aria-hidden="false">Strikethrough</span></a><span class="cke_toolbar_separator" role="separator"></span><a id="cke_40" class="cke_button cke_button__removeformat cke_button_disabled " href="javascript:void(&#39;Remove Format&#39;)" title="Remove Format" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_40_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(65,event);" onfocus="return CKEDITOR.tools.callFunction(66,event);" onclick="CKEDITOR.tools.callFunction(67,this);return false;"><span class="cke_button_icon cke_button__removeformat_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -792px;background-size:auto;">&nbsp;</span><span id="cke_40_label" class="cke_button_label cke_button__removeformat_label" aria-hidden="false">Remove Format</span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_41" class="cke_toolbar" aria-labelledby="cke_41_label" role="toolbar"><span id="cke_41_label" class="cke_voice_label">Paragraph</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_42" class="cke_button cke_button__numberedlist cke_button_disabled " href="javascript:void(&#39;Insert/Remove Numbered List&#39;)" title="Insert/Remove Numbered List" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_42_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(68,event);" onfocus="return CKEDITOR.tools.callFunction(69,event);" onclick="CKEDITOR.tools.callFunction(70,this);return false;"><span class="cke_button_icon cke_button__numberedlist_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -648px;background-size:auto;">&nbsp;</span><span id="cke_42_label" class="cke_button_label cke_button__numberedlist_label" aria-hidden="false">Insert/Remove Numbered List</span></a><a id="cke_43" class="cke_button cke_button__bulletedlist cke_button_disabled " href="javascript:void(&#39;Insert/Remove Bulleted List&#39;)" title="Insert/Remove Bulleted List" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_43_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(71,event);" onfocus="return CKEDITOR.tools.callFunction(72,event);" onclick="CKEDITOR.tools.callFunction(73,this);return false;"><span class="cke_button_icon cke_button__bulletedlist_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -600px;background-size:auto;">&nbsp;</span><span id="cke_43_label" class="cke_button_label cke_button__bulletedlist_label" aria-hidden="false">Insert/Remove Bulleted List</span></a><span class="cke_toolbar_separator" role="separator"></span><a id="cke_44" class="cke_button cke_button__outdent cke_button_disabled " href="javascript:void(&#39;Decrease Indent&#39;)" title="Decrease Indent" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_44_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(74,event);" onfocus="return CKEDITOR.tools.callFunction(75,event);" onclick="CKEDITOR.tools.callFunction(76,this);return false;"><span class="cke_button_icon cke_button__outdent_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -456px;background-size:auto;">&nbsp;</span><span id="cke_44_label" class="cke_button_label cke_button__outdent_label" aria-hidden="false">Decrease Indent</span></a><a id="cke_45" class="cke_button cke_button__indent cke_button_disabled " href="javascript:void(&#39;Increase Indent&#39;)" title="Increase Indent" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_45_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(77,event);" onfocus="return CKEDITOR.tools.callFunction(78,event);" onclick="CKEDITOR.tools.callFunction(79,this);return false;"><span class="cke_button_icon cke_button__indent_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -408px;background-size:auto;">&nbsp;</span><span id="cke_45_label" class="cke_button_label cke_button__indent_label" aria-hidden="false">Increase Indent</span></a><span class="cke_toolbar_separator" role="separator"></span><a id="cke_46" class="cke_button cke_button__blockquote cke_button_disabled " href="javascript:void(&#39;Block Quote&#39;)" title="Block Quote" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_46_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(80,event);" onfocus="return CKEDITOR.tools.callFunction(81,event);" onclick="CKEDITOR.tools.callFunction(82,this);return false;"><span class="cke_button_icon cke_button__blockquote_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -168px;background-size:auto;">&nbsp;</span><span id="cke_46_label" class="cke_button_label cke_button__blockquote_label" aria-hidden="false">Block Quote</span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_47" class="cke_toolbar" aria-labelledby="cke_47_label" role="toolbar"><span id="cke_47_label" class="cke_voice_label">Styles</span><span class="cke_toolbar_start"></span><span id="cke_10" class="cke_combo cke_combo__styles " role="presentation"><span id="cke_10_label" class="cke_combo_label">Styles</span><a class="cke_combo_button" title="Formatting Styles" tabindex="-1" href="javascript:void(&#39;Formatting Styles&#39;)" hidefocus="true" role="button" aria-labelledby="cke_10_label" aria-haspopup="true" onkeydown="return CKEDITOR.tools.callFunction(84,event,this);" onfocus="return CKEDITOR.tools.callFunction(85,event);" onclick="CKEDITOR.tools.callFunction(83,this);return false;"><span id="cke_10_text" class="cke_combo_text cke_combo_inlinelabel">Styles</span><span class="cke_combo_open"><span class="cke_combo_arrow"></span></span></a></span><span id="cke_11" class="cke_combo cke_combo__format " role="presentation"><span id="cke_11_label" class="cke_combo_label">Format</span><a class="cke_combo_button" title="Paragraph Format" tabindex="-1" href="javascript:void(&#39;Paragraph Format&#39;)" hidefocus="true" role="button" aria-labelledby="cke_11_label" aria-haspopup="true" onkeydown="return CKEDITOR.tools.callFunction(87,event,this);" onfocus="return CKEDITOR.tools.callFunction(88,event);" onclick="CKEDITOR.tools.callFunction(86,this);return false;"><span id="cke_11_text" class="cke_combo_text cke_combo_inlinelabel">Format</span><span class="cke_combo_open"><span class="cke_combo_arrow"></span></span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_48" class="cke_toolbar" aria-labelledby="cke_48_label" role="toolbar"><span id="cke_48_label" class="cke_voice_label">Colors</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_49" class="cke_button cke_button__textcolor cke_button_off " href="javascript:void(&#39;Text Color&#39;)" title="Text Color" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_49_label" aria-haspopup="true" aria-disabled="false" onkeydown="return CKEDITOR.tools.callFunction(89,event);" onfocus="return CKEDITOR.tools.callFunction(90,event);" onclick="CKEDITOR.tools.callFunction(91,this);return false;"><span class="cke_button_icon cke_button__textcolor_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -1104px;background-size:auto;">&nbsp;</span><span id="cke_49_label" class="cke_button_label cke_button__textcolor_label" aria-hidden="false">Text Color</span><span class="cke_button_arrow"></span></a><a id="cke_50" class="cke_button cke_button__bgcolor cke_button_off " href="javascript:void(&#39;Background Color&#39;)" title="Background Color" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_50_label" aria-haspopup="true" aria-disabled="false" onkeydown="return CKEDITOR.tools.callFunction(92,event);" onfocus="return CKEDITOR.tools.callFunction(93,event);" onclick="CKEDITOR.tools.callFunction(94,this);return false;"><span class="cke_button_icon cke_button__bgcolor_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 -1080px;background-size:auto;">&nbsp;</span><span id="cke_50_label" class="cke_button_label cke_button__bgcolor_label" aria-hidden="false">Background Color</span><span class="cke_button_arrow"></span></a></span><span class="cke_toolbar_end"></span></span><span id="cke_51" class="cke_toolbar" aria-labelledby="cke_51_label" role="toolbar"><span id="cke_51_label" class="cke_voice_label">about</span><span class="cke_toolbar_start"></span><span class="cke_toolgroup" role="presentation"><a id="cke_52" class="cke_button cke_button__about cke_button_disabled " href="javascript:void(&#39;About CKEditor&#39;)" title="About CKEditor" tabindex="-1" hidefocus="true" role="button" aria-labelledby="cke_52_label" aria-haspopup="false" aria-disabled="true" onkeydown="return CKEDITOR.tools.callFunction(95,event);" onfocus="return CKEDITOR.tools.callFunction(96,event);" onclick="CKEDITOR.tools.callFunction(97,this);return false;"><span class="cke_button_icon cke_button__about_icon" style="background-image:url(https://cdn.codementor.io/assets/lib/ckeditor/plugins/icons.png?t=EAPE);background-position:0 0px;background-size:auto;">&nbsp;</span><span id="cke_52_label" class="cke_button_label cke_button__about_label" aria-hidden="false">About CKEditor</span></a></span><span class="cke_toolbar_end"></span></span></span></div></div></div><script src="./Learning to make stuff with computers_ from CPUs to Haskell Web Apps Quick Tips _ Codementor_files/s.js"></script></body></html>
