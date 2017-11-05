from User import *

class Professor(User):
	"""docstring for Professor"""
	def __init__(self, name, email, password, employeeNumber):
		""" Constructor for Professor object """
		super().__init__(name, email, password, employeeNumber, "P")
		self._courses = []

	def insertSelf(self):
		super().insertSelf("Professors.csv")

	def addCourse(self, courseName):
		self._courses.append(courseName)

	def removeCourse(self, courseName):
		if courseName in self._courses:
			self._courses.remove(courseName)

	def getAllCourses(self):
		return self._courses

	def signUpIndex(root,Title):
		""" Index page for the Profile Registration """

		header = Label(root, text=Title).grid(row=0,column=1)

		nameLabel = Label(root, text="Name:").grid(row=1)
		nameEntry = Entry(root, width=50)
		nameEntry.grid(row=1, column=1)

		emailLabel = Label(root, text="Email:").grid(row=2)
		emailEntry = Entry(root, width=50)
		emailEntry.grid(row=2, column=1)

		passwordLabel = Label(root, text="Password:").grid(row=3)
		passwordEntry = Entry(root, show="*", width=50)
		passwordEntry.grid(row=3, column=1)

		passwordDupLabel = Label(root, text="Confirm Password:").grid(row=4)
		passwordDupEntry = Entry(root, show="*", width=50)
		passwordDupEntry.grid(row=4, column=1)

		UserNumLabel = Label(root, text="Student Number:").grid(row=5)
		UserNumEntry = Entry(root, width=50)
		UserNumEntry.grid(row=5, column=1)

		submitBtn = Button(root, text="Submit", command = lambda: self.createSelf(root, nameEntry, emailEntry, passwordEntry, passwordDupEntry, studentNumEntry))
		submitBtn.grid(row=6, column=1)

		# set fixed window size
		root.resizable(width=False, height=False)
