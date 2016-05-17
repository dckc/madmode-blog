# On investing in Etherium and DAO tokens


I'm the proud owner of ~250 DAO tokens, I think. I can't confirm on [the creation page](https://daohub.org/creation.html) but I have a receipt:
[0x1be4715b9fc0e3b6c6793f6d27ba1ca00d4a47d9b4ab1fe51fa456a33adde355](https://etherscan.io/tx/0x1be4715b9fc0e3b6c6793f6d27ba1ca00d4a47d9b4ab1fe51fa456a33adde355)

read some stuff on https://daohub.org/; several links and several pages in, I find a proposal for a generalized airbnb.
follow-the-money seems to lead to slock.it

The DAO is rewarding - er... any argument to back that claim? a simple 3-point argument that there's some ROI in here... is that too much to ask?
The DAO is code -- OK, that's something I understand. Though the code is kinda scary. All imperative.
https://solidity.readthedocs.io/en/latest/control-structures.html
The VM is nearly ocap-happy; *what was the one exception I found?*

The DAO Raises More Than $117 Million in World's Largest Crowdfunding to Date
May 16, 2016 06:09 PM by Giulio Prisco
https://bitcoinmagazine.com/articles/the-dao-raises-more-than-million-in-world-s-largest-crowdfunding-to-date-1463422191

darn... did I just miss a 10x price hike? no... more like 10%
https://blog.daohub.org/the-dao-creation-period-price-schedule-4a8bc7a76e04#.oj0kv9z2x

OK... so how do I do it?
> To obtain DAO tokens, ... send ETH from your Ethereum Wallet ... to The DAO’s address below.
> 0xbb9bc244d798123fde783fcc1c72d3bb8c189413

and there's a wizard... it recommends paying eith ETH, but I don't have any, so I choose USD,
so they refer me to bity
  - register button wouldn't light up when I used a password manager to enter a password
    - had to manually type a char and then delete it
  - when I ordered some ETH, they gave me international bank transfer instructions, not a credit card form.

mist takes forever to sync... and eats disk space in ~/.ethereum without really telling you what's going on


https://ethereumwallet.com/index.html
ETH address
...8f3c

paid 2.5 ETH to TheDao

Searching turned up [How do I buy Ethereum with USD? answer](http://ethereum.stackexchange.com/a/1916) Mar 8 at 5:38 by niksmac

coinbase
bought ~$30 of BTC using a credit card... nice...
SMS callback, 2FA with TOTP (google authenticator)

bought 2.55384881 Ether
https://etherscan.io/tx/0x77fef130c7b576e188018602206141723bd11ff47cb8baadaab370fc29892618


https://www.reddit.com/r/ethereum/comments/41tbmp/ethereum_mist_how_long_does_it_take_to_sync/

geth --fast


> As an additional safety feature, if a fast sync fails close to or after the random pivot point, fast sync is disabled as a safety precaution and the node reverts to full, block-processing based synchronization.

https://github.com/ethereum/go-ethereum/issues/2469
https://github.com/ethereum/go-ethereum/pull/1889

todo:

Verifying the DAO code
https://github.com/slockit/DAO/wiki/The-DAO-v1.0-Code#verifying-the-dao-code

Is The DAO going to be DOA? (by Dan Larimer of BitShares)
https://www.reddit.com/r/ethereum/comments/4jnem4/is_the_dao_going_to_be_doa_by_dan_larimer_of/

https://gitter.im/ethereum/go-ethereum

learn the math... merkel trees... patricia...
https://github.com/jamshidh/ethereum-client-haskell
https://github.com/ethereum/wiki/wiki/Patricia-Tree
https://en.wikipedia.org/wiki/Radix_tree
