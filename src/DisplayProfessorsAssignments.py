from tkinter import *
from DisplayAllAssignments import *

def getProfessorsAssignments(profId):
	print("profId", profId)
	displayListOfAssignments(profId)


if __name__ == "__main__":
	profId = 1
	getProfessorsAssignments(profId)
