import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load audio
audio, sr = librosa.load("output.wav", sr=16000)

# Create figure
plt.figure(figsize=(12, 4))

# Draw waveform
librosa.display.waveshow(audio, sr=sr)

# Labels
plt.title("Original Audio Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")


plt.savefig("waveform.png")

# Show graph
plt.show()