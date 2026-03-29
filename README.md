# NiRepurpose

NiRepurpose is a desktop GUI app inspired by NiClean's style and workflow, but built for bulk image repurposing.

It processes images in a folder, applies subtle random visual changes, strips metadata, and exports with configurable naming styles:

- `Keep Original`
- `iOS Style`
- `Android Style`
- `Random Style` (`IMG_`, `PHOTO_`, `PIC_`, `SHOT_`, etc.)

## Features

- NiClean-style UI layout using `customtkinter`
- Light mode / dark mode / system mode switcher
- Bulk image processing from an input folder
- Repeat processing per image
- Optional random horizontal/vertical flip
- Metadata stripping via `exiftool`
- Randomized image transforms via `ffmpeg`
- Output naming modes for iOS, Android, original names, and fully random names

## Requirements

You need:

- Python 3.10+ (3.11 recommended)
- pip
- ffmpeg available on your PATH
- exiftool available on your PATH

Python package dependencies:

- `customtkinter`
- `Pillow`
- `numpy`

## Install

### 1) Clone or download project

```bash
git clone https://github.com/TheDevWhoSaysNi/NiRepurpose.git
cd NiRepurpose
```

### 2) Create and activate a virtual environment

#### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install Python dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4) Install ffmpeg + exiftool

#### Windows (winget)

```powershell
winget install Gyan.FFmpeg
winget install OliverBetz.ExifTool
```

#### macOS (Homebrew)

```bash
brew install ffmpeg exiftool
```

#### Ubuntu / Debian

```bash
sudo apt update
sudo apt install -y ffmpeg libimage-exiftool-perl
```

#### Fedora

```bash
sudo dnf install -y ffmpeg perl-Image-ExifTool
```

## Run

```bash
python NiRepurpose.py
```

## Usage

1. Select your input folder (source images).
2. Select your output folder.
3. Set `Repeats per image`.
4. Choose `Filename mode`:
   - `Keep Original`: keep source base names (with repeat suffix if repeats > 1)
   - `iOS Style`: names like `IMG_1234.JPG`
   - `Android Style`: names like `IMG_20260328_113000.jpg` / `PXL_...`
   - `Random Style`: random `IMG_`, `PHOTO_`, `PIC_`, `SHOT_` naming
5. Click `Process Images`.

## Cross-platform release plan (later)

When you are ready to publish GitHub releases for Windows, Linux, and macOS, you can package with PyInstaller:

```bash
pip install pyinstaller
pyinstaller --noconfirm --windowed --name NiRepurpose NiRepurpose.py
```

Then create CI jobs (GitHub Actions) to build artifacts on each OS runner and attach to releases.

## Notes

- NiRepurpose does **not** bundle ffmpeg or exiftool.
- Users install system tools themselves and keep them on PATH.
- Test with sample photos before running on large production folders.

## Ni

Ni
