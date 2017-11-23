from tkinter import *
import random
import io
import csv

from randomalgo import *

class SelectQuestions(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        # Give instructions to the user
        self._label = Label(self, text="WELCOME!!\nPlease choose questions to appear on an assignment\n", font=("Helvetica", 32))
        self._label.pack()

        # Initialize a button for users to display the existing questions
        self._display_button = Button(self, text="Display Questions", command=self.display)
        self._display_button.pack()

        # Initialize an entry
        self._entry = Entry(self)

        # Initialize the assignment window
        self._assignmentWindow = None
        
        # This will be the list of chosen question formulas
        self._chosenQuestionFormulas = []
        
        # This is the number of questions
        self._numQuestions = 0
        
        # This will be the Assignment object that randomalgo.py returns
        self._assignment = None

    def display(self):
        # Read all the question formulas in questions.csv and display them to
        # the screen
        with open("questions.csv", "rU") as csvFile:
            reader = csv.reader(csvFile, delimiter="\n", dialect=csv.excel_tab)
            for row in reader:
                splitRow = row[0].split(',')
                self.singleQuestion = Label(self, text=splitRow[0] + ":" + splitRow[3], font=("Helvetica", 28))
                self.singleQuestion.pack()
            
            # Have a button for the user to submit
            Button(self, text="Submit", command=self.create_window).pack()
        
            # Have an entry for the user to enter question ids
            self._entry.pack()
            
            # Disable the display button once clicked
            self._display_button.config(state = 'disabled')

    def create_window(self):
        # Create a new window for the assignment
        self._assignmentWindow = Toplevel(self)
        self._assignmentWindow.wm_title("ASSIGNMENT")
        
        # Get the user input
        chosenQuestionNums = self._entry.get()
        questionNumChosen = chosenQuestionNums.split(',')
        chosenQ = []
        for qNumWithSpace in questionNumChosen:
            qNum = qNumWithSpace.replace(' ','')
            chosenQ.append(qNum)

        Label(self._assignmentWindow, text="These are the questions created on the assignment:\n", font=("Times New Romans", 30)).pack()
        
        # Get the chosen question formulas and append to the list self._chosenQuestionFormulas
        with open("questions.csv", "rU") as csvFile:
            for lineList in csv.reader(csvFile):
                # if the question is one of the chosen questions, then add it
                # to self._chosenQuestionFormulas
                if lineList[0] in chosenQ:
                    self._chosenQuestionFormulas.append(lineList)
        
        # Make an assignment and store it inside Assignment.csv (using the
        # function makeAssignment() in randomalgo.py)
        self._assignment = makeAssignment(self._chosenQuestionFormulas)
        
        # Read from Assignment.csv and display the questions to the window
        listOfQ = self._assignment.getListOfQuestions()
        self._numQuestions = len(listOfQ)
        for question in listOfQ:
            questionEntry = Label(self._assignmentWindow, text=question.getQuestion(), font=("Helvetica", 28))
            questionEntry.pack()

        Button(self._assignmentWindow, text="Close", command=self.destroyWindows).pack()

    def destroyWindows(self):
        self._assignmentWindow.destroy()
        self.destroy()

root = Tk()
main = SelectQuestions(root)
main.pack(side="top", expand=True)
root.mainloop()