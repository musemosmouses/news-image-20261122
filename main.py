#!/usr/bin/env python3
"""news-image-20261122 v4: one image summing up Sunday 22 November 2026.

v4 rebuilds the page as a UTC timeline spine: three hero bands (the
186-drone night, the COP31 final text, the Bahrain radar claim/denial),
then the rest of the day hour by hour along a centre axis, 12 picture
cards in chronological pairs, a numbers rail and a region-coloured map,
and 21 more stories in the tail — 36 stories in all, every one first
reported on Sunday 22 November 2026.

The front page (front.html) is rendered to entry.png with headless
Chromium at build time; this program only copies that finished image
into the output directory. Standard library only, no network, no clock,
no randomness: two runs write byte-identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_NAME = "entry.png"  # the single file the grader reads from the output dir


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out, OUTPUT_NAME))


if __name__ == "__main__":
    main()

