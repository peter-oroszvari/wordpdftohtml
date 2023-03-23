from io import StringIO
from bs4 import BeautifulSoup

from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

# Set the path to the input PDF file
pdf_file_path = 'pdf-sample.pdf'

# Set the path to the output HTML file
html_file_path = 'output_pdf.html'

# Set up the PDF to HTML converter
output_string = StringIO()
manager = PDFResourceManager()
converter = HTMLConverter(manager, output_string, laparams=LAParams())
interpreter = PDFPageInterpreter(manager, converter)

# Convert each page of the PDF to HTML
with open(pdf_file_path, 'rb') as infile:
    for page in PDFPage.get_pages(infile):
        interpreter.process_page(page)

# Clean up the HTML using BeautifulSoup
soup = BeautifulSoup(output_string.getvalue(), 'html.parser')
for tag in soup(['span', 'div']):
    tag.unwrap()

# Save the cleaned-up HTML to a file
with open(html_file_path, 'w') as outfile:
    outfile.write(str(soup))