#!/usr/bin/env python3
"""Compatibility entry point for the self-contained tour map.

Edit the stops array in tools/map_fragment.html to update the bill, then run
python3 tools/build_pages.py. The map now renders in the browser and needs no
Python generation step. Keep this entry point for existing rebuild commands.
"""
from pathlib import Path

if __name__ == "__main__":
    fragment = Path(__file__).with_name("map_fragment.html")
    if not fragment.is_file():
        raise SystemExit("Missing tools/map_fragment.html")
    print("Tour map source: tools/map_fragment.html. Run tools/build_pages.py to rebuild pages.")
