import cv2
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("dice.jpg")  # Replace with your image path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
(h, w, c) = image.shape  # Get image dimensions

# Reshape the image into a 2D array of pixels
pixels = image.reshape((-1, 3))

# Apply Gaussian Mixture Model (GMM) with 3 clusters (adjust as needed)
num_clusters = 3
gmm = GaussianMixture(n_components=num_clusters, covariance_type='tied', random_state=42)
gmm.fit(pixels)

# Predict cluster labels
labels = gmm.predict(pixels)

# Reshape labels to match the image dimensions
segmented_image = labels.reshape((h, w))

# Plot the original and segmented images
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(image)
ax[0].set_title("Original Image")
ax[0].axis("off")

ax[1].imshow(segmented_image, cmap="viridis")
ax[1].set_title("Segmented Image using GMM")
ax[1].axis("off")

plt.show()