import io
import csv

class User(object):
	"""docstring for User"""
	def __init__(self, name="", email="", password="", personnelNumber="", userType=""):
		""" Constructor for Student object """
		self._name = name
		self._email = email
		self._password = password
		self._personnelNumber = personnelNumber
		self._type = userType
		self._id = int(self.getLatestId())
		self._fi = self.FileNameMake()

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

	def getPersonnelNumber(self):
		return self._personnelNumber

	def setPersonnelNumber(self, pn):
		this._personnelNumber = pn

	def setAll(self, name, email, password, personnelNumber):
		self._name = name
		self._email = email
		self._password = password
		self._personnelNumber = personnelNumber

	def getType(self):
		return self._type

	def getId(self):
		return self._id

	# CSV HELPER METHODS

	def FileNameMake():
		return (str(self.__class__)[8:-2] + ".csv")

	def insertSelf(self, file):
		""" Inserts user's information into their CSV file """
		# prepare data
		data = []
		data.append(self.getId())
		data.append(self.getName())
		data.append(self.getEmail())
		data.append(self.getPassword())
		data.append(self.getPersonnelNumber())
		data.append(self.getType())
		# insert data into the csv file
		csv_file = open(self.fi, "a")
		writer = csv.writer(csv_file)
		writer.writerow(data)
		csv_file.close()

	def getLatestId(self):
		""" Returns the last user ID in their csv file. """
		csv_file = open(self._fi , "r")
		reader = csv.reader(csv_file)
		# else, calculate the number of rows
		rowCount = len(list(reader))
		# close CSV file
		csv_file.close()
		return rowCount

	def createSelf(self):
		""" Insert self into its proper .csv file """
		name = nameEntry.get()
		email = emailEntry.get()
		pwd = passwordEntry.get()
		pwdDup = passwordDupEntry.get()
		UserNum = UserNumEntry.get()

		resultLabel = Label(root, text="")
		resultLabel.grid(row=8, column=1)

		# check if fields are empty
		if entriesEmpty:
			resultLabel.config(text="One or more fields are empty.")
		else:
			if matchPasswords(pwd, pwdDup):

				# Set User object's information
				self.setAll(namename, email, pwd, UserNum)
				resultLabel.config(text="Profile Successfully Created!")

				# insert into CSV
				self.insertSelf()

				# clear fields
				nameEntry.delete(0, 'end')
				emailEntry.delete(0, 'end')
				passwordEntry.delete(0, 'end')
				passwordDupEntry.delete(0, 'end')
				UserNumEntry.delete(0, 'end')

			else:
				resultLabel.config(text="Passwords don't match")

	def matchPasswords(pwd, pwdDup):
		""" Returns true iff the password and confirm password fields match """
		return (pwd == pwdDup)

	def entryIsEmpty(entry):
		""" Returns true iff a field is empty """
		return (len(entry) == 0)

	def entriesEmpty():
		""" Returns true iff any field is empty """
		return (entryIsEmpty(name) or entryIsEmpty(email) or entryIsEmpty(pwd)
		    or entryIsEmpty(pwdDup) or entryIsEmpty(studentNum))

	def displayProfile(root, user):
		""" Display the information about a user in a window with these widgets. """
		nameLabel = Label(root, text="Name: " + user.getName()).pack()
		emailLabel = Label(root, text="Email: " + user.getEmail()).pack()
		UserNumLabel = Label(root, text="Student Number: " + user.getPersonnelNumber()).pack()
