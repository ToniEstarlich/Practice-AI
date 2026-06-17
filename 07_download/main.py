import yt_dlp

url = input("here the URL de YouTube: ").strip()

if "youtube.com" not in url and "youtu.be" not in url:
    print("❌ URL inválida")
    exit()

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    
    # 👇 tip: audio  (AAC)
    "postprocessors": [{
        "key": "FFmpegVideoConvertor",
        "preferedformat": "mkv"
    },{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "aac",
        "preferredquality": "192",
    }],

    "ffmpeg_location": r"C:\Users\Antonio Estarlich\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin",

    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])