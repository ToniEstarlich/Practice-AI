import yt_dlp 

url = input("here the URL de YouTube: ").strip()

if "youtube.com" not in url and "youtu.be" not in url:
    print("❌ URL inválida")
    exit()

ydl_opts = {
    "format": "bv*[vcodec^=avc1]+ba/b",
   #  "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mkv",
    "ffmpeg_location": r"C:\Users\Antonio Estarlich\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin",
    "outtmpl": "%(title)s.%(ext)s",
    "noplaylist": True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

"""
 cmd note: in the folder press cmd, and in the cmn, write

 " for %i in (*.mkv) do ffmpeg -i "%i" -c:v copy -c:a aac -b:a 192k "fixed_%~ni.mkv" "

now the file can listening the audio in TV 

"""