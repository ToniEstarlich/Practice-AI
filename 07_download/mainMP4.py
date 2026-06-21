import yt_dlp

# Ask for the YouTube URL
url = input("Enter YouTube URL: ").strip()

# Basic URL validation
if "youtube.com" not in url and "youtu.be" not in url:
    print("Invalid YouTube URL")
    exit()

# yt-dlp configuration
ydl_opts = {
    # Download the best video and audio available
    "format": "bestvideo+bestaudio/best",

    # Merge into MP4
    "merge_output_format": "mp4",

    # Path to FFmpeg
    "ffmpeg_location": r"C:\Users\Antonio Estarlich\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin",

    # Output filename
    "outtmpl": "%(title)s.%(ext)s",

    # Do not download playlists
    "noplaylist": True,
}

# Download video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])