import librosa
import matplotlib.pyplot as plt

audio, sr = librosa.load("sample.wav")

print("Sample Rate:", sr)
print("Audio Length:", len(audio))

plt.figure(figsize=(10,4))
plt.plot(audio)
plt.title("Waveform")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()