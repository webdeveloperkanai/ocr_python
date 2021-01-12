import PyPDF2

name = input("Enter pdf name and it should be in same dir : ")
book = open(name, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print('Total Pages : ',pages)

no = int(input("Enter ocr page : "))
dname = input("Enter ocr document name  : ")

flname = dname+'.txt'
print('file name : ', flname)

fpage = pdfReader.getPage(no)
fullText = fpage.extractText()
file = open(flname, 'w')
file.write(fullText)
file.close()
print("Document Created ")
