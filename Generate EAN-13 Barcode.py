# This script uses the 'python-barcode' library to generate an EAN-13 barcode
# and save it in both PNG and SVG formats.
# The 'ImageWriter' is used to output the barcode as an image file.

from barcode import EAN13
from barcode.writer import ImageWriter
from IPython.display import Image, display

# -----------------
# Create PNG barcode
# -----------------
# We create an EAN13 barcode instance with the provided number (590123412345).
# The writer is set to ImageWriter to produce an image file.
img = EAN13("590123412345", writer=ImageWriter())

# We save the barcode instance, which generates the 'ean13_img.png' file.
png_file = img.save("ean13_img")

# -----------------
# Create SVG barcode
# -----------------
# We create a new EAN13 instance specifically for the SVG output.
img_svg = EAN13("590123412345")

# We save the barcode instance. By default (or if explicitly using SVGWriter),
# this generates the 'ean13_img_svg.svg' file.
svg_file = img_svg.save("ean13_img_svg")

# Display the generated PNG file (common in Jupyter environments).
display(Image(png_file))
