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

class SelectQuestions(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.label = tk.Label(self, text="WELCOME!!\nPlease choose questions \
to appear on an assignment (without spaces)\n", font=("Helvetica", 32))
        self.label.pack()

        self.display_button = tk.Button(self, text="Display Questions", \
                                        command=self.display)
        self.display_button.pack()

        self.submit_button = tk.Button(self, text="Submit", \
                                       command=self.create_window)

        self.entry = tk.Entry(self)
        
        self.assignmentEntry = None
        
        # This will be the list of actual questions chosen
        self.chosenQuestions = []
        
        self.questionNumPair = {}
        
        self.passList = []

    def display(self):
        # Read all the questions in questions.csv and display them on the
        # screen
        with open("questions.csv", "r") as csvFile:
            reader = csv.reader(csvFile, delimiter="\n")
            for row in reader:
                splitRow = row[0].split(',')
                self.questionNumPair[splitRow[0]] = splitRow[3]
                self.singleQuestion = tk.Label(self, text=splitRow[0] + ":" + \
                                               splitRow[3],\
                                               font=("Helvetica", 28))
                self.singleQuestion.pack()
                
            self.submit_button.pack()
    
            self.entry.pack()
            
            self.display_button.config(state = 'disabled')

    def create_window(self):
        # Create a new window for the assignment
        assignmentWindow = tk.Toplevel(self)
        root.withdraw()
        assignmentWindow.wm_title("ASSIGNMENT")
        
        # Get the user input
        chosenQuestionNums = self.entry.get()
        questionNumChosen = chosenQuestionNums.split(',')
        
        # Get the chosen questions and append to the list self.chosenQuestions
        with open("questions.csv", "r") as csvFile:
            reader = csv.reader(csvFile, delimiter="\n")
            for row in reader:
                for num in questionNumChosen:
                    if num.strip() in row[0]:
                        self.chosenQuestions.append(row[0])

        # For every element in self.chosenQuestions, split it by comma
        for csvInfo in self.chosenQuestions:
            indivList = csvInfo.split(',')
            
            # Add the element at index 5 with the one at index 4
            indivList[4] = indivList[4] + ", " + indivList[5]
            
            # Delete the 5th element
            del indivList[5]
            
            self.passList.append(indivList)
        
        # Make an assignment and store it inside Assignment.csv
        self.makeAssignment(self.passList)

    def RandomInRange(self, L):
        """
        len(L) == 2
        list[int(min), int(max)] -> int
        min <= max
        a function that return a integer randomly in the range(min,max)
        //RandomInRange(2, 6)
        //5
        """
        return random.randint(L[0], L[1])
    
    def makeAssignment(self, L):
        '''
        :param L: the list of all the selected questions [[q1], [q2], [q3]]
        '''
        result = []
        for question in L:
            allrange = question[3].split(',')
            vals = []
            for index in allrange:
                vals.append(self.RandomInRange(index.split('|')))
            i = 0
            for val in vals:
                old = "VAR"+ str(i)
                Q_B = question[2]
                Q_A = question[4]
                Q_B.replace(old, vals[i])
                Q_A.replace(old, vals[i])
                i += 1
            result.append([question[1], Q_B, Q_A])
    
        with open("Assignment.csv", "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(result)
            
    def validate(self):
        # TODO later
        pass

root = tk.Tk()
root.geometry('%sx%s' % (2000, 2000))
main = SelectQuestions(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()

'''
self.question = tk.Label(assignmentWindow, text=\
                         self.questionNumPair.get(key),\
                         font=("Helvetica", 28))
self.question.pack()
'''