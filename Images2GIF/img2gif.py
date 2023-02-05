import os
from PIL import Image

# Get a list of all image filenames in the directory
image_filenames = [f for f in os.listdir(".") if f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".png")]

# Load all the images
images = [Image.open(f) for f in image_filenames]

# Save the images as an animated GIF
images[0].save("animated.gif", save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)
