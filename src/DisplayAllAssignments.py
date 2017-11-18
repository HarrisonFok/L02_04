from tkinter import *
from DisplayAssignment import *
from CheckUserType import *
import csv
import io

# display a new window 

def displayListOfAssignments(studentNum):
	""" Creates a window to display all assignments for a student and its 
	corresponding information. """
	studentCol = 8
	profCol = 7

	userType = checkUserType(studentNum)

	if (userType == 'S'):
		typeCol = studentCol
	else:
		typeCol = profCol

	root = Tk()
	assignmentIdsList = []
	assignmentsInfo = []

	# parse the Assignment.csv to get information for an assignment based on its ID
	assignmentsFile = open("Assignment.csv", "r")

	reader = csv.reader(assignmentsFile)

	# get all the student's assignments by ID
	for row in reader:
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
	createAssignmentLabels(root, studentNum, assignmentsInfo)
	# display the assignment name, due date and assignment ID
	assignmentsFile.close()
	root.mainloop()

def createAssignmentLabels(root, studentNum, assignmentsInfo):
	""" Creates a label for each assignment displaying it's information and
	is stacked vertically. """

	rowNum = 0
	# iterate through assignments
	for a in assignmentsInfo:
		info = "Assignment Name: " + a[1] + "\nDue Date: " + a[2]
		infoLabel = Label(root, text=info).grid(row=rowNum, column = 0)
		a_id = a[0]

		viewAssignmentBtn = Button(root, text="View", command = lambda a_id=a_id:displaySpecificAssignment(a_id, studentNum))
		viewAssignmentBtn.grid(row=rowNum, column = 1)
		rowNum+=1


def displaySpecificAssignment(assignmentId, studentNum):
	# launch window from DisplayAssignment.py
	displayMenu(studentNum, assignmentId)

if __name__ == "__main__":
	""" for testing when running from terminal """
	displayListOfAssignments(0)

