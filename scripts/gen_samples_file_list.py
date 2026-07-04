#!/usr/bin/env python3
"""Generate samples/file-list.json — a flat manifest of every file under samples/.

Static hosts (e.g. GitHub Pages) can't list a directory over HTTP, so a
browser-only client (dgml-app-sample.html served with no backend) can't
discover what's in samples/<scenario>/dgml-workspace/ on its own. This
script is the one piece of "pre-cooking" that static deployment needs: a
plain list of real, unmodified file paths. Everything else (docset.json,
file.json, *.dgml.xml, page_images/*.png) is fetched as-is once the client
knows those paths exist — no content is duplicated or transformed.

Re-run this after adding or regenerating any sample workspace under
samples/, and commit the resulting samples/file-list.json alongside it.

Usage:
    python3 scripts/gen_samples_file_list.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def gen_file_list(samples_dir: Path) -> list[str]:
    output = samples_dir / "file-list.json"
    return sorted(p.as_posix() for p in samples_dir.rglob("*") if p.is_file() and p != output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--samples-dir",
        type=Path,
        default=Path("samples"),
        help="Directory to list (default: ./samples, run from the repo root).",
    )
    args = parser.parse_args()

    samples_dir: Path = args.samples_dir
    if not samples_dir.is_dir():
        raise SystemExit(f"no such directory: {samples_dir}")

    files = gen_file_list(samples_dir)
    output = samples_dir / "file-list.json"
    output.write_text(json.dumps(files, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(files)} path(s) to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
