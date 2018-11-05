The RChain ecosystem has been developing nicely the past few months. I've had fun writing smart contracts as well as tools that make writing smart contracts nicer. Simple contracts like Be the 10th caller to win! work fine, but anything where we cast votes, post statuses, or spend REV tokens needs signatures to connect off-chain actions with on-chain capabilities.
Since I have a little experience building WebExtensions, I wrote RSign. RSign is a extension to create signatures that Rholang contracts can verify. It works a little bit like MetaMask for Ethereum:

rsign-0.4.0.crx is an alpha release (Sep 21 2ddc1d5). Using Chrome or Chromium on linux, in developer mode, you should be able to just drop it on to chrome://extensions/, go to options to generate a key, then enter some data (using JSON) and sign it. The README has a few more screenshots and details.
How it Works
In Rholang, we use unforgeable names to represent object capabilities. These names exist only on the blockchain; we can’t turn off-chain data into an unforgeable name any more than we can turn an integer into an object reference in javascript. Public-key crypto to the rescue. The user can lock their unforgeable name into a "safe" contract that anyone can call. When called, the safe will give back the correct unforgeable name only if it is given a valid cryptographic signature.
When you hit Generate, it feeds a random seed to tweetnacl and stores an ed25519 key pair in your browser's local storage, with the private key encrypted with a password you supplied.
When you hit Sign, we convert the JSON data into a subset of Rholang called RHOCore. We mimic the Rholang .toByteArray() functionality that serializes any Rholang process using protobuf. Finally, we use the tweetnacl key to sign the serialized data and we show the results.
Unlocking Superpowers
For example, this contract "wraps" a superpower capability in a sort of wallet so that only Jim (the holder of the 3f3709d... key) can exercise it:

Jim signed his desired height, 12345, and sent it to the contract:

And presto, we got @{["flying", 12345]}.
