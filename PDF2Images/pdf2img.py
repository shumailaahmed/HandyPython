import fitz
import os

pdf_directory = "."
image_directory = "images"

# Create the image directory if it doesn't exist
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# Iterate through all PDF files in the directory
for pdf_file in os.listdir(pdf_directory):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, pdf_file)
        doc = fitz.open(pdf_path)

        # Create a subdirectory for the current PDF file
        pdf_name = pdf_file.rsplit(".", 1)[0]
        pdf_image_directory = os.path.join(image_directory, pdf_name)
        if not os.path.exists(pdf_image_directory):
            os.makedirs(pdf_image_directory)

        # Iterate through all pages of the PDF file
        for i in range(len(doc)):
            page = doc[i]
            pix = page.get_pixmap()
            image_name = f"{pdf_name}_page_{i + 1}.png"
            image_path = os.path.join(pdf_image_directory, image_name)
            pix.save(image_path)
