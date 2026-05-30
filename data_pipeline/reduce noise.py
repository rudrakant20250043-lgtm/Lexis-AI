'''import librosa
import noisereduce as nr
import soundfile as sf
import numpy as np

# Load audio
audio, sr = librosa.load("output.wav", sr=16000)

# Normalize volume
audio = audio / np.max(np.abs(audio))

# Reduce noise
cleaned_audio = nr.reduce_noise(
    y=audio,
    sr=sr
)

# Save cleaned audio
sf.write("cleaned_audio.wav", cleaned_audio, sr)

print("Noise reduction completed!")'''

import librosa
import noisereduce as nr
import soundfile as sf
import numpy as np

# Load audio
audio, sr = librosa.load("output.wav", sr=16000)

# Normalize
audio = audio / np.max(np.abs(audio))

# Take first second as noise profile
noise_part = audio[0:16000]

# Reduce noise
cleaned_audio = nr.reduce_noise(
    y=audio,
    sr=sr,
    y_noise=noise_part,
    prop_decrease=0.8
)

# Save output
sf.write("cleaned_audio.wav", cleaned_audio, sr)

print("Audio cleaned successfully!")