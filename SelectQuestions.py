# MCQ - multiple choice
# FIB - fill in blanks
# The assignment creates one for each student

try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk
    
import random
import io
import csv

from randomalgo import *

class SelectQuestions(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self._label = tk.Label(self, text="WELCOME!!\nPlease choose questions \
to appear on an assignment\n", font=("Helvetica", 32))
        self._label.pack()

        self._display_button = tk.Button(self, text="Display Questions", \
                                        command=self.display)
        self._display_button.pack()

        self._entry = tk.Entry(self)
        self._assignmentWindow = None
        
        # This will be the list of chosen question formulas
        self._chosenQuestionFormulas = []
        
        self._handInBut = None
        
        self._label = None
        self._labels = []
        
        self._numCorrect = 0
        self._numQuestions = 0
        
        self.assignment = None

    def display(self):
        # Read all the question formulas in questions.csv and display them to
        # the screen
        with open("questions.csv", "r") as csvFile:
            reader = csv.reader(csvFile, delimiter="\n")
            for row in reader:
                splitRow = row[0].split(',')
                self.singleQuestion = tk.Label(self, text=splitRow[0] + ":" + \
                                               splitRow[3],\
                                               font=("Helvetica", 28))
                self.singleQuestion.pack()
                
            tk.Button(self, text="Submit", command=self.create_window).pack()
    
            self._entry.pack()
            
            self.display_button.config(state = 'disabled')

    def create_window(self):
        # Create a new window for the assignment
        self._assignmentWindow = tk.Toplevel(self)
        root.withdraw()
        self._assignmentWindow.wm_title("ASSIGNMENT")
        
        # Get the user input
        chosenQuestionNums = self._entry.get()
        questionNumChosen = chosenQuestionNums.split(',')
        chosenQ = []
        for qNumWithSpace in questionNumChosen:
            qNum = qNumWithSpace.replace(' ','')
            chosenQ.append(qNum)
        
        # Get the chosen question formulas and append to the list
        # self._chosenQuestionFormulas
        with open("questions.csv", "r") as csvFile:
            for lineList in csv.reader(csvFile):
                # if the question is one of the chosen questions, then add it
                # to self._chosenQuestionFormulas
                if lineList[0] in chosenQ:
                    self._chosenQuestionFormulas.append(lineList)
        
        # Make an assignment and store it inside Assignment.csv (using the
        # function in randomalgo.py)
        self.assignment = makeAssignment(self._chosenQuestionFormulas)
        
        # Read from Assignment.csv and display the questions to the window
        listOfQ = self.assignment.getListOfQuestions()
        self._numQuestions = len(listOfQ)
        for question in listOfQ:
            questionEntry = tk.Label(self._assignmentWindow, \
                                     text=question.getQuestion(), \
                                     font=("Helvetica", 28))
            questionEntry.pack()

        self._handInBut = tk.Button(self._assignmentWindow, text="Hand in", \
                  font=("Helvetica", 28), command=self.validate)
        self._handInBut.pack()
        
        self.assignmentAnswersEntry = tk.Entry(self._assignmentWindow, \
                                              font=("Helvetica", 28))
        self.assignmentAnswersEntry.pack()

    def validate(self):
        assignmentAnswers = self.assignmentAnswersEntry.get()
        assignmentAnswersList = [x.strip() for x in \
                                 assignmentAnswers.split(',')]
        questionsWithStudentAnswers = []
        
        # Update the Question objects in the Assignment object
        for i in range(len(assignmentAnswersList)):
            for j in range(self.assignment.getNumQuestions()):
                if i == j:
                    self.assignment.\
                        setStudentAnswerAtIndex(j, assignmentAnswersList[i])
        
        # Create a new spreadsheet that stores only the question and the
        # student answer
        assignmentFileName = "assignment_"+ \
            str(self.assignment.getAssignmentId()) + ".csv"
        
        questionAnswerCorrectness = []
        
        with open(assignmentFileName, 'w') as assignmentFile:
            for question in self.assignment.getListOfQuestions():
                questionAnswerCorrectness.append([question.getStudentAnswer(),\
                                           question.getAnswer()])
            writer = csv.writer(assignmentFile)
            writer.writerows(questionAnswerCorrectness)
        
        # For every student answer in assignmentAnswersList, compare them with
        # the answers. If the student didn't answer all the questions, it would
        # still output "WRONG"
        listOfQ = self.assignment.getListOfQuestions()
        for question in listOfQ:
            # if the student answer is correct, output "CORRECT"
            if int(question.getStudentAnswer()) == question.getAnswer():
                self._numCorrect += 1
                question.setCorrectness(True)
                self._label = tk.Label(self._assignmentWindow, \
                                             text="CORRECT")
                self._label.after(1000, self.clear_labels)
                self._label.pack()
                self._labels.append(self._label)

                # if the student got perfect, then disable the hand in button
                # and output the grade
                if self.assignment.checkIfPerfect():
                    self._handInBut.config(state='disabled')
                    tk.Label(self._assignmentWindow, text=str(self._numCorrect)\
                             + "/" + str(self._numQuestions)).pack()               
            # if the student answers are incorrect, output "WRONG"
            else:
                self._label = tk.Label(self._assignmentWindow, \
                                               text="WRONG")
                self._label.after(1000, self.clear_labels)
                self._label.pack()
                self._labels.append(self._label)
                
    def clear_labels(self):
        for label in self._labels:
            label.destroy()
        
root = tk.Tk()
root.geometry('%sx%s' % (2000, 2000))
main = SelectQuestions(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()