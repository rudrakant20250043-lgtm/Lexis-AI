from moviepy import VideoFileClip

video = VideoFileClip("old_video.mp4")
video.audio.write_audiofile("output.wav")