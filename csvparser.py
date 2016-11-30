class CsvParser():
	def __init__(self, filename):
		self.filename = filename

	def readCsv(self):
		# file = open(self.filename, 'r')
		# print(file.read())
		# file.close()

		# with open(self.filename) as f:
		# 	self.lines = f.readlines()
		
		self.lines = [line.rstrip('\n') for line in open(self.filename)]
		self.length = len(self.lines)
		# print(self.lines)
		self.getSubject()

	def getSubject(self):
		if 'GROUP' in self.lines[3]:
			del self.lines[self.length-2:self.length]
			del self.lines[0:4]
			self.printList()
		else:
			print('Error')

	def printList(self):
		print('\n'.join('{}: {}'.format(*k) for k in enumerate(self.lines)))

	# usage: findWholeWord('seek')('those who seek shall find')
	# def findWholeWord(self, word):
	# 	return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search

parse = CsvParser("StudentStudyLoad.csv")
parse.readCsv()