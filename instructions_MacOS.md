# Instructions - macOS

## Which download should I use?

First confirm your Mac architecture:

```bash
uname -m
```

- `arm64` = Apple Silicon (M1/M2/M3/M4)
- `x86_64` = Intel

Then pick an edition:

- **Full (recommended):**
  - Apple Silicon: `NiRepurpose-Full-macOS.zip`
  - Intel: `NiRepurpose-Full-macOS-Intel.zip`
  - Includes bundled `ffmpeg` + `exiftool`
  - Best for most users
- **Lite:**
  - Apple Silicon: `NiRepurpose-Lite-macOS.zip`
  - Intel: `NiRepurpose-Lite-macOS-Intel.zip`
  - Smaller file
  - Requires `ffmpeg` and `exiftool` installed on PATH

Intel Macs need the Intel zip. The Apple Silicon build will not run on Intel.

Releases: https://github.com/TheDevWhoSaysNi/NiRepurpose/releases

## Full edition (easiest)

1. Download the Full zip for your architecture (`NiRepurpose-Full-macOS.zip` or `NiRepurpose-Full-macOS-Intel.zip`)
2. Extract it
3. Open `NiRepurpose.app`
4. If macOS blocks first launch: right-click -> `Open` -> `Open`
5. Click `Select Folder` for your media folder
6. Output appears in `NiRepurpose_repurposed` inside that folder

Note: the Full macOS build still needs a system `perl` install to run the bundled ExifTool script (usually already present on macOS).

## Lite edition (tools on PATH)

Install Homebrew tools:

```bash
brew install ffmpeg exiftool
```

If `ffmpeg` is installed but not found on PATH (Apple Silicon Homebrew), add it:

```bash
sudo ln -s /opt/homebrew/bin/ffmpeg /usr/local/bin/ffmpeg
```

Intel Homebrew already installs into `/usr/local/bin`, so that extra symlink is usually unnecessary.

Verify:

```bash
ffmpeg -version
exiftool -ver
```

Then extract the Lite zip for your architecture and open `NiRepurpose.app`.
