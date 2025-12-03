# Converts a PDF file into a DOCX (Microsoft Word) document using 'pdf2docx'.

# You must install the pdf2docx library: pip install pdf2docx
from pdf2docx import Converter
import os

# --- 1. Define the Conversion Function ---
def convert_pdf_to_docx(pdf_file: str, docx_file: str) -> None:
    """
    Converts a PDF document to a DOCX document.
    
    :param pdf_file: Path to the input PDF file.
    :param docx_file: Path to save the output DOCX file.
    """
    print(f"Attempting to convert '{pdf_file}' to '{docx_file}'...")
    try:
        # Initialize the Converter object with the input PDF
        cv = Converter(pdf_file)
        
        # Perform the conversion and save the result to the DOCX file
        cv.convert(docx_file, start=0, end=None) # start and end are optional for page range
        
        # Close the converter to release resources
        cv.close()
        
        print(f"✅ Conversion complete. File saved as '{docx_file}'")
        
    except FileNotFoundError:
        print(f"Error: Input PDF file not found at '{pdf_file}'.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

# --- 2. Example Usage ---
if __name__ == "__main__":
    # IMPORTANT: You must have a file named 'clcoding.pdf' in the same directory
    # or replace the path with an existing PDF file.
    input_pdf_file = 'clcoding.pdf'
    output_docx_file = 'clcoding.docx'

    if not os.path.exists(input_pdf_file):
        print(f"Note: Please ensure the input PDF '{input_pdf_file}' exists before running.")
    
    convert_pdf_to_docx(input_pdf_file, output_docx_file)