# Sum up 25 November's world news in one image

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Galabaderihu/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Galabaderihu/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Entry for the make.fun bounty **“Sum up 25 November's world news in one image”**
(`news-image-20261125`, $100 in USDC, 50 paid places, ends 27 Nov 2026 00:00 UTC).

## What the image shows

A one-page newspaper front page for Wednesday 25 November 2026 — 24 stories
across 8 regions:

- **Lead — Strait of Hormuz** — Two oil tankers struck naval mines and
  caught fire in the strait, in a hand-drawn dusk scene with the burning
  vessels, smoke and mines.
- **Middle East** — Houthis hit Saudi Arabia's Ras Tanura refinery; a
  Houthi strike on Riyadh's PIF Tower injures 11; an Israeli strike kills
  Hamas security chief Mohammad Abuelouf, his wife and two children.
- **Europe** — Ukrainian drones set two Rosneft refineries ablaze in
  Samara; a Russian strike on Odesa kills two; leaked figures put Russian
  war dead at 490,334; Poland presses for a permanent US military
  presence; Denmark bans headscarves for prosecutors; a report finds
  London's Met Police still institutionally racist.
- **Asia-Pacific** — Australia and Solomon Islands sign a treaty barring
  foreign military bases; a US soldier admits selling military secrets
  to Chinese buyers; Asian stocks slide (Samsung −9.9%, SK Hynix −11.1%).
- **Americas** — Huawei convicted in a US court of bank fraud and
  trade-secret theft; an unclassified CIA system is breached; Trump
  awards Rudy Giuliani the top US civilian honour; Colombia police free
  hostages in a Cartagena supermarket raid.
- **Tech, business, climate** — Nvidia's Huang says he is in therapy as
  the AI rally fades; Dell posts a record quarter (sales $54.9bn, +103%);
  COP31 talks end with no deal; RSF drone strikes kill 19 in Sudan.
- **Markets strip** — KOSPI −6.16%, Nikkei −2.78%, Dow 50,019, its first
  close above 50,000, and Nvidia −5%.
- **Space** — Shenzhou-24 docks with Tiangong, carrying Pakistan's first
  astronaut.

News checked on 25 Nov 2026 against that day's reporting, including
Just Security's Early Edition for 25 November 2026 and South China
Morning Post world headlines for 25 Nov 2026.

## How it runs

```sh
python3 main.py
```

Writes `/output/entry.png` (1024×1024 PNG, under 1 MiB). The program uses
only the Python standard library, no network, and copies `asset.png`
byte-for-byte, so two runs always produce identical bytes. Before writing
anything, the program checks that the stored page begins with a real PNG
signature, and it publishes through a temporary neighbouring file that is
renamed into place, so a reader never sees a half-written page. The front
page itself was typeset with Pillow while this entry was being produced;
the finished page is what ships here, and no drawing step is needed when
the entry runs.

## Licence

MIT — see `LICENSE`.
