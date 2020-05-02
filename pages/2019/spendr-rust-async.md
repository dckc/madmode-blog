---
title: "spendr: toward an rchain gRPC client in rust using tokio and async / await"
tags: [rust, grpc, tokio, async, rchain, programming]
date: 2019-09-10
published: true
---


Inspired by mention of a gRPC client and server library in [Tokio alpha release with async &
await](https://tokio.rs/blog/2019-08-alphas/), I tried building an rchain wallet client
in rust.

A couple hours later, I had the hello-world client from [tower-grpc][]
adapted to talk to the shiny new [0.9.12 release of rnode][0.9.12]:

```
~/projects/spendr$ cargo run
   Compiling spendr v0.1.0 (/home/connolly/projects/spendr)
    Finished dev [unoptimized + debuginfo] target(s) in 3.00s
     Running `target/debug/spendr`
RESPONSE = Response { metadata: MetadataMap { headers: {"content-type": "application/grpc", "grpc-encoding": "identity", "grpc-accept-encoding": "gzip"} }, message: Streaming }
```

But that client code doesn't use the yummy new async / await stuff.
It doesn't look like async / await has made it up to the gRPC level yet.
I think I mis-read the blog post; I think it was just saying that
tokio has a gRPC client and server library.

[tower-grpc]: https://github.com/tower-rs/tower-grpc/issues/198
[0.9.12]: https://github.com/rchain/rchain/releases/tag/v0.9.12
