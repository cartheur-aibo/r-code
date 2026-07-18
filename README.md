# AIBO R-CODE Redistributions and Reference Files

This repository is a curated archive of Sony AIBO R-CODE redistributions, Memory Stick images, sample scripts, and reference assets for several classic AIBO platforms.

Its purpose is to keep the redistributable R-CODE materials for `ERS-111`, `ERS-210`, and `ERS-7` in one place so they can be studied, preserved, and reused when working with original AIBO hardware and OPEN-R based development environments.

## What Is In This Repo

- `ERS-111/`
  Contains the `PMS-RCODE11x_E` package for `ERS-110/111`, including:
  - Memory Stick execution image contents under `MSImage/`
  - Sony documentation in `Document/`
  - Example `.R` scripts in `sample/`

- `ERS-210/`
  Contains two ERS-210 era redistributions:
  - `PMS101E/`
  - `redist210e/`
  These include OPEN-R application, middleware, and system files, plus PC-side R-CODE support files.

- `ERS-7/`
  Contains `Redist7_ver3/Redist7` for `ERS-7`, including:
  - English and Japanese redistribution trees
  - Sample `.R` scripts
  - Command reference documents
  - AIBO sound and tone MIDI assets

- `src/`
  Holds original archive files such as ZIP and TAR.GZ packages that appear to be the source redistributions used to populate the extracted folders.

## What This Repo Is For

This repo is mainly useful for:

- preserving historical AIBO R-CODE materials
- inspecting the file layouts used on AIBO programming Memory Sticks
- referencing Sony sample scripts and documentation
- rebuilding or comparing Memory Stick contents for supported AIBO models
- supporting hobbyist research around OPEN-R and R-CODE based workflows

This is not a modern software project with a build system, test suite, or application entry point. It is primarily a reference and archival repository of vendor-supplied assets.

## Model Coverage

- `ERS-111`
- `ERS-210`
- `ERS-7`

The contents are organized by robot family rather than by programming task, because the underlying files differ by model and redistribution version.

## Important Licensing Note

Much of this repository appears to come from Sony redistribution packages and bundled documentation.

- The top-level [LICENSE](/home/cartheur/ame/aiventure/aiventure-github/cartheur-aibo/r-code/LICENSE) is `GPL-3.0`, but some included Sony files also contain their own license or redistribution terms.
- For example, files such as [ERS-111/PMS-RCODE11x_E/Document/readme.txt](/home/cartheur/ame/aiventure/aiventure-github/cartheur-aibo/r-code/ERS-111/PMS-RCODE11x_E/Document/readme.txt:1) and [ERS-7/Redist7_ver3/Redist7/Redist_E.txt](/home/cartheur/ame/aiventure/aiventure-github/cartheur-aibo/r-code/ERS-7/Redist7_ver3/Redist7/Redist_E.txt:1) describe Sony-specific usage and redistribution conditions.
- Anyone reusing or republishing these materials should review the original package documents carefully and confirm what may legally be redistributed.

## Quick Orientation

If you are exploring the repo for the first time:

1. Start in the model folder you care about: `ERS-111`, `ERS-210`, or `ERS-7`.
2. Read the bundled documentation files in that tree.
3. Check the sample `.R` scripts for working R-CODE examples.
4. Use `src/` if you need the original packaged archives instead of the extracted contents.

## Summary

In short, this repository is a preservation and reference collection for Sony AIBO R-CODE materials, not a standalone codebase in the usual modern sense.
