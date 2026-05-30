
import librosa

audio, sr = librosa.load("output.wav", sr=16000)

print("Sample Rate:", sr)
print("Audio Length:", len(audio))