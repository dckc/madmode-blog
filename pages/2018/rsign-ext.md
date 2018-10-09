---
title: RSign - Extending Browsers to Sign Data on RChain
tags: [capabilities, smart-contracts, rchain, javascript, webextensions]
date: 2018-10-08
published: false
---


The RChain ecosystem has been developing nicely the past few months. I've had fun writing smart contracts, as well as tools that make writing smart contracts nicer. With "hello world" and [other simple contracts][nth] in the rear-view mirror, we've reached the point where data need to be signed by users. Why do data need to be signed? Because without signatures anyone on the internet could cast votes, post statuses, or spend REV tokens on my behalf.

In the world of rholang, we facilitate object capabilities by using unforgeable names. These names exist only on the blockchain, and cannot be saved to disk or locked in a safe in the real world. Public-key crypto to the rescue. The user can lock their unforgeable name into "safe" a contract that anyone can call. When called the safe will give back the correct unforgeable name only if it is given a valid cryptographic signature

Since I have a little experience [building WebExtensions][ext], I put one together to make signatures that Rholang contracts can verify. If you've heard of metamask in the ethereum ecosystem, RSign may look familiar.

![RSign screenshot](https://github.com/dckc/RSign/raw/master/docs/screenshots/enterjson.png)

[ext]: https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions
[nth]: https://github.com/JoshOrndorff/nth-caller-game

[rsign-0.4.0.crx](https://github.com/dckc/RSign/releases/download/0.4.0-alpha/rsign-0.4.0.crx)
is an alpha release (Sep 21 2ddc1d5). Using Chrome or Chromium on linux, in developer mode,
you should be able to just drop it on to `chrome://extensions/`, got to options to generate a key,
then enter some data (using JSON) and sign it.
The [README](https://github.com/dckc/RSign#readme) has a few more screenshots and details.

Behind the scenes, when you hit **Generate**, we feed a random seed to
[tweetnacl](https://tweetnacl.js.org/) and store an ed25519 key pair in
your browser's local storage, with the private key encrypted under
a password you supply.

When you hit **Sign**, we convert the JSON data into a subset of Rholang
called RHOCore. Then we mimic the Rholang `.toByteArray()` functionality
that serializes any Rholang process using protobuf. Finally, we use
the tweetnacl key to sign the serialized data and we show the results.

For example, this contract "wraps" a `superpower` capability in a sort
of wallet so that only Jim (the holder of the `3f3709d...` key) can exercise it:

```scala
new superpower, stdout(`rho:io:stdout`) in {
  contract @"flyJim"(@height, @sig, done) = {
    new verifyOut in {
      @"ed25519Verify"!(height.toByteArray(), sig,
        "3f3709d027c6db135cd415d6b1f2e1709d8d1295cfcbd16cc228b513b7045aa3".hexToBytes(),
        *verifyOut) |
      for (@ok <- verifyOut) {
        if(ok) { superpower!(height, *done) }
        else { stdout!("bad sig!!!") }
      }
    }
  }
  |
  contract superpower(@height, out) = {
    out!(["flying", height])
  }
}
```

Jim signed his desired height, `12345`, and sent it to the contract:

```scala
new stdout(`rho:io:stdout`) in {
@"flyJim"!(12345,"e7595db3425b4ea24d97877077972ee17bc8c0e14ed2c32d0805d2e5b7148fb7db79150659d8aa064f3c2957ea1c24aa6204ebe08fdeafe7218a3d073f0bbc08".hexToBytes(),*stdout)
}
```

And presto, we got `@{["flying", 12345]}`.
