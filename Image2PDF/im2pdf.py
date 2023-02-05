#combine images to pdf
import os
from PIL import Image

directory = r"<path>"

image_files = [file for file in os.listdir(directory) if file.endswith(".jpg") or file.endswith(".png")]
images = [Image.open(os.path.join(directory, file)) for file in image_files]

if images:
    images[0].save(os.path.join(directory, "combined.pdf"), save_all=True, append_images=images[1:])
