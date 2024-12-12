title: awesome-ocap stargazers grow steadily since 2017
date: 2024-12-12
published: true
tags: [capabilities, advocacy, data-visualization, generative-ai]

The number of stars on my [awesome-ocap](https://github.com/dckc/awesome-ocap) repo has grown steadily since
[My Capability Security 2017 Wish-List](../2017/ocap-wish-list).

![stargazers_chart.svg](https://gist.githubusercontent.com/dckc/53d44b5b11b9c462c9f3d0e33db2994f/raw/0d7ec8befbc841f56934c14d194fcac65c84182d/stargazers_chart.svg)

My github feed shows new stars now and then, which made me
curious about how folks are discovering it. I expected
the growth would be episodic -- prompted by events now and then.

The nearly straight line over 7 years is quite a surprise!

_TODO: check the linear hypothesis with pandas. Get slope, coefficient._

## The web knows how to make this chart

I just wished into a popular LLM:

> for my dckc/awesome-ocap github repo, how do I get a chart of when the stargazers arrived? I want to make a chart

and it got [script.py](https://gist.github.com/dckc/53d44b5b11b9c462c9f3d0e33db2994f#file-script-py) right on the 1st try, IIRC.

## PyData tool setup: uv beat nix

The LLM's first draft for fetching was some shell code that had a silent endless loop, which put me in rate-limiting penalty box at github.
I tried using nix to set up a python env for pandas and such, but the rate limiting put the kibosh on that.
So I used uv to manage the dependencies.

I used direnv to manage `$GITHUB_TOKEN`.

- [Makefile](https://gist.github.com/dckc/53d44b5b11b9c462c9f3d0e33db2994f#file-makefile)
- [fetch_stargazers.py](https://gist.github.com/dckc/53d44b5b11b9c462c9f3d0e33db2994f#file-fetch_stargazers-py)

p.s. commit history for the [gist](https://gist.github.com/dckc/53d44b5b11b9c462c9f3d0e33db2994f):

```
2024-12-12 00:29 496c37f
2024-12-12 00:27 0d7ec8b
2024-12-09 09:41 035f04b
```
