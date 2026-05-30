import librosa
import soundfile as sf
import numpy as np

# Load audio (16 kHz recommended)
audio, sr = librosa.load("output.wav", sr=16000)

chunk_duration = 5  # seconds
chunk_samples = chunk_duration * sr

# Split into chunks
for i in range(0, len(audio), chunk_samples):
    chunk = audio[i:i + chunk_samples]

    # skip very small chunks
    if len(chunk) < chunk_samples // 2:
        continue

    filename = f"chunk_{i // chunk_samples}.wav"
    sf.write(filename, chunk, sr)

print("Audio split into chunks!")
