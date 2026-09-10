# Instructions - Linux

## Which download should I use?

- **Full (recommended):** `NiRepurpose-Full-Linux.zip`
  - Includes bundled `ffmpeg` + `exiftool`
  - No CLI setup required for tools
- **Lite:** `NiRepurpose-Lite-Linux.zip`
  - Smaller file
  - Requires `ffmpeg` and `exiftool` installed on PATH

Releases: https://github.com/TheDevWhoSaysNi/NiRepurpose/releases

## Full edition (easiest)

```bash
# After downloading NiRepurpose-Full-Linux.zip
unzip NiRepurpose-Full-Linux.zip
chmod +x NiRepurpose
./NiRepurpose
```

Then click `Select Folder` for your media folder. Output is created in `NiRepurpose_repurposed`.

## Lite edition (tools on PATH)

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

Then:

```bash
unzip NiRepurpose-Lite-Linux.zip
chmod +x NiRepurpose
./NiRepurpose
```
