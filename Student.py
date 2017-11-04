from User import *
class Student(User):
	"""docstring for Student"""
	def __init__(self, name, email, password, studentNumber):
		""" Constructor for Student object """
		super().__init__(name, email, password, studentNumber, "S")
	
	def insertStudent(self):
		super().insertUser()