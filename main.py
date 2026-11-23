#!/usr/bin/env python3
"""news-image-20261122 v3: one image summing up Sunday 22 November 2026.

The front page (front.html) is rendered to entry.png with headless
Chromium at build time; this program only copies that finished image
into the output directory. Standard library only, no network, no clock,
no randomness: two runs write byte-identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out, "entry.png"))


if __name__ == "__main__":
    main()

