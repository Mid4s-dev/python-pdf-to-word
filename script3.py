from pdf2docx import Converter
import os

# Accept input for directory path
path_input = input("Enter the directory path for PDF files: ")
path_output = input("Enter the directory path for output DOCX files: ")

# Scan directory for PDF files that can be converted
pdf_files = [file for file in os.listdir(path_input) if file.endswith('.pdf')]
print("The following PDF files can be converted:")
for i, file in enumerate(pdf_files):
    print(f"{i+1}. {file}")

# Prompt user to select files to convert
selection = input("Enter the numbers of the files you want to convert (separated by commas): ")
selected_files = [pdf_files[int(i)-1] for i in selection.split(',')]

# Convert selected files to DOCX
for file in selected_files:
    cv = Converter(os.path.join(path_input, file))
    cv.convert(os.path.join(path_output, file.replace('.pdf', '.docx')), start=0, end=None)
    cv.close()
    print(f"{file} converted successfully.")
