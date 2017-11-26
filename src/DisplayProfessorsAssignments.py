from tkinter import *
from DisplayAllAssignments import *

def getProfessorsAssignments(user):
	""" displays the list of assignments for a professor. """
	displayListOfAssignments(user)


if __name__ == "__main__":
	""" used for testing """
	profId = 1
	getProfessorsAssignments(profId)
