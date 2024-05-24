from TTS.api import TTS
from TTS.utils.manage import ModelManager
import simpleaudio as sa

# Download a pre-trained TTS model
model_name = 'tts_models/en/ljspeech/tacotron2-DDC'
model_path = ModelManager().download_model(model_name)

# Initialize TTS with the model name
tts = TTS(model_name)

# Your meditation script
meditation_text = """
Take a deep breath. Close your eyes. Relax and let go of all your worries.
Feel the calmness spreading through your body. You are at peace.
"""

# Convert text to speech
try:
    wav_file = "meditation_coqui2.wav"
    tts.tts_to_file(text=meditation_text, file_path=wav_file)

    # Load and play the WAV file
    wave_obj = sa.WaveObject.from_wave_file(wav_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until the sound has finished playing

    print("Meditation audio played successfully.")

except Exception as err:
    print(f"An error occurred: {err}")
