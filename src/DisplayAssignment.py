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

	# compare answers if the submit button is clicked
	submitBtn = Button(root, text="Submit", command = lambda: getStudentAnswers(questionStudentAnsPair))
	submitBtn.grid(row = rowNum)



def getStudentAnswers(questionStudentAnsPair):
	""" This method replaces the values of the questionStudentAnsPair dictionary with the entries 
		in the form. """
	questionStudentAnsCopy = questionStudentAnsPair.copy()
	# replace the entry with the student's answer
	for question in questionStudentAnsCopy:
		tempAnswer = questionStudentAnsCopy[question].get().strip()
		questionStudentAnsCopy[question] = tempAnswer

	compareAnswers(questionStudentAnsCopy)

def compareAnswers(questionStudentAnsPair):
	""" Retrieves the answers from the entry fields and compares it against
	the correct answer. Also overwrites the answer.csv to store this latest
	attempt. """
	total = len(questionStudentAnsPair.keys())
	mark = 0
	# open Assignment.csv
	assignmentCSV = open("Assignment.csv", "r")
	assignmentReader = csv.reader(assignmentCSV)

	# iterate through the value of the questionStudentAnsPair dictionary
	for q in questionStudentAnsPair:
		studentAns = questionStudentAnsPair[q]
		for row in assignmentReader:
			if (row[3].strip() == studentAns.strip()):
				mark+=1
				break

	numRows = len(questionStudentAnsPair)
	totalMark = Label(root, text="Your mark is: " + str(mark) + "/" + str(total)).grid(row = numRows + 2)

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
		assignmentIdColumn = 4
		questionBodyColumn = 2
		# append it to the list
		if (line[assignmentIdColumn] == str(assignmentID)):
			questions.append(line[questionBodyColumn])

	csvFile.close()
	# return this list
	return questions

root = Tk()
displayAssignmentWindow(root, 1, 0)
root.mainloop()
