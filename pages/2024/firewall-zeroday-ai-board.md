---
title: 'faster, "smarter" and more dangerous'
date: 2024-12-18
tags: [capabilities, security]
published: true
---

"Computers are getting faster, smaller, more connected, and more capable, but when it comes to security, everything is broken." -- [Quinn Norton](https://medium.com/message/everything-is-broken-81e5f33a24e1)

Case in point: on the same day, I see headlines for:

 - [81,000 firewall boxes compromised by a zero-day](https://cybernews.com/security/doj-indicts-ofac-sanctions-chinese-hacker-exploits-sophos-firewalls-/)
 - [a $250 embedded AI board with network connectivity](https://www.msn.com/en-us/technology/tech-companies/nvidia-introduces-device-aimed-at-small-companies-hobbyists/ar-AA1w1tH5)

What do these have in common? The Linux security architecture; that is: ACLs and unverified, unsafe code.

Not just insecure but insecurable.

There's a better way: [operating systems using capability-based security](https://github.com/dckc/awesome-ocap#os) and [formally verified subsystems](https://pmc.ncbi.nlm.nih.gov/articles/PMC5597724/).

See [15min explanation](https://www.youtube.com/watch?v=wW9-KuezPp8) by Mark Miller, Chief Scientist at Agoric.
