title: "Closet Librarian Approach to Cloud Services"
date: 2021-12-18
tags: ["cloud-services", "scm", "writing", "publishing", "IndieWeb", "closet-librarian"]
published: true
summary: "I don't trust any cloud services. I keep my own copies."

A colleague suggested we shouldn't delete calendar items of old meetings.
I said I don't rely on my calendar for records of the past.
Then I admitted that actually, I keep version-controlled backups of my cloud-hosted calendars.

I'm content to use the [Google calendar export feature](https://support.google.com/calendar/answer/37111?hl=en)
manually. I tend to do it in preparation for travel or perhaps when reviewing a trip:

```
gdata$ hg log10
790:9efa3d723bb1 2021-10-16 before SFO trip
789:03f577c7a24e 2021-08-08 RedRocks Road Trip KML data from Google Timeline
```

In general, I don't trust any cloud services. I keep backups of
linkedin contacts, tweets, etc.

I'm much more comfortable using github issues to capture my thoughts
since I discovered "Include your own updates" in the
[email notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#customizing-your-email-notifications).

I generally follow the [IndieWeb PESOS](https://indieweb.org/PESOS) pattern: Publish Elsewhere, Syndicate (to your) Own Site
rather than [POSSE](https://indieweb.org/POSSE): Publish (on your) Own Site, Syndicate Elsewhere.
The cost of keeping backups in an open format is manageable (I avoid services that don't support it)
but economies of scale naturally result in rich knowledge capture and sharing user interfaces for large
communities--why should I limit myself to the writing tools I can maintain on my own site?

The ownership risk seems manageable: in large communities including many of my peers,
I rely on them to alert me to poor terms of service, and when I venture out on new ground,
I read the TOS myself fairly carefully.

PESOS also gives me editorial discretion over which syndicated copies go on the front page of my blog
and which go on backups in a closet.
