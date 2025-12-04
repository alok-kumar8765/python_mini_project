# This script uses the OpenCV (cv2) library to apply a cartoon-like filter
# to an input image ("dog.jpg").

import cv2

# Read the image file. Ensure "dog.jpg" exists in the same directory.
img = cv2.imread("dog.jpg")

# 1. Convert the image to grayscale, which is needed for edge detection.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 2. Apply a median blur to the grayscale image to smooth out noise.
# A kernel size of 5x5 is used.
blur = cv2.medianBlur(gray, 5)

# 3. Use adaptive thresholding to find and sharpen the edges (lines) of the image.
# This serves as the mask for the cartoon effect.
edges = cv2.adaptiveThreshold(
    blur,
    255, # Max value to use
    cv2.ADAPTIVE_THRESH_MEAN_C, # Adaptive method: average of neighborhood
    cv2.THRESH_BINARY, # Threshold type: binary
    9, # Block size
    5 # Constant subtracted from the mean
)

# 4. Apply a bilateral filter to the original color image. This smooths colors
# while preserving edges, which is a key component of the cartoon effect.
color = cv2.bilateralFilter(img, 10, 250, 250)
# Arguments: source image, diameter of pixel neighborhood, sigmaColor (large for big color mixes), sigmaSpace

# 5. Combine the smoothed color image with the sharp edges using a bitwise AND operation.
# The 'edges' image acts as a mask, only showing the color where the edge is not white.
cartoon = cv2.bitwise_and(color, color, mask=edges)

# Display the resulting cartoonified image in a window titled "Cartoon Image".
cv2.imshow("Cartoon Image", cartoon)

# Wait indefinitely for a keypress to close the window.
cv2.waitKey(0)
