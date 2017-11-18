from tkinter import *
import csv
import io

def displayAssignmentWindow(root, studentNum, assignmentID):
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
	submitBtn = Button(root, text="Submit", command = lambda: getStudentAnswers(root, questionStudentAnsPair, studentNum, assignmentID))
	submitBtn.grid(row = rowNum)



def getStudentAnswers(root, questionStudentAnsPair, studentNum, assignmentID):
	""" This method replaces the values of the questionStudentAnsPair dictionary with the entries 
		in the form. """
	questionStudentAnsCopy = dict()
	for q in questionStudentAnsPair:
		q_body = q.cget("text")
		q_ans = questionStudentAnsPair[q].get().strip()
		questionStudentAnsCopy[q_body] = q_ans

	compareAnswers(root, questionStudentAnsCopy, studentNum, assignmentID)

def compareAnswers(root, questionStudentAnsPair, studentNum, assignmentID):
	""" Retrieves the answers from the entry fields and compares it against
	the correct answer. Also overwrites the answer.csv to store this latest
	attempt. """
	total = len(questionStudentAnsPair.keys())
	mark = 0
	# open Assignment.csv
	assignmentCSV = open("Assignment.csv", "r")
	assignmentReader = csv.reader(assignmentCSV)

	answersDict = dict()
	# create a dictionary to hold all the questions and answers
	for row in assignmentReader:
		if (row[4].strip() == str(assignmentID)):
			answersDict[row[2].strip()] = row[3].strip()
	# iterate through the value of the questionStudentAnsPair dictionary
	for q1 in questionStudentAnsPair:
		studentAns = questionStudentAnsPair[q1]
		for q2 in answersDict:
			if (answersDict[q1] == studentAns):
				mark+=1
				break
			

	numRows = len(questionStudentAnsPair)
	totalMark = Label(root, text="Your mark is: " + str(mark) + "/" + str(total)).grid(row = numRows + 2)
	# write to the assignment_studentNo file
	filename = "Assignment_" + str(studentNum) + ".csv"
	csvFileWrite = open(filename, "w")
	csvFileRead = open(filename, "r")
	writer = csv.writer(csvFileWrite)
	reader = csv.reader(csvFileRead)

	firstAttempt = True
	# updates the previous attempt stored in the .csv file
	for row in reader:
		if row[3] == assignmentID:
			firstAttempt = False
			# find that particular question and modify student's answer
			q = row[0].strip()
			# update the column with student's answer
			row[1] = questionStudentAnsPair[q]

	if (firstAttempt):
		# appends the most recent attempt to the csv file
		for q in questionStudentAnsPair:
			data = []
			data.append(q)
			data.append(questionStudentAnsPair[q])
			data.append(answersDict[q])
			data.append(assignmentID)
			# insert into the csv file
			writer.writerow(data)
	# close opened CSV files
	csvFileRead.close()
	csvFileWrite.close()
	assignmentCSV.close()


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

def displayMenu(studentNum, assignmentID):
	root = Tk()
	displayAssignmentWindow(root, studentNum, assignmentID)
	root.mainloop()



if __name__ == "__main__":
	# for testing
	displayMenu(1, 0)

