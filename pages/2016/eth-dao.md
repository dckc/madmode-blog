# Etherium and DAO tokens: an experience report

**Tada! I own 227.27 [DAO][] tokens.** Why? As a student of capability security and
computer-supported collaboration in general, I'm naturally interested in
smart contracts. When an autonomous smart-contract platform raises [$100M+ in a week][Prisco],
I figure I should know how it works.

[DAO]: https://daohub.org/
[Prisco]: https://bitcoinmagazine.com/articles/the-dao-raises-more-than-million-in-world-s-largest-crowdfunding-to-date-1463422191

The buzzwords run thick and fast:
 - The DAO is **Code**.
 - The DAO is **Autonomous**.
 - The DAO is **Revolutionary**.
 - The DAO is **Rewarding**.

Which of these do I believe?
  - **Code**: Check. The evidence is clear and compelling. The bytes are `0x60606040523615...` and a [straightforward verification process][verifying] establishes that the [source code](https://github.com/slockit/DAO) compiles to this output.
  - **Autonomous**: It autonomously does _something_ (inasmuch as miners keep the Etherium distributed VM going). An [audit][dv] has vouched that the contract is "secure" and, I gather, faithful to the [DAO whitepaper][wp]. I haven't digested the argument that what it does is fair and not controlled by any one or few actors. I'm still digesting basics such as [patricia trees](https://github.com/ethereum/wiki/wiki/Patricia-Tree), actually.
  - **Revolutionary**: Perhaps $100M in a week constitutes a revolution. But whether there will be any lasting
  effect is unclear to me. The argument from [BitShares experience](https://www.reddit.com/r/ethereum/comments/4jnem4/is_the_dao_going_to_be_doa_by_dan_larimer_of/) that voter apathy and mis-aligned incentives will result in failure is more substantive than any argument I found in favor of the DAO.
  - **Rewarding**: Finding _any_ substance behind this claim was quite a challenge. I looked for a simple 3-point argument that there's some ROI in here... Is that too much to ask? Apparently so. The whitepaper didn't
  elucidate much for me; it started with a bit of history of smart contracts (citing Szabo 1997 and Miller 1997 was
  good to see) and then immediately dove into details of the values of various constants in the contract algorithm.
  Buried several layers into the web site, I found that proposal 1 includes for a sort of [generalized, automated airbnb][p1]. Ok, that's at least somewhat plausible. Follow-the-money seems to lead to slock.it. I'm sure it's rewarding for _them_.

[dv]: https://blog.slock.it/deja-vu-dao-smart-contracts-audit-results-d26bc088e32e#.6wtj3lwqg
[p1]: https://forum.daohub.org/t/slock-it-proposal-1-discussion-thread/539

I get anxious reading the code: too many of the security properties seem to rely on programmer dilligence:
  
```
    function transfer(address _to, uint256 _amount) noEther returns (bool success) {
        if (balances[msg.sender] >= _amount && _amount > 0) {
            balances[msg.sender] -= _amount;
            balances[_to] += _amount;
            Transfer(msg.sender, _to, _amount);
            return true;
        }
```

Compare the above from [Token.sol][] to the elegant simplicity of [simple money in E][fc2000]:
```
                to deposit(amount :int, src) :void {
                    unsealer.unseal(src.getDecr())(amount)
                    balance += amount
                }
```

[Token.sol]: https://github.com/slockit/DAO/blob/master/Token.sol
[fc2000]: http://erights.org/elib/capability/ode/ode-capabilities.html

[verifying]: https://github.com/slockit/DAO/wiki/The-DAO-v1.0-Code#verifying-the-dao-code. 
[wp]: https://download.slock.it/public/DAO/WhitePaper.pdf


OK... so how do I do it?
> To obtain DAO tokens, ... send ETH from your Ethereum Wallet ... to The DAO’s address below.
> `0xbb9bc244d798123fde783fcc1c72d3bb8c189413`

... and there's a wizard... it recommends paying eith ETH. But I don't have any. So I choose USD,
at which point they refer me to bity.
  - The register button wouldn't light up when I used a password manager to enter a password
    - I eventually found a work-around: manually type a character and then delete it.
  - After filling in all the info to order some ETH, they gave me international bank transfer instructions.
    I have no idea how to execute such a transfer, but I'm quite sure it's not something I can do now, when
    my bank is closed.

So I back-track and try the recommended wallet. Mist is an node+webkit style app. When I start it up, it says it has to sync with the blockchain and stays like that for longer than my attention span. _How about some advanced notice that this is going to take hours and GB of disk space?_ I guess one should not expect good road signs in the wild west.

Back-track again... Searching turned up a [How do I buy Ethereum with USD? answer](http://ethereum.stackexchange.com/a/1916) Mar 8 at 5:38 by niksmac:
   1. Buy BTC with a debit card at coinbase.
      - The experience is much more what I expected. I did the SMS callback verification dance and exchanged $30 for BTC using a debit card within 10 or 15 minutes. I switched the 2FA on my account from SMS to TOTP (google authenticator) in the process.
   2. Exchange BTC for ETH using shapeshift.
      - This presumes I have an ETH address. [EtheriumWallet by Krypokit](https://ethereumwallet.com/index.html) lets you make one right in your browser in a minute or so. While I'm sure a full blockchain sync is more secure, I'm only risking a few dollars here and "more" is probably a difference between getting struck by lighting once and getting struck twice. Do I really care?
      - shapeshift result: [receipt for 2.55384881 Ether](https://etherscan.io/tx/0x77fef130c7b576e188018602206141723bd11ff47cb8baadaab370fc29892618)
   3. Send ETH to the DAO contract address.
      - I got plenty of confirmations on [transaction 0x1be4715b...](https://etherscan.io/tx/0x1be4715b9fc0e3b6c6793f6d27ba1ca00d4a47d9b4ab1fe51fa456a33adde355), so I thought I was all set. But the last step of the DAO wizard was to confirm on [the creation page](https://daohub.org/creation.html), but I kept getting 0 tokens for my address there.
      -  Eventually I learned the [out of gas](https://forum.daohub.org/t/out-of-gas-could-not-get-doa/2148) warning really matters. That Krypokit wallet worked fine for sending ETH around, but it didn't add any gas, so non-trivial contracts didn't work.
      -  I back-tracked to [MyEtherWallet](https://www.myetherwallet.com/#the-dao), which added sufficient gas to run the contract. Bingo! I did a smaller transaction to be sure I had enough for gas and then another for the rest:
         - [1 ETH](https://etherscan.io/tx/0x06bee04bc3f3286557e0aa9e12313a169184f074a41b3c650b0fa13c69daa9f6)
         - [1.5 ETH](https://etherscan.io/tx/0x7340c3f8b91cb64c811b9079b0c716d86fd7568cd23f390b0333d467d337c858)

I eventually did a full blockchain sync. I kept starting over thinking I was doing something wrong. But no, it really iterates through all 1.5M blocks on the blockchain _twice_, which takes a few hours and uses about 2GB using `geth --fast`.


