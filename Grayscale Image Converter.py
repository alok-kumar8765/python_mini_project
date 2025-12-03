# Converts a color image to grayscale using the Pillow (PIL) library.

from PIL import Image
import os

# --- 1. Define the Conversion Function ---
def convert_to_grayscale(input_img_path: str, output_img_path: str) -> None:
    """
    Opens an image, converts it to grayscale, and saves the result.
    
    :param input_img_path: Path to the input color image.
    :param output_img_path: Path to save the output grayscale image.
    """
    try:
        # Open the image file
        img = Image.open(input_img_path)
        
        # Convert the image to grayscale. 'L' stands for Luminance (8-bit grayscale).
        gray = img.convert("L")
        
        # Save the resulting grayscale image
        gray.save(output_img_path)
        
        print(f"✅ Successfully converted '{input_img_path}' to grayscale and saved as '{output_img_path}'")
        
    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_img_path}'.")
    except Exception as e:
        print(f"An error occurred during image processing: {e}")

# --- 2. Example Usage ---
if __name__ == "__main__":
    # IMPORTANT: You must have a file named 'LM.jpg' in the same directory
    # or replace the path with an existing image file.
    input_file = "LM.jpg"
    output_file = "LM_gray.jpg"
    
    if not os.path.exists(input_file):
        print(f"Note: Please ensure the input image '{input_file}' exists before running.")
    
    convert_to_grayscale(input_file, output_file)