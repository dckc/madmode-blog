---
title: "KC Strip Staking on the Agoric Testnet"
published: false
date: 2020-05-01
tags: ["javascript", "economics", "devops", "ansible", "smart-contracts", "capabilities", "agoric"]
---

> [KC Strip Staking](https://explorer.testnet.agoric.com/validator/2784E6C7B40CF883BC409DBD856C403F2AE15BCE) is open for (testnet) business!

said I, 14 Mar in [agoric](https://keybase.io/team/agoric)#validators
after **michaelfig** helped me make my way thru the [Agoric Validator
Guide](https://github.com/Agoric/agoric-sdk/wiki/Validator-Guide).

Agoric updates their testnet every couple weeks. I caught up again on
Apr 5. But now I'm out of date again as of 2:36PM yesterday:

> Beginning the testnet upgrade now.
> [testnet](https://explorer.testnet.agoric.com/)-2.2.0 is live!

How did this thing work again?


## Colo node access

I can `ssh kc-strip` thanks to some details I squirrelled away in
`~/.ssh/config`:

```
Host kc-strip
     Hostname kc-strip.madmode.com
     IdentityFile /keybase/private/...
     User ...
```

## Devops with docker, ansible, and dotenv

Use dotenv to make a python3 environment...

`.envrc`:

```
layout python3
```

Install ansible...

```bash
$ pip install ansible
Successfully installed MarkupSafe-1.1.1 PyYAML-5.3.1 ansible-2.9.7 cffi-1.14.0 cryptography-2.9.2 jinja2-2.11.2 pycparser-2.20 six-1.14.0
```

When I run my play, I see the container is already up:

@@... `inventory.yml` in `priv/`

```bash
kc-strip$ ansible-playbook --ask-vault-pass -i priv/inventory.yml plays/ag-node.yml >,x
```


```json
"ag_container": {
        "ansible_facts": {
            "docker_container": {
...
                "StartedAt": "2020-04-05T03:53:57.97736014Z",
```


## Update `agoric/agoric-sdk` image

`docker kill ag-cosmos`

```
docker pull agoric/agoric-sdk`

Digest: sha256:3fd048c0cdafc4bc4cf472420c45926bb1ded2a6869bb093d42f8c74b478a199
Status: Downloaded newer image for agoric/agoric-sdk:latest
docker.io/agoric/agoric-sdk:latest
```
https://hub.docker.com/r/agoric/agoric-sdk


Is `0.15.0` current? I don't see a commit hash:

```
customer@s159403:~$ sudo docker run --rm -ti agoric/agoric-sdk:latest version --long
name: '@agoric/cosmic-swingset'
server_name: ag-chain-cosmos
client_name: ag-cosmos-helper
version: 0.15.0
commit: ""
build_tags: ""
go: go version go1.13.10 linux/amd64
```
