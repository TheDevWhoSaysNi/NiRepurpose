#!/usr/bin/env python3
"""
NiRepurpose by TheDevWhoSaysNi
License: Apache-2.0 (see LICENSE)
Third party disclosures: (see NOTICE)
Ni! 🌿
"""

from __future__ import annotations

import datetime
import os
import platform
import random
import shutil
import subprocess
import sys
import tempfile
import threading
import webbrowser
from datetime import timedelta
from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter as ctk

APP_NAME = "NiRepurpose"
APP_VERSION = "v0.1.0"
DEFAULT_OUTPUT_FOLDER = "NiRepurpose_repurposed"

FFMPEG_PATH = "ffmpeg"
EXIFTOOL_PATH = "exiftool"
VIDEO_CRF = "14"
VIDEO_PRESET = "slow"
AUDIO_BITRATE = "320k"

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff", ".heic", ".heif", ".gif"}
VIDEO_EXTS = {".mp4", ".mov", ".m4v", ".mkv", ".avi", ".webm"}

NAME_KEEP = "Original"
NAME_IOS = "iPhone"
NAME_ANDROID = "Android"
NAME_RANDOM = "Random"


def default_input_dir() -> Path:
    if getattr(sys, "frozen", False):
        exe_path = Path(sys.executable).resolve()
        if platform.system() == "Darwin":
            for ni_parent in exe_path.parents:
                if ni_parent.suffix == ".app":
                    return ni_parent.parent
        return exe_path.parent
    return Path(__file__).resolve().parent


def resource_path(relative: str) -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        base = Path(sys._MEIPASS)  # type: ignore[attr-defined]
    else:
        base = Path(__file__).resolve().parent
    return str(base / relative)


