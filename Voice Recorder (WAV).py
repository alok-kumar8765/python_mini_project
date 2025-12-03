# Records audio for a specified duration and saves it as a WAV file using 'sounddevice' and 'scipy'.

import sounddevice as sd
from scipy.io.wavfile import write as wav_write
import numpy as np

# --- 1. Define Recording Parameters ---
# The standard sampling frequency (samples per second) for CD quality audio
FS = 44100  
CHANNELS = 2  # Stereo recording

# --- 2. Define the Recording Function ---
def record_audio(duration: int, filename: str = "record.wav") -> None:
    """
    Records audio from the microphone for a given duration and saves it as a WAV file.
    
    :param duration: The number of seconds to record.
    :param filename: The name of the output WAV file.
    """
    print(f"Recording for {duration} seconds...")
    
    try:
        # Record the audio. The result is a NumPy array.
        # sd.rec(samples, samplerate, channels)
        audio = sd.rec(int(duration * FS), samplerate=FS, channels=CHANNELS, dtype=np.int16)
        
        # Wait until the recording is finished
        sd.wait() 
        
        # Save the NumPy array data to a WAV file
        # wav_write(filename, samplerate, data_array)
        wav_write(filename, FS, audio)
        
        print(f"✅ Saved audio to {filename}")
        
    except ValueError as e:
        print(f"Error: A ValueError occurred. Ensure your microphone is connected and working. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during recording: {e}")

# --- 3. Example Usage ---
if __name__ == "__main__":
    try:
        # Prompt the user for the recording duration
        sec = int(input("Record seconds: "))
        
        # Start the recording process
        record_audio(sec)
        
    except ValueError:
        print("Invalid input. Please enter an integer for the number of seconds.")