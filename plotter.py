import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hi_there = tk.Button(self)
		self.hi_there["text"] = "Read PDF"
		self.hi_there["command"] = self.parsePdf
		self.hi_there.pack(side="top")

		self.quit = tk.Button(self, text="QUIT", fg="red",
							command=root.destroy)
		self.quit.pack(side="bottom")

	def parsePdf(self):
		file = open('StudentStudyLoad.pdf', 'rb')
		# print(file.read())
		# towrite = open('file.txt', 'wb')
		# towrite.write(file.read())
		
		# pdfFileObj = open('StudentStudyLoad.pdf', 'rb')
		# pdfReader = pypdf.PdfFileReader(pdfFileObj)
		# print(pdfReader.numPages)
		# pageObj = pdfReader.getPage(0)
		# print(pageObj.extractText())

root = tk.Tk()
app = Application(master=root)
app.mainloop()