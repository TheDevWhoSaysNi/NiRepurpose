# NiRepurpose

NiRepurpose is a desktop app inspired by NiClean, focused on bulk repurposing media for social posting.

It supports both images and videos, applies subtle randomized processing, strips metadata, and exports into an automatic output subfolder.

## Features

- NiClean-style dark UI and workflow
- Bulk media processing (`images + videos`)
- Optional recursive scan with `Include Subfolders`
- Copies-per-media control (`1` to `100`)
- Naming modes:
  - `iPhone`
  - `Android`
  - `Original`
  - `Random` (`IMG_`, `PIC_`, `SHOT_`, `VID_`, `CLIP_`, etc.)
- Random mirror flip option (`hflip` only)
- Optional run log generation (`NiRepurpose_log.txt`)
- Metadata stripping via `exiftool`
- Social-friendly encode defaults via `ffmpeg`

## Requirements

- Python `3.10+` (3.11 recommended)
- `pip`
- `ffmpeg` on PATH
- `exiftool` on PATH

Python dependency:

- `customtkinter`

## Quick Start (Release App)

For easiest use, download packaged builds from GitHub Releases:

- [NiRepurpose Releases](https://github.com/TheDevWhoSaysNi/NiRepurpose/releases)

Then follow your OS guide below.

## How Output Works

- Choose `Destination Folder` in the UI.
- NiRepurpose writes output to:
  - `<Destination Folder>/NiRepurpose_repurposed`
- No separate output-picker is required.

## OS-specific Setup Docs

Use these for easy copy/paste install commands:

- `Instructions_Windows.md`
- `Instructions_Linux.md`
- `Instructions_MacOS.md`

## Packaging

Tagging `v*` in GitHub triggers the release workflow and builds Windows, Linux, and macOS artifacts.

## Developer Run (from source)

If you are developing locally:

```bash
git clone https://github.com/TheDevWhoSaysNi/NiRepurpose.git
cd NiRepurpose
python -m venv .venv
```

Activate environment:

- Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install dependency and run:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python NiRepurpose.py
```

For manual local packaging:

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed --name NiRepurpose NiRepurpose.py
```

## Notes

- NiRepurpose does **not** bundle `ffmpeg` or `exiftool`.
- Install both tools system-wide before running.
- Test on sample media before large runs.
