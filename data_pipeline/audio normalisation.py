'''import librosa
import soundfile as sf
import numpy as np

# Load audio
audio, sr = librosa.load("output.wav", sr=None)

# Normalize (peak normalization)
audio = audio / np.max(np.abs(audio))

# Save file
sf.write("normalized.wav", audio, sr)'''
import librosa
import soundfile as sf
import numpy as np
import os
# Check file exists
input_file = "output.wav"

if not os.path.exists(input_file):
    raise FileNotFoundError(f"{input_file} not found in current folder")

# load audio
audio, sr = librosa.load(input_file, sr=None)

print("Sample Rate:", sr)
print("Audio Shape:", audio.shape)
# Peak Normalization (safe)-
peak = np.max(np.abs(audio))

if peak > 0:
    audio = audio / peak
else:
    print("Warning: silent audio detected")
# Safety clipping
audio = np.clip(audio, -1.0, 1.0)
# Save output
output_file = "normalized.wav"
sf.write(output_file, audio, sr)

print("Done! Saved as:", output_file)