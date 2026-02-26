import os
import sys
import yt_dlp
import questionary
import dotenv

dotenv.load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))

def download_media():
    print("=== YouTube Downloader (yt-dlp) ===")
    
    # 1. Recieve URL
    url = input("Paste URL YouTube here: ").strip()
    if not url:
        print("❌ Not founded URL")
        return

    # 2. Select file type (MP4 / MP3)
    file_type = questionary.select(
        "\n--- Choose file type ---",
        choices=[
            "Video - MP4",
            "Audio only - MP3",
        ]
    ).ask()

    # setting for yt-dlp
    # default to ./downloaded if DOWNLOAD_DIR not set
    download_dir = os.environ.get("DOWNLOAD_DIR") or os.path.join(current_dir, 'downloaded')
    os.makedirs(download_dir, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
    }

    # Case MP4 (Video)
    if "MP4" in file_type:
        res_choice = questionary.select(
            "\n--- Choose Video Resolution ---",
            choices=[
                "4K (2160p)",
                "2K (1440p)",
                "Full HD (1080p) [Recommended]",
                "HD (720p)",
                "SD (480p)",
            ]
        ).ask()

        res_map = {
            "4K (2160p)": 2160,
            "2K (1440p)": 1440,
            "Full HD (1080p)": 1080,
            "HD (720p)": 720,
            "SD (480p)": 480
        }
        height = res_map.get(res_choice, 1080)
        print(f"\n⏳ preparing to download MP4 ({height}p)...")
        
        ydl_opts.update({
            # Select the best video (within the specified height limit) + the best audio.
            'format': f'bestvideo[height<={height}]+bestaudio/best[height<={height}]',
            'merge_output_format': 'mp4'
        })

    # Case MP3 (Audio)
    else:
        print("\n⏳ Preparing to download and convert to MP3...")
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })

    # 3. Starting Download
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: # type: ignore
            ydl.download([url])
            print("\n✅ Download completed!")
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")

if __name__ == "__main__":
    download_media()