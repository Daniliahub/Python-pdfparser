import csv
from datetime import datetime, timedelta

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
		with open(self.filename+"csv", 'r') as f:
			reader = csv.reader(f)
			self.lines = list(reader)
		self.length = len(self.lines)
		self.buildSubjects()

	def buildSubjects(self):
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
		if self.length % 2 == 0:
			# self.printList(self.lines, self.length)
			self.buildSched()
		else:
			print('Error. Incorrect Processing of Subjects')

	def buildSched(self):
		self.subjs = []
		y = 0
		for line in self.lines:
			index = self.lines.index(line)
			if index % 2 == 0:
				self.subjs.append([line[1]])
			else:
				(self.subjs[y]).append(line[0])
				y += 1
		for subj in self.subjs:
			# self.subjs[0][1] = self.subjs[0][1].split('  ')
			(subj).extend(subj[1].split('  '))
			del subj[1]
		self.subjsLen = len(self.subjs)
		self.dispSched()

	def dispSched(self):
		# subj[0] - Class Code
		# subj[1] - Days
		# subj[2][0] - Start time
		# subj[2][1] - End time
		# subj[2][2] - Number of 30 minute intervals
		# subj[3] - Class Location
		dates = [['M','Monday'],['T','Tuesday'],['W','Wednesday'],['Th','Thursday'],['F','Friday'],['Sat','Saturday']]
		str = "<table><tr><th>Time</th><th>Monday</th><th>Tuesday</th><th>Wednesday</th><th>Thursday</th><th>Friday</th><th>Saturday</th></tr>"
		for subj in self.subjs:
			subj[2] = subj[2].split(' - ')
			date = [datetime.strptime(subj[2][0],"%I:%M %p"), datetime.strptime(subj[2][1],"%I:%M %p")]
			# print(date[0].time()," ",date[1].time())
			diff = date[1] - date[0]
			diff = diff/30
			diff = (diff.seconds//60)%60
			(subj[2]).append(diff)
		timeval = datetime.strptime("07:30","%H:%M")
		y = timedelta(0, 1800)
		for x in range(1, 26):
			# print(timeval.time()," ",x)
			str += "<tr><td>"+timeval.strftime("%I:%M %p")+"</td>"
			for subj in self.subjs:
				if timeval.time() == datetime.strptime(subj[2][0],"%I:%M %p").time():
					# print(subj[2][0],' ')
					for date in dates:
						if subj[1] == date:
							pass
					pass
				else:
					pass
			str += "</tr>"
			timeval += y
			# print(timeval.strftime("%I:%M %p"))
			# subj[2][1] = subj[2][1].replace(" PM","")
		self.printList(self.subjs, self.subjsLen)

	def printList(self, list, length):
		print('\n'.join('{}: {}'.format(*k) for k in enumerate(list)))
		print("Length: ",(length))

	# usage: findWholeWord('seek')('those who seek shall find')
	# def findWholeWord(self, word):
	# 	return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search

parse = CsvParser("StudentStudyLoad.")
parse.readCsv()