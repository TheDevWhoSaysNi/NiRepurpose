# Instructions - macOS (Release App)

These steps are for end users downloading the packaged app from GitHub Releases.

## 1) Install required tools (one-time)

If Homebrew is not installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install required tools:

```bash
brew install ffmpeg exiftool
```

Verify:

```bash
ffmpeg -version
exiftool -ver
```

Add FFMPEG to PATH:

```bash
sudo ln -s /opt/homebrew/bin/ffmpeg /usr/local/bin/ffmpeg
```

## 2) Download the app from GitHub Releases

1. Open: `https://github.com/TheDevWhoSaysNi/NiRepurpose/releases`
2. Download the latest `NiRepurpose-macOS.zip`
3. Extract the zip

## 3) Run the app

1. Open `NiRepurpose.app` from the extracted folder
2. If macOS blocks first launch:
   - Right-click `NiRepurpose.app` -> `Open`
   - Click `Open` again

## 4) Use it on your media

- Click `Select Folder` and choose the folder that has your media
- Output is automatically created in:
  - `NiRepurpose_repurposed` inside the selected folder
