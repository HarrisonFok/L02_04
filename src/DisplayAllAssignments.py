from tkinter import *
from DisplayAssignment import *
from CheckUserType import *
from Quit import *
import SelectQuestions
import csv
import io
import os

# display a new window

def displayListOfAssignments(usr):
	""" Creates a window to display all assignments for a student and its 
	corresponding information. """

	# declare a global variable for the current user
	global user
	user = usr

	studentCol = 8
	profCol = 7
	studentNum = user.getId()

	userType = checkUserType(studentNum)

	if userType == 'S': 
		typeCol = studentCol
		studentNum = user.getPersonnelNumber()
	else:
		typeCol = profCol

	root = Tk()
	root.attributes('-topmost', 'true')
	assignmentIdsList = []
	assignmentsInfo = []

	# parse the Assignment.csv to get information for an assignment based on its ID
	assignmentsFile = open("Assignment.csv", "r")

	reader = csv.reader(assignmentsFile)

	# get all the student's assignments by ID
	for row in reader:
		print("row", row)
		if row[typeCol].strip() == str(studentNum):
			if not (row[4].strip() in assignmentIdsList):
				assignmentIdsList.append(row[4].strip())

	# reset the reader
	assignmentsFile.seek(0)
	reader = csv.reader(assignmentsFile)
	
	for assignmentId in assignmentIdsList:
		# reset the reader
		assignmentsFile.seek(0)
		reader = csv.reader(assignmentsFile)

		for row in reader:
			if row[4].strip() == assignmentId:
				tempValues = []
				tempValues.append(assignmentId)
				# append the assignment name
				tempValues.append(row[5].strip())
				# append the due date
				tempValues.append(row[6].strip())
				assignmentsInfo.append(tempValues)
				break

	# create the necessary labels on the window
	createAssignmentLabels(root, studentNum, assignmentsInfo, userType)
	# display the assignment name, due date and assignment ID
	assignmentsFile.close()
	root.mainloop()

def createAssignmentLabels(root, studentNum, assignmentsInfo, userType):
	""" Creates a label for each assignment displaying it's information and
	is stacked vertically. """

	rowNum = 0
	# iterate through assignments
	for a in assignmentsInfo:
		info = "Assignment Name: " + a[1] + "\nDue Date: " + a[2]
		infoLabel = Label(root, text=info).grid(row=rowNum, column = 0)
		a_id = a[0]

		viewAssignmentBtn = Button(root, text="View", command = lambda a_id=a_id:displaySpecificAssignment(a_id, studentNum, userType))
		viewAssignmentBtn.grid(row=rowNum, column = 1)
		rowNum+=1

	# add button for creating a new assignment if it's a prof
	if userType == 'P':
		Button(root, text="Create new assignment", command= lambda: callMakeAssignments(root, user)).grid(row=rowNum, column=0)

	Button(root, text="Back", command = lambda:quit(root, user)).grid(row = rowNum, column=1)


def displaySpecificAssignment(assignmentId, studentNum, userType):
	# launch window from DisplayAssignment.py
	displayMenu(studentNum, assignmentId, userType)

def callMakeAssignments(root, user):
	root.destroy()
	SelectQuestions.runSelectQuestions(user)

