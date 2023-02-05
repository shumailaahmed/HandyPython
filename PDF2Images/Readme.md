This script uses the fitz library to extract the image data from each PDF file, and the os library to access the file system. 

The script first creates the image directory if it doesn't exist, and then iterates through all PDF files in the pdfs directory. 

For each PDF file, the script creates a subdirectory with the same name as the PDF file (without the ".pdf" extension), and then iterates through all pages of the PDF file.

For each page, the script extracts the image data and saves it as a separate PNG file with a naming convention of <pdf_name>_page_<page_number>.png.
