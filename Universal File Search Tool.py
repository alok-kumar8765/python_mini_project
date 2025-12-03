# A command-line tool to recursively search for a file by name within a specified directory tree.

import os

# --- 1. Define the Search Function ---
def search_file() -> None:
    """
    Prompts the user for a search root directory and a filename, then searches recursively.
    """
    # Prompt user for the starting search directory
    root_dir = input("Search in (Root Directory): ")
    # Prompt user for the file name to find (case-sensitive by default)
    file_name = input("File name (e.g., clcoding.pdf): ")

    print(f"\nSearching for '{file_name}' starting in '{root_dir}'...")

    # --- 2. Perform Recursive Walk ---
    # os.walk generates a tuple of (dirpath, dirnames, filenames) for each directory
    # 'path' is the current directory being examined
    # '_' is the list of subdirectories (we ignore this here)
    # 'files' is the list of files in the current directory
    
    found = False
    
    # Traverse the directory tree top-down
    for path, _, files in os.walk(root_dir):
        # Check if the target file name is present in the current directory's file list
        if file_name in files:
            # If found, construct the full absolute path
            full_path = os.path.join(path, file_name)
            print(f"✅ Found at: {full_path}")
            found = True
            # Stop the search immediately after the first file is found
            break
            
    # If the loop completes without finding the file (i.e., 'break' was not called)
    if not found:
        print("❌ Not found.")

# --- 3. Example Usage ---
if __name__ == "__main__":
    # Note: Ensure the root directory exists and is accessible.
    search_file()