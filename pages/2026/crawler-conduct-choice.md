---
title: "AI crawlers: conduct is a choice"
date: 2026-11-05
published: false
tags:
  - generative-ai
  - open-web
  - aaronsw
  - inference-coop
  - law
  - power
summary: When Aaron Swartz downloaded journal articles, he was relentlessly prosecuted. When AI companies scrape the whole web, the bill goes to the sites they scraped.
---

When Aaron Swartz downloaded journal articles he was [entitled to read for free](https://www.nytimes.com/2011/07/20/us/20compute.html), he was relentlessly prosecuted. When AI companies scrape the whole web, the bill goes to the sites they scraped.

How a crawler behaves is up to the people who build the model. Which models we use is up to us. I'm a member of the [Inference Cooperative](https://inference.coop), where members choose the models we buy together. The co-op already says it values

> Open, sovereign models built as public goods rather than proprietary products.
>
> -- [AI, governed together](https://inference.coop), Inference Cooperative, Oct 2026

Full disclosure:

- I've been an Open Source, Open Web advocate since 1993. My equilibrium with the web: I can share anything by hurling a URL.
- I work at Agoric, which is all-in on AI, and I use LLMs [a lot](https://www.madmode.com/search/label/generative-ai/), including to research this.
- When my co-op allotment runs out, I go back to a frontier lab. Why is a topic for another day.

## We knew how to crawl politely in 1994

Crawlers were on the program at the [first Web conference](https://archives.iw3c2.org/www1/FinalProgramme.html), in Geneva in May 1994. David Eichmann wrote that spider authors

> must exercise reasonable restraint in the scope and frequency of execution
>
> -- [The RBSE Spider — Balancing Effective Search Against Web Load](https://archives.iw3c2.org/www1/PdfWWW94/spider.pdf), David Eichmann, WWW94, May 1994

and spoke of "needing to return something to the Web community in return for the intermittent load that we have placed upon their servers." Oliver McBryan's crawler [sent his email address](https://archives.iw3c2.org/www1/PdfWWW94/mcbryan.pdf) along, so sites could write to him "if problems develop." A month later, the robots mailing list settled on [robots.txt](https://www.robotstxt.org/orig.html).

Say who you are, honor the sign, go easy, give something back. HTTP has long had the tools: conditional GET, `429 Too Many Requests`, an honest `User-Agent`.

Grade today's crawlers on those four and you get a spectrum:

| Conduct | Example | Misses |
|---|---|---|
| Exemplary | [Apertus](https://arxiv.org/abs/2509.14233): honors robots.txt, even retroactively; publishes data reconstruction scripts | — |
| Compliant, named, sends visitors back | search crawlers like Googlebot | load, sometimes |
| Compliant and named, little back | the big labs' training crawlers: [~38,000 crawls per referral](https://blog.cloudflare.com/crawlers-click-ai-bots-training/) for Anthropic; ClaudeBot [~a million hits in 24 hours](https://pcgamer.com/software/ai/ifixit-ceo-takes-shots-at-anthropic-for-hitting-our-servers-a-million-times-in-24-hours-and-even-the-ai-companys-own-chatbot-disapproves/) at iFixit | give back, go easy |
| Crawls, no published policy | DeepSeek, [re-bootstrapped from Common Crawl](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf); Z.ai's GLM-5, [web datasets and code-host snapshots](https://arxiv.org/abs/2602.15763) | say who you are (unknown) |
| Agents off the leash | [OpenAI agents at Wikimedia](https://diff.wikimedia.org/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/), 2026 | go easy |
| Evasive, named | [Perplexity](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/) | honor the sign, say who you are |
| Evasive, anonymous | random user agents from "tens of thousands of IP addresses – mostly residential" ([DeVault](https://drewdevault.com/blog/Stop-externalizing-your-costs-on-me/), [LWN](https://lwn.net/Articles/1008897/), [Ars Technica](https://arstechnica.com/ai/2025/03/devs-say-ai-crawlers-dominate-traffic-forcing-blocks-on-entire-countries/)) | all of them |

The top row is not a toy. "Retroactively" means sites that opted out by January 2025 were dropped from earlier crawls too, across 15T tokens of training data.

The bottom rows are where it gets ugly:

> If you think these crawlers respect robots.txt then you are several assumptions of good faith removed from reality.
>
> -- [Please stop externalizing your costs directly into my face](https://drewdevault.com/blog/Stop-externalizing-your-costs-on-me/), Drew DeVault, Mar 2025

## Somebody else pays

> it's not free, and the costs add up at scale. These costs ... are causing some to block or otherwise try to frustrate these uses.
>
> -- [Some Thoughts on the Open Web](https://www.mnot.net/blog/2026/open_web), Mark Nottingham, Jan 2026

Read the Docs saw one crawler take 73 TB in a month: [over $5,000 in bandwidth](https://about.readthedocs.com/blog/2024/07/ai-crawlers-abuse/). Xe Iaso's robots.txt already said `Disallow: /`:

> please reach out to me so we can arrange for payment for hardware upgrades commensurate to your egregious resource usage
>
> -- [Amazon's AI crawler is making my git server unstable](https://xeiaso.net/notes/2025/amazon-crawler/), Xe Iaso, Jan 2025

So sites put up walls: CAPTCHAs, and Xe's [Anubis](https://xeiaso.net/blog/2025/anubis/) with its cute "making sure you're not a bot" page. From the reader's side, I can't reliably `curl` a web page anymore. While looking up trespass law for this item, my assistant got 403s from two municipal code sites and a bot check instead of a Supreme Court opinion. The walls keep out archives, researchers, and small search engines too.

We've seen this before. When spam got bad, small mail servers couldn't keep up, and I ended up trading my privacy to Google for spam filtering ([2018](https://www.madmode.com/2018/rchain-gov-forum-sea)). Defend yourself alone, or move in with a giant.

## Why not the laws they used on Aaron?

Why don't the laws they charged Aaron under apply to the AI companies? Which was it, the DMCA? No, mostly the Computer Fraud and Abuse Act: [13 felonies](https://en.wikipedia.org/wiki/United_States_v._Swartz), with a maximum of 35 years. When MIT and JSTOR blocked his laptop, he changed its addresses ([MIT's report](https://swartz-report.mit.edu/)), which is what evasive crawlers do from tens of thousands of IP addresses.

The CFAA is about getting in "without authorization," and the Ninth Circuit has since said that scraping public pages likely isn't that, even after the site objects ([hiQ v. LinkedIn](https://www.courtlistener.com/opinion/6460342/hiq-labs-inc-v-linkedin-corporation/)). Robots.txt doesn't change that; [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309) says so itself: "These rules are not a form of access authorization."

So why doesn't robots.txt work like a No Trespassing or No Soliciting sign? On land, ignoring a posted sign can be [a crime](https://www.ksrevisor.gov/statutes/chapters/ch21/021_058_0008.html), and the owner can sue without showing any harm. But a server isn't land. Courts treat it more like a car than a field, and then the owner has to show harm ([Intel v. Hamidi](https://en.wikipedia.org/wiki/Intel_Corp._v._Hamidi)). The harm is real but small per site, a few hundred dollars against a lawyer's fees, and you can't sue a crawler you can't identify.

Meanwhile, the Justice Department that prosecuted Aaron filed a brief [on OpenAI's side](https://en.wikipedia.org/w/index.php?title=The_New_York_Times_v._Microsoft_and_OpenAI&oldid=1375498373) in the *New York Times* case.

Aaron was before his time. In 2002 he [blew my mind](https://www.madmode.com/search/label/aaronsw/) about copyright on IRC:

> **DanC:** but if I can play my song without a license, what motivates me to acquire a license... or to compensate the artist in any way?
> **aaronsw:** you pay because you want the artist to live well and continue making music
>
> -- [RDF Interest Group IRC log](http://web.archive.org/web/20190630005615/http://chatlogs.planetrdf.com/rdfig/2002-06-28.html), Jun 2002 ([A Return to Patronism](https://www.madmode.com/2010/06/return-to-patronism.html))

Nine years later he was arrested. Every plea offer that followed meant pleading guilty to felonies, and a felony record would have closed off the political life he wanted.

> The question this government needs to answer is why it was so necessary that Aaron Swartz be labeled a 'felon'. For in the 18 months of negotiations, that was what he was not willing to accept.
>
> -- [Prosecutor as bully](https://lessig.tumblr.com/post/40347463044/prosecutor-as-bully), Lawrence Lessig, Jan 2013

The law caught up some, eventually: in 2021 the Supreme Court [narrowed the CFAA](https://www.courtlistener.com/opinion/4888668/van-buren-v-united-states/), and federally funded research now has to be [free to read, with no embargo](https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/08/08-2022-OSTP-Public-Access-Memo.pdf).

## So, choose

The co-op's models were trained by developers who crawled the web; I don't want to pretend otherwise. Our default, DeepSeek, says it [re-bootstrapped its crawler from Common Crawl](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf), but I couldn't find a published crawler policy. OpenAI's are the agents Wikimedia flagged. Apertus is right there in the [model list](https://git.inference.coop/co-op/docs/src/branch/main/models.md).

The co-op lets members choose by privacy, green energy, and public good. And public good means good crawler conduct.

I plan to bring this up at the co-op's November 6 meeting.

---

_p.s. Researching this, I had an AI assistant fetch a lot of web pages on my behalf. It sent a generic browser `User-Agent`. Hmm._

---

## Appendix A: the law, a little more

- **DMCA §1201** bans circumventing access controls ([17 U.S.C. §1201](https://www.law.cornell.edu/uscode/text/17/1201)). It got there by way of a treaty ([WIPO Copyright Treaty, Art. 11](https://ipmall.info/sites/default/files/hosted_resources/lipa/copyrights/WIPO%20COPYRIGHT%20TREATY.pdf)) that the US then [implemented, and then some](https://en.wikipedia.org/wiki/WIPO_Copyright_and_Performances_and_Phonograms_Treaties_Implementation_Act). Big fences get criminal penalties; robots.txt gets nothing.
- **Inside W3C,** the 2001 DRM workshop gave us "Readers, viewers, and listeners are fans, not thieves" ([Manasse](https://www.w3.org/2000/12/drm-ws/pp/compaq.html); [A Return to Patronism](https://www.madmode.com/2010/06/return-to-patronism.html)).
- **CFAA:** a public page is a gate that's up ([Van Buren](https://www.courtlistener.com/opinion/4888668/van-buren-v-united-states/), [hiQ](https://www.courtlistener.com/opinion/6460342/hiq-labs-inc-v-linkedin-corporation/)), and DOJ [won't charge](https://www.justice.gov/archives/opa/pr/department-justice-announces-new-policy-charging-cases-under-computer-fraud-and-abuse-act) mere terms-of-service violations. A bill called [Aaron's Law](https://www.wired.com/2013/06/aarons-law-is-finally-here/) would have written that into the statute; it never got out of committee.
- **Trespass to land** needs no harm, and a sign revokes the implied invitation to walk up and knock ([Florida v. Jardines](https://www.law.cornell.edu/supremecourt/text/11-564)). "No Soliciting" signs are fine where city permit schemes aren't ([Watchtower v. Stratton](https://www.law.cornell.edu/supremecourt/text/00-1737)). Courts treat servers as chattels instead ([eBay v. Bidder's Edge](https://en.wikipedia.org/wiki/EBay_v._Bidder%27s_Edge), [Intel v. Hamidi](https://en.wikipedia.org/wiki/Intel_Corp._v._Hamidi)).
- **The EU** makes a machine-readable opt-out binding on commercial AI crawlers, without saying what the signal is. Mark Nottingham [on why the design matters](https://www.mnot.net/blog/2024/ai-control); the IETF [AI Preferences](https://datatracker.ietf.org/wg/aipref/about/) working group is on it. None of that reaches the evasive end of the spectrum.

## Appendix B: sources

Everything I consulted, newest first.

- 2026-10-05: Selena Deckelmann, [OpenAI “rogue” agent activities found on Wikimedia projects](https://diff.wikimedia.org/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/), Diff (Wikimedia Foundation).
- 2026-10: Inference Cooperative, [AI, governed together](https://inference.coop), homepage.
- 2026-10: Inference Cooperative, [Models](https://git.inference.coop/co-op/docs/src/branch/main/models.md), co-op documentation.
- 2026-09-18: [The New York Times v. Microsoft and OpenAI](https://en.wikipedia.org/w/index.php?title=The_New_York_Times_v._Microsoft_and_OpenAI&oldid=1375498373), Wikipedia, revision of Sep. 18, 2026.
- 2026-09-18: [David Chisnall, post on Infosec Exchange](https://infosec.exchange/@david_chisnall/117290835262126012).
- 2026-09-17: Jason Koebler, ['Doom Loop': OpenAI and Microsoft Admits LLMs Are Destroying the Web and Built on Theft](https://www.404media.co/doom-loop-openai-and-microsoft-admits-llms-are-destroying-the-web-and-built-on-theft/), *404 Media*.
- 2026-09: DeepSeek-AI, [DeepSeek-V4.1 Technical Report](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf).
- 2026-06-15: [Nathan Schneider, reply on social.coop](https://social.coop/@ntnsndr/116756181172623122).
- 2026-06: Nathan Schneider, [An inference cooperative for academic AI](https://nathanschneider.info/2026/06/an-inference-cooperative-for-academic-ai/). · [social.coop post, Jun. 14, 2026](https://social.coop/@ntnsndr/116750348962878181)
- 2026-05: Ropes & Gray, [Web Scraping in the Age of AI: Guidance for Data Owners and Scrapers](https://www.ropesgray.com/en/insights/alerts/2026/05/web-scraping-in-the-age-of-ai-guidance-for-data-owners-and-scrapers).
- 2026-04-27: [The Moat or the Commons](https://www.warman.life/blog/2026-04-27-the-moat-or-the-commons/), *Warman Notes*. · my reply citing it: [social.coop, Jun. 15, 2026](https://social.coop/@dckc/116754035978430967)
- 2026-04-27: Eric Vandevelde, Ilissa Samplin and Josh Leopold (Gibson Dunn), [The Article III Standing Problem for AI-Scraping Anti-Circumvention Claims](https://www.managingip.com/article/2ga02si5c24xaq46ren7k/copyright/the-article-iii-standing-problem-for-ai-scraping-anti-circumvention-claims), *Managing IP*.
- 2026-02: GLM-5 Team (Z.ai), [GLM-5: from Vibe Coding to Agentic Engineering](https://arxiv.org/abs/2602.15763), arXiv:2602.15763, Feb. 2026, §2.2.
- 2026-01-20: Mark Nottingham, [Some Thoughts on the Open Web](https://www.mnot.net/blog/2026/open_web), *mnot's blog*.
- 2025-12-23: Peter Devlin, [Is Your Site's Robots.txt Giving Content to AI Models for Free?](https://technologylaw.fkks.com/post/102lz1g/is-your-sites-robots-txt-giving-content-to-ai-models-for-free), Frankfurt Kurnit Klein & Selz, *Technology Law* blog.
- 2025-10: David Atkinson, [Revitalizing Trespass to Chattels in the Era of GenAI Scraping](https://arxiv.org/abs/2510.16049), arXiv:2510.16049, Oct. 2025.
- 2025-09: [Anthropic](https://en.wikipedia.org/wiki/Anthropic), Wikipedia (pirated books; $1.5 billion settlement, 2025).
- 2025-09: Swiss AI Initiative, [Apertus: Democratizing Open and Compliant LLMs for Global Language Environments](https://arxiv.org/abs/2509.14233), arXiv:2509.14233, Sep. 2025, §3.1.1 and App. B.
- 2025-08-29: Cloudflare, [The crawl-to-click gap: Cloudflare data on AI bots, training, and referrals](https://blog.cloudflare.com/crawlers-click-ai-bots-training/), Cloudflare Blog.
- 2025-08-04: Cloudflare, [Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/), Cloudflare Blog.
- 2025-08: OpenAI, [gpt-oss-120b & gpt-oss-20b Model Card](https://arxiv.org/abs/2508.10925), arXiv:2508.10925, Aug. 2025, §2.4.
- 2025-05: Qwen Team, [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388), arXiv:2505.09388, May 2025.
- 2025-04-01: Wikimedia Foundation, [How crawlers impact the operations of the Wikimedia projects](https://diff.wikimedia.org/2025/04/01/how-crawlers-impact-the-operations-of-the-wikimedia-projects/), Diff.
- 2025-03-27: Techaro (Xe Iaso), [*Anubis*](https://github.com/TecharoHQ/anubis/releases/tag/v1.15.0) v1.15.0, release.
- 2025-03-17: Drew DeVault, [Please stop externalizing your costs directly into my face](https://drewdevault.com/blog/Stop-externalizing-your-costs-on-me/).
- 2025-03: [Open source devs say AI crawlers dominate traffic, forcing blocks on entire countries](https://arstechnica.com/ai/2025/03/devs-say-ai-crawlers-dominate-traffic-forcing-blocks-on-entire-countries/), *Ars Technica*.
- 2025-02-14: Jonathan Corbet, [Fighting the AI scraperbot scourge](https://lwn.net/Articles/1008897/), LWN.net.
- 2025-01-19: Xe Iaso, [Block AI scrapers with Anubis](https://xeiaso.net/blog/2025/anubis/).
- 2025-01-17: Xe Iaso, [Amazon's AI crawler is making my git server unstable](https://xeiaso.net/notes/2025/amazon-crawler/).
- 2025-01-07: [IETF AI Preferences (aipref) Working Group, chartered](https://datatracker.ietf.org/wg/aipref/about/).
- 2024-07-25: Eric Holscher, [AI crawlers need to be more respectful](https://about.readthedocs.com/blog/2024/07/ai-crawlers-abuse/), Read the Docs blog.
- 2024-07: [iFixit CEO takes shots at Anthropic for 'hitting our servers a million times in 24 hours'](https://pcgamer.com/software/ai/ifixit-ceo-takes-shots-at-anthropic-for-hitting-our-servers-a-million-times-in-24-hours-and-even-the-ai-companys-own-chatbot-disapproves), *PC Gamer*.
- 2024-07: Shayne Longpre et al. (Data Provenance Initiative), [Consent in Crisis: The Rapid Decline of the AI Data Commons](https://arxiv.org/abs/2407.14933), arXiv:2407.14933, Jul. 2024.
- 2024-04-21: Mark Nottingham, [Considerations for AI Opt-Out](https://www.mnot.net/blog/2024/ai-control), *mnot's blog*.
- 2024-01-23: [*Meta Platforms, Inc. v. Bright Data Ltd.*](https://cdn.ca9.uscourts.gov/datastore/opinions/2023/04/18/20-16387.pdf) (N.D. Cal. Jan. 23, 2024)
- 2024: Daniel J. Solove and Woodrow Hartzog, [The Great Scrape: The Clash Between Scraping and Privacy](https://scholarship.law.bu.edu/cgi/viewcontent.cgi?article=4885&context=faculty_scholarship), SSRN working paper 4884485, 2024.
- 2023-12: [*The New York Times Co. v. Microsoft Corp.*](https://www.courtlistener.com/docket/68117049/the-new-york-times-company-v-microsoft-corporation/), No. 1:23-cv-11195-SHS (S.D.N.Y. filed Dec. 2023).
- 2022-12: Alec Radford et al., [Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356), arXiv:2212.04356.
- 2022-09: M. Koster, G. Illyes, H. Zeller, L. Sassman, [Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309), RFC 9309, Sep. 2022.
- 2022-08-25: Alondra Nelson, White House Office of Science and Technology Policy, [Ensuring Free, Immediate, and Equitable Access to Federally Funded Research](https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/08/08-2022-OSTP-Public-Access-Memo.pdf), memorandum.
- 2022-05: U.S. Department of Justice, [Department of Justice Announces New Policy for Charging Cases under the Computer Fraud and Abuse Act](https://www.justice.gov/archives/opa/pr/department-justice-announces-new-policy-charging-cases-under-computer-fraud-and-abuse-act).
- 2022-04-18: [*hiQ Labs, Inc. v. LinkedIn Corp.*](https://www.courtlistener.com/opinion/6460342/hiq-labs-inc-v-linkedin-corporation/), 31 F.4th 1180 (9th Cir. 2022).
- 2021-06-03: [*Van Buren v. United States*](https://www.courtlistener.com/opinion/4888668/van-buren-v-united-states/), 593 U.S. 374 (2021).
- 2020-04-27: [*Georgia v. Public.Resource.Org, Inc.*](https://www.law.cornell.edu/supremecourt/text/18-1150), 590 U.S. 255 (2020).
- 2020-04-15: Giovanni Garcia, [Expanded access to JSTOR during COVID-19 crisis](https://about.jstor.org/news/expanded-access-to-jstor-during-covid-19-crisis), *About JSTOR*, (updated from March 2020).
- 2019: Julie E. Cohen, *Between Truth and Power: The Legal Constructions of Informational Capitalism* (Oxford Univ. Press, 2019).
- 2017: Lina M. Khan, "Amazon's Antitrust Paradox," 126 Yale L.J. 710 (2017).
- 2015: Frank Pasquale, *The Black Box Society* (Harvard Univ. Press, 2015).
- 2013-07-26: Harold Abelson, Peter A. Diamond, Andrew Grosso and Douglas W. Pfeiffer, [Report to the President: MIT and the Prosecution of Aaron Swartz](https://swartz-report.mit.edu/), MIT.
- 2013-06-20: Zoe Lofgren and Ron Wyden, [Introducing Aaron's Law, a Desperately Needed Reform of the Computer Fraud and Abuse Act](https://www.wired.com/2013/06/aarons-law-is-finally-here/), *Wired*.
- 2013-06: [Aaron's Law](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#Aaron's_Law) (H.R. 2454 / S. 1196, 113th Cong., 2013; reintroduced as H.R. 1918 / S. 1030, 2015), as summarized in "Computer Fraud and Abuse Act," Wikipedia.
- 2013-03-26: [*Florida v. Jardines*](https://www.law.cornell.edu/supremecourt/text/11-564), 569 U.S. 1 (2013).
- 2013-01-14: [United States v. Swartz](https://en.wikipedia.org/wiki/United_States_v._Swartz), Wikipedia (facts, JSTOR's statement, state charges, penalties).
- 2013-01-12: Lawrence Lessig, [Prosecutor as bully](https://lessig.tumblr.com/post/40347463044/prosecutor-as-bully), *Lessig Tumblr*. (quoted in Wikipedia, "Aaron Swartz")
- 2013-01-11: [Aaron Swartz](https://en.wikipedia.org/wiki/Aaron_Swartz), Wikipedia (plea offers, Lessig's "Prosecutor as Bully," congressional briefing on the Manifesto).
- 2012-09-12: Superseding Indictment, [*United States v. Swartz*](https://web.archive.org/web/20130608041804/https://www.wired.com/images_blogs/threatlevel/2012/09/swartzsuperseding.pdf), No. 1:11-cr-10260 (D. Mass. Sept. 12, 2012).
- 2012-04: M. Nottingham, R. Fielding, [Additional HTTP Status Codes](https://www.rfc-editor.org/rfc/rfc6585), RFC 6585, Apr. 2012.
- 2011-07-19: John Schwartz, [Open-Access Advocate Is Arrested for Huge Download](https://www.nytimes.com/2011/07/20/us/20compute.html), *New York Times*.
- 2011-07-01: [K.S.A. 21-5808, Criminal trespass (recodified criminal code, eff. July 1, 2011)](https://www.ksrevisor.gov/statutes/chapters/ch21/021_058_0008.html).
- 2010-01-21: [*Citizens United v. Federal Election Commission*](https://www.courtlistener.com/opinion/1741/citizens-united-v-federal-election-commission/), 558 U.S. 310 (2010).
- 2008-07: Aaron Swartz, [Guerilla Open Access Manifesto](https://archive.org/details/GuerillaOpenAccessManifesto).
- 2004: Ben Laurie and Richard Clayton, ['Proof-of-Work' Proves Not to Work](https://www.cl.cam.ac.uk/~rnc1/proofwork.pdf), WEIS 2004.
- 2004: Lawrence Lessig, [*Free Culture*](http://www.free-culture.cc/) (Penguin), ch. 12, "Harms."
- 2003: *Intel Corp. v. Hamidi*, 30 Cal. 4th 1342 (2003).
- 2002-06-28: [RDF Interest Group, IRC log, June 28, 2002 (aaronsw and DanC)](http://web.archive.org/web/20190630005615/http://chatlogs.planetrdf.com/rdfig/2002-06-28.html).
- 2002-06-17: [*Watchtower Bible & Tract Society of N.Y., Inc. v. Village of Stratton*](https://www.law.cornell.edu/supremecourt/text/00-1737), 536 U.S. 150 (2002).
- 2001-01: Mark S. Manasse, [Why Rights Management is Wrong (and What to Do Instead)](https://www.w3.org/2000/12/drm-ws/pp/compaq.html), position paper, W3C Workshop on Digital Rights Management.
- 2000: *eBay, Inc. v. Bidder's Edge, Inc.*, 100 F. Supp. 2d 1058 (N.D. Cal. 2000).
- 1998-10-28: [WIPO Copyright and Performances and Phonograms Treaties Implementation Act](https://en.wikipedia.org/wiki/WIPO_Copyright_and_Performances_and_Phonograms_Treaties_Implementation_Act), Pub. L. 105-304, tit. I; Wikipedia.
- 1998: [17 U.S.C. § 1201, Circumvention of copyright protection systems (criminal penalties at § 1204)](https://www.law.cornell.edu/uscode/text/17/1201).
- 1996-12-20: [WIPO Copyright Treaty, Dec. 20, 1996, art. 11](https://ipmall.info/sites/default/files/hosted_resources/lipa/copyrights/WIPO%20COPYRIGHT%20TREATY.pdf).
- 1994-06-30: Martijn Koster, [A Standard for Robot Exclusion](https://www.robotstxt.org/orig.html), consensus of the robots mailing list.
- 1994-05: First International Conference on the World-Wide Web (WWW94), CERN, Geneva, May 25–27, 1994: [final programme](https://archives.iw3c2.org/www1/FinalProgramme.html), Indexing session · [preliminary proceedings](https://archives.iw3c2.org/www1/PrelimProcs.html)
- 1994-05: David Eichmann, [The RBSE Spider — Balancing Effective Search Against Web Load](https://archives.iw3c2.org/www1/PdfWWW94/spider.pdf), in R. Cailliau, O. Nierstrasz, M. Ruggier, eds., *First International World-Wide Web Conference* (advance proceedings), CERN, Geneva, May 25–27, 1994, pp. 113–120.
- 1994-05: Martijn Koster, [ALIWEB — Archie-Like Indexing in the Web](https://archives.iw3c2.org/www1/PdfWWW94/aliweb.pdf), in R. Cailliau, O. Nierstrasz, M. Ruggier, eds., *First International World-Wide Web Conference* (advance proceedings), CERN, Geneva, May 25–27, 1994, pp. 91–100.
- 1994-05: Oliver A. McBryan, [GENVL and WWWW: Tools for Taming the Web](https://archives.iw3c2.org/www1/PdfWWW94/mcbryan.pdf), in R. Cailliau, O. Nierstrasz, M. Ruggier, eds., *First International World-Wide Web Conference* (advance proceedings), CERN, Geneva, May 25–27, 1994, pp. 79–90.
- 1993: Martijn Koster, [Guidelines for Robot Writers](https://www.robotstxt.org/guidelines.html).
- 1979: [Trespass to land](https://en.wikipedia.org/wiki/Trespass_to_land), Wikipedia (Restatement (Second) of Torts §158, Am. Law Inst. 1979).
- 1979: [Trespass to chattels](https://en.wikipedia.org/wiki/Trespass_to_chattels), Wikipedia (Restatement (Second) of Torts §218, Am. Law Inst. 1979).
