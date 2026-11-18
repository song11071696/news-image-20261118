#!/usr/bin/env python3
"""news-image-20261118: write the bundled world-news image to /output/entry.png.

The image sums up Wednesday 18 November 2026 in one 1024x1024 picture:
Quad summit in Manila, Ukraine's second strike on the Crimea bridge,
Iran's drone strike on the US radar in Bahrain, Nvidia's earnings without
Jensen Huang, the Siberian plane crash, and the US losing measles-free
status. Text was composited with PIL at build time; the background is an
AI-generated world map with no text.

Deterministic by construction: this program only copies the bundled
entry.png (same bytes every run). No network, no randomness, no clock.
Standard library only.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.environ.get("NEWS_IMAGE_OUTPUT", "/output/entry.png")


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(DST, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("output is not a valid PNG: %s" % DST)
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
