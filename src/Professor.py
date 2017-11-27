from User import *

class Professor(User):
	"""docstring for Professor"""
	def __init__(self, name, email, password, employeeNumber, _id=None):
		""" Constructor for Professor object """
		super().__init__(name, email, password, employeeNumber, "P", _id)
		self._courses = []

	def insertProfessor(self):
		super().insertUser()

	def addCourse(self, courseName):
		self._courses.append(courseName)

	def removeCourse(self, courseName):
		if courseName in self._courses:
			self._courses.remove(courseName)

	def getAllCourses(self):
		return self._courses