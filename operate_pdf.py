from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file = 'lidar.pdf'

pdf_object = PdfFileReader(pdf_file)
pdf_info = pdf_object.getDocumentInfo()
print('pdf_info:%s' % pdf_info)
pdf_pages = pdf_object.getNumPages()
print('pdf_pages:%s' % pdf_pages)
