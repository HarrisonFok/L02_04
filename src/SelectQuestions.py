from tkinter import *
import random
import io
import csv

from randomalgo import *
from __main__ import *

class SelectQuestions(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        # Give instructions to the user
        self._label = Label(self, text="WELCOME!!\nPlease choose questions to appear on an assignment\n", font=("Helvetica", 32))
        self._label.pack()

        # Initialize a button for users to display the existing questions
        self._display_button = Button(self, text="Display Questions", command=self.display)
        self._display_button.pack()

        # Initialize entrys
        self._entry = Entry(self)
        self._additionalInfoEntry = None

        # Initialize the window for showing what questions are added
        self._addedQWindow = None
        
        # This will be the list of chosen question formulas
        self._chosenQuestionFormulas = []
        
        # This is the number of questions
        self._numQuestions = 0
        
        # This will be the Assignment object that randomalgo.py returns
        self._assignment = None

        # This will be the id of the professor
        # self._prof_id = profId

    def display(self):
        # Read all the question formulas in questions.csv and display them to
        # the screen
        with open("questions.csv", "rU") as csvFile:
            reader = csv.reader(csvFile, dialect=csv.excel_tab)
            for row in reader:
                splitRow = row[0].split(",")
                # remove any \n characters
                splitRow[0] = splitRow[0].strip()
                # temporary solution: break out of this loop if it's the end of the record .csv
                if (splitRow[0] == ""):
                    break;
                self.singleQuestion = Label(self, text=splitRow[0] + ":" + splitRow[3], font=("Helvetica", 28))
                self.singleQuestion.pack()

            # Have an entry for the user to enter question ids
            self._entry.pack()
            
            # Disable the display button once clicked
            self._display_button.config(state = 'disabled')

            # Allow the user to allow the user to give additional info of assignment name, due date, and student id
            Label(self, text="Please enter the additional information of assignment name, due date, and student id").pack()
            self._additionalInfoEntry = Entry(self)
            self._additionalInfoEntry.pack()

               # Have a button for the user to submit
            Button(self, text="Submit", command=self.create_window).pack()

    def create_window(self):
        addInfoList = self._additionalInfoEntry.get().split(',')
        # Create a new window
        self._addedQWindow = Toplevel(self)
        self._addedQWindow.wm_title("ASSIGNMENT")
        self._addedQWindow.attributes('-topmost', 'true')
        
        # Get the user input
        chosenQuestionNums = self._entry.get()
        questionNumChosen = chosenQuestionNums.split(',')
        chosenQ = []
        for qNumWithSpace in questionNumChosen:
            qNum = qNumWithSpace.replace(' ','')
            chosenQ.append(qNum)

        Label(self._addedQWindow, text="These are the questions created on the assignment:\n", font=("Times New Romans", 30)).pack()
        
        # Get the chosen question formulas and append to the list self._chosenQuestionFormulas
        with open("questions.csv", "rU") as csvFile:
            for lineList in csv.reader(csvFile):
                lineList[5] = lineList[5].strip()
                # if the question is one of the chosen questions, then add it
                # to self._chosenQuestionFormulas
                if lineList[0] in chosenQ:
                    self._chosenQuestionFormulas.append(lineList)
        
        # Make an assignment and store it inside Assignment.csv (using the
        # function makeAssignment() in randomalgo.py)
        assignmentId = str(randint(000000000, 999999999))
        self._assignment = makeAssignment(self._chosenQuestionFormulas, addInfoList, profId, assignmentId)
        
        # Read from Assignment.csv and display the questions to the window
        listOfQ = self._assignment.getListOfQuestions()
        self._numQuestions = len(listOfQ)
        for question in listOfQ:
            questionEntry = Label(self._addedQWindow, text=question.getQuestion(), font=("Helvetica", 28))
            questionEntry.pack()

        Button(self._addedQWindow, text="Close", command=self.destroyWindows).pack()
        
    def destroyWindows(self):
        # Close the assignment window and clear the main frame
        self._addedQWindow.destroy()
        self.destroy()

def runSelectQuestions(user):
    root = Tk()
    root.wm_attributes("-topmost", 'true')
    # make a global variable to hold the prof's id throughout this script
    global profId
    profId = user.getId()
    main = SelectQuestions(root)
    main.pack(side="top", expand=True)

    root.mainloop()