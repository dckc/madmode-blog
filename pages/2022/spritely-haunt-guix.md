title: "Hello Spritely Institute! And Haunt. And Guix, again"
date: 2022-08-08
published: true
tags: ["ocaps", "virtual-reality", "games", "publishing"]

Hello, [Spritely Institute](https://spritely.institute/)!

> ... ActivityPub, social networks, smart contracts, object capabilities, and
> secure distributed virtual worlds. ... freely licensed open source ...

Yum, yum, gimme some! Can't wait for mind-boggling stuff like
this [VRChat hack](https://blog.pimaker.at/texts/rvc1/) powered by ocaps and open source!

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/G2u7NOpzcBQ?controls=0&amp;start=5110" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

> Privacy & moderation issues have triggered the permanent shutdown of millions
> of networked communities and the destruction of their relationships and artifacts.

I was just talking with [@simonw](https://twitter.com/simonw)
about [portable posts using ERTP](https://twitter.com/dckc/status/1479108723494699021).
More on that later...

Nice [site](https://spritely.institute/) btw... shiny!

> Powered by [Haunt](https://dthompson.us/projects/haunt.html).

Keep talking... looks clean...

> gives authors the ability to treat websites as Scheme programs.

Or maybe Scheme programs that are also Hardened JavaScript programs,
using James / Jessie on [rockit](https://github.com/cwebber/rockit)?

Let's give it a spin as-is before stretching it...

> To install Haunt ..., run:
> ```
> guix install haunt
> ```

Ah yes... [guix for ocaps at the systemd level](https://github.com/dckc/madmode-blog/issues/144)
is on my wish-list too. I have `guix` on my Ubuntu workstation, don't I? Let's see...
`guix install haunt`...
<strong title="haunt 0.2.5 /gnu/store/5pk6cwrh11bgchm68phj556srvcvdlvb-profile.drv">bingo!</strong>

## Catching up with Guix after 55 days

meanwhile...

```
guix install: warning: Your Guix installation is 55 days old.
guix install: warning: Consider running 'guix pull' followed by
'guix package -u' to get up-to-date packages and security updates.
```

so...

```
15:38 jambox$ guix pull
Updating channel 'guix' from Git repository at 'https://git.savannah.gnu.org/git/guix.git'...
Authenticating channel 'guix', commits 9edb3f6 to 2dfbd03 (5,405 new commits)...
...
```

Ugh... taking a while... I wonder what it's doing, so
I hop over to [#guix](https://matrix.to/#/#guix:libera.chat)
and learn that the 5K commits include a big merge recently.
I'm just about to give up on it when it comes back to life...

```
185.4 MB will be downloaded
building /gnu/store/7y8wijc8zmbf8il1yzrv4ivmggi5zx7i-compute-guix-derivation.drv...
Computing Guix derivation for 'x86_64-linux'...

News for channel 'guix'
  Icedove 91: profile folder moved to `~/.thunderbird'
  `gdm-service-type' now supports Wayland

16:10 jambox$ guix package -u
The following derivation will be built:
   /gnu/store/gpf86rpdl5k21v65xdshv7qdypwc3w89-profile.drv
33.2 MB will be downloaded

16:15 jambox$ guix install haunt
The following derivation will be built:
   /gnu/store/kciishw2a3xb52ql3m55m3g16dry7p0h-profile.drv
```

Thansk for the "News..." bit. The editorial discretion shows user-centered design.
`guix search` is another breath of fresh air in contrast to the way `apt` and `nix`
seem to grudgingly provide a search feature. Likewise:

```
hint: Consider setting the necessary environment variables by running:

     GUIX_PROFILE="/home/connolly/.guix-profile"
     . "$GUIX_PROFILE/etc/profile
```

`guix install emacs` gives 27.2 (2021) where Ubuntu gives 26.3 (2019).
And `guix install gnucash` has the new sqlite3 and postgres support.
Yes, this could be my tribe. I can't go all in yet because I use Brave
and I think there's a reason guix doesn't support it.

Now let's pop back...

## Blogging with Haunt eval, cont.

Stubbed my toe on `ERROR: In procedure setlocale: Invalid argument`.
But `guix search locale` guided me nicely to `guix install glibc-locales`.
Then `asset processing failed with errno:  "images" 2` because the homepage
has `(static-directory "images")` in the example config but neglects `mkdir images`.
(The tutorial doesn't have this bug.) Now we're rolling:

```
09:48 connolly@jambox$ haunt serve
serving site on port 8080
```

So close! If it were `serving site on http://localhost:8080` I could just follow the link.

> First post!
> by Eva Luator

There's my tribe again :)

But I doubt netlify supports guix as well as they support python and node.js.
Here's hoping they do it well enough...
