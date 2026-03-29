# Instructions - Windows (Release App)

These steps are for end users downloading the packaged app from GitHub Releases.

## 1) Install required tools (one-time)

Open PowerShell and run:

```powershell
winget install Gyan.FFmpeg
winget install OliverBetz.ExifTool
```

Verify:

```powershell
ffmpeg -version
exiftool -ver
```

## 2) Download the app from GitHub Releases

1. Open: `https://github.com/TheDevWhoSaysNi/NiRepurpose/releases`
2. Download the latest `NiRepurpose-Windows.zip`
3. Extract the zip anywhere on your computer

## 3) Run the app

1. Open the extracted folder
2. Double-click `NiRepurpose.exe`

## 4) Use it on your media

- Click `Select Folder` and choose the folder that has your media
- Output is automatically created in:
  - `NiRepurpose_repurposed` inside the selected folder
