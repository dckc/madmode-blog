date: 2012-02-13
published: true
tags: [data, finances, cloud, integrity]
title: Got my data back from Mint, thanks to GnuCash/mysql
updated: 2012-02-13


My ideal personal accounting system would<br />
<br />
<ul>
<li>support double-entry accounting, with budgeting, reports, and charts</li>
<li>have an open architecture with</li>
<ul>
<li>an SQL back-end</li>
<li>a flat-file serialization of the data suitable for use with version control</li>
</ul>
<li>integrate with the Web, both</li>
<ul>
<li>allowing access from any machine with a web browser</li>
<li>syncing with banking web sites</li>
</ul>
</ul>
<br />
After trying Mint for a year and a half, I realized that while Web integration is nice, it's no good without double-entry integrity. While GnuCash's UI isn't as nice as modern web apps, it lets me keep my data in SQL, which keeps my options open.<br />
<br />
<a name='more'></a><br /><br />
Before Mint, I used Quicken for decades. I stopped paying for updates after Quicken 2001 and hence lost bank syncing.&nbsp;But&nbsp;I did find a flat-file serialization suitable for use with version control (and no, QIF doesn't cut it. See my <a href="http://dig.csail.mit.edu/breadcrumbs/node/96">March 2006 item</a>). And while&nbsp;Wine continues to support Quicken 2001 after all this time, I don't have any API to update Quicken's store.&nbsp;So there's no going back to Quicken after Mint.<br />
<br />
Mint has no concept whatsoever of double-entry accounting. It will give you a balance for your bank account at the beginning of each month and a list of income and expenses in between. You might think that the old balance + income - expenses = new balance. You would be wrong.<br />
<br />
Mint fails to download a few credit card transactions on occasion, so it's unreliable auditing. It relies on the user to notice duplicate transactions, so it's unreliable for budgeting. As to the idea that Mint's categorization would save me work,&nbsp;Marc Hedlund put it this way in&nbsp;<a href="http://blog.precipice.org/why-wesabe-lost-to-mint"><i>Why Wesabe Lost to Mint</i></a>:<br />
<blockquote class="tr_bq">
<span style="background-color: white; color: #333333; font-family: depot-new-1, depot-new-2, sans-serif; font-size: 16px; line-height: 25px; text-align: left;">I was focused on trying to make the usability of editing data as easy and functional as it could be; Mint was focused on making it so you never had to do that at all. Their approach completely kicked our approach's ass. (To be defensive for just a moment, their data accuracy -- how well they automatically edited -- was really low, and <b>anyone who looked deeply into their data at Mint, especially in the beginning, was shocked at how inaccurate it was</b>. The point, though, is hardly anyone seems to have looked.)</span></blockquote>
So I had to double-check the categorization. And since they lack support for any sort of transaction reconciliation, I had to cobble together something out of their tags to keep track of which transactions I had already reviewed. And sometimes, Mint just spontaneously threw away my work and changed the categories anyway. I know this because I carefully exported all my transactions in CSV format after each significant session and reviewed the diffs before checking them in to a version control repository.<br />
<br />
<br />
The UI for splitting transactions is incredibly tedious. And once you have split a transaction, you can no longer search for the transaction by the total.<br />
<br />
I had to resort to a Google docs spreadsheet to make up for limitations of Mint's budgeting. You can only budget for the current month. No longer term planning, and <a href="http://satisfaction.mint.com/mint/topics/edit_past_budgets">no retrospective changes to the budget</a>. On November 31, you don't have all your spending info for November, since transaction data takes a few days to flow through banks and credit card systems. But on Dec 1st, Mint will no longer let you re-allocate budget funds between November and later months. As if plans were the important thing. "Plans are worthless, but planning is everything." -- <a href="http://en.wikiquote.org/wiki/Dwight_D._Eisenhower">Eisenhower</a><br />
<br />
Mint has a notes field, but won't let you search them and trains you not to use them by <a href="http://satisfaction.mint.com/mint/topics/notes_section_not_saving_properly">deleting your work</a> if you change any other field in the transaction.<br />
<br />
I was willing to risk giving them my bank passwords, since I audit everything pretty carefully, but their <a href="https://www.mint.com/how-it-works/security/">security story</a> is a boldface lie:<br />
<br />
<blockquote class="tr_bq">
Mint is a "read-only" service. You can organize and analyze your finances, but you can't move funds between–or out of–any account using Mint. And neither can anyone else.</blockquote>
They had my bank passwords to download transaction data. They could do anything I could do at my bank web site. They promise not to, but to say they (or anyone who hacks their system) cannot move funds is just a lie.<br />
<br />
So enough is enough.<br />
<br />
I went into mad mode over the holiday break, first <a href="https://bitbucket.org/DanC/quacken/changeset/a4389fd1fcf6">exploring a greasemonkey userscript</a>:<br />
<br />
<br />
<pre class="addition" style="background-color: white; background: inherit; border-bottom-color: rgb(204, 255, 204); border-bottom-left-radius: 0px; border-bottom-right-radius: 0px; border-color: initial; border-image: initial; border-left-color: rgb(204, 255, 204); border-right-color: rgb(204, 255, 204); border-style: initial; border-top-color: rgb(204, 255, 204); border-top-left-radius: 0px; border-top-right-radius: 0px; border-top-style: solid; border: inherit; color: #393939; font-family: 'Bitstream Vera Sans Mono', 'DejaVu Sans Mono', Monaco, monospace; font-size: 11px; height: 17px; line-height: 17px; padding-bottom: 0px; padding-left: 0.2em; padding-right: 0.2em; padding-top: 0px; vertical-align: baseline;">@description Mint: I want my data back</pre>
<br />
<br />
I was pleased to find that &nbsp;SQL support in GnuCash had matured as of the Dec 2010 release of version 2,4, and the <a href="http://wiki.gnucash.org/wiki/SQL">SQL structure that gnucash uses</a> is quite straightforward: accounts, transactions, splits, etc. Using guuids instead of integers for primary keys is somewhat novel but works OK. Note that the GnuCash string form of a uuid has no '-' characters, so in &nbsp;mysql, I use&nbsp;<span style="font-family: 'Courier New', Courier, monospace;">replace(uuid(), '-', '')</span>.<br />
<br />
I went back to the last comprehensive financial snapshot that I trusted, i.e. my last quarterly balance sheet from Quicken before the Mint experiment. I didn't load the decade+ of flat-file transaction data that lead up to that point, but I'm confident I could if I wanted to. For now, I just created an equity account for "Quicken transition" and used it to reproduce the balance sheet.<br />
<br />
Since I didn't trust Mint to correctly enumerate transactions, I used OFX from my financial institutions to fill in the transaction information for the past year, reconciling statements as I went. (After getting the initial balance sync'd, reconciling statements was trivial, aside from glitches in my understanding of how GnuCash's OFX import UI worked.)<br />
<br />
Then I sync'd the categorization info from Mint with GnuCash. While much of it was a one-time bulk import, running both systems in parallel for a short time was an important goal. This would require <a href="http://satisfaction.mint.com/mint/topics/exported_transactions_should_have_unique_id?from_gsfn=true">stable transaction identifiers from Mint</a>, something they don't provide in their CSV export. While <a href="http://satisfaction.mint.com/mint/topics/an_api_for_manipulation_of_personal_data">Mint doesn't advertise an API</a>, fortunately, it was straightforward to reverse-engineer the way their Ajax client gets transaction data:&nbsp;<a href="http://mcc.py/">mcc.py</a>, my Mint cloud client, is only 100 lines of python.<br />
<br />
I put some effort into trying to reproduce Mint's .csv export using my GnuCash database, but reached a point of diminishing returns. I do maintain the <span style="font-family: 'Courier New', Courier, monospace;">mint_re_export</span> SQL view for version control purposes. I also discovered a version-control-friendly way to back up the whole mysql database:<br />
<br />
<br />
<span style="font-family: 'Courier New,courier';">$ mysqldump -u $LOGNAME&nbsp;</span><span style="font-family: 'Courier New,courier';">--skip-dump-date</span><span style="font-family: 'Courier New,courier';">&nbsp;--tab=$BAK_DIR -p $DB_NAME</span><br />
<span style="font-family: 'Courier New,courier';"><br /></span><br />
<span style="font-family: 'Courier New,courier';">Beware: mysqldump --tab defaults timezones to UTC but mysqlimport uses local time, with no TZ choice. The work around: set global timezone=UTC before mysqlimport.</span><br />
<span style="font-family: 'Courier New,courier';"><br /></span><br />
<span style="font-family: 'Courier New,courier';">Also, if you use Ubuntu, like I do, and you don't specifically authorize mysql to write there, apport will stop it and you'll get a mysterious:&nbsp;</span><span style="font-family: 'Courier New', Courier, monospace;">(Errcode: 13) when executing 'SELECT INTO OUTFILE'</span><span style="font-family: 'Courier New,courier';"> You need to edit&nbsp;</span><span style="font-family: 'Courier New,courier';"><b>/etc/apparmor.d/local/usr.sbin.mysqld</b> and add a line </span><span style="font-family: 'Courier New', Courier, monospace;">/bak/dir/** rw,</span><span style="font-family: 'Courier New,courier';"> .</span><br />
<br />
<br />
One of the real tests of the results is doing my 2011 tax return. So far, I haven't had to log back in to Mint, though I have worked around shortcomings in the GnuCash UI using hand-crafted SQL or grep on the .csv export from Mint a few times.<br />
<br />
Highlights from the <a href="https://bitbucket.org/DanC/quacken/changesets">changelog</a> include:<br />
<br />
<br />
152:955de3fe6de7 2012-01-16 budget loads into gnucash DB<br />
151:3945105a6728 2012-01-16 budget_sync.py groks my budget spreadsheet<br />
145:d1854d4ef26c 2011-12-31 handle split transactions using mint parent/child info rather than guessing<br />
144:bbd55121161f 2011-12-31 more straightforward account sync between mint and gnucash<br />
141:48669cd9ec01 2011-12-30 oops; don't exclude the id column; that's the _whole point_!<br />
140:76830ffc5cb2 2011-12-30 trx_explore supports mysql as well as sqlite; parses amount straightforwardly<br />
139:42363cb4e1e0 2011-12-30 trx_explore with date handling loads thousands of mint transactions<br />
137:dc26b4e483c6 2011-12-30 mint client fetches all transactions<br />
135:503f9b7ef4af 2011-12-29 more matching work for credit cards<br />
134:f9f7358da70c 2011-12-29 - incremental matching<br />
133:2b463e2e73ff 2011-12-29 mint_re_export view is mostly working<br />
130:023bbfc79025 2011-12-29 merge split transactions from mint into gnucash/OFX<br />
129:f7301444308f 2011-12-29 updated OFX checking account data w.r.t. mint categorization work<br />
127:2c0312b96f58 2011-12-28 figured out how to import mint accounts into gnucash DB<br />
117:26fe6a26a345 2011-12-25 matching worked for 100 transactions (warnings/logging tamed)<br />
110:1af3fef89487 2011-12-25 created SqlAlchemy object from JSON data<br />
109:4fa21822a6c9 2011-12-24 explore gnucash sqlite file<br />
106:80134e7a8730 2011-12-24 JSON dump of Mint transaction data<br />
105:6d5bb42201c7 2011-12-24 got access to the transaction data<br />
103:a4389fd1fcf6 2011-12-22 mint greasemonkey exploration (bookmarklet looks easier)<br />
<br />
<br />
<div>
<span id="internal-source-marker_0.5895237079821527"></span><br />
<div>
<div>
</div>
</div>
<span id="internal-source-marker_0.5895237079821527">
</span></div>