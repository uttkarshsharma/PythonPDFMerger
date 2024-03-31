import os
from PyPDF2 import PdfWriter, PdfReader

def merge_pdfs(directory=os.getcwd(), output_filename='outputfile.pdf'):
    pdf_files = []

    # Find all PDF files in the specified directory and its subdirectories
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, filename))

    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    # Sort the list of PDF files alphabetically
    pdf_files.sort(key=str.lower)

    # Create a PdfWriter object to write the merged PDF
    pdf_writer = PdfWriter()

    # Iterate over each PDF file, read its content, and add it to the PdfWriter
    for pdf_file in pdf_files:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    # Prompt the user for the desired output filename
    user_output_filename = input("Enter the desired output filename (without extension): ").strip()
    if not user_output_filename:
        user_output_filename = output_filename
    else:
        user_output_filename += ".pdf"

    # Write the merged PDF to the user-specified output file
    with open(user_output_filename, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f"Merged {len(pdf_files)} PDF files into '{user_output_filename}'.")

# Example usage:
merge_pdfs()
