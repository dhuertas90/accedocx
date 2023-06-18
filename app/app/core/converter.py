from pdf2docx import Converter
from docx2pdf import convert

def converterPDF(pdf_file, docx_file):    
    """convert pdf to docx
    
    pdf_file = '/path/to/sample.pdf'
    docx_file = 'path/to/sample.docx'

    """
    
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()


def converterDOCX(pdf_file, docx_file):   
    """convert docx to pdf
    
    pdf_file = '/path/to/sample.pdf'
    docx_file = 'path/to/sample.docx'
    
    """
    
    convert(docx_file, pdf_file)