

import librosa
import soundfile as sf

audio, sr = librosa.load("output.wav", sr=16000)

# remove leading & trailing silence
trimmed_audio, _ = librosa.effects.trim(audio, top_db=20)

sf.write("no_silence.wav", trimmed_audio, sr)

print("Silence trimmed!")