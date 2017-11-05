from User import *
from QuestionMake import *

class Professor(User):
	"""docstring for Professor"""
	def __init__(self, name, email, password, employeeNumber):
		""" Constructor for Professor object """
		super().__init__(name, email, password, employeeNumber, "P")
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
	
	def QuestionMake(self):
		QuestionMakeScreen()
