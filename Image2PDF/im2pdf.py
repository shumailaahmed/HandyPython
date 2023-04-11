#combine images to pdf
import os
from PIL import Image

directory = r"."
images_new=[]
image_files = [file for file in os.listdir(directory) if file.endswith(".jpg") or file.endswith(".png")]
images = [Image.open(os.path.join(directory, file)) for file in image_files]
for image in images:
    if image.mode == 'RGBA':
                image = image.convert('RGB')
    images_new.append(image)
if images_new:
    images_new[0].save(os.path.join(directory, "combined.pdf"), save_all=True, append_images=images_new[1:])
