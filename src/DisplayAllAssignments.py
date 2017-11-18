from tkinter import *
from DisplayAssignment import *
import csv
import io

# display a new window 

def displayListOfAssignments(studentNum):
	""" Creates a window to display all assignments for a student and its 
	corresponding information. """
	root = Tk()
	# get the file with the name Assignment_studentNum
	filename = "Assignment_" + str(studentNum) + ".csv"
	studentFile = open(filename, "r")
	reader = csv.reader(studentFile)

	assignmentIdsList = []
	# create a list of distinct assignmentIDs
	for row in reader:
		# if the the IDs 
		if not (row[3] in assignmentIdsList):
			assignmentIdsList.append(row[3].strip())

	assignmentsInfo = []

	# parse the Assignment.csv to get information for an assignment based on its ID
	assignmentsFile = open("Assignment.csv", "r")
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
	studentFile.close()
	root.mainloop()

def createAssignmentLabels(root, studentNum, assignmentsInfo):
	""" Creates a label for each assignment displaying it's information and
	is stacked vertically. """

	# create dictionary to hold label : button for each assignment
	# button will take user to the specific assignment

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
	displayListOfAssignments(1)

