# The World in One Day — Sunday 22 November 2026 (v3)

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/musemosmouses/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/musemosmouses/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

A make.fun bounty entry: one image summing up the world's news of
Sunday 22 November 2026 — 33 stories, every one of them checked
against the wires for that date.

A full rebuild after v2: v2's pixel font is gone, its two wrong-date
leads are gone (the Peru quake was 20 Nov, the 'El Chapo Isidro'
capture 20–21 Nov), and the day's two biggest stories — Russia's
186-drone night over Ukraine and the COP31 final text — now lead the
page, with Iran's Bahrain radar claim as the third lead.

## What is on the page

- **3 leads:** 186 Russian drones at Ukraine overnight, 161 downed,
  Dymer block destroyed; COP31's final text names no fossil fuels,
  drops the $120bn adaptation target, keeps the 35% electricity goal
  for 2035 — and the deal collapses; Iran claims two US Patriot radars
  hit in Bahrain, Bahrain denies it.
- **The day in numbers:** 186 / 161 / 25 / 35% / $120bn / 720-9.
- **A UTC day-arc ribbon** following the drone wave hour by hour.
- **12 picture cards** with drawn scenes, a source and a certainty
  badge each: Hong Kong, India 720/9, Verstappen, Wembanyama 50,
  Iran power rationing, the Nigeria boat, the Serang candy-factory
  fire, Gaza, Leeds 4–1 Chelsea, Pope Leo XIV's lunch, the
  Netanyahu–Eisenkot talks, Belgium's grounded Monday flights.
- **A dotted world map with numbered pins**, a region bar (7 regions),
  18 more stories in "Also on Sunday", and a red **date check** naming
  the stories left out because they happened on other days.
- **Verification depth:** every card names its sources (Reuters + AP +
  BBC, and the like) and its time; COP31 carries a "What changed"
  draft-to-final box; each lead has a locator inset with coordinates.

## How it is built

`front.html` (single file, HTML + CSS, system serif fonts) is the
front page. It is rendered to `entry.png` (1024×1024) with headless
Chromium at build time. `main.py` (Python 3.13, standard library
only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`:
deterministic — two runs write byte-identical output, no network,
no clock, no randomness.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

