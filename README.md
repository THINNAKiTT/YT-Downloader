# YT-Downloader

Simple interactive YouTube downloader using `yt-dlp`.

Features
- Download video (MP4) at selectable resolutions (2160p, 1440p, 1080p, 720p, 480p).
- Download audio only and convert to MP3 (requires `ffmpeg`).
- Saves outputs to the `downloaded/` folder.

Requirements
- Python 3.11+
- `yt-dlp` Python package
- `questionary` (used for interactive prompts)
- `ffmpeg` (required for MP3 conversion)
  

Installation

Recommended (use `uv` package manager):

```bash
uv sync    # installs dependencies from pyproject.toml
```

If you don't have `uv`, install from `requirements.txt`:

1) Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

Or install the main dependency directly:

```bash
pip install yt-dlp questionary
```

Usage

Run the script and follow the interactive prompts:

```bash
python main.py
```

Workflow when running:
- Paste a YouTube URL when prompted.
- Choose whether to download Video (MP4) or Audio (MP3).
- If Video, choose the target resolution.
- Files are saved into the `downloaded/` directory in the project root.

Notes
- If you want MP3 output make sure `ffmpeg` is installed and available on your PATH.
- The script uses `yt-dlp` options to select best video/audio and will merge into MP4 when downloading video.

Contributing

Feel free to open issues or send PRs to improve features or add CLI flags.

License

This project is provided as-is. Add a license if you intend to publish.

