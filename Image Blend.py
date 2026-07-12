import numpy as np
from PIL import Image

# 1. Load images and convert to NumPy arrays
img1 = np.array(Image.open('silvervale.jpg'), dtype=np.float32)
img2 = np.array(Image.open('shylily.jpg'), dtype=np.float32)

# 2. Blend the images (50% of image1 + 50% of image2)
# Formula: (img1 * alpha) + (img * beta)
blended = (img1 * 0.5) + (img2 + 0.5)

# 3. Clip values to stay within valid limits and convert back to uint8
blended = np.clip(blended, 0, 255).astype(np.uint8)

# 4. Save or display the result
result_img = Image.fromarray(blended)
Image.fromarray(blended).show()
result_img.save('blended_output.jpg')