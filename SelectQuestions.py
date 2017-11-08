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

        self.label = tk.Label(self, text="WELCOME!!\nPlease choose questions \
to appear on an assignment\n", font=("Helvetica", 32))
        self.label.pack()

        self.display_button = tk.Button(self, text="Display Questions", \
                                        command=self.display)
        self.display_button.pack()

        self.submit_button = tk.Button(self, text="Submit", \
                                       command=self.create_window)

        self.entry = tk.Entry(self)
        
        self.assignmentEntry = None
        
        self.assignmentWindow = None
        
        # This will be the list of actual questions chosen
        self.chosenQuestions = []
        
        self.assignmentAnswerEntry = None
        
        self.handInBut = None
        
        self.label = None
        self.labels = []
        
        #self.numCorrect = 0
        
        self.numQuestions = 0

    def display(self):
        # Read all the questions in questions.csv and display them on the
        # screen
        with open("questions.csv", "r") as csvFile:
            reader = csv.reader(csvFile, delimiter="\n")
            for row in reader:
                splitRow = row[0].split(',')
                self.singleQuestion = tk.Label(self, text=splitRow[0] + ":" + \
                                               splitRow[3],\
                                               font=("Helvetica", 28))
                self.singleQuestion.pack()
                
            self.submit_button.pack()
    
            self.entry.pack()
            
            self.display_button.config(state = 'disabled')

    def create_window(self):
        # FIX: WHEN QUESTIONS SPAN MORE THAN THE SCREEN, UNABLE TO SCROLL DOWN
        # Create a new window for the assignment
        self.assignmentWindow = tk.Toplevel(self)
        root.withdraw()
        self.assignmentWindow.wm_title("ASSIGNMENT")
        
        # Get the user input
        chosenQuestionNums = self.entry.get()
        questionNumChosen = chosenQuestionNums.split(',')
        
        # Get the chosen questions and append to the list self.chosenQuestions
        with open("questions.csv", "r") as csvFile:
            for lineList in csv.reader(csvFile):
                self.chosenQuestions.append(lineList)
        
        # Make an assignment and store it inside Assignment.csv (using the
        # function in randomalgo.py)
        makeAssignment(self.chosenQuestions)
        
        # Read from Assignment.csv and display the questions to the window
        with open('Assignment.csv', 'r') as assignmentFile:
            for question in csv.reader(assignmentFile):
                self.numQuestions += 1
                questionEntry = tk.Label(self.assignmentWindow, \
                                         text=question[2],\
                                         font=("Helvetica", 28))
                questionEntry.pack()
                
        self.handInBut = tk.Button(self.assignmentWindow, text="Hand in", \
                  font=("Helvetica", 28), command=self.validate)
        self.handInBut.pack()
        
        self.assignmentAnswersEntry = tk.Entry(self.assignmentWindow, \
                                              font=("Helvetica", 28))
        self.assignmentAnswersEntry.pack()

    def validate(self):
        assignmentAnswers = self.assignmentAnswersEntry.get()
        assignmentAnswersList = [x.strip() for x in \
                                 assignmentAnswers.split(',')]
        questionsWithStudentAnswers = []
        
        # Read from Assignment.csv and append/change student answers into a list
        with open('Assignment.csv', 'r') as assignmentFile:
            i = 0
            for question in csv.reader(assignmentFile):
                # If first time, append to question
                if len(question) < 5:
                    # add the student answer to the row
                    question.append(assignmentAnswersList[i])
                # If not first time, change the value
                else:
                    question[4] = assignmentAnswersList[i]
                # Add the updated row to a list
                questionsWithStudentAnswers.append(question)
                i += 1
        
        # Write the list into Assignment.csv
        with open('Assignment.csv', 'w') as assignmentFile:
            writer = csv.writer(assignmentFile)
            writer.writerows(questionsWithStudentAnswers)
        
        # For every student answer in assignmentAnswersList, compare them with
        # the answers. If the student didn't answer all the questions, it would
        # still output "WRONG"
        with open('Assignment.csv', 'r') as assignmentFile:
            # Display the correct label
            for question in csv.reader(assignmentFile):
                # If the student answer matches the actual answer, output
                # "CORRECT"
                if question[3].strip() == question[4].strip():
                    #self.numCorrect += 1
                    self.label = tk.Label(self.assignmentWindow, \
                                                 text="CORRECT")
                    self.label.after(1000, self.clear_labels)
                    self.label.pack()
                    self.labels.append(self.label)
                # If the student answers are incorrect, output "WRONG"
                else:
                    self.label = tk.Label(self.assignmentWindow, \
                                                   text="WRONG")
                    self.label.after(1000, self.clear_labels)
                    self.label.pack()
                    self.labels.append(self.label)
        
    def clear_labels(self):
        for label in self.labels:
            # TODO: Check the number of CORRECT labels
            label.destroy()
        
root = tk.Tk()
root.geometry('%sx%s' % (2000, 2000))
main = SelectQuestions(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()

'''
if (self.numQuestions == self.numCorrect):
    # TODO: Record the last attempt
    self.handInBut.config(state = 'disabled')
    tk.Label(self.assignmentWindow, text="Congratulations! \
    You gotall the questions correct.").pack()
    
    # The "Close" button will close the assignment window
    tk.Button(self.assignmentWindow, text="Close", \
              command=self.assignmentWindow.destroy).pack()
'''