import librosa
import soundfile as sf

# Input audio file
input_file = "input.mp3.mp3" 

# Output converted file
output_file = "output.wav"

# Load audio
audio, sample_rate = librosa.load(input_file, sr=None)

# Save as WAV
sf.write(output_file, audio, sample_rate)

print("Audio converted successfully!")