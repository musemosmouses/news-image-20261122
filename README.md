# The World in One Day — Sunday 22 November 2026 (v4)

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/musemosmouses/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/musemosmouses/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122)

A make.fun bounty entry: one image summing up the world's news of
Sunday 22 November 2026 — 36 stories, every one of them checked
against the wires for that date.

A full rebuild after v3: v3 looked like a near-copy of the winning
entry's layout and ranked below #200, so v4 changes the geometry
completely. The page is now a UTC timeline spine — three hero bands
for the day's defining stories, then the rest of the day hour by hour
along a centre axis — with the numbers as a vertical rail and a
region-coloured map, instead of a numbers strip and a corner map.
The one-line date check replaces v3's cramped exclusion box, and no
timestamp on the page falls outside Sunday 22 November 2026.

## What is on the page

- **3 heroes:** 186 Russian drones at Ukraine overnight, 161 downed,
  Dymer block destroyed; COP31's final text names no fossil fuels,
  drops the $120bn adaptation target, keeps the 35% electricity goal
  for 2035 — and the deal collapses; Iran claims two US Patriot radars
  hit in Bahrain, Bahrain denies it.
- **The day in UTC:** 12 picture cards in chronological pairs along
  the spine — Wembanyama 50 (00:40), Verstappen (05:30), India 720/9
  (06:30), the Serang candy-factory fire (07:00), Iran power rationing
  (08:00), Belgium's grounded Monday flights (10:53), Pope Leo XIV's
  lunch (12:30), Hong Kong 98.79% (17:00), Leeds 4–1 Chelsea (17:00),
  Alcaraz wins the ATP Finals (17:00), Gaza (21:30), the
  Netanyahu–Eisenkot talks (21:48) — each with a drawn scene, a source
  and a certainty badge.
- **By the numbers (rail):** 186 / 161 / 25 / 720-9 / 98.79% / 50.
- **Also on Sunday:** 21 more stories, including the Sparta II still
  burning, Bolsonaro in intensive care, the FBI crime-database probe
  and BepiColombo entering Mercury orbit.
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

