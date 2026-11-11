#!/usr/bin/env python3
"""Checks release/ against release/catalog.json: tag, file set, sizes and SHA-256."""
import hashlib
import json
import pathlib
import sys

RELEASE = pathlib.Path(__file__).resolve().parent.parent / "release"


def problems(tag):
    catalog = json.loads((RELEASE / "catalog.json").read_text(encoding="utf-8"))
    found = []
    if catalog["release"] != tag:
        found.append(f"tag {tag!r} is not the catalog release {catalog['release']!r}")
    listed = set()
    for entry in catalog["dictionaries"]:
        name = entry["url"].rsplit("/", 1)[1]
        listed.add(name)
        if not entry["url"].endswith(f"/releases/download/{catalog['release']}/{name}"):
            found.append(f"{name}: address does not point at release {catalog['release']}")
        path = RELEASE / name
        if not path.is_file():
            found.append(f"{name}: missing")
            continue
        data = path.read_bytes()
        if len(data) != entry["bytes"]:
            found.append(f"{name}: {len(data)} bytes, catalog says {entry['bytes']}")
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            found.append(f"{name}: SHA-256 differs from the catalog")
    for path in RELEASE.glob("*.dict"):
        if path.name not in listed:
            found.append(f"{path.name}: not in the catalog")
    return found


if __name__ == "__main__":
    result = problems(sys.argv[1])
    for line in result:
        print("ERROR:", line)
    if result:
        sys.exit(1)
    print("release/ matches catalog.json")
