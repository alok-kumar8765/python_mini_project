# Scans a directory for duplicate files based on their content hash (MD5).

import os
import hashlib

# --- 1. Define the Duplicate Finder Function ---
def find_duplicates(path: str) -> None:
    """
    Traverses a given path to find and report duplicate files.
    
    :param path: The folder path to search for duplicates.
    """
    # Dictionary to store file hashes and the name of the first file seen with that hash.
    # Format: {hash_value: filename}
    seen = {}
    
    print(f"\nScanning folder: {path}")

    # Iterate over every entry (file/folder) in the specified path
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        
        # Skip directories and non-files
        if not os.path.isfile(full_path):
            continue

        try:
            # Open the file in binary read mode ('rb')
            with open(full_path, "rb") as f:
                data = f.read()
            
            # Generate the MD5 hash of the file's content
            h = hashlib.md5(data).hexdigest()
            
            # Check if this hash has been seen before
            if h in seen:
                # Duplicate found! Print the current file and the file it duplicates
                print(f"Duplicate: {entry} <-> {seen[h]}")
            else:
                # First time seeing this hash, store the file name
                seen[h] = entry
                
        except Exception as e:
            # Handle potential permissions errors or file access issues
            print(f"Could not process file {entry}: {e}")

# --- 2. Example Usage ---
if __name__ == "__main__":
    # Prompt the user for the folder path
    folder_path = input("Folder path to check for duplicates: ")
    
    # Example: If the user inputs 'my_test_folder', the output will show duplicates within it.
    find_duplicates(folder_path)