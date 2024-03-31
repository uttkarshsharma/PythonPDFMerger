# PDF Merger Python Program

This Python script merges all PDF files found within the current working directory and its subdirectories into a single PDF file named "outputfile.pdf". Here's how the script works:
1. It imports necessary modules: os for file operations and PyPDF2 for working with PDF files.
2. It initializes an empty list pdfFiles to store paths of PDF files found in the directory.
3. It traverses through the current working directory and its subdirectories using os.walk(), and for each file found, it checks if the file has a ".pdf" extension. If it does, it adds the file's path to the pdfFiles list.
4. It sorts the pdfFiles list alphabetically (case-insensitive).
5. It initializes a PdfWriter object from PyPDF2.
6. It iterates over each PDF file in the pdfFiles list:
7. Opens the PDF file in binary read mode.
8. Initializes a PdfReader object from PyPDF2.
9. Iterates over each page in the PDF and adds it to the pdfWriter object.
10. After iterating through all PDF files, it opens a new PDF file named "sbi.pdf" in binary write mode.
11. It writes the content of the pdfWriter object (which contains all pages from the input PDF files) to the output PDF file.

Finally, it closes the output PDF file.

This script effectively merges multiple PDF files into one, consolidating their contents into a single PDF document.
