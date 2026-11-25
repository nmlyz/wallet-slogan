# wallet-slogan

[![make.fun · u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![rank](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/nmlyz/wallet-slogan/rank.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![reward](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/nmlyz/wallet-slogan/reward.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)

wallet-slogan writes one line to a text file: the tagline of a Solana wallet agent. The line was picked from 36 candidates by pairwise judging against the brief — a wallet that does the reading so its owner can get on with life, told as a two-sided contrast on the single word "read". The wallet reads the chain; the owner reads the room.

## The line

> The wallet that reads Solana so you can read the room.

It is 54 characters and 11 words, a single line. It names the wallet and Solana plainly, uses only everyday words a newcomer understands, and promises nothing more than the wallet doing the reading — checking the chain, following the transactions — while the owner stays with the people in front of them.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The program builds the line from two clauses — what the wallet reads, then what the owner reads instead — and checks the result against the entry gate (length, word count, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

## Why this line

Thirty-six slogans were written first, each from a different angle — a doorman, a night shift, a concierge, a pair of hands, a pocket turned partner — and the stock crypto lines were thrown out before judging began: no keys, no moons, no bags, no "be your own bank". The survivors were compared two at a time by three readers (a copy chief, a newcomer, someone judging by ear) until one line won every round: the one whose two halves mirror each other on a single verb.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)</sub>
