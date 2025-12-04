# This script generates a highly customized WordCloud (word art) image
# using the 'wordcloud' and 'matplotlib' libraries.

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Define the text content for the word cloud generation.
# This text is tokenized, and word frequency determines word size in the output.
text = "Data Science AI Python Visualization Art Creativity ML " * 20

# -----------------
# Configure WordCloud
# -----------------
wc = WordCloud(
    width=800,              # Set the width of the generated image.
    height=400,             # Set the height of the generated image.
    background_color="black", # Set the background color to black.
    colormap='plasma',      # Use the 'plasma' color map for word colors.
    contour_color='cyan',   # Set a cyan color for the contour outline.
    contour_width=2         # Set the width of the contour line.
).generate(text)            # Generate the word cloud from the input text.

# -----------------
# Display using Matplotlib
# -----------------
# Create a figure to display the word cloud.
plt.figure(figsize=(8,4))

# Display the word cloud image. 'interpolation' is set for smoother rendering.
plt.imshow(wc, interpolation="bilinear")

# Turn off the axis ticks and labels for a cleaner look.
plt.axis("off")

# Set the title for the plot.
plt.title("Artistic Wordcloud", color='white')

# Display the plot window.
plt.show()
