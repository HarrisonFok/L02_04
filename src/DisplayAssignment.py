from tkinter import *

def displayAssignmentWindow(root, studentID, assignmentID):
	""" Displays the window for completing the assignment """

	header = Label(root, text="Answer the following questions.").grid(row=0)

	# get a list of assignments and display them
	assignments = getQuestionsFromAssignment(assignmentID)

def getQuestionsFromAssignment(assignmentID):
	""" Returns a list of questions for that assignment """
	''' Assume 1 file stores all questions'''

	# get the CSV file with all chosen assignment questions
	 csvFile = open("Assignment.csv", "r")
	 

	 # iterate through each row checking for the proper assignmentID

	 # create a question object and append it to the list

	 # return this list


if __name__ == "__main__":
	root = Tk()
	displayAssignmentWindow(root, 1)
	root.mainloop()
