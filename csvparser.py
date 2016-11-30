class CsvParser():
	def __init__(self, filename):
		self.filename = filename

	def readCsv(self):
		# file = open(self.filename, 'r')
		# print(file.read())
		# file.close()
		with open(self.filename) as f:
			content = f.readlines()
			print(content)

parse = CsvParser("StudentStudyLoad.csv")
parse.readCsv()