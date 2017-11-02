import io
import csv

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, email, password, studentNumber):
		""" Constructor for Student object """
		self._name = name
		self._email = email
		self._password = password
		self._studentNumber = studentNumber
		self._type = "S"

	# getters and setters for class attributes
	def getName(self):
		return self._name

	def setName(self, name):
		this._name = name

	def getEmail(self):
		return self._email

	def setEmail(self, email):
		this._email = email

	def getPassword(self):
		return self._password

	def setPassword(self, password):
		this._password = password

	def getStudentNumber(self):
		return self._studentNumber

	def setStudentNumber(self, sn):
		this._studentNumber = sn

	def getType(self):
		return self._type

	def insertStudent(self):
		""" Inserts student's information into the CSV file """
		# prepare data
		data = []
		data.append(self.getName())
		data.append(self.getEmail())
		data.append(self.getPassword())
		data.append(self.getStudentNumber())
		data.append(self.getType())
		# insert data into the csv file
		csv_file = open("Students.csv", "a")
		writer = csv.writer(csv_file)
		writer.writerow(data)
		csv_file.close()


