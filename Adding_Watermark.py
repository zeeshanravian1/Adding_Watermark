import PyPDF2
import sys


def add_watermark(original, watermark, output):
    for i in range(original.getNumPages()):
        page = original.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

    return output


original = PyPDF2.PdfFileReader(sys.argv[1])
watermark = PyPDF2.PdfFileReader(sys.argv[2])
output = PyPDF2.PdfFileWriter()

result = add_watermark(original, watermark, output)

with open('Watermarked_PDF.pdf', 'wb') as file:
    result.write(file)
