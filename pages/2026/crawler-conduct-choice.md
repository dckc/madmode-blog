---
title: "Invasive AI crawlers: what happened to manners?"
date: 2026-10-30
published: true
tags:
  - generative-ai
  - open-web
  - aaronsw
  - inference-coop
  - invasive-ai
  - Agoric
  - capabilities
bib: llm-scrapers-references.json
summary: When Aaron Swartz cached a bunch of journal articles, he was relentlessly prosecuted. When AI companies ravenously scrape the whole web, they get off scot-free and the bill goes to the sites they scraped.
---

When Aaron Swartz cached a bunch of journal articles he was [entitled to read for free](https://www.nytimes.com/2011/07/20/us/20compute.html), he was relentlessly prosecuted. When AI companies ravenously scrape the whole web, they get off scot-free and the bill goes to the sites they scraped.

As an Open Source, Open Web advocate since 1993, my habit is to share/post/push any time I rub two brain cells together. I'm at equilibrium with the web when I can hurl you an URL for anything I learned. I'm conflicted when it comes to generative AI. I'm learning a lot about it lately; I think it's another area where capability security has a lot to offer. And [Agoric](https://agoric.com) is all in on it. But lots of my peers are in the "burn it with fire" camp, and with good reasons, including invasive AI crawling.

So I was delighted by [Nathan's invitation](https://social.coop/@ntnsndr/117334306285281470) to "change [my] relationship to the weirdness of AI" by joining [inference.coop](https://inference.coop/), a member-governed platform with private, green-energy, and public models, including Apertus, a model with explicitly respectful crawling.

## We knew how to crawl politely in 1994

Crawlers were on the program at the [first Web conference](https://archives.iw3c2.org/www1/FinalProgramme.html), in Geneva in May 1994. David Eichmann wrote that spider authors "must exercise reasonable restraint in the scope and frequency of execution," and spoke of "needing to return something to the Web community in return for the intermittent load that we have placed upon their servers." [\[Eichmann94\]](https://archives.iw3c2.org/www1/PdfWWW94/spider.pdf) Oliver McBryan's crawler [sent his email address](https://archives.iw3c2.org/www1/PdfWWW94/mcbryan.pdf) along, so sites could write to him "if problems develop." A month later, the robots mailing list settled on [robots.txt](https://www.robotstxt.org/orig.html).

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

In the top row, "retroactively" means sites that opted out by January 2025 were dropped from earlier crawls too, across 15T tokens of training data.

The bottom rows are where it gets ugly:

> If you think these crawlers respect robots.txt then you are several assumptions of good faith removed from reality.
>
> -- [Please stop externalizing your costs directly into my face](https://drewdevault.com/blog/Stop-externalizing-your-costs-on-me/), Drew DeVault, Mar 2025

## Somebody else pays

> it's not free, and the costs add up at scale. These costs ... are causing some to block or otherwise try to frustrate these uses.
>
> -- [Some Thoughts on the Open Web](https://www.mnot.net/blog/2026/open_web), Mark Nottingham, Jan 2026

Read the Docs saw one crawler take 73 TB in a month: [over $5,000 in bandwidth](https://about.readthedocs.com/blog/2024/07/ai-crawlers-abuse/).

When Anthropic's crawler hit iFixit's servers a million times in 24 hours, iFixit's CEO wrote, "You're not only taking our content without paying, you're tying up our devops resources." iFixit's terms of service already forbade it. Anthropic's answer was that its crawler "respected that signal when iFixit implemented it": the signal being a line in robots.txt ([Engadget](https://www.engadget.com/websites-accuse-ai-startup-anthropic-of-bypassing-their-anti-scraping-rules-and-protocol-133022756.html)). OpenAI's bot came at Triplegangers, a seven-person company, from 600 IP addresses. "It was basically a DDoS attack," said its CEO; the `robots.txt` opt-out "puts the onus on the business owner to understand how to block them" ([TechCrunch](https://techcrunch.com/2025/01/10/how-openais-bot-crushed-this-seven-person-companys-web-site-like-a-ddos-attack/)). Lack of a `robots.txt` line is no excuse for hammering a web site. And having one doesn't always help; one developer's already said `Disallow: /`:

> please reach out to me so we can arrange for payment for hardware upgrades commensurate to your egregious resource usage
>
> -- [Amazon's AI crawler is making my git server unstable](https://xeiaso.net/notes/2025/amazon-crawler/), Xe Iaso, Jan 2025

So sites put up walls: CAPTCHAs, and Xe's [Anubis](https://xeiaso.net/blog/2025/anubis/) with its cute "making sure you're not a bot" page.

More and more, when I try to `curl` a web page, I get some defense against invaders instead of a 200 OK. Try it on my own city's code, at [Municode](https://library.municode.com/ks/overland_park) or [American Legal Publishing](https://codelibrary.amlegal.com/codes/overland_park/latest/overview), or anything at [eCode360](https://ecode360.com/): 403, "Just a moment..." (_Fight [the good fight](https://law.resource.org/), Carl Malamud!_) The walls keep out archives, researchers, and small search engines too.

We've seen this before. When spam got bad, small mail servers couldn't keep up, and I ended up trading my privacy to Google for spam filtering ([2018](https://www.madmode.com/2018/rchain-gov-forum-sea)). Defend yourself alone, or move in with a giant.

## Why not the laws they used on Aaron?

Why don't the laws they charged Aaron under apply to the AI companies? Which was it, the DMCA? No, mostly the Computer Fraud and Abuse Act: [13 felonies](https://en.wikipedia.org/wiki/United_States_v._Swartz), with a maximum of 35 years.

The CFAA reaches locks, not signs. The Supreme Court reads "without authorization" like a parking-garage arm: "a gates-up-or-down inquiry—one either can or cannot access a computer system" ([Van Buren v. United States](https://www.law.cornell.edu/supremecourt/text/19-783)), leaving open whether a contract can be a gate. For the public web, the Ninth Circuit found no gate at all: a computer hosting publicly available webpages "has erected no gates to lift or lower in the first place." LinkedIn had sent hiQ a cease-and-desist letter and was blocking its IP addresses; the court still upheld an order to take the blocks down ([hiQ v. LinkedIn](https://www.courtlistener.com/opinion/6460342/hiq-labs-inc-v-linkedin-corporation/)). `robots.txt` is a sign, not a lock; [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309) says so itself: "These rules are not a form of access authorization." On the public web, the arm is always up, by design. That's how I can hurl you an URL.

So why doesn't `robots.txt` work like a **No Trespassing** or **No Soliciting** sign? On land, ignoring a posted sign can be [a crime](https://www.ksrevisor.gov/statutes/chapters/ch21/021_058_0008.html), and the owner can sue without showing any harm. But the courts treat a server more like a car than a field, and then the owner has to show harm ([Intel v. Hamidi](https://en.wikipedia.org/wiki/Intel_Corp._v._Hamidi)). The harm may be  small per site, but a small site can't afford to sue a big lab; there's no Ralph Nader for web sites.

In principle, the FTC could go after it as an [unfair practice](https://www.law.cornell.edu/uscode/text/15/45). But in this administration, the same Justice Department that prosecuted Aaron filed a brief [on OpenAI's side](https://en.wikipedia.org/w/index.php?title=The_New_York_Times_v._Microsoft_and_OpenAI&oldid=1375498373) in the *New York Times* case.

Aaron was before his time. In [2002 #swig chat](http://web.archive.org/web/20190630005615/http://chatlogs.planetrdf.com/rdfig/2002-06-28.html), he [blew my mind](/2010/06/return-to-patronism.html) about copyright:

> **DanC:** but if I can play my song without a license, what motivates me to acquire a license... or to compensate the artist in any way?
>
> **aaronsw:** you pay because you want the artist to live well and continue making music

Nine years later he was arrested. Lawrence Lessig asked why it was "so necessary that Aaron Swartz be labeled a 'felon'"; in 18 months of plea negotiations, "that was what he was not willing to accept" ([Prosecutor as bully](https://lessig.tumblr.com/post/40347463044/prosecutor-as-bully)).

The law caught up some, eventually: in 2021 the Supreme Court [narrowed the CFAA](https://www.courtlistener.com/opinion/4888668/van-buren-v-united-states/), and federally funded research now has to be [free to read, with no embargo](https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/08/08-2022-OSTP-Public-Access-Memo.pdf).

## Choosing the good ones

The co-op lets members choose by privacy, green energy, and public good. And public good means good crawler conduct.

- DeepSeek, our default, says it [re-bootstrapped its crawler from Common Crawl](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf), but I couldn't find a published crawler policy.
- Keenable, which fetches pages for our web search, [says who it is and follows RFC 9309](https://app.keenable.ai/bot).
- Apertus gets full marks.

---

## Appendix A: my trip thru some laws

- **DMCA §1201** bans circumventing access controls ([17 U.S.C. §1201](https://www.law.cornell.edu/uscode/text/17/1201)). It got there by way of a treaty ([WIPO Copyright Treaty, Art. 11](https://ipmall.info/sites/default/files/hosted_resources/lipa/copyrights/WIPO%20COPYRIGHT%20TREATY.pdf)) that the US then [implemented, and then some](https://en.wikipedia.org/wiki/WIPO_Copyright_and_Performances_and_Phonograms_Treaties_Implementation_Act). Big fences get criminal penalties; robots.txt gets nothing.
- **CFAA:** a public page is a gate that's up ([Van Buren](https://www.courtlistener.com/opinion/4888668/van-buren-v-united-states/), [hiQ](https://www.courtlistener.com/opinion/6460342/hiq-labs-inc-v-linkedin-corporation/)), and DOJ [won't charge](https://www.justice.gov/archives/opa/pr/department-justice-announces-new-policy-charging-cases-under-computer-fraud-and-abuse-act) mere terms-of-service violations. A bill called [Aaron's Law](https://www.wired.com/2013/06/aarons-law-is-finally-here/) would have written that into the statute; it never got out of committee.
- **Trespass to land** needs no harm, and a sign revokes the implied invitation to walk up and knock ([Florida v. Jardines](https://www.law.cornell.edu/supremecourt/text/11-564)). "No Soliciting" signs are fine where city permit schemes aren't ([Watchtower v. Stratton](https://www.law.cornell.edu/supremecourt/text/00-1737)). Courts treat servers as chattels instead ([eBay v. Bidder's Edge](https://en.wikipedia.org/wiki/EBay_v._Bidder%27s_Edge), [Intel v. Hamidi](https://en.wikipedia.org/wiki/Intel_Corp._v._Hamidi)).
- **Damages:** copyright has statutory damages, up to $150,000 per work for willful infringement ([17 U.S.C. §504(c)](https://www.law.cornell.edu/uscode/text/17/504)). That's what made a class action over pirated books worth $1.5 billion ([Anthropic](https://en.wikipedia.org/wiki/Anthropic), Wikipedia). Trespass to chattels pays only for actual harm; nothing pays per crawl.
- **The EU** makes a machine-readable opt-out binding on commercial AI crawlers, without saying what the signal is. Mark Nottingham [on why the design matters](https://www.mnot.net/blog/2024/ai-control); the IETF [AI Preferences](https://datatracker.ietf.org/wg/aipref/about/) working group is on it. None of that reaches the evasive end of the spectrum.

## Appendix B: related works

See also my [ai-scrape26](https://www.zotero.org/connolly/collections/HASFRI4G) Zotero collection.
