import PyPDF2
import os

def merge_pdfs(pdf_list, output):
    pdf_merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        with open(pdf, 'rb') as file:
            pdf_merger.append(file)
    with open(output, 'wb') as file:
        pdf_merger.write(file)

if __name__ == '__main__':
    pdf_files = [f for f in os.listdir() if f.endswith('.pdf')]
    merge_pdfs(pdf_files, 'merged.pdf')
