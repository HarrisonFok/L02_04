import io
import csv

class User(object):
	"""docstring for User"""
	def __init__(self, name, email, password, personnelNumber, userType, _id=None):
		""" Constructor for Student object """
		self._name = name
		self._email = email
		self._password = password
		self._personnelNumber = personnelNumber
		self._type = userType
		if _id is None:
			self._id = int(self.getLatestId())
		else:
			self._id = _id

	# getters and setters for class attributes
	def getName(self):
		return self._name

	def setName(self, name):
		self._name = name

	def getEmail(self):
		return self._email

	def setEmail(self, email):
		self._email = email

	def getPassword(self):
		return self._password

	def setPassword(self, password):
		self._password = password

	def getPersonnelNumber(self):
		return self._personnelNumber

	def setPersonnelNumber(self, pn):
		self._personnelNumber = pn

	def getType(self):
		return self._type
	
	def getId(self):
		return self._id

	# CSV HELPER METHODS
	def insertUser(self):
		""" Inserts student's information into the CSV file """
		# prepare data
		data = []
		data.append(self.getId())
		data.append(self.getName())
		data.append(self.getEmail())
		data.append(self.getPassword())
		data.append(self.getPersonnelNumber())
		data.append(self.getType())
		# insert data into the csv file
		csv_file = open("Users.csv", "a")
		writer = csv.writer(csv_file)
		writer.writerow(data)
		csv_file.close()

	def getLatestId(self):
		""" Returns the last student ID in the csv file. """
		csv_file = open("Users.csv", "r")
		reader = csv.reader(csv_file)
		# else, calculate the number of rows
		rowCount = len(list(reader))
		# close CSV file
		csv_file.close()
		return rowCount
