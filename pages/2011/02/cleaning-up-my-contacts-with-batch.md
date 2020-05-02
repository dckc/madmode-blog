date: 2011-02-02
published: true
tags: [microformats, mobile, cloud, contacts, free culture, python, programming,
  android, pim]
title: Cleaning up my contacts with batch edits in the Google Contacts Data API
updated: 2011-09-23


The <a href="http://en.wikinews.org/wiki/Massive_snowstorm_blasts_most_of_United_States">Blizzard of Oz</a>&nbsp;snow day gave me a chance to get my taxes done yesterday, and today I used the time to scratch a long-standing itch to clean up my contacts, which have been a bit of a mess since I merged two sources into one.<br />
<br />
<a name='more'></a><br />
<br />
When I got my first android phone, a G1, I used&nbsp;the <a href="http://code.google.com/apis/contacts/docs/1.0/developers_guide_python.html">Google Contacts Data API</a>&nbsp;to write&nbsp;<a href="https://bitbucket.org/DanC/palmagent/src/c87196981537/hipg.py">hipg.py</a> for migrating my sidekick/hiptop contacts to gmail contacts. Then I grew disappointed with the G1 and went <a href="http://www.advogato.org/diary/edit.html?key=68">back to the sidekick</a>. And then Microsoft bought Danger and lost everybody's sidekick contacts for a week or so. They restored some of the data, but all my street addresses were gone. I had back-ups, of course; I know better than to completely trust any cloud provider. But I hadn't written code to restore from my back-ups. So I lived without street addresses in my phone for a while.<br />
<br />
Then I got another android phone, a Samsung Galaxy S Vibrant. I migrated the sidekick contacts again, and then, to get the street addresses, I imported the contacts from the G1 days. Google's merge tools cleaned things up to a tolerable level, but they left 2 issues:<br />
<br />
<ol>
<li>Duplicate phone numbers like:</li>
<ul>
<li>+1-212-555-1212</li>
<li><span class="gc-cs-link" id="gc-number-29" title="Call with Google Voice">212-555-1212</span></li>
</ul>
<li>Duplicated notes like:<br />
alllinestogether<br />
<br />
all<br />
lines<br />
like they should be</li>
</ol>
<br />
I fixed a few of these by hand, but knowing that I could get the computer to do them all in batch has been itching at me for a while.<br />
<br />
It took just a&nbsp;few hours and a couple hundred lines of python to scratch that itch today with&nbsp;<a href="https://bitbucket.org/DanC/palmagent/src/c87196981537/contact_fix.py">contact_fix.py</a>.<br />
<br />
<br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">475:c87196981537 2011-02-02 fix all_contacts (self.)</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">474:80739018dbfa 2011-02-02 - make group optional; default to all</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">473:61412465cfed 2011-02-02 - fix duplicate phone numbers as well as doubled notes</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">472:01c2becd5cfb 2011-02-02 batch edit works/tested in one case</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">471:e7840a73836d 2011-02-02 batch edit operation (tested non-destructively)</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">470:e4e531aae635 2011-02-02 run fix_note() on data from the server</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">469:2ec84b8d0363 2011-02-02 - print names of contacts in a group</span><br />
<span class="Apple-style-span" style="font-family: 'Courier New', Courier, monospace;">468:b919239097e7 2011-02-02 contact_fix.py can login and get contact data</span><br />
<div>
<br /></div>
I'm also working on archiving my contacts using hCard. More on that soon, I hope.
