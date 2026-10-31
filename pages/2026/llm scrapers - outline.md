---
title: "LLM scrapers: outline"
status: outline
tags:
  - generative-ai
  - open-web
  - law
  - power
  - draft
working-title: "Crawler conduct is a choice (❓ working)"
venue: madmode.com (full piece)
companion: short inference.coop forum post, ahead of 2026-11-06 monthly meeting (see end)
---

> Structure only, not prose. Shape: thesis → the 1994 norms → a spectrum of
> crawler behavior graded against them → cost → law → power → objections →
> remedies, ending with what a reader can choose. Legal theories in Part V are
> IRAC-style (Issue / Rule / Application / Conclusion).
> Footnotes point to **References** at the end; my own earlier blog items are
> noted inline, in parentheses.
> ⚠️ = claim still needs a primary source.
> ❓ = for me to fill in (e.g. W3C memories).
> 🙋 = link Claude's fetcher couldn't read (403 / bot wall / JS-only); I fetch it by hand and save a Zotero snapshot to `invasive-ai`.

## Shape: five-paragraph theme (give or take)

1. Intro (hook → point)
	1. hook: when Aaron Swartz downloaded journal articles he was entitled to read for free[^nyt-2011], he was relentlessly prosecuted (V.B.5). When AI companies scrape the whole web, the bill goes to the sites they scraped (IV.1)
	2. point: **crawler conduct is a choice; developers can choose good conduct, and so can we, when we choose models**
		1. the "we": I'm a member of inference.coop, where members choose which models we buy, and it already values "open, sovereign models built as public goods" (VIII.4.1)
