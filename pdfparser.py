import PyPDF2 as pypdf
# pip install pypdf2

class PdfParser():
	def __init__(self, filename):
		self.filename = filename
		print(self.filename)

	def readPdf(self):
		pdfFileObj = open(self.filename, 'rb')
		pdfReader = pypdf.PdfFileReader(pdfFileObj)
		pageObj = pdfReader.getPage(0)
		print(pdfReader.getDocumentInfo())
		# print(pageObj.extractText())

parse = PdfParser("StudentStudyLoad.pdf")
parse.readPdf()