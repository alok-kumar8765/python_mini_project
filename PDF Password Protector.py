# Adds password protection to a PDF file using 'PyPDF2' and 'getpass' for secure input.

from PyPDF2 import PdfReader, PdfWriter
import getpass
import os

# --- 1. Define the Protection Function ---
def protect_pdf(input_pdf: str, output_pdf: str) -> None:
    """
    Encrypts an input PDF file with a password and saves it to an output file.
    
    :param input_pdf: Path to the original PDF file.
    :param output_pdf: Path to save the protected PDF file.
    """
    try:
        # Create a PdfReader object to read the input PDF
        reader = PdfReader(input_pdf)
        # Create a PdfWriter object to build the new encrypted PDF
        writer = PdfWriter()

        # Copy all pages from the reader to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Securely prompt the user for a password (input will not be displayed)
        print("--- Enter Password ---")
        password = getpass.getpass("Enter a password: ")
        
        # Encrypt the PDF content with the provided password
        writer.encrypt(password)
        
        # Write the encrypted content to the output file
        # 'wb' mode is used for binary write
        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

        print(f"Success: The PDF '{input_pdf}' has been protected and saved as '{output_pdf}'.")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_pdf}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- 2. Example Usage ---
if __name__ == "__main__":
    # IMPORTANT: You must have a file named 'clcoding.pdf' in the same directory
    # or replace the path with an existing PDF file.
    
    input_file_name = "clcoding.pdf"
    output_file_name = "protected_file.pdf"

    # Create a dummy file for demonstration if it doesn't exist 
    # (A real PDF is required to run this successfully)
    if not os.path.exists(input_file_name):
        print(f"Note: Dummy file '{input_file_name}' needs to be a valid PDF for protection to work.")
        print("Please ensure the input PDF exists before running.")
    
    # Call the function to protect the PDF
    protect_pdf(input_file_name, output_file_name)