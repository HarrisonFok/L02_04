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
	submitBtn = Button(root, text="Submit", command = lambda: compareAnswers(questionStudentAnsPair))
	submitBtn.grid(row = rowNum)



def compareAnswers(questionStudentAnsPair):
	""" Retrieves the answers from the entry fields and compares it against
	the correct answer. Also overwrites the answer.csv to store this latest
	attempt. """

	# open Assignment.csv

	# iterate through the value of the questionStudentAnsPair dictionary

		# given the question body, find the correct answer in Assignment.csv

		# compare the answer with the entry value

	# keep track of how many questions were right and how many were wrong

		# call another method to display the results in another window


	pass

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

	csvFile.close()
	# return this list
	return questions

if __name__ == "__main__":
	root = Tk()
	displayAssignmentWindow(root, 1, 0)
	root.mainloop()
