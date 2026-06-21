import yt_dlp

url = input("Enter YouTube URL: ").strip()

if "youtube.com" not in url and "youtu.be" not in url:
    print("Invalid YouTube URL")
    exit()

ydl_opts = {
    "format": "bestvideo+bestaudio/best",

    # Convert to a TV-friendly MP4
    "postprocessors": [{
        "key": "FFmpegVideoConvertor",
        "preferedformat": "mp4"
    }],

    "ffmpeg_location": r"C:\Users\Antonio Estarlich\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin",

    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])