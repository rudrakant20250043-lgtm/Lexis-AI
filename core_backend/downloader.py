import yt_dlp
import os

def download_youtube_audio(youtube_url):
    # Destination folder path
    output_dir = 'data_pipeline'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, 'raw_audio.wav'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    
    print("Bhai, audio download ho gayi aur data_pipeline folder mein save hai!")

# Test run
test_link = "https://www.youtube.com/watch?v=1OxKLppXgXA"
download_youtube_audio(test_link)
