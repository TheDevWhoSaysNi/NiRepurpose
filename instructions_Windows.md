# Instructions - Windows

## Which download should I use?

- **Full (recommended):** `NiRepurpose-Full-Windows.zip`
  - Includes bundled `ffmpeg` + `exiftool`
  - No CLI setup required
- **Lite:** `NiRepurpose-Lite-Windows.zip`
  - Smaller file
  - Requires `ffmpeg` and `exiftool` installed on PATH

Releases: https://github.com/TheDevWhoSaysNi/NiRepurpose/releases

## Full edition (easiest)

1. Download `NiRepurpose-Full-Windows.zip`
2. Extract it
3. Double-click `NiRepurpose.exe`
4. Click `Select Folder` for your media folder
5. Output appears in `NiRepurpose_repurposed` inside that folder

## Lite edition (tools on PATH)

### 1) Install tools (one-time)

```powershell
winget install Gyan.FFmpeg
winget install OliverBetz.ExifTool
```

Verify:

```powershell
ffmpeg -version
exiftool -ver
```

### 2) Download and run

1. Download `NiRepurpose-Lite-Windows.zip`
2. Extract and run `NiRepurpose.exe`
3. Select your media folder and process
