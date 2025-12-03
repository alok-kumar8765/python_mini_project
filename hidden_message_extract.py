# Extracts the Least Significant Bit (LSB) from the first 8 pixels of an image 
# to demonstrate a basic Steganography decoding concept using Pillow (PIL).

from PIL import Image
from typing import List, Tuple

# --- 1. Define the Extraction Function ---
def extract_hidden_bits(image_path: str) -> None:
    """
    Loads an image and extracts the LSB from the first 8 pixels' red channel.
    
    :param image_path: Path to the image file containing the potential message.
    """
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Get all pixel data as a sequence of (R, G, B) tuples
        pixels: List[Tuple[int, int, int]] = list(img.getdata())
        
        # --- 2. Extract LSB from the first 8 pixels ---
        # We only look at the first 8 pixels for a simple 8-bit message (1 byte).
        # We use the Red channel (index [0]) for extraction.
        # '& 1' is a bitwise AND operation that isolates the Least Significant Bit.
        bits = [p[0] & 1 for p in pixels[:8]]
        
        # Convert the list of integers (0s and 1s) into a single binary string
        msg = "".join(str(b) for b in bits)
        
        # Print the extracted binary message
        print(f"Hidden bits: {msg}")
        
    except FileNotFoundError:
        print(f"Error: Input file not found at '{image_path}'.")
    except Exception as e:
        print(f"An error occurred during image processing: {e}")

# --- 3. Example Usage ---
if __name__ == "__main__":
    # IMPORTANT: You must have a file named 'bird.jpeg' in the same directory
    # or replace the path with an existing image file.
    input_file = "bird.jpeg"
    
    if not os.path.exists(input_file):
        print(f"Note: Please ensure the input image '{input_file}' exists before running.")
        
    # The image snippet shows an output of '11001111'
    extract_hidden_bits(input_file)