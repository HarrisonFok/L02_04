from tkinter import *
import csv

def displayAssignmentWindow(root, studentID, assignmentID):
	""" Displays the window for completing the assignment """

	header = Label(root, text="Answer the following questions.").grid(row=0)

	# get a list of assignments and display them
	questions = getQuestionsFromAssignment(assignmentID)

	# dictionary to store the label to display the question and the entry for student's answer
	questionStudentAnsPair = dict()

	# print out each question vertically with a textbox beside each question
	for q in questions:
		# create a label
		questionLabel = Label(root, text=q)
		answerEntry = Entry(root, width=50)
		questionStudentAnsPair[questionLabel] = answerEntry
	
	# display the question body along with a field to answer it
	rowNum = 1
	for questionBody in questionStudentAnsPair:
		questionBody.grid(row=rowNum, column = 0)
		questionStudentAnsPair[questionBody].grid(row = rowNum, column = 1)
		rowNum+=1

	submitBtn = Button(root, text="Submit").grid(row = rowNum)


def getQuestionsFromAssignment(assignmentID):
	""" Returns a list of questions for that assignment """
	''' Assume 1 file stores all questions'''

	# get the CSV file with all chosen assignment questions
	csvFile = open("Assignment.csv", "r")
	reader = csv.reader(csvFile)
	questions = []
	# iterate through each row checking for the proper assignmentID
	for line in reader:
		# check if question belongs to assignmentID
		assignmentIdColumn = 5
		questionBodyColumn = 2
		# append it to the list
		if (line[assignmentIdColumn] == str(assignmentID)):

			questions.append(line[questionBodyColumn])

	# return this list
	return questions

if __name__ == "__main__":
	root = Tk()
	displayAssignmentWindow(root, 1, 0)
	root.mainloop()
