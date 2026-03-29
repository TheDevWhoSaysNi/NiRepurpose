# Instructions - Linux (Release App)

These steps are for end users downloading the packaged app from GitHub Releases.

## 1) Install required tools (one-time)

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install -y ffmpeg libimage-exiftool-perl unzip
```

### Fedora

```bash
sudo dnf install -y ffmpeg perl-Image-ExifTool unzip
```

Verify:

```bash
ffmpeg -version
exiftool -ver
```

## 2) Download the app from GitHub Releases

1. Open: `https://github.com/TheDevWhoSaysNi/NiRepurpose/releases`
2. Download the latest `NiRepurpose-Linux.zip`
3. Extract it

## 3) Run the app

From terminal in the extracted folder:

```bash
chmod +x NiRepurpose
./NiRepurpose
```

## 4) Use it on your media

- Click `Select Folder` and choose the folder that has your media
- Output is automatically created in:
  - `NiRepurpose_repurposed` inside the selected folder