def generate_random_image_name() -> str:
    now = datetime.datetime.now()
    random_days = random.randint(-90, 0)
    random_date = now + timedelta(
        days=random_days,
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    date_compact = random_date.strftime("%Y%m%d%H%M%S")
    date_split = random_date.strftime("%Y%m%d_%H%M%S")
    prefix = random.choice(["IMG_", "PHOTO_", "PIC_", "SHOT_"])
    if random.random() < 0.5:
        return f"{prefix}{random.randint(1000, 9999)}.JPG"
    if random.random() < 0.5:
        return f"{prefix}{date_split}.JPG"
    return f"{prefix}{date_compact}.JPG"


def generate_ios_name() -> str:
    return f"IMG_{random.randint(1000, 9999)}.JPG"


def generate_android_name() -> str:
    now = datetime.datetime.now() + timedelta(
        days=random.randint(-45, 0),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    if random.random() < 0.5:
        return f"IMG_{now.strftime('%Y%m%d_%H%M%S')}.jpg"
    return f"PXL_{now.strftime('%Y%m%d_%H%M%S')}.jpg"


def generate_random_video_name() -> str:
    now = datetime.datetime.now()
    random_days = random.randint(-90, 0)
    random_date = now + timedelta(
        days=random_days,
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    date_compact = random_date.strftime("%Y%m%d%H%M%S")
    date_split = random_date.strftime("%Y%m%d_%H%M%S")
    prefix = random.choice(["VID_", "VIDEO_", "CLIP_", "REC_", "MOV_"])
    if random.random() < 0.5:
        return f"{prefix}{random.randint(1000, 9999)}.MP4"
    if random.random() < 0.5:
        return f"{prefix}{date_split}.MP4"
    return f"{prefix}{date_compact}.MP4"


def strip_all_metadata(path: str) -> None:
    try:
        subprocess.run(
            [EXIFTOOL_PATH, "-all=", "-overwrite_original", path],
            capture_output=True,
            timeout=30,
        )
    except Exception:
        pass


def random_filter_chain(allow_mirror=False) -> str:
    # Keep transforms extremely subtle to preserve visual quality.
    crop_percent = random.uniform(0.992, 0.999)
    rotate_deg = random.uniform(-0.15, 0.15)
    saturation = random.uniform(0.995, 1.01)
    contrast = random.uniform(0.995, 1.01)
    brightness = random.uniform(-0.003, 0.003)
    noise_strength = random.uniform(0.25, 0.9)
    zoom = random.uniform(1.000, 1.006)

    filters = [
        f"crop=iw*{crop_percent}:ih*{crop_percent}",
        f"rotate={rotate_deg}*PI/180:fillcolor=black",
        f"scale=iw*{zoom}:ih*{zoom}",
        f"eq=saturation={saturation}:contrast={contrast}:brightness={brightness}",
        "unsharp=5:5:0.4",
        f"noise=alls={noise_strength}:allf=t",
    ]

    # Mirror-only random flip (no vertical flip)
    if allow_mirror and random.random() < 0.5:
        filters.append("hflip")

    return ",".join(filters)


def repurpose_image(input_path: str, output_path: str, mirror_flip=False):
    try:
        filter_string = random_filter_chain(allow_mirror=mirror_flip)
        cmd = [
            FFMPEG_PATH,
            "-y",
            "-i",
            input_path,
            "-vf",
            filter_string,
            "-map_metadata",
            "-1",
            "-map_chapters",
            "-1",
            "-q:v",
            "1",
            "-qmin",
            "1",
            "-qmax",
            "2",
            output_path,
        ]
        proc = subprocess.run(cmd, capture_output=True)
        if not os.path.exists(output_path) or os.path.getsize(output_path) < 100:
            err_lines = proc.stderr.decode("utf-8", errors="replace").strip().splitlines()
            last_err = next((line for line in reversed(err_lines) if line.strip()), "Processing failed")
            return False, last_err
        strip_all_metadata(output_path)
        return True, None
    except Exception as exc:
        return False, str(exc)


def repurpose_video(input_path: str, output_path: str, mirror_flip=False):
    try:
        filter_string = random_filter_chain(allow_mirror=mirror_flip)
        filter_string = f"{filter_string},scale=trunc(iw/2)*2:trunc(ih/2)*2"
        cmd = [
            FFMPEG_PATH,
            "-y",
            "-i",
            input_path,
            "-vf",
            filter_string,
            "-c:v",
            "libx264",
            "-preset",
            VIDEO_PRESET,
            "-crf",
            VIDEO_CRF,
            "-profile:v",
            "high",
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
            "-c:a",
            "aac",
            "-b:a",
            AUDIO_BITRATE,
            "-map_metadata",
            "-1",
            "-map_chapters",
            "-1",
            output_path,
        ]
        proc = subprocess.run(cmd, capture_output=True)
        if not os.path.exists(output_path) or os.path.getsize(output_path) < 1000:
            err_lines = proc.stderr.decode("utf-8", errors="replace").strip().splitlines()
            last_err = next((line for line in reversed(err_lines) if line.strip()), "Processing failed")
            return False, last_err
        strip_all_metadata(output_path)
        return True, None
    except Exception as exc:
        return False, str(exc)


class RepurposerApp(ctk.CTk):
    def __init__(self, initial_dir: Path):
        super().__init__()

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.input_dir = initial_dir
        self._processing = False

        self.title(f"{APP_NAME} {APP_VERSION}")
        self.geometry("550x700")
        self.minsize(550, 700)

        try:
            if platform.system() == "Windows":
                self.iconbitmap(resource_path("assets/nirepurpose.ico"))
            else:
                import tkinter as tk

                ni_img = tk.PhotoImage(file=resource_path("assets/nirepurpose.png"))
                self.iconphoto(True, ni_img)
                self._icon_img = ni_img
        except Exception:
            pass

        self._build_ui()
        self._refresh_file_count()

    def _build_ui(self):
        self.github_btn = ctk.CTkButton(
            self,
            text="GitHub",
            width=90,
            fg_color="transparent",
            border_width=1,
            text_color=("black", "white"),
            border_color=("black", "white"),
            command=lambda: webbrowser.open("https://github.com/TheDevWhoSaysNi/NiRepurpose"),
        )
        self.github_btn.pack(pady=10, padx=20, anchor="ne")

        self.label = ctk.CTkLabel(self, text="NiRepurpose Image Repurposer", font=("Arial", 24, "bold"))
        self.label.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="Ready To Repurpose Media", font=("Arial", 14))
        self.status_label.pack(pady=(20, 0))

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.pack(pady=10)
        self.progress_bar.set(0)

        self.dir_frame = ctk.CTkFrame(self)
        self.dir_frame.pack(padx=40, pady=(10, 10), fill="x")

        ctk.CTkLabel(self.dir_frame, text="Destination Folder:").pack(anchor="w", padx=12, pady=(10, 0))
        self.dir_label = ctk.CTkLabel(self.dir_frame, text=str(self.input_dir), wraplength=430, justify="left")
        self.dir_label.pack(anchor="w", padx=12, pady=(4, 10))

        self.choose_dir_btn = ctk.CTkButton(
            self.dir_frame,
            text="Select Folder",
            command=self.choose_input_dir,
            width=140,
        )
        self.choose_dir_btn.pack(anchor="w", padx=12, pady=(0, 12))

        self.settings_frame = ctk.CTkFrame(self)
        self.settings_frame.pack(pady=20, padx=40, fill="both", expand=True)

        copies_row = ctk.CTkFrame(self.settings_frame, fg_color="transparent")
        copies_row.grid(row=0, column=0, columnspan=2, padx=20, pady=(12, 4), sticky="ew")
        ctk.CTkLabel(copies_row, text="Copies Per Media:").pack(side="left")

        self.copies_var = ctk.IntVar(value=1)
        ctk.CTkButton(
            copies_row,
            text="-",
            width=30,
            command=self._decrement_copies,
        ).pack(side="left", padx=(12, 4))
        self.copies_entry = ctk.CTkEntry(copies_row, textvariable=self.copies_var, width=60, justify="center")
        self.copies_entry.pack(side="left", padx=2)
        ctk.CTkButton(
            copies_row,
            text="+",
            width=30,
            command=self._increment_copies,
        ).pack(side="left", padx=(4, 0))

        ctk.CTkLabel(self.settings_frame, text="Naming Convention:").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.naming_var = ctk.StringVar(value=NAME_IOS)
        self.name_menu = ctk.CTkOptionMenu(
            self.settings_frame,
            values=[NAME_IOS, NAME_ANDROID, NAME_KEEP, NAME_RANDOM],
            variable=self.naming_var,
        )
        self.name_menu.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

        self.subfolders_var = ctk.BooleanVar(value=False)
        self.subfolders_switch = ctk.CTkSwitch(
            self.settings_frame,
            text="Include Subfolders",
            variable=self.subfolders_var,
            command=self._refresh_file_count,
        )
        self.subfolders_switch.grid(row=2, column=0, columnspan=2, pady=(10, 10), sticky="w", padx=20)

        self.mirror_var = ctk.BooleanVar(value=False)
        self.mirror_switch = ctk.CTkSwitch(
            self.settings_frame,
            text="Random Mirror Flip",
            variable=self.mirror_var,
        )
        self.mirror_switch.grid(row=3, column=0, columnspan=2, pady=(10, 20), sticky="w", padx=20)

        self.log_var = ctk.BooleanVar(value=False)
        self.log_switch = ctk.CTkSwitch(
            self.settings_frame,
            text="Generate Processing Log",
            variable=self.log_var,
        )
        self.log_switch.grid(row=4, column=0, columnspan=2, pady=(0, 20), sticky="w", padx=20)

        self.settings_frame.grid_columnconfigure(1, weight=1)

        self.run_btn = ctk.CTkButton(
            self,
            text="NiRepurpose my Media",
            command=self.start_processing,
            height=50,
            width=260,
            font=("Arial", 18, "bold"),
        )
        self.run_btn.pack(pady=(0, 40))

    def choose_input_dir(self) -> None:
        folder = filedialog.askdirectory(initialdir=str(self.input_dir))
        if folder:
            self.input_dir = Path(folder)
            self.dir_label.configure(text=str(self.input_dir))
            self.status_label.configure(text="Ready To Repurpose Media")
            self.progress_bar.set(0)
            self._refresh_file_count()

    def _scan_media(self):
        if self.subfolders_var.get():
            return [
                ni_path
                for ni_path in self.input_dir.rglob("*")
                if ni_path.is_file() and (ni_path.suffix.lower() in IMAGE_EXTS or ni_path.suffix.lower() in VIDEO_EXTS)
            ]
        return [
            ni_path
            for ni_path in self.input_dir.iterdir()
            if ni_path.is_file() and (ni_path.suffix.lower() in IMAGE_EXTS or ni_path.suffix.lower() in VIDEO_EXTS)
        ]

    def _refresh_file_count(self) -> None:
        # Folder scanning is still used by processing logic; no inline count text shown.
        return

    def _set_status(self, text: str) -> None:
        self.after(0, lambda: self.status_label.configure(text=text))

    def _set_progress(self, value: float) -> None:
        self.after(0, lambda: self.progress_bar.set(value))

    def _enable_run(self) -> None:
        self.after(0, lambda: self.run_btn.configure(state="normal"))

    def _sanitize_copies(self) -> int:
        try:
            ni_copies = int(self.copies_var.get())
        except Exception:
            ni_copies = 1
        ni_copies = max(1, min(100, ni_copies))
        self.copies_var.set(ni_copies)
        return ni_copies

    def _increment_copies(self) -> None:
        ni_copies = self._sanitize_copies()
        self.copies_var.set(min(100, ni_copies + 1))

    def _decrement_copies(self) -> None:
        ni_copies = self._sanitize_copies()
        self.copies_var.set(max(1, ni_copies - 1))

    def _resolve_name(self, src_path: Path, mode: str) -> str:
        src_stem = src_path.stem
        src_ext = src_path.suffix.lower()
        is_image = src_ext in IMAGE_EXTS
        is_video = src_ext in VIDEO_EXTS
        if mode == NAME_KEEP:
            if is_video:
                return f"{src_stem}.mp4"
            return f"{src_stem}.jpg"
        if mode == NAME_IOS:
            if is_video:
                return f"IMG_{random.randint(1000, 9999)}.MOV"
            return generate_ios_name()
        if mode == NAME_ANDROID:
            if is_video:
                now = datetime.datetime.now()
                return f"VID_{now.strftime('%Y%m%d_%H%M%S')}.mp4"
            return generate_android_name()
        if is_video:
            return generate_random_video_name()
        return generate_random_image_name()

    def _unique_path(self, path: Path) -> Path:
        if not path.exists():
            return path
        base, ext = path.stem, path.suffix
        ni = 2
        while True:
            candidate = path.parent / f"{base}_{ni}{ext}"
            if not candidate.exists():
                return candidate
            ni += 1

    def start_processing(self) -> None:
        if self._processing:
            return
        if shutil.which(FFMPEG_PATH) is None:
            messagebox.showerror(APP_NAME, "ffmpeg is not on PATH. Install it first.")
            return
        if shutil.which(EXIFTOOL_PATH) is None:
            messagebox.showerror(APP_NAME, "exiftool is not on PATH. Install it first.")
            return

        files = self._scan_media()
        total = len(files)
        if total == 0:
            self._set_status("No media found in this folder. The Knights Who Say Ni demand a sacrifice!")
            return
        ni_copies = self._sanitize_copies()

        out_root = self.input_dir / DEFAULT_OUTPUT_FOLDER
        out_root.mkdir(parents=True, exist_ok=True)

        self._processing = True
        self.run_btn.configure(state="disabled")
        self.progress_bar.set(0)
        self._set_status("Starting...")

        threading.Thread(
            target=self._worker,
            args=(files, out_root, ni_copies),
            daemon=True,
        ).start()

    def _worker(self, files, out_root: Path, ni_copies: int) -> None:
        total = len(files) * ni_copies
        scrubbed = 0
        failed = 0
        naming_mode = self.naming_var.get()
        mirror_flip = bool(self.mirror_var.get())
        write_log = bool(self.log_var.get())
        log_file_path = out_root / "NiRepurpose_log.txt"

        if write_log:
            try:
                with log_file_path.open("a", encoding="utf-8") as ni_log:
                    ni_log.write(f"\n=== NiRepurpose Run {datetime.datetime.now().isoformat(timespec='seconds')} ===\n")
                    ni_log.write(f"Source: {self.input_dir}\n")
                    ni_log.write(f"Destination: {out_root}\n")
                    ni_log.write(f"Total files queued: {total}\n")
                    ni_log.write(f"Copies per media: {ni_copies}\n")
                    ni_log.write(f"Include subfolders: {bool(self.subfolders_var.get())}\n")
                    ni_log.write(f"Naming mode: {naming_mode}\n")
                    ni_log.write(f"Random mirror flip: {mirror_flip}\n\n")
            except Exception:
                write_log = False

        ni_done = 0
        for ni, src in enumerate(files, start=1):
            for ni_copy in range(1, ni_copies + 1):
                ni_done += 1
                self._set_progress(ni_done / total)
                if ni_copies > 1:
                    self._set_status(
                        f"Repurposing {ni_done} of {total}: {src.name} (copy {ni_copy}/{ni_copies}) Ni! Ping! Nee-wopp."
                    )
                else:
                    self._set_status(f"Repurposing {ni_done} of {total}: {src.name} Ni! Ping! Nee-wopp.")

                temp_out = None
                try:
                    src_ext = src.suffix.lower()
                    is_video = src_ext in VIDEO_EXTS
                    tmp_suffix = ".mp4" if is_video else ".jpg"
                    tmp = tempfile.NamedTemporaryFile(suffix=tmp_suffix, dir=out_root, delete=False)
                    temp_out = Path(tmp.name)
                    tmp.close()

                    if is_video:
                        success, err = repurpose_video(str(src), str(temp_out), mirror_flip=mirror_flip)
                    else:
                        success, err = repurpose_image(str(src), str(temp_out), mirror_flip=mirror_flip)
                    if not success:
                        failed += 1
                        if temp_out.exists():
                            temp_out.unlink()
                        print(f"Ni! Failed on {src.name}: {err}")
                        if write_log:
                            try:
                                with log_file_path.open("a", encoding="utf-8") as ni_log:
                                    ni_log.write(f"[FAIL] {src.name} (copy {ni_copy}/{ni_copies}) :: {err}\n")
                            except Exception:
                                pass
                        continue

                    ni_name = self._resolve_name(src, naming_mode)
                    ni_dest = self._unique_path(out_root / ni_name)
                    temp_out.replace(ni_dest)
                    scrubbed += 1
                    if write_log:
                        try:
                            with log_file_path.open("a", encoding="utf-8") as ni_log:
                                ni_log.write(f"[OK] {src.name} (copy {ni_copy}/{ni_copies}) -> {ni_dest.name}\n")
                        except Exception:
                            pass
                except Exception as exc:
                    failed += 1
                    if temp_out and temp_out.exists():
                        temp_out.unlink()
                    print(f"Ni! Error processing {src}: {exc}")
                    if write_log:
                        try:
                            with log_file_path.open("a", encoding="utf-8") as ni_log:
                                ni_log.write(f"[ERROR] {src.name} (copy {ni_copy}/{ni_copies}) :: {exc}\n")
                        except Exception:
                            pass

        if write_log:
            try:
                with log_file_path.open("a", encoding="utf-8") as ni_log:
                    ni_log.write(
                        f"\nSummary: Processed={total}, Scrubbed={scrubbed}, Issues={failed}\n"
                    )
            except Exception:
                pass

        self._set_progress(1.0)
        self._set_status("Complete!")
        self._processing = False
        self._enable_run()
        self._refresh_file_count()

        self.after(
            0,
            lambda: messagebox.showinfo(
                "NiClean Complete",
                f"Processed: {total}\nScrubbed: {scrubbed}\nIssues: {failed}\n\nDone. I mean, Ni!",
            ),
        )


if __name__ == "__main__":
    app = RepurposerApp(default_input_dir())
    app.mainloop()
