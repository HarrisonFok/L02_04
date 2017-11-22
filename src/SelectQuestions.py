# MCQ - multiple choice
# FIB - fill in blanks
# The assignment creates one for each student

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

        self._display_button = tk.Button(self, text="Display Questions", command=self.display)
        self._display_button.pack()

        self._entry = tk.Entry(self)
        self.assignmentWindow = None
        
        # This will be the list of chosen question formulas
        self._chosenQuestionFormulas = []
        
        self._handInBut = None
        
        self._label = None
        self._labels = []
        
        self._numCorrect = 0
        self._numQuestions = 0
        
        self._assignment = None

    def display(self):
        # Read all the question formulas in questions.csv and display them to
        # the screen
        with open("questions.csv", "rU") as csvFile:
            reader = csv.reader(csvFile, delimiter="\n", dialect=csv.excel_tab)
            for row in reader:
                splitRow = row[0].split(',')
                self.singleQuestion = tk.Label(self, text=splitRow[0] + ":" + \
                                               splitRow[3],\
                                               font=("Helvetica", 28))
                self.singleQuestion.pack()
                
            tk.Button(self, text="Submit", command=self.create_window).pack()
    
            self._entry.pack()
            
            self._display_button.config(state = 'disabled')

    def create_window(self):
        # Create a new window for the assignment
        self.assignmentWindow = tk.Toplevel(self)
        self.assignmentWindow.wm_title("ASSIGNMENT")
        
        # Get the user input
        chosenQuestionNums = self._entry.get()
        questionNumChosen = chosenQuestionNums.split(',')
        chosenQ = []
        for qNumWithSpace in questionNumChosen:
            qNum = qNumWithSpace.replace(' ','')
            chosenQ.append(qNum)

        tk.Label(self.assignmentWindow, text="These are the questions created on the\
assignment:\n", font=("Times New Romans", 30)).pack()
        
        # Get the chosen question formulas and append to the list
        # self._chosenQuestionFormulas
        with open("questions.csv", "rU") as csvFile:
            for lineList in csv.reader(csvFile):
                # if the question is one of the chosen questions, then add it
                # to self._chosenQuestionFormulas
                if lineList[0] in chosenQ:
                    self._chosenQuestionFormulas.append(lineList)
        
        # Make an assignment and store it inside Assignment.csv (using the
        # function in randomalgo.py)
        self._assignment = makeAssignment(self._chosenQuestionFormulas)
        
        # Read from Assignment.csv and display the questions to the window
        listOfQ = self._assignment.getListOfQuestions()
        self._numQuestions = len(listOfQ)
        for question in listOfQ:
            questionEntry = tk.Label(self.assignmentWindow, \
                                     text=question.getQuestion(), \
                                     font=("Helvetica", 28))
            questionEntry.pack()

        tk.Button(self.assignmentWindow, text="Close", command=self.destroyWindows).pack()

    def destroyWindows(self):
        self.assignmentWindow.destroy()
        self.destroy()

root = tk.Tk()
main = SelectQuestions(root)
main.pack(side="top", expand=True)
root.mainloop()