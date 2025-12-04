# Purpose: Convert user-input text into audible speech using a local Text-to-Speech engine.
# Dependencies:
# pip install pyttsx3
import pyttsx3

# --- Configuration ---
MIN_SPEED = 100
MAX_SPEED = 300

# ---------------------

def speak_text_from_input():
    """
    Initializes the TTS engine, prompts the user for text and speed, and speaks the text.
    """
    print("--- Text-to-Speech Tool ---")
    
    # 1. Initialize the TTS engine
    engine = pyttsx3.init()
    
    # 2. Get input text
    msg = input("Enter text to speak: ").strip()
    
    if not msg:
        print("No text entered. Exiting.")
        return

    # 3. Get input speed, handling non-integer inputs gracefully
    while True:
        try:
            speed_str = input(f"Speed ({MIN_SPEED}-{MAX_SPEED}): ").strip()
            if not speed_str:
                print("Using default speed (200).")
                speed = 200
                break
            speed = int(speed_str)
            if MIN_SPEED <= speed <= MAX_SPEED:
                break
            else:
                print(f"Please enter a number between {MIN_SPEED} and {MAX_SPEED}.")
        except ValueError:
            print("Invalid input. Please enter a whole number for speed.")
            
    try:
        # 4. Set speech properties (rate/speed)
        engine.setProperty("rate", speed)
        
        # 5. Queue the message to be spoken
        engine.say(msg)
        
        print(f"Speaking text: '{msg}' at speed: {speed}")
        
        # 6. Block while all queued speech commands are processed
        engine.runAndWait()

    except Exception as e:
        print(f"An error occurred during speech synthesis: {e}")

# --- Execution ---
if __name__ == "__main__":
    speak_text_from_input()

# Use Cases:
# 1. Development: Debugging by outputting status messages audibly.
# 2. Accessibility: Providing audio feedback or narrating application content.
# 3. Simple Automation: Creating voice alerts for specific events.