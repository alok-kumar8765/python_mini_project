# =================================
# Image Color Extraction in Python
# =================================

from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping
from sklearn.cluster import KMeans

Image.open('w2.jpg')

image = mpimg.imread('w2.jpg')
w, h, d = image.shape

pixels = image.reshape(w*h, d)

n_colors= 10
kmeans KMeans(n_clusters = n_colors, random_state=42).fit(pixels)

palette = np. uint8(kmeans.cluster_centers_)

plt.imshow([palette])
plt.axis('off')
plt.show()