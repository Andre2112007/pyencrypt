import tkinter 
from PyPDF2 import PdfFileReader, PdfFileWriter
from tkinter import filedialog
        
def encrypt_pdf(filename=filedialog.askopenfile().name):
    pdf_reader = PdfFileReader(filename)
    pdf_writer = PdfFileWriter()
    
    password = input("Type password\n")
    
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, use_128bit=True)
    
    with open(filename + ".encrypted.pdf", 'wb') as out:
        pdf_writer.write(out)
        
    print("Done!")
        
encrypt_pdf()