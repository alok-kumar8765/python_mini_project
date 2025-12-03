# Automatically changes the desktop wallpaper on Windows using 'ctypes'.
# NOTE: This script is designed ONLY for Windows operating systems.

import ctypes
import os
import random

# Define the Windows API constant for setting the desktop wallpaper
SPI_SETDESKWALLPAPER = 20
# Define flags to update the user profile and send a system message
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDCHANGE = 0x02

# --- 1. Define the Wallpaper Changing Function ---
def change_wallpaper() -> None:
    """
    Prompts for a folder, selects a random image, and sets it as the desktop wallpaper.
    """
    # Check if the operating system is Windows
    if os.name != 'nt':
        print("Error: This script is Windows-specific and requires the 'ctypes' library for Windows API interaction.")
        return

    # Prompt the user for the folder containing wallpapers
    folder = input("Wallpaper folder path: ")
    
    # --- 2. Filter for Image Files ---
    # List all files in the folder and filter for common image extensions (.jpg, .png)
    files = [
        f for f in os.listdir(folder) 
        if f.lower().endswith((".jpg", ".png", ".jpeg")) and os.path.isfile(os.path.join(folder, f))
    ]
    
    if not files:
        print(f"Error: No JPEG or PNG image files found in '{folder}'.")
        return

    # --- 3. Select Random Image and Get Full Path ---
    # Randomly choose one file from the filtered list
    wall_file = random.choice(files)
    
    # Construct the full absolute path to the chosen wallpaper file
    path = os.path.abspath(os.path.join(folder, wall_file))
    
    # --- 4. Call Windows API to Set Wallpaper ---
    # SystemParametersInfoW(action, param, path, flags)
    # 20 (SPI_SETDESKWALLPAPER), 0 (unused), path (the file to set), 3 (flags combined)
    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 
        0, 
        path, 
        SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
    )
    
    if result:
        print(f"✅ Wallpaper successfully changed to: {wall_file}")
    else:
        # Handle cases where the API call fails (e.g., path is too long, permission issues)
        print(f"Error: Failed to change wallpaper. Check path and permissions.")

# --- 5. Example Usage ---
if __name__ == "__main__":
    # Example input from the image: "C:\Users\91748\Downloads\walpaper.jpeg"
    # The script expects a FOLDER, not a specific file, so the user should enter the directory.
    # e.g., 'C:\Users\91748\Downloads' if 'walpaper.jpeg' is inside.
    change_wallpaper()