# Purpose: Generate a simple QR code from user-provided text or a URL and save it as a PNG image.
# Dependencies:
# pip install qrcode
import qrcode
import os

# --- Configuration ---
OUTPUT_FILENAME = "qr.png"

# ---------------------

def generate_simple_qr_code(filename: str):
    """
    Prompts the user for data, generates a QR code, and saves it.

    Args:
        filename (str): The name of the output PNG file.
    """
    print("--- Simple QR Code Generator ---")
    
    # 1. Get input data from the user
    data = input("Enter text/URL for QR code: ").strip()
    
    if not data:
        print("No data entered. Exiting.")
        return

    try:
        # 2. Generate the QR code image object
        img = qrcode.make(data)
        
        # 3. Save the image to a file
        img.save(filename)
        
        print(f"\nQR code saved as {filename}")
        print(f"File path: {os.path.abspath(filename)}")

    except Exception as e:
        print(f"An error occurred during QR code generation: {e}")

# --- Execution ---
if __name__ == "__main__":
    generate_simple_qr_code(OUTPUT_FILENAME)

# Use Cases:
# 1. Link Sharing: Creating quick, scannable links for mobile users.
# 2. Contact Information: Encoding vCard data for easy saving of contact details.
# 3. Inventory Tagging: Encoding simple product IDs or serial numbers.