import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

audio, sr = librosa.load("cleaned_audio.wav", sr=16000)

# Convert to spectrogram
D = librosa.amplitude_to_db(
    np.abs(librosa.stft(audio)),
    ref=np.max
)

# Plot
plt.figure(figsize=(12, 5))

librosa.display.specshow(
    D,
    sr=sr,
    x_axis='time',
    y_axis='hz'
)

plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram")

plt.show()