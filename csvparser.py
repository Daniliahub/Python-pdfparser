import csv

class CsvParser():
	def __init__(self, filename):
		self.filename = filename

	def readCsv(self):
		# file = open(self.filename, 'r')
		# print(file.read())
		# file.close()

		# with open(self.filename) as f:
		# 	self.lines = f.readlines()
		
		# self.lines = [line.rstrip('\n') for line in open(self.filename)]

		with open(self.filename, 'r') as f:
			reader = csv.reader(f)
			self.lines = list(reader)
		self.length = len(self.lines)
		self.getSubjects()

	def getSubjects(self):
		# if 'GROUP' in self.lines[3]:
		del self.lines[self.length-2:self.length]
		del self.lines[0:4]
		# str_list = filter(None, self.lines)
		y = 0
		for line in self.lines:
			line = [x for x in self.lines[y] if x is not '']
			line = [x for x in line if x is not ' ']
			line = list(map(str.strip, line))
			self.lines[y] = line
			y+=1
		self.length = len(self.lines)
		self.printList()
		# else:
		# 	print('Error')

	def printList(self):
		print('\n'.join('{}: {}'.format(*k) for k in enumerate(self.lines)))
		print("Length: ",(self.length))

	# usage: findWholeWord('seek')('those who seek shall find')
	# def findWholeWord(self, word):
	# 	return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search

parse = CsvParser("StudentStudyLoad.csv")
parse.readCsv()