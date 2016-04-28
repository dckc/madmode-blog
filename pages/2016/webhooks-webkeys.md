# On webhooks and webkeys


So... [webhooks][]; how do they compare to [webkeys]?

e.g. [github commit status API](https://github.com/blog/1227-commit-status-api)

    X-Hub-Signature  HMAC hex digest of the payload, using the hook's secret as the key (if configured).

this looks familiar:

    X-GitHub-Delivery  Unique ID for this delivery.

but designation is separate from authority. hook URLs are discoverable/forgeable:

    GET /repos/:owner/:repo/hooks/:id

[webhooks]: https://developer.github.com/webhooks/
[webkeys]: @@IOU-url

