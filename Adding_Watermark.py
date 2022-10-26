import PyPDF2
import sys


original = PyPDF2.PdfFileReader(sys.argv[1])
watermark = PyPDF2.PdfFileReader(sys.argv[2])
output = PyPDF2.PdfFileWriter()

for i in range(original.getNumPages()):
    page = original.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('Watermarked_PDF.pdf', 'wb') as file:
    output.write(file)