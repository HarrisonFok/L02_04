from tkinter import *
from CheckUserType import *
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

	userType = checkUserType(studentNum)
	# if user is a student, show this button.
	if userType == 'S':
		submitBtn = Button(root, text="Submit", command = lambda: getStudentAnswers(root, questionStudentAnsPair, studentNum, assignmentID))
	else:
		submitBtn = Button(root, text="Submit", state=DISABLED)
	# if user is a prof, don't allow for submission
	# compare answers if the submit button is clicked
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
	# CHANGING THE VALUES INLINE. IE. if the question has been answered before
	r = csv.reader(open(filename, "r"))
	lines = [l for l in r]
	found = False
	for line in lines:
		print("assignmentID", assignmentID)
		print("row[3]", line[3])
		print((line[3].strip()) == str(assignmentID))
		print(line)
		if (line[3].strip()) == str(assignmentID):
			found = True
			line[1] = questionStudentAnsPair[line[0].strip()]
		print(line)

	writer = csv.writer(open(filename, "w"))
	writer.writerows(lines)

	# if this is a new question, just append it to the end of the file
	if not (found):
		for q in questionStudentAnsPair:
			writer = csv.writer(open(filename, "a"))
			newAns = []
			newAns.append(q)
			newAns.append(questionStudentAnsPair[q])
			newAns.append(answersDict[q])
			newAns.append(assignmentID)
			# write to the file
			writer.writerow(newAns)

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

