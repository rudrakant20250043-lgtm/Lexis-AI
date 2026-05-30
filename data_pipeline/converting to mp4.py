from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=JGpmQvlYRdU"

ydl_opts = {
    'format': 'best',
    'outtmpl': 'video.mp4'
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])