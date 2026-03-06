---
title: "February 2023 Bookmarks: security, nixpkgs, and nixos"
date: 2023-02-01
published: true
tags: ["bookmarks", "diigo", "shared", "KC", "car-culture", "collaboration", "cosmos", "genode", "genodians", "governance", "sculptos"]
---

Shared bookmarks saved in February 2023.

- total bookmarks: 29
- total annotations captured: 3

## Links

<ul class="bookmarks">
  <li>
    <a href="https://www.flickr.org/why-were-doing-this/?utm_campaign=flickr-foundation&amp;utm_source=Flickr&amp;utm_medium=email&amp;utm_content=announcement">Why we're doing this - Flickr Foundation</a><br>
    2023-02-27<br>
    <blockquote>we’re thrilled to announce the founding of our very own nonprofit, the <strong>Flickr Foundation</strong>.</blockquote>
  </li>
  <li>
    <a href="https://www.hpl.hp.com/techreports/2009/HPL-2009-53.pdf">"Not One Click for Security" -- how you can engineer a capab...</a><br>
    2023-02-26 tweet<br>
    <p class="bm-desc">"Not One Click for Security" -- how you can engineer a capability-secure UI so that natural user actions produce authorization information (it works so well that one user even told them it's great, but they should add security). <a href="https://t.co/3osAJdOcwU">https://t.co/3osAJdOcwU</a> ht A great Stiegler paper on secure UI design: <a href="https://t.co/FiWk0kvkCe">https://t.co/FiWk0kvkCe</a></p>
  </li>
  <li>
    <a href="https://github.com/NixOS/nixpkgs/blob/a3e89389930f5f2d0efed3578bff2f4b39896fbc/flake.nix">nixpkgs/flake.nix at a3e89389930f5f2d0efed3578bff2f4b39896fbc · NixOS/nixpkgs</a><br>
    2023-02-25<br>
    <blockquote><tr><td id="LC47" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># The "legacy" in `legacyPackages` doesn't imply that the packages exposed</span></td> </tr> <tr> <td id="L48" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="48"></td> <td id="LC48" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># through this attribute are "legacy" packages. Instead, `legacyPackages`</span></td> </tr> <tr> <td id="L49" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="49"></td> <td id="LC49" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># is used here as a substitute attribute name for `packages`. The problem</span></td> </tr> <tr> <td id="L50" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="50"></td> <td id="LC50" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># with `packages` is that it makes operations like `nix flake show</span></td> </tr> <tr> <td id="L51" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="51"></td> <td id="LC51" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># nixpkgs` unusably slow due to the sheer number of packages the Nix CLI</span></td> </tr> <tr> <td id="L52" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="52"></td> <td id="LC52" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># needs to evaluate. But when the Nix CLI sees a `legacyPackages`</span></td> </tr> <tr> <td id="L53" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="53"></td> <td id="LC53" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># attribute it displays `omitted` instead of evaluating all packages,</span></td> </tr> <tr> <td id="L54" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="54"></td> <td id="LC54" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># which keeps `nix flake show` on Nixpkgs reasonably fast, though less</span></td> </tr> <tr> <td id="L55" class="blob-num js-line-number js-code-nav-line-number js-blob-rnum" data-line-number="55"></td> <td id="LC55" class="blob-code blob-code-inner js-file-line highlighted"> <span class="pl-c"># information rich.</span></td></tr></blockquote>
  </li>
  <li>
    <a href="https://polymerlabs.medium.com/zkmint-the-first-zk-friendly-tendermint-consensus-engine-116000b9d4f9">zkMint: The First ZK-friendly Tendermint Consensus Engine | by Polymer Labs | Feb, 2023 | Medium</a><br>
    2023-02-24<br>
    <blockquote>To bring IBC to Ethereum, <strong class="jl hz">we need to be able to prove Tendermint consensus in the EVM.</strong></blockquote>
  </li>
  <li>
    <a href="https://www.dexerto.com/csgo/csgo-skins-worth-millions-allegedly-stolen-with-help-from-steam-support-staff-2066939/">CSGO skins worth millions allegedly stolen with help from Steam Support staff - Dexerto</a><br>
    2023-02-24<br>
  </li>
  <li>
    <a href="https://discourse.nixos.org/t/snowflakeos-creating-a-gui-focused-nixos-based-distro/21856">SnowflakeOS - Creating a GUI focused NixOS-based distro - Announcements - NixOS Discourse</a><br>
    2023-02-24<br>
  </li>
  <li>
    <a href="https://flathub.org/apps/details/org.gnome.dspy">D-Spy—Linux Apps on Flathub</a><br>
    2023-02-21<br>
  </li>
  <li>
    <a href="https://flathub.org/apps/details/com.borgbase.Vorta">Vorta—Linux Apps on Flathub</a><br>
    2023-02-21<br>
  </li>
  <li>
    <a href="https://www.borgbackup.org/demo.html">Demo — BorgBackup</a><br>
    2023-02-21<br>
    <p class="bm-desc">`borg list` fills a gap in bup</p>
  </li>
  <li>
    <a href="https://t.co/Q2fAy2gAEN">Today I'm open-sourcing Tangle: a new library that automatic...</a><br>
    2023-02-18 tweet<br>
    <p class="bm-desc">Today I'm open-sourcing Tangle: a new library that automatically 'entangles' and syncs WebAssembly. Play with the demo: <a href="https://t.co/Q2fAy2gAEN">https://t.co/Q2fAy2gAEN</a> And check out the code: <a href="https://t.co/MnTd8KLAV7">https://t.co/MnTd8KLAV7</a> <a href="https://t.co/V5O8iqWlPC">https://t.co/V5O8iqWlPC</a></p>
  </li>
  <li>
    <a href="https://www.mintscan.io/cosmos/proposals/88">COSMOS Proposal#88</a><br>
    2023-02-17 governance collaboration cosmos<br>
    <p class="bm-desc">10% community tax</p>
  </li>
  <li>
    <a href="https://fosdem.org/2023/schedule/event/network_hole_punching_in_the_wild/">FOSDEM 2023 - Hole punching in the wild</a><br>
    2023-02-17<br>
  </li>
  <li>
    <a href="https://codesandbox.io/blog/how-we-clone-a-running-vm-in-2-seconds">How we clone a running VM in 2 seconds</a><br>
    2023-02-17<br>
  </li>
  <li>
    <a href="https://codesandbox.io/blog/announcing-sandpack-2">Announcing Sandpack 2.0 and a Node.js runtime for any browser</a><br>
    2023-02-17<br>
  </li>
  <li>
    <a href="https://pedegoelectricbikes.com/dealers/overland-park/rentals-tours/">Pedego Rentals &amp; Tours - Local Electric Bike Shop | Pedego Electric Bikes</a><br>
    2023-02-11 KC car-culture<br>
    <p class="bm-desc">daily rentals too</p>
  </li>
  <li>
    <a href="https://t.co/BNZuR5g7X9">Cross platform shell tools for Deno inspired by zx https:/...</a><br>
    2023-02-11 tweet<br>
    <p class="bm-desc">Cross platform shell tools for Deno inspired by zx <a href="https://t.co/BNZuR5g7X9">https://t.co/BNZuR5g7X9</a> <a href="https://t.co/fDmOKatwAw">https://t.co/fDmOKatwAw</a></p>
  </li>
  <li>
    <a href="https://www.newyorker.com/tech/annals-of-technology/chatgpt-is-a-blurry-jpeg-of-the-web">ChatGPT Is a Blurry JPEG of the Web | The New Yorker</a><br>
    2023-02-11 tweet<br>
    <p class="bm-desc">As much as Ted Chiang's fiction is fantastic, it's really his non-fiction that I could read forever. His two paragraphs here about using ChatGPT as a writing tool are the most thoughtful comments I've seen about its utility and the practice of writing. ht</p>
  </li>
  <li>
    <a href="https://t.co/3a4g3DNACD">But, it shouldn't matter, even under existing law --</a><br>
    2023-02-11 tweet<br>
    <p class="bm-desc">@jespow @ArthurB But, it shouldn't matter, even under existing law -- <a href="https://t.co/3a4g3DNACD">https://t.co/3a4g3DNACD</a></p>
  </li>
  <li>
    <a href="https://adactio.com/journal/19894">Adactio: Journal—Home stream</a><br>
    2023-02-11<br>
    <p class="bm-desc">ideas for weekly posse</p>
  </li>
  <li>
    <a href="https://gitlab.com/spritely/goblins/-/merge_requests/25/diffs">Draft: feat: Add raw UNIX socket netlayer (!25) · Merge requests · spritely / Goblins - Racket implementation · GitLab</a><br>
    2023-02-10<br>
  </li>
  <li>
    <a href="https://security.googleblog.com/2022/12/memory-safe-languages-in-android-13.html?m=1">Google Online Security Blog: Memory Safe Languages in Android 13</a><br>
    2023-02-10 tweet<br>
    <p class="bm-desc">Android 13 has ~1.5 million lines of Rust code, and zero memory safety vulnerabilities discovered in Android’s Rust code have been found so far. This compares to 1 vuln per &lt;1,000 lines code that Android has had historically. <a href="https://t.co/Y54X2qS5iu">https://t.co/Y54X2qS5iu</a></p>
  </li>
  <li>
    <a href="https://webinstall.dev/caddy/">Caddy | webinstall.dev</a><br>
    2023-02-05<br>
  </li>
  <li>
    <a href="https://til.simonwillison.net/webassembly/python-in-a-wasm-sandbox">Run Python code in a WebAssembly sandbox | Simon Willison’s TILs</a><br>
    2023-02-04 tweet<br>
    <p class="bm-desc">Thanks to @pims I finally have a working recipe for running untrusted Python code inside a WebAssembly sandbox inside a parent Python script! I've been wanting this for ages. This solution uses wasmtime-py and VMware research's Python WASM build https:/</p>
  </li>
  <li>
    <a href="https://webkit.org/blog/13706/interop-2023/">Pushing Interop Forward in 2023 | WebKit</a><br>
    2023-02-04 tweet<br>
    <p class="bm-desc">Interop 2022 did a lot to advance consistent, standards-compliant behavior among browsers. Check out this post for Safari/WebKit results on Interop 2022 (we went from last place to a near-perfect) and looks forward to the even more ambitious Interop 2023.</p>
  </li>
  <li>
    <a href="https://t.co/Fk0x1zw5pU">untitled</a><br>
    2023-02-03 tweet<br>
  </li>
  <li>
    <a href="https://cloud.google.com/compute/confidential-vm/docs/about-cvm">Confidential Computing concepts | Confidential VM | Google Cloud</a><br>
    2023-02-03<br>
  </li>
  <li>
    <a href="https://t.co/GmWzVTXYAL">IBC is finally coming to the OG tendermint fork peppermint a...</a><br>
    2023-02-02 tweet<br>
    <p class="bm-desc">IBC is finally coming to the OG tendermint fork peppermint and the Polygon ecosystem. Saga team pulls off the impossible. <a href="https://t.co/h0wH2gej0d">https://t.co/h0wH2gej0d</a></p>
  </li>
  <li>
    <a href="https://genodians.org/nfeske/2023-02-01-mobile-sculpt">First system image of mobile Sculpt OS</a><br>
    2023-02-02 genodians genode sculptos tweet<br>
    <p class="bm-desc">We are proud to present the first ready-to-use image of mobile Sculpt OS #genodians #genode #sculptos <a href="https://t.co/INqCkUnLmY">https://t.co/INqCkUnLmY</a></p>
  </li>
  <li>
    <a href="https://www.morello-project.org/resources/cheriseed-port-effortlessly-to-cheri/">CHERIseed – port effortlessly to CHERI - Morello Project</a><br>
    2023-02-02<br>
  </li>
</ul>
