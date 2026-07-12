import numpy as np
from PIL import Image

# -----------------------------------
# Load image and convert to grayscale
# -----------------------------------
img = Image.open("photo.PNG").convert("L")

# Convert image to NumPy array
image = np.array(img)

print("Original Image Matrix:\n")
print(image)

# Display original image
Image.fromarray(image).show()

# -----------------------------------
# Part 1: Brightness +30%
# -----------------------------------
bright = np.clip(image * 1.3, 0, 255).astype(np.uint8)

print("\nBrightened Image Matrix:\n")
print(bright)

Image.fromarray(bright).show()

# -----------------------------------
# Part 2: Dark mode -40%
# -----------------------------------
dark = np.clip(image * 0.6, 0, 255).astype(np.uint8)

print("\nDarkened Image Matrix:\n")
print(dark)

Image.fromarray(dark).show()

# -----------------------------------
# Part 3: Image Negative
# -----------------------------------
negative = 255 - image

print("\nNegative Image Matrix:\n")
print(negative)

Image.fromarray(negative.astype(np.uint8)).show()

# -----------------------------------
# Part 4: Threshold Black/White
# -----------------------------------
threshold = np.where(image > 128, 255, 0)

print("\nThreshold Image Matrix:\n")
print(threshold)

Image.fromarray(threshold.astype(np.uint8)).show()

# -----------------------------------
# Part 5: Flip Image Horizontally
# -----------------------------------
flipped = np.fliplr(image)

print("\nFlipped Image Matrix:\n")
print(flipped)

Image.fromarray(flipped.astype(np.uint8)).show()