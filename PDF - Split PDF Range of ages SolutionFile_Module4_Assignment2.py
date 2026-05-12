#You are writing a Python Program to create an application
#that will split a PDF file to create a new file that has contents
#from continuous pages such as pages starting from
#110 to 215 from our original PDF file.
from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_file_path = 'file1.pdf'
pdf = PdfFileReader(pdf_file_path)

pdfwriter = PdfFileWriter()

for page_num in range(2,6):
    pdfwriter.addPage(pdf.getPage(page_num))

with open('newoutput.pdf', 'wb') as out:
    pdfwriter.write(out)

print('PDF file has been split')