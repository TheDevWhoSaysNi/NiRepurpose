# Instructions - macOS

## Which download should I use?

- **Full (recommended):** `NiRepurpose-Full-macOS.zip`
  - Includes bundled `ffmpeg` + `exiftool`
  - Best for most users
- **Lite:** `NiRepurpose-Lite-macOS.zip`
  - Smaller file
  - Requires `ffmpeg` and `exiftool` installed on PATH

Releases: https://github.com/TheDevWhoSaysNi/NiRepurpose/releases

## Full edition (easiest)

1. Download `NiRepurpose-Full-macOS.zip`
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

Verify:

```bash
ffmpeg -version
exiftool -ver
```

Then extract `NiRepurpose-Lite-macOS.zip` and open `NiRepurpose.app`.
