from User import *
class Student(User):
	"""docstring for Student"""
	def __init__(self, _id, name, email, password, studentNumber, assigmentIds=[]):
		""" Constructor for Student object """
		super().__init__(name, email, password, studentNumber, "S", _id)
		self._assignmentIds = assigmentIds

	def insertStudent(self):
		super().insertUser()

	def addAssignment(self, assignmentId):
		self._assignmentIds.append(assignmentId)

	def getAssignmentIds(self):
		return self._assignmentIds