# This script demonstrates how to generate and display a Code128 barcode
# using the 'python-barcode' library.

# Installation requirement (if running outside an environment where it's installed):
# pip install python-barcode

from barcode import Code128
from barcode.writer import ImageWriter
from IPython.display import Image, display

# -----------------
# Create barcode
# -----------------
# We create a Code128 barcode instance with the text "BCODING-123".
# The writer is set to ImageWriter to ensure an image file output.
bcoding = Code128("BCODING-123", writer=ImageWriter())

# We save the barcode instance, which generates the image file (e.g., 'code128_bcoding.png').
filename = bcoding.save("code128_bcoding")

# -----------------
# Display inside notebook
# -----------------
# We use the IPython display function to show the generated image directly
# in a notebook environment (like Jupyter).
display(Image(filename))
