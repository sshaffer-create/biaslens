from PyPDF2 import PdfReader, PdfWriter

pdf_file_path = r"C:\Users\shaff\Downloads\Python project - Module 3 and 4.pdf"

reader = PdfReader(pdf_file_path)
writer = PdfWriter()

for page_num in range(2,6):
    writer.add_page(reader.pages[page_num])

with open("newoutput.pdf", "wb") as out:
    writer.write(out)

print("PDF file has been split")