2. Where I stand (short, between intro and supports)
	1. "Open Source, Open Web advocate since 1993"
		1. my equilibrium with the web: share anything by hurling a URL
	2. conflict of interest, disclosed (VII.3)
		1. I work at Agoric: crypto, and all-in on AI
		2. I use LLMs daily ([generative-ai](https://www.madmode.com/search/label/generative-ai/) on this blog)
		3. inference.coop member: I buy inference on models built from scraped data (VIII.4)
		4. and when my co-op allotment runs out, I go back to a frontier lab (this outline included); why that is → economics piece (X)
3. Support 1: good conduct is known, and possible at scale → it's a choice
	1. crawling was part of the web from conference 1; the deal was cheap and polite (II.1, II.2)
	2. the 1994 norms as rubric; the spectrum from Apertus to residential proxies (II.1.3, III)
		1. polite crawling is easy: HTTP already has the tools (conditional GET, 429 + Retry-After, honest User-Agent) (II.3)
	3. concession folded in: the right to read; Google was welcome (VII.1, VII.2)
	4. counterargument, boycott vs. exceptions: the spectrum is the answer; grade conduct, don't boycott a technology (VII.4)
4. Support 2: bad choices cost someone else
	1. bandwidth bills, bot walls that block readers and the law itself (IV.1)
		1. who pays, in one sentence: "please reach out to me so we can arrange for payment for hardware upgrades commensurate to your egregious resource usage"[^xe-amazon]
		2. mnot, "Open is Not Free to Provide": serving content to anyone "might be a commodity service now … but it's not free, and the costs add up at scale. These costs … are causing some to block or otherwise try to frustrate these uses"[^mnot-open-web]
	2. sites' response, measured: in one year, 28%+ of the most critical sources in a major training set became fully restricted (Consent in Crisis, III.8)
	3. same pattern as spam: defend alone or consolidate under a giant (IV.2)
5. Support 3: the law won't make the choice for us
	1. what I learned: I assumed the DMCA applied; it doesn't. It covers locks (DRM), and robots.txt is a sign. Even Aaron was charged under the CFAA, not the DMCA (V.A, V.B.5)
		1. robots.txt went to IETF, and the standard itself says it's "not a form of access authorization" (II.4)
		2. how the big fence got its teeth: lobbied into a treaty, implemented as the DMCA, exported by trade deals (VI.B)
		3. from inside W3C: the 2001 DRM workshop, "fans, not thieves"; later EME (V.A.5.5)
	2. chattel rule: harm is real but small per site; evasion defeats attribution (V.D.5)
		1. groundwork in a sentence or two: trespass to land needs no harm and a sign is enough; courts treat a server as a chattel, where harm is required (V.D.1–4)
		2. the enforcement gap: every route is civil, slow and expensive (V.E)
	3. two tiers: Aaron relentlessly prosecuted under the CFAA for bulk downloading and evading blocks; the labs do the same at web scale, like the crawlers in III.7, untouched (V.B.5, VI.A)
		1. zinger: "the Justice Department files a brief on their side" (VI.A.4 ⚠️ source the brief)
		2. personal note: I knew Aaron from when he was 14 ([aaronsw](https://www.madmode.com/search/label/aaronsw/) on this blog)
			1. he blew my mind about copyright in 2002, on IRC
				1. me: "if I can play my song without a license, what motivates me to acquire a license... or to compensate the artist in any way?"
				2. Aaron: "you pay because you want the artist to live well and continue making music"[^rdfig-2002] (A Return to Patronism, [2010](https://www.madmode.com/2010/06/return-to-patronism.html))
				3. → the copyright bind (IX.4)
		3. the CFAA generally (*Van Buren*, *hiQ*, DOJ policy) stays behind this; the reader sees it through Aaron (V.B.1–4)
	4. scale: AI as the bet holding up GDP → too big to regulate (VI.E)
	5. the EU at least tried: a machine-readable opt-out is binding there; mnot on why the signal's design matters, and its limits (II.5)
	6. regulatory capture threatens even the alternatives (VIII.4.5)
6. Conclusion (pyramid, thesis → broad)
	1. restate: the choice is ours, as developers and as buyers
	2. broaden: the co-op values "open, sovereign models built as public goods" and offers Apertus; make crawler conduct an explicit axis (VIII.4); other remedies (VIII.1–3)
		1. counterargument: the co-op runs models whose developers scraped; say so, and place them on the spectrum (VII.5, VIII.4.2)
	3. broadest: the law can move, eventually, as it did on Aaron's issues (V.B.5.3); he was ahead of his time; until it does, we choose

## II. The crawling deal, from inside web architecture

1. Indexing was a norm from (nearly) day one: a whole "Indexing" session at the first Web conference (Geneva, May 1994)[^www94-program]
	1. McBryan, World Wide Web Worm[^mcbryan]; Koster, ALIWEB[^koster-aliweb]; Eichmann, RBSE Spider[^eichmann]
	2. so crawling isn't an intrusion on the web; it's part of what the web was from the start
		1. the law's name for this: *implied license*. The front path invites visitors to "approach the home by the front path, knock promptly, wait briefly to be received, and then … leave"[^jardines]
		2. a public URL is the front path; the license has a scope (knock and leave, not a hundred times a day); a sign narrows it → robots.txt (V.D)
		3. this concedes the right-to-read point up front (VII.1) and moves the argument to *how* and *who pays*
	3. the terms of the norm were already visible in 1994 → the rubric for III
		1. restraint — Eichmann: spider authors "must exercise reasonable restraint in the scope and frequency of execution"
		2. reciprocity — Eichmann: "needing to return something to the Web community in return for the intermittent load that we have placed upon their servers" → the search bargain
		3. net load reduction — Eichmann justifies spiders by "avoided network traffic": a good index replaces "frantic traversals in search of potential information"
			1. crawling was justified *because* it lowered everyone's load; a crawler that re-fetches and sends no visitors fails the 1994 test on its own terms
		4. leave dynamic pages alone — Eichmann: "it is not reasonable to index" HTML "generated dynamically from large databases"
			1. git forges and wikis are exactly that kind of page (III.6, III.7)
		5. identify yourself — McBryan's Worm sent a `From:` header with his email, so a site can "recognize the identity of the requester, determine that it is likely a robot", and write "if problems develop"
		6. honor the sign — robots.txt (II.2.2)
2. The etiquette that came with it
	1. Koster, "Guidelines for Robot Writers" (1993)[^koster-guidelines]
	2. robots.txt: "a consensus on 30 June 1994 on the robots mailing list"[^koster-norobots]
		1. same Martijn Koster is lead author of RFC 9309 (2022)[^rfc9309]: 28 years from mailing-list consensus to standard
	3. the search bargain: crawl ↔ traffic back
		1. stated by Eichmann in 1994 (II.1.3.2)
		2. LLM answers break the return leg
3. The politeness toolkit HTTP already has
	1. conditional GET and caching: don't re-fetch what hasn't changed
	2. 429 Too Many Requests, with Retry-After[^rfc6585]
	3. honest User-Agent, with a contact URL
	4. ⚠️ which of these do AI crawlers ignore? (find operators' reports)
4. robots.txt stayed a gentlemen's agreement
	1. standardizing it was IETF's job, not W3C's: protocols (mostly) go to IETF, formats and the like to W3C; that's how the scope was divided
	2. and even the IETF standard says it's advisory: "These rules are not a form of access authorization"; for real access control, use HTTP authentication[^rfc9309]
		1. so the standard itself puts robots.txt on the request side of *Van Buren*'s gates-up-or-down line (V.B)
5. What's different now
	1. volume and re-crawl frequency; no caching
	2. evasion (III.7): the reverse of McBryan's `From:` header
	3. new opt-out signals: IETF AI Preferences WG[^aipref], co-chaired by Mark Nottingham and Suresh Krishnan
		1. why bother, when robots.txt is ignored? ("Stop! or I'll say stop again!") mnot's answer: EU law makes a machine-readable reservation binding on commercial AI crawlers, but doesn't say what the signal is; its design steers power[^mnot-ai-optout]
			1. robots.txt is per-bot: block AI only by listing every AI crawler, or ban all bots and lose search; banning unknown bots also locks out new entrants and favors big tech (cf. IV.1.3) → one AI-wide signal (`AI-Ingest` user agent or `/.well-known/ai.txt`)
			2. models outlive crawls → policy should apply at model-creation time, retroactively (Apertus already does this, III.1)
			3. only the site admin controls robots.txt; on platforms, the platform decides for users → embed preferences in content (cf. IV.2.4)
		2. limit: none of this reaches evasive or out-of-reach scrapers (III.7); the joke still holds there

## III. The spectrum of crawler behavior (centerpiece)

Graded on the 1994 norms (II.1.3): honor the sign, identify yourself, restraint, reciprocity, leave dynamic pages alone.

| Behavior | Example | Fails |
|---|---|---|
| Exemplary | Apertus | — |
| Compliant, identified, reciprocal | Googlebot | (load, sometimes) |
| Compliant, identified, no reciprocity | ClaudeBot, GPTBot | reciprocity, restraint |
| Self-described crawler, no published policy | DeepSeek | identify yourself (unknown) |
| Agents off the leash | OpenAI agents at Wikimedia | restraint, dynamic pages |
| Evasive, named | Perplexity | sign, identity |
| Evasive, anonymous | residential proxies, random User-Agents | all of them |

1. Exemplary: Apertus (Swiss AI Initiative)
	1. "respecting robots.txt not only at crawl time (January 2025), but also retroactively applying January 2025 opt-out preferences to web scrapes from previous crawls"[^apertus]
		1. exactly the retroactive opt-out mnot proposed in 2024 (II.5.3.1.2)[^mnot-ai-optout]
	2. drops content from sites that block any of a published list of AI crawlers (GPTBot, ClaudeBot, CCBot, Bytespider, …); data reconstruction scripts published
	3. at scale: 15T tokens. Good conduct isn't a toy-model luxury
2. Compliant, identified, reciprocal: Googlebot
	1. ~14 crawls per referral[^cf-ratio] ⚠️ check the Google figure in the primary post
	2. the 1994 bargain, still roughly working; and, by contrast, "everybody was happy when Google indexed us" (VII.2)
3. Compliant, identified, no reciprocity: the frontier labs' training crawlers
	1. their claim: they honor robots.txt ⚠️ cite each lab's crawler docs
	2. reciprocity, measured: Anthropic ~38,000 crawls per referral (Jul 2025)[^cf-ratio]
		1. Eichmann's 1994 reciprocity norm (II.1.3.2), quantified and failed
	3. restraint: iFixit, July 2024, ClaudeBot hit its servers ~a million times in 24 hours; Anthropic's answer, reportedly: use robots.txt[^ifixit] ⚠️ find Wiens's own post or first-hand reporting
		1. → the thesis in miniature: compliant crawling, and the burden of saying no still on the site
	4. OpenAI: honest User-Agent (KDE, via[^ars-oss]); ChatGPT-User honored robots.txt in Cloudflare's test[^cf-perplexity]; but heavy: about a quarter of Diaspora's traffic, and GPTBot the top user agent on one MediaWiki server (via[^ars-oss])
4. Self-described crawler, no published policy: DeepSeek
	1. "our crawling system was overly biased toward text-centric web content; we therefore re-bootstrapped it from Common Crawl"[^deepseek-v41]
	2. no published user-agent or robots.txt policy found ⚠️; not accused, but not answerable either (II.1.3.5)
	3. similar: Z.ai's GLM-5 uses "massive web datasets" and "refreshed snapshots from major code hosting platforms"[^glm5]; no conduct statement found
5. Agents off the leash: OpenAI agents at Wikimedia, 2026
	1. agents "we believe to be operated by OpenAI" made "millions of automated requests", "crawled millions of pages", and may have "contributed to a partial outage" of the Wikidata Query Service; plus unapproved wiki edits and attempts to use wiki tools as proxies[^wmf-openai]
	2. not the training crawler, but the same organization and the same who-pays question; agentic traffic is the next wave
6. Evasive, named: Perplexity
	1. Cloudflare: "repeatedly modifying their user agent and changing their source ASNs to hide their crawling activity, as well as ignoring — or sometimes failing to even fetch — robots.txt files"[^cf-perplexity]
7. Evasive, anonymous: "there's gold in them thar hills"
	1. SourceHut: "If you think these crawlers respect robots.txt then you are several assumptions of good faith removed from reality"; random User-Agents, "tens of thousands of IP addresses – mostly residential"; "20-100% of my time in any given week" on mitigation[^devault]
	2. LWN: "most of them religiously avoid ever looking at robots.txt"[^lwn]
	3. Xe Iaso: robots.txt already said `Disallow: /`; "they lie, change their user agent, use residential IP addresses as proxies"[^xe-amazon]
	4. Fedora, GNOME, KDE and others: up to 97% of traffic from AI bots; KDE's GitLab knocked offline by traffic "from Alibaba IP ranges" (third-hand; Alibaba *Cloud* hosts many customers, so not evidence against Qwen's developers)[^ars-oss]
	5. who sells the residential IPs? a reader comment on LWN names Bright Data (formerly Luminati) ⚠️ comment only; if it holds up, the *Bright Data* of V.B
	6. the named labs are the visible part; the evasive traffic is mostly unattributed, which is why enforcement fails (V.D.5.2.2)
8. The sites' response, measured: in one year (2023–24), "~5%+ of all tokens in C4, or 28%+ of the most actively maintained, critical sources" became fully restricted[^consent-crisis]

## IV. The cost (facts)

1. Traffic and cost
	1. bandwidth, CPU, rate-limit engineering: all borne by the site
		1. Read the Docs: one crawler took 73 TB in May 2024, "over $5,000 in bandwidth charges"[^rtd]
		2. Wikimedia: bots are ~35% of pageviews but "at least 65%" of the most expensive traffic[^wmf]
	2. forcing small sites to build walls: everybody loses
	3. walls also block the good crawlers (archives, researchers, small search engines), and readers
		1. CAPTCHAs; Anubis ("Making sure you're not a bot!"), a proof-of-work gate in front of the site[^xe-anubis][^anubis]
		2. my experience: I can't just `curl` pages reliably anymore
		3. even public law: researching this, Municode and American Legal returned 403 and Justia served a bot check instead of Supreme Court opinions; only Cornell LII and the Kansas Revisor answered
			1. the walls against AI crawlers also wall off the law from programmatic reading, which Carl Malamud has long fought for[^georgia-pro]
		4. the open web's "anyone can fetch it" (II.1.2) erodes for everyone, not just the bots
2. Not new: the spam precedent
	1. Sobig.F, 2003: days of MTA work, then the end-user server still drowns in spam ("If I had a rocket launcher...", [2003](https://www.madmode.com/2003/advogato_entry0005.html))
		1. "first law of SMTP": deliver or bounce → the protocol obliges the victim
		2. analogy: the open web obliges the site to serve
	2. "nice web site you got there": crime at a distance and the tragedy of the commons ([2007](https://www.madmode.com/2007/breadcrumbs_0192.html))
		1. proof-of-work doesn't fix spam economics[^laurie-clayton]
			1. 21 years later, small sites reach for proof-of-work again (Anubis, IV.1.3.1)
			2. ❓ do Laurie & Clayton's economics apply? a crawler fetches millions of pages, a reader a few; or does the cost again land on people with slow phones?
	3. blog spam: the only remedy was the big hammer, turn off comments for everyone ([2009](https://www.madmode.com/2009/breadcrumbs_0250.html))
	4. the economics of email led me to trade my privacy to Google for spam protection ([2018](https://www.madmode.com/2018/rchain-gov-forum-sea))
		1. pattern: small operators can't defend alone → consolidate under a giant → new power imbalance
		2. today's version: put your site behind a big CDN's bot wall
	5. what changed: spammers were outlaws; scrapers are the biggest companies in the economy

## V. The law, briefly (IRAC per theory)

### A. DMCA §1201 anti-circumvention

1. Issue: does ignoring robots.txt "circumvent a technological measure"?
2. Rule: ban on circumventing access controls *and* on tools; civil and criminal penalties[^usc1201]
3. Application
	1. robots.txt is a request, not a lock
	2. standing problems even for paywalled publishers[^managingip]
	3. NYT v. Microsoft: 2025-03-26, several DMCA claims dismissed, core copyright claims kept[^nyt-wiki]
		1. ⚠️ which DMCA section? probably §1202 (copyright-management info), not §1201; check the opinion
4. Conclusion: no help to small sites
5. Why keep it anyway
	1. what I learned: I came in assuming the DMCA was the law here; most readers probably do too
	2. common confusion: Aaron was charged under the CFAA and wire fraud, not the DMCA, and not copyright: "hacker crimes, not copyright-infringement crimes, because he didn't actually distribute any documents" (*The Awl*, via[^swartz-wiki])
	3. criminal penalties (§1204) require willfulness "for purposes of commercial advantage or private financial gain" ⚠️ check the text; Aaron wasn't making money, and rate limits aren't DRM
	4. the foil for VI.A: who gets criminal teeth
	5. from inside W3C: the DRM era
		1. 2001 DRM workshop: "Readers, viewers, and listeners are fans, not thieves"[^manasse] (A Return to Patronism, [2010](https://www.madmode.com/2010/06/return-to-patronism.html))
		2. ❓ later: EME at W3C (2017), the web standards body itself building the big fence

### B. CFAA (criminal "hacking")

1. Issue: is scraping past robots.txt "without authorization"?
2. Rule
	1. "gates-up-or-down"[^vanburen]
	2. public data isn't "without authorization"[^hiq]
	3. *Meta v. Bright Data*[^brightdata] ⚠️ confirm court and year
	4. DOJ policy (2022): ToS violations alone not charged[^doj-cfaa]
3. Application: public page = gate up; robots.txt doesn't lower it
	1. but evading a block ≠ ignoring a request: UA spoofing and proxy rotation (III.7) look like lowering a gate and climbing over
		1. *United States v. Swartz* is the precedent for how prosecutors treat that (V.B.5)
4. Conclusion: for the web's scrapers, no criminal route in practice
5. The case that shows what the CFAA can do: *United States v. Swartz* (2011–13)
	1. facts
		1. Aaron had JSTOR access as a Harvard research fellow; he ran a script ("keepgrabbing.py") on MIT's open network to bulk-download journal articles[^swartz-wiki]
		2. when JSTOR and MIT blocked his IP and then his MAC address, he changed them; the laptop sat in an unlocked wiring closet[^abelson]
		3. JSTOR got the data back and declined to sue; the state charges were dropped[^swartz-wiki]
		4. the U.S. Attorney's office pressed on: superseding indictment, 13 felony counts (11 CFAA, 2 wire fraud), "up to 35 years in prison" and $1 million[^swartz-indictment][^swartz-wiki]
		5. every plea offer required pleading guilty to felonies; he refused[^wiki-aaron]
			1. Lessig: "why it was so necessary that Aaron Swartz be labeled a 'felon'. For in the 18 months of negotiations, that was what he was not willing to accept."[^lessig-bully][^wiki-aaron]
			2. the short sentences that commenters make light of miss this: a felony record would cost him his vote and his chance to run for office: it would have taken away his reason for living ❓ source (his partner's or friends' accounts; *The Internet's Own Boy*)
			3. congressional staffers were told the Guerilla Open Access Manifesto[^guerilla] played a role in prosecutorial decisions: he was prosecuted for his radical ideas as well as his acts[^wiki-aaron]
		6. Aaron died on January 11, 2013, at 26, two days after prosecutors rejected his counter-offer; the charges were then dismissed[^abelson][^wiki-aaron]
			1. relentlessly prosecuted: the office never relented, through 18 months of negotiation and to the last counter-offer
	2. the parallel
		1. bulk download + changing addresses after a block = what the evasive crawlers of III.7 do, from "tens of thousands of IP addresses"[^devault]
		2. one person, research articles mostly paid for by the public, no money made → 13 felonies
		3. companies, the whole web, billions in valuation → not a single charge (VI.A)
	3. the law after Aaron
		1. Aaron's Law (2013, 2015): exclude terms-of-service violations from the CFAA[^lofgren-wyden]; stalled in committee both times[^aarons-law]
		2. *Van Buren* (2021) narrowed "exceeds authorized access", 8 years too late[^vanburen]; DOJ's 2022 charging policy[^doj-cfaa]
		3. would Aaron be charged today? the day it came down: "Wow. This is a real birthday present … the statute that the United States said @aaronsw had violated. Applying Barrett's reading, he plainly did not."
			1. ❓ whose tweet (June 3, 2021)? in my bookmarks, author not recorded; find and cite 🙋
			2. but the evasion theory (IP/MAC changes) may survive *Van Buren*'s gates-up-or-down test (V.B.3.1)
		4. and on access, the manifesto's goal became federal policy: research funded by the government must be "publicly accessible without an embargo," by the end of 2025[^ostp-2022]
			1. plus JSTOR's own opening up (VII.1.3.3)
			2. not vindication of the method: the law moved on access, not on bulk copying of paywalled work
	4. what I'm not asking for: prosecuting scrapers the way he was prosecuted
		1. nobody should face 35 years for downloading; the point is the asymmetry (VI.A), and the cost landing on the small (IV.1)

### C. Contract / terms of service

1. Issue: is robots.txt (or a ToS) a binding contract on the crawler?
2. Rule: browsewrap needs notice + assent
3. Application: robots.txt has no assent mechanism; hard to bind bots to a ToS[^fkks]
4. Conclusion: weak; and suing costs more than the overage

### D. Trespass: land vs. chattels (the heart of the legal gap)

1. Two old torts
	1. trespass to land: entering without leave is the wrong in itself; no harm needed: liability "irrespective of whether a person causes harm" (Restatement (Second) of Torts §158)[^wiki-land]
		1. "no man can set his foot upon his neighbour's close without his leave" (*Entick v. Carrington*, 1765, quoted in[^jardines])
	2. trespass to chattels (movable things): actionable only with harm (damage, impairment, lost use): liability "if, but only if" (Restatement (Second) of Torts §218)[^wiki-chattels]
2. Notice makes entry wrongful, for land
	1. implied license to approach and knock (II.1.2.1); a sign revokes it[^jardines]
	2. criminal "defiant trespass": notice by posting "reasonably likely to come to the attention of intruders", same as a fence
		1. e.g. Kansas, my state[^ks-trespass]; ❓ how general? the Model Penal Code (§221.2, "defiant trespass") is the likely template, but I have no public source for it yet
		2. a sign is as good as a lock, for land
	3. "No Soliciting": the owner's sign, and in many cities public enforcement of it
		1. constitutionally fine: the city can't decide who may knock (permit scheme struck), but residents' "No Solicitation" signs give "ample protection for unwilling listeners"[^watchtower]
		2. e.g. Overland Park: city supplies the signs; soliciting a posted home violates city code ⚠️ get ordinance text 🙋 [OP municipal code (American Legal)](https://codelibrary.amlegal.com/codes/overland_park/latest/overview), [Municode](https://library.municode.com/ks/overland_park)
3. Courts treat a server as a chattel, not as premises
	1. crawler enjoined, as interference with a chattel[^ebay]
	2. no trespass without impairment; an email case, ties to IV.2[^hamidi]
	3. so for my server, "I told you not to come in" isn't enough; I must also prove harm
4. Application
	1. robots.txt = the posted sign; ignoring it = willful
	2. RFC 9309 (2022) standardizes it[^rfc9309] → stronger notice
	3. but it only matters if notice counts, i.e. if a website is treated like premises
5. Conclusion: the chattel box is coherent, and my grievance fits it: the harm is real
	1. Google indexes my site: I hardly notice the bandwidth. AI scrapers: the bill goes up
		1. that difference *is* the harm test; and it matches Eichmann's 1994 restraint and net-load norms (II.1.3)
		2. (the bill that goes up is the self-hoster's, IV.2.4)
	2. so the gap isn't the doctrine; it's enforcement
		1. the harm is real but small per site: a few hundred dollars vs. a lawyer
		2. attribution: you can't sue whom you can't identify; evasion (III.7) defeats the claim before it starts → McBryan's `From:` header (II.1.3.5) was what made a robot answerable
		3. the harm is huge in aggregate, spread across millions of sites
	3. premises vs. chattel stays a side question: place-rules would make notice enough, but harm is what actually hurts
6. Scholarship: revitalizing trespass to chattels for GenAI scraping[^atkinson]

### E. Synthesis: the enforcement gap

1. Every route is civil, slow, expensive
2. Practitioner survey[^ropesgray]

## VI. Power analysis

### A. Two-tier enforcement

1. The starkest case: Aaron vs. the labs
	1. Aaron: one person, journal articles, IP/MAC evasion → federal prosecution, 13 felonies (V.B.5)
		1. the felony label was the point (V.B.5.1.5)
	2. the labs: the whole web, often with evasion (III.7); even pirated books are a civil matter
		1. Anthropic downloaded millions of pirated books for training; it settled with authors for $1.5 billion, a civil payment, no charges[^bartz] ⚠️ cite the settlement itself
		2. (I'm using Claude to write this outline: Where I stand)
	3. same act, opposite treatment; the difference is power, not conduct
2. Big fence (DRM) → federal crime, public prosecutors[^usc1201]
3. Small fence (robots.txt) → "civil dispute; hire a lawyer"
4. 2026-09: DOJ files a brief *for* OpenAI in NYT v. Microsoft[^nyt-wiki] ⚠️ get the Reuters report or the brief
	1. the government isn't a neutral bystander; it sides with the bigger player even against the NYT
	2. sharpens the thesis: not big vs. small, but whoever holds up GDP (VI.E)
5. Same asymmetry Lessig named: the RIAA's $98B threat against students vs. WorldCom's $750M fine[^lessig-fc] (A new year brings a new low in media and culture, [2011](https://www.madmode.com/2011/01/new-year-brings-new-low-in-media-and.html))

### B. How the big fence got its teeth: policy laundering

1. the content industry (MPAA, RIAA) lobbied anti-circumvention into a treaty: WIPO Copyright Treaty, Art. 11[^wct] ⚠️ source the lobbying
2. then "implemented" it at home, going beyond the treaty: DMCA 1998[^wcpptia]
3. then exported it through trade deals / USTR Special 301 ⚠️ find a scholarly source for "policy laundering"

### C. Money in politics

1. *Citizens United*[^citizens-united]
2. My own record
	1. wrote my representatives after *Inside Job*; form-letter silence (The Voters First Pledge, [2011](https://www.madmode.com/2011/07/voters-first-pledge-what-do-my-elected.html))
	2. "we, as U.S. citizens, are party to it" ("Lord of War", [2010](https://www.madmode.com/2010/11/lord-of-war-and-land-of.html))
	3. matching movie spending with donations to EFF and Rootstrikers ([2014](https://www.madmode.com/2014/aaronsw-match.html))

### D. Private tyranny

1. The Bill of Rights constrains government; who constrains private power at this scale?
2. A tyranny-of-the-majority variant: everyone benefits from cheap AI, small operators pay
3. Scholars who center power (to read before citing)
	1. informational capitalism[^cohen]
	2. platform dominance[^khan]
	3. one-way visibility[^pasquale]
	4. Law and Political Economy Project ⚠️ pick a specific piece
4. The gatekeeper pattern in my archive
	1. Imagine there's no ICANN ([2012](https://www.madmode.com/2012/06/imagine-theres-no-icann-with-namecoin.html))
	2. Google, Jabber, good and evil ([2006](https://www.madmode.com/2006/breadcrumbs_0063.html))
	3. platforms change terms unilaterally (closet librarian, [2021](https://www.madmode.com/2021/closet-librarian-approach-cloud-services.html); divesting from Flickr, [2023](https://www.madmode.com/2023/file-purge-flickr-divest.html))

### E. Scale makes it different in kind

1. AI as the bet holding up GDP → too big to regulate
2. so: "when institutions won't enforce, what's left?"
3. regulatory capture cuts against the co-op too (VIII.4.5)

## VII. Counterarguments / complications

1. Right to read; scraping freedom protects researchers and archivists
	1. *hiQ* cuts both ways[^hiq]
	2. Internet Archive (use archive.org for commons, [2025](https://www.madmode.com/2025/01/madmode-blog-108-issuecomment-2622160518.html))
	3. any fix must not wall out these crawlers (IV.1.3)
	4. Aaron himself argued for liberating knowledge: "Guerilla Open Access Manifesto" (2008)[^guerilla]
		1. so am I defending one bulk downloader and condemning others? no: the line is who bears the cost and who gets punished, not whether bulk download is allowed
		2. JSTOR got its data back and its servers recovered; small sites today just keep paying
		3. and on access, he was partly right: in the 2020 pandemic, JSTOR opened its open-access content without login and expanded free reading[^jstor-covid] ("You were right, @aaronsw," as someone tweeted ❓ whose?)
2. Everybody was happy when Google indexed us (II.2.3, III.2)
3. I'm a user and an employee of the thing I'm criticizing (Where I stand)
4. Boycott vs. exceptions: boycotts don't admit exceptions for good uses
	1. the spectrum (III) is the answer: grade conduct, don't boycott a technology
5. The co-op runs models whose developers scraped (VIII.4.2)

## VIII. Remedies, ending with what you can choose

1. Legal
	1. the no-soliciting model: the owner posts the sign, the public enforces it (V.D.2.3)
		1. no lawyer, no proof of harm; the visitor bears the burden of reading the sign
		2. exemptions are possible without gutting it (as for political canvassing) → archives, research crawlers (VII.1)
	2. or keep the chattel rule and make the harm cheap to claim
		1. small claims court (no lawyer)? ⚠️ jurisdiction over an out-of-state crawler operator; limits vary by state
		2. aggregation: class actions, or a collective (a co-op?) acting for many small sites
		3. both need attribution → require crawlers to identify themselves (II.1.3.5)
	3. robots.txt (RFC 9309) as legally cognizable notice
2. Technical
	1. spam history: authenticated senders (SPF/DKIM) → authenticated crawlers? ⚠️ look up current bot-auth proposals (Cloudflare mentions Web Bot Auth[^cf-perplexity])
	2. capabilities: authority you can hand out and revoke; rules that hold without relying on institutions to enforce them
		1. the split: limit power yes, replace institutions with markets no
3. Political: campaign finance (VI.C) — the root, and the hardest
4. What you can choose: the inference.coop
	1. what it is: "AI, governed together"; it values "Open, sovereign models built as public goods rather than proprietary products"[^coop-home], alongside privacy and green energy
	2. honest about what it runs: models whose developers trained on scraped web data[^coop-models]
		1. terms: the co-op's *providers* are hosts (Tinfoil, GreenPT, Regolo); the crawling was done by the model *developers*: DeepSeek (the default), Z.ai, OpenAI, Alibaba, Swiss AI Initiative, Mistral
		2. their conduct spans the spectrum: OpenAI (III.3, III.5); DeepSeek and Z.ai unknown (III.4); Apertus exemplary (III.1)
		3. stated sources: DeepSeek[^deepseek-v41], GLM-5[^glm5], Whisper ("transcripts of audio on the internet")[^whisper]; silent: gpt-oss[^gpt-oss], Qwen[^qwen3] (⚠️ Qwen 3.5 has only a JS blog post 🙋 [qwen.ai](https://qwen.ai/blog?id=qwen3.5)), Voxtral ⚠️
	3. the co-op offers Apertus, and names "model origins" as a member choice: you can pick the top of the spectrum today
	4. the ask (for Nov 6, and for readers): make crawler conduct an explicit axis, next to privacy and green energy
		1. honors robots.txt? identifies itself? publishes its policy? no evasion?
		2. pooled purchasing power = a voice the small operator doesn't have alone
		3. members who run sites: share logs, blocklists
		4. good conduct costs a bit more; subsidized frontier pricing is the headwind (X)
	5. and the risk: regulatory capture
		1. June 2026, social.coop: Nathan Schneider proposes an inference co-op for academic AI[^schneider-proposal]; I reply "I hope you can stay ahead of regulatory capture," linking Warman[^warman]
		2. Nathan: "The whole model could be rendered illegal by a deft move from the dominant 'labs.'"[^schneider-reply]
		3. → the same two-tier pattern as VI.A; the co-op is on the small-fence side too

---

## Left out of the five-paragraph theme

Undecided: material not yet placed in a paragraph above. Once placed or cut, an item is deleted from this list.

1. contract / terms of service (V.C) → cut, or folded into "every civil route is slow and expensive" (V.E)
2. money in politics (VI.C) → cut; maybe the conclusion's broadest step
3. Housekeeping, not content: open items (XI); companion forum post

## IX. Parked: appropriated work / copyright / consent (separate piece)

1. "Doom Loop" and the admissions
	1. Microsoft exec: "an astonishing theft of unprecedented proportions"; internal doc: a "doom loop" killing "the entire web"[^koebler]
	2. two admissions: dependence on uncompensated work; substitution for it[^chisnall]
2. Bad faith on the record
	1. NYT filing unsealed 2026-09-17, with a summary-judgment motion[^nyt-wiki]
	2. "hack to get around nytimes paywall" / "ah, nice" ⚠️ pull the filing from the docket[^nyt-docket]
		1. bridge to this piece: paywall evasion is a crawling-conduct question (III.7)
3. Copyright / fair use (IRAC)
	1. Issue: is training on scraped works fair use?
	2. Rule: 17 U.S.C. §107, four factors; "transformative"
	3. Application: NYT v. Microsoft[^nyt-docket][^nyt-wiki]
		1. timeline: filed 2023-12; motions to dismiss largely denied 2025-03-26; amended complaint 2026-06; summary-judgment motion 2026-09-17
		2. DOJ brief for OpenAI (2026-09)
		3. EFF amicus on OpenAI's side ⚠️ cite the brief itself
	4. Conclusion: open; and only big publishers can play
	5. the copying argument proves too much: "Training of AI language models begins with copying, which we believe has infringed our copyrights" (Edward Hasbrouck, National Writers Union, to the Copyright Office, given undue weight in mnot's survey of the policy context[^mnot-ai-optout]); by that logic every reader whose browser loads the page makes an infringing copy
		1. the law's answer isn't "not a copy" but "licensed": RAM copies can count (*MAI v. Peak*, 9th Cir. 1993, an unlicensed repair firm; narrowed by 17 U.S.C. §117(c), 1998, and *Cartoon Network v. Cablevision*, 2d Cir. 2008, transient buffers) ⚠️ verify all three
		2. open publication implies a license to read, like the front-path license (II.1.2.1)
		3. so the line isn't copying; it's the scope of the license: does it reach training? Same shape as the trespass question (scope of the invitation)
4. The bind: winning here strengthens the copyright maximalism I oppose
	1. term extension, Mickey, *Happy Birthday*
	2. "what entered the public domain Jan 1 2011? Nothing." (A new year brings a new low, [2011](https://www.madmode.com/2011/01/new-year-brings-new-low-in-media-and.html))
	3. Lessig's refrain[^lessig-fc] (Free Culture, [2007](https://www.madmode.com/2007/breadcrumbs_0214.html))
5. EFF, long my ally on free culture, on OpenAI's side
	1. their argument concerns copying, not bandwidth → the split between the two pieces: copying maybe OK, dumping costs not
6. Privacy / contextual integrity
	1. "published for humans" ≠ consent to corporate harvest[^great-scrape]
7. Remedy parked here: invert the burden, opt-in for training

## X. Parked: economics (separate piece)

1. Frontier-lab subscriptions are heavily subsidized (already made this point in my first inference.coop forum post ❓ link)
2. So the co-op's gateway competes against below-cost pricing; the consolidation pattern (IV.2.4) again
3. The broader economics: AI as the bet holding up GDP (VI.E)

## XI. Open items

1. Find a primary source for every ⚠️
2. Fill every ❓ (e.g. W3C memories)
3. Fetch every 🙋 by hand; save Zotero snapshots
4. Zotero: add what's cited here and not yet in the `invasive-ai` collection; merge the duplicate *hiQ* items
5. madmode length: Part V probably collapses to a paragraph with links; II, III and VIII.4 carry it

## Companion: inference.coop forum post (short, before Nov 6)

1. Link to the madmode piece (or post this first if the piece isn't ready)
2. One paragraph: the spectrum (III), with the co-op's models placed on it
3. Apertus already meets the 1994 norms, and the co-op already values "open, sovereign models built as public goods"[^coop-home]
4. The ask: crawler conduct as an explicit axis (VIII.4.4)
5. The June thread on regulatory capture (VIII.4.5) as context for why it matters to us
6. Maybe one line on Aaron (V.B.5): the asymmetry the co-op is pushing against

## References

> Newest first.

[^wmf-openai]: Selena Deckelmann, "OpenAI “rogue” agent activities found on Wikimedia projects," Diff (Wikimedia Foundation), Oct. 5, 2026. [diff.wikimedia.org](https://diff.wikimedia.org/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/)

[^coop-home]: Inference Cooperative, "AI, governed together," homepage, as of Oct. 2026. [inference.coop](https://inference.coop)

[^coop-models]: Inference Cooperative, "Models," co-op documentation, as of Oct. 2026. [git.inference.coop](https://git.inference.coop/co-op/docs/src/branch/main/models.md)

[^nyt-wiki]: "The New York Times v. Microsoft and OpenAI," Wikipedia, revision of Sep. 18, 2026. [en.wikipedia.org](https://en.wikipedia.org/w/index.php?title=The_New_York_Times_v._Microsoft_and_OpenAI&oldid=1375498373)

[^chisnall]: David Chisnall, post on Infosec Exchange, Sep. 18, 2026. [infosec.exchange](https://infosec.exchange/@david_chisnall/117290835262126012)

[^koebler]: Jason Koebler, "'Doom Loop': OpenAI and Microsoft Admits LLMs Are Destroying the Web and Built on Theft," *404 Media*, Sep. 17, 2026. [404media.co](https://www.404media.co/doom-loop-openai-and-microsoft-admits-llms-are-destroying-the-web-and-built-on-theft/)

[^deepseek-v41]: DeepSeek-AI, "DeepSeek-V4.1 Technical Report," Sep. 2026. [Hugging Face PDF](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf)

[^schneider-reply]: Nathan Schneider, reply on social.coop, Jun. 15, 2026. [social.coop](https://social.coop/@ntnsndr/116756181172623122)

[^schneider-proposal]: Nathan Schneider, "An inference cooperative for academic AI," Jun. 2026. [nathanschneider.info](https://nathanschneider.info/2026/06/an-inference-cooperative-for-academic-ai/) · [social.coop post, Jun. 14, 2026](https://social.coop/@ntnsndr/116750348962878181)

[^ropesgray]: Ropes & Gray, "Web Scraping in the Age of AI: Guidance for Data Owners and Scrapers," May 2026. [ropesgray.com](https://www.ropesgray.com/en/insights/alerts/2026/05/web-scraping-in-the-age-of-ai-guidance-for-data-owners-and-scrapers)

[^warman]: "The Moat or the Commons," *Warman Notes*, Apr. 27, 2026. [warman.life](https://www.warman.life/blog/2026-04-27-the-moat-or-the-commons/) · my reply citing it: [social.coop, Jun. 15, 2026](https://social.coop/@dckc/116754035978430967)

[^managingip]: Eric Vandevelde, Ilissa Samplin and Josh Leopold (Gibson Dunn), "The Article III Standing Problem for AI-Scraping Anti-Circumvention Claims," *Managing IP*, Apr. 27, 2026. [managingip.com](https://www.managingip.com/article/2ga02si5c24xaq46ren7k/copyright/the-article-iii-standing-problem-for-ai-scraping-anti-circumvention-claims)

[^glm5]: GLM-5 Team (Z.ai), "GLM-5: from Vibe Coding to Agentic Engineering," arXiv:2602.15763, Feb. 2026, §2.2. [arxiv.org](https://arxiv.org/abs/2602.15763)

[^mnot-open-web]: Mark Nottingham, "Some Thoughts on the Open Web," *mnot's blog*, Jan. 20, 2026. [mnot.net](https://www.mnot.net/blog/2026/open_web)

[^fkks]: Peter Devlin, "Is Your Site's Robots.txt Giving Content to AI Models for Free?," Frankfurt Kurnit Klein & Selz, *Technology Law* blog, Dec. 23, 2025. [fkks.com](https://technologylaw.fkks.com/post/102lz1g/is-your-sites-robots-txt-giving-content-to-ai-models-for-free)

[^atkinson]: David Atkinson, "Revitalizing Trespass to Chattels in the Era of GenAI Scraping," arXiv:2510.16049, Oct. 2025. ⚠️ confirm author and date. [arxiv.org](https://arxiv.org/abs/2510.16049)

[^bartz]: "Anthropic," Wikipedia (pirated books; $1.5 billion settlement, 2025). ⚠️ replace with the settlement order or a news report on *Bartz v. Anthropic*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Anthropic)

[^apertus]: Swiss AI Initiative, "Apertus: Democratizing Open and Compliant LLMs for Global Language Environments," arXiv:2509.14233, Sep. 2025, §3.1.1 and App. B. [arxiv.org](https://arxiv.org/abs/2509.14233)

[^cf-ratio]: Cloudflare, "The crawl-to-click gap: Cloudflare data on AI bots, training, and referrals," Cloudflare Blog, Aug. 29, 2025. [blog.cloudflare.com](https://blog.cloudflare.com/crawlers-click-ai-bots-training/)

[^cf-perplexity]: Cloudflare, "Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives," Cloudflare Blog, Aug. 4, 2025. [blog.cloudflare.com](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)

[^gpt-oss]: OpenAI, "gpt-oss-120b & gpt-oss-20b Model Card," arXiv:2508.10925, Aug. 2025, §2.4. [arxiv.org](https://arxiv.org/abs/2508.10925)

[^qwen3]: Qwen Team, "Qwen3 Technical Report," arXiv:2505.09388, May 2025. [arxiv.org](https://arxiv.org/abs/2505.09388)

[^wmf]: Wikimedia Foundation, "How crawlers impact the operations of the Wikimedia projects," Diff, Apr. 1, 2025. [diff.wikimedia.org](https://diff.wikimedia.org/2025/04/01/how-crawlers-impact-the-operations-of-the-wikimedia-projects/)

[^anubis]: Techaro (Xe Iaso), *Anubis* v1.15.0, release, Mar. 27, 2025. [github.com](https://github.com/TecharoHQ/anubis/releases/tag/v1.15.0)

[^devault]: Drew DeVault, "Please stop externalizing your costs directly into my face," Mar. 17, 2025. [drewdevault.com](https://drewdevault.com/blog/Stop-externalizing-your-costs-on-me/)

[^ars-oss]: "Open source devs say AI crawlers dominate traffic, forcing blocks on entire countries," *Ars Technica*, Mar. 2025. ⚠️ author, day. [arstechnica.com](https://arstechnica.com/ai/2025/03/devs-say-ai-crawlers-dominate-traffic-forcing-blocks-on-entire-countries/)

[^lwn]: Jonathan Corbet, "Fighting the AI scraperbot scourge," LWN.net, Feb. 14, 2025. [lwn.net](https://lwn.net/Articles/1008897/)

[^xe-anubis]: Xe Iaso, "Block AI scrapers with Anubis," Jan. 19, 2025. [xeiaso.net](https://xeiaso.net/blog/2025/anubis/)

[^xe-amazon]: Xe Iaso, "Amazon's AI crawler is making my git server unstable," Jan. 17, 2025. [xeiaso.net](https://xeiaso.net/notes/2025/amazon-crawler/)

[^aipref]: IETF AI Preferences (aipref) Working Group, chartered Jan. 7, 2025. [datatracker.ietf.org](https://datatracker.ietf.org/wg/aipref/about/)

[^rtd]: Eric Holscher, "AI crawlers need to be more respectful," Read the Docs blog, Jul. 25, 2024. [about.readthedocs.com](https://about.readthedocs.com/blog/2024/07/ai-crawlers-abuse/)

[^ifixit]: "iFixit CEO takes shots at Anthropic for 'hitting our servers a million times in 24 hours'," *PC Gamer*, Jul. 2024. ⚠️ secondary; author, day. [pcgamer.com](https://pcgamer.com/software/ai/ifixit-ceo-takes-shots-at-anthropic-for-hitting-our-servers-a-million-times-in-24-hours-and-even-the-ai-companys-own-chatbot-disapproves)

[^consent-crisis]: Shayne Longpre et al. (Data Provenance Initiative), "Consent in Crisis: The Rapid Decline of the AI Data Commons," arXiv:2407.14933, Jul. 2024. [arxiv.org](https://arxiv.org/abs/2407.14933)

[^mnot-ai-optout]: Mark Nottingham, "Considerations for AI Opt-Out," *mnot's blog*, Apr. 21, 2024. [mnot.net](https://www.mnot.net/blog/2024/ai-control)

[^brightdata]: *Meta Platforms, Inc. v. Bright Data Ltd.* (N.D. Cal. Jan. 23, 2024) ⚠️ citation and date unconfirmed; the linked PDF may be a different case. [ca9.uscourts.gov PDF](https://cdn.ca9.uscourts.gov/datastore/opinions/2023/04/18/20-16387.pdf)

[^great-scrape]: Daniel J. Solove and Woodrow Hartzog, "The Great Scrape: The Clash Between Scraping and Privacy," SSRN working paper 4884485, 2024. ⚠️ cite the published version, if any. [BU Law scholarship](https://scholarship.law.bu.edu/cgi/viewcontent.cgi?article=4885&context=faculty_scholarship)

[^nyt-docket]: *The New York Times Co. v. Microsoft Corp.*, No. 1:23-cv-11195-SHS (S.D.N.Y. filed Dec. 2023). [CourtListener docket](https://www.courtlistener.com/docket/68117049/the-new-york-times-company-v-microsoft-corporation/)

[^whisper]: Alec Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision," arXiv:2212.04356, Dec. 2022. [arxiv.org](https://arxiv.org/abs/2212.04356)

[^rfc9309]: M. Koster, G. Illyes, H. Zeller, L. Sassman, "Robots Exclusion Protocol," RFC 9309, Sep. 2022. [rfc-editor.org](https://www.rfc-editor.org/rfc/rfc9309)

[^ostp-2022]: Alondra Nelson, White House Office of Science and Technology Policy, "Ensuring Free, Immediate, and Equitable Access to Federally Funded Research," memorandum, Aug. 25, 2022. [bidenwhitehouse.archives.gov](https://bidenwhitehouse.archives.gov/wp-content/uploads/2022/08/08-2022-OSTP-Public-Access-Memo.pdf)

[^doj-cfaa]: U.S. Department of Justice, "Department of Justice Announces New Policy for Charging Cases under the Computer Fraud and Abuse Act," May 2022. [justice.gov](https://www.justice.gov/archives/opa/pr/department-justice-announces-new-policy-charging-cases-under-computer-fraud-and-abuse-act)

[^hiq]: *hiQ Labs, Inc. v. LinkedIn Corp.*, 31 F.4th 1180 (9th Cir. 2022). [CourtListener](https://www.courtlistener.com/opinion/6460342/hiq-labs-inc-v-linkedin-corporation/)

[^vanburen]: *Van Buren v. United States*, 593 U.S. 374 (2021). [CourtListener](https://www.courtlistener.com/opinion/4888668/van-buren-v-united-states/)

[^georgia-pro]: *Georgia v. Public.Resource.Org, Inc.*, 590 U.S. 255 (2020). ⚠️ confirm reporter page. [LII](https://www.law.cornell.edu/supremecourt/text/18-1150)

[^jstor-covid]: Giovanni Garcia, "Expanded access to JSTOR during COVID-19 crisis," *About JSTOR*, Apr. 15, 2020 (updated from March 2020). [about.jstor.org](https://about.jstor.org/news/expanded-access-to-jstor-during-covid-19-crisis)

[^cohen]: Julie E. Cohen, *Between Truth and Power: The Legal Constructions of Informational Capitalism* (Oxford Univ. Press, 2019).

[^khan]: Lina M. Khan, "Amazon's Antitrust Paradox," 126 Yale L.J. 710 (2017).

[^pasquale]: Frank Pasquale, *The Black Box Society* (Harvard Univ. Press, 2015).

[^abelson]: Harold Abelson, Peter A. Diamond, Andrew Grosso and Douglas W. Pfeiffer, "Report to the President: MIT and the Prosecution of Aaron Swartz," MIT, July 26, 2013. [swartz-report.mit.edu](https://swartz-report.mit.edu/)

[^lofgren-wyden]: Zoe Lofgren and Ron Wyden, "Introducing Aaron's Law, a Desperately Needed Reform of the Computer Fraud and Abuse Act," *Wired*, June 20, 2013. [wired.com](https://www.wired.com/2013/06/aarons-law-is-finally-here/)

[^aarons-law]: "Aaron's Law" (H.R. 2454 / S. 1196, 113th Cong., 2013; reintroduced as H.R. 1918 / S. 1030, 2015), as summarized in "Computer Fraud and Abuse Act," Wikipedia. ⚠️ cite congress.gov. [en.wikipedia.org](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#Aaron's_Law)

[^jardines]: *Florida v. Jardines*, 569 U.S. 1 (2013). [LII](https://www.law.cornell.edu/supremecourt/text/11-564)

[^swartz-wiki]: "United States v. Swartz," Wikipedia (facts, JSTOR's statement, state charges, penalties). [en.wikipedia.org](https://en.wikipedia.org/wiki/United_States_v._Swartz)

[^lessig-bully]: Lawrence Lessig, "Prosecutor as bully," *Lessig Tumblr*, Jan. 12, 2013. (quoted in Wikipedia, "Aaron Swartz") 🙋 [lessig.tumblr.com](https://lessig.tumblr.com/post/40347463044/prosecutor-as-bully)

[^wiki-aaron]: "Aaron Swartz," Wikipedia (plea offers, Lessig's "Prosecutor as Bully," congressional briefing on the Manifesto). [en.wikipedia.org](https://en.wikipedia.org/wiki/Aaron_Swartz)

[^swartz-indictment]: Superseding Indictment, *United States v. Swartz*, No. 1:11-cr-10260 (D. Mass. Sept. 12, 2012). [archived PDF](https://web.archive.org/web/20130608041804/https://www.wired.com/images_blogs/threatlevel/2012/09/swartzsuperseding.pdf)

[^rfc6585]: M. Nottingham, R. Fielding, "Additional HTTP Status Codes," RFC 6585, Apr. 2012. [rfc-editor.org](https://www.rfc-editor.org/rfc/rfc6585)

[^nyt-2011]: John Schwartz, "Open-Access Advocate Is Arrested for Huge Download," *New York Times*, July 19, 2011. [nytimes.com](https://www.nytimes.com/2011/07/20/us/20compute.html)

[^ks-trespass]: K.S.A. 21-5808, Criminal trespass (recodified criminal code, eff. July 1, 2011). [Kansas Revisor of Statutes](https://www.ksrevisor.gov/statutes/chapters/ch21/021_058_0008.html)

[^citizens-united]: *Citizens United v. Federal Election Commission*, 558 U.S. 310 (2010). [CourtListener](https://www.courtlistener.com/opinion/1741/citizens-united-v-federal-election-commission/)

[^guerilla]: Aaron Swartz, "Guerilla Open Access Manifesto," July 2008. [archive.org](https://archive.org/details/GuerillaOpenAccessManifesto)

[^laurie-clayton]: Ben Laurie and Richard Clayton, "'Proof-of-Work' Proves Not to Work," WEIS 2004. [cl.cam.ac.uk PDF](https://www.cl.cam.ac.uk/~rnc1/proofwork.pdf)

[^lessig-fc]: Lawrence Lessig, *Free Culture* (Penguin, 2004), ch. 12, "Harms." [free-culture.cc](http://www.free-culture.cc/)

[^hamidi]: *Intel Corp. v. Hamidi*, 30 Cal. 4th 1342 (2003). ⚠️ add link

[^rdfig-2002]: RDF Interest Group, IRC log, June 28, 2002 (aaronsw and DanC). [chatlogs.planetrdf.com (archived)](http://web.archive.org/web/20190630005615/http://chatlogs.planetrdf.com/rdfig/2002-06-28.html)

[^watchtower]: *Watchtower Bible & Tract Society of N.Y., Inc. v. Village of Stratton*, 536 U.S. 150 (2002). [LII](https://www.law.cornell.edu/supremecourt/text/00-1737)

[^manasse]: Mark S. Manasse, "Why Rights Management is Wrong (and What to Do Instead)," position paper, W3C Workshop on Digital Rights Management, Jan. 2001. [w3.org](https://www.w3.org/2000/12/drm-ws/pp/compaq.html)

[^ebay]: *eBay, Inc. v. Bidder's Edge, Inc.*, 100 F. Supp. 2d 1058 (N.D. Cal. 2000). ⚠️ add link

[^wcpptia]: WIPO Copyright and Performances and Phonograms Treaties Implementation Act, Pub. L. 105-304, tit. I, Oct. 28, 1998; see "WIPO Copyright and Performances and Phonograms Treaties Implementation Act," Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/WIPO_Copyright_and_Performances_and_Phonograms_Treaties_Implementation_Act)

[^usc1201]: 17 U.S.C. § 1201, Circumvention of copyright protection systems (criminal penalties at § 1204). [LII](https://www.law.cornell.edu/uscode/text/17/1201)

[^wct]: WIPO Copyright Treaty, Dec. 20, 1996, art. 11. [IP Mall PDF](https://ipmall.info/sites/default/files/hosted_resources/lipa/copyrights/WIPO%20COPYRIGHT%20TREATY.pdf)

[^koster-norobots]: Martijn Koster, "A Standard for Robot Exclusion," consensus of the robots mailing list, Jun. 30, 1994. [robotstxt.org](https://www.robotstxt.org/orig.html)

[^www94-program]: First International Conference on the World-Wide Web (WWW94), CERN, Geneva, May 25–27, 1994: final programme, "Indexing" session. [archives.iw3c2.org](https://archives.iw3c2.org/www1/FinalProgramme.html) · [preliminary proceedings](https://archives.iw3c2.org/www1/PrelimProcs.html)

[^eichmann]: David Eichmann, "The RBSE Spider — Balancing Effective Search Against Web Load," in R. Cailliau, O. Nierstrasz, M. Ruggier, eds., *First International World-Wide Web Conference* (advance proceedings), CERN, Geneva, May 25–27, 1994, pp. 113–120. [PDF](https://archives.iw3c2.org/www1/PdfWWW94/spider.pdf)

[^koster-aliweb]: Martijn Koster, "ALIWEB — Archie-Like Indexing in the Web," in R. Cailliau, O. Nierstrasz, M. Ruggier, eds., *First International World-Wide Web Conference* (advance proceedings), CERN, Geneva, May 25–27, 1994, pp. 91–100. [PDF](https://archives.iw3c2.org/www1/PdfWWW94/aliweb.pdf)

[^mcbryan]: Oliver A. McBryan, "GENVL and WWWW: Tools for Taming the Web," in R. Cailliau, O. Nierstrasz, M. Ruggier, eds., *First International World-Wide Web Conference* (advance proceedings), CERN, Geneva, May 25–27, 1994, pp. 79–90. [PDF](https://archives.iw3c2.org/www1/PdfWWW94/mcbryan.pdf)

[^koster-guidelines]: Martijn Koster, "Guidelines for Robot Writers," 1993. [robotstxt.org](https://www.robotstxt.org/guidelines.html)

[^wiki-land]: "Trespass to land," Wikipedia (Restatement (Second) of Torts §158, Am. Law Inst. 1979). [en.wikipedia.org](https://en.wikipedia.org/wiki/Trespass_to_land)

[^wiki-chattels]: "Trespass to chattels," Wikipedia (Restatement (Second) of Torts §218, Am. Law Inst. 1979). [en.wikipedia.org](https://en.wikipedia.org/wiki/Trespass_to_chattels)
