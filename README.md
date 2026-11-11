# Keybro dictionaries

Dictionaries that Keybro Online offers under Settings > Typing > Dictionaries. They are published as
files of a release of this repository; the app holds a catalog with the size and SHA-256 of every
file and keeps a download only when both match.

The files can also be downloaded by hand and imported in either edition of Keybro
(Settings > Typing > Dictionaries > Import dictionary).

## Files

`catalog.json` lists every dictionary with its language, word count, size, checksum, licence and
attribution. The `.dict` files are AOSP binary dictionaries (the format of the AOSP keyboard and
HeliBoard).

## Sources and licence

The dictionaries are built from the word lists of the Android Open Source Project (LatinIME) with
the AOSP `dicttool`, by `tools/dictionaries/build.py` of the Keybro repository; the sources are
pinned by commit and SHA-256 there. They are licensed under the Apache License 2.0, see `NOTICE.txt`.

Only AOSP word lists are published here. Dictionaries of other projects are not mirrored.

## Publishing

The files of the current release are committed in `release/`. The workflow `Release` (run by hand
with the tag, or by pushing the tag) checks that the tag equals `release` in `release/catalog.json`
and that every file has the catalogued size and SHA-256, and then creates the release with the
`.dict` files and `catalog.json` attached.

A published release is never changed: a new or corrected dictionary gets a new release tag and a new
catalog in a new version of the app.
