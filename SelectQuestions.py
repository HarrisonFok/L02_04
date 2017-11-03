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
to appear on an assignment\n", font=("Helvetica", 32))
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

    def display(self):
        # Display every question formula below
        with open('questions.txt', 'r') as f:
            # read the file and then split them by newline character
            self.questions = f.read()
            self.allQuestions = self.questions.split('\n')

            # add every question to the GUI
            for i in range(len(self.allQuestions)-1):

                # display the question
                self.singleQuestion = tk.Label(self, text=str(i) + ":" + \
                                               self.allQuestions[i].\
                                               split('|||')[0].split(':')[1],
                                               font=("Helvetica", 28))
                
                self.singleQuestion.pack()

        self.submit_button.pack()

        self.entry.pack()
        
        #self.display_button.config(state = 'disabled')

    def create_window(self):
        # Create a new window for the assignment
        assignmentWindow = tk.Toplevel(self)
        root.withdraw()
        assignmentWindow.wm_title("ASSIGNMENT")

        # Get the list of question numbers the user chose and search in the 
        # text file
        chosenQuestionNums = self.entry.get().split(',')
        
        # Will call the validation method when the Submit button is pressed

        # Read all the questions in questions.txt and split them into a list
        with open('questions.txt', 'r') as f:
            self.questions = f.read()
            self.allQuestions = self.questions.split('\n')
            
            # write instruction
            instructions = tk.Label(assignmentWindow, text="Please answer the \
following questions to the best of your abilities\n\n", font=("Helvetica", 28))
            instructions.pack()
            
            # If any chosen question numbers appear in the list, add the label
            # to the new screen
            for questionNum in range(len(self.allQuestions)-1):
                if str(questionNum) in chosenQuestionNums:
                    currentQuestion = self.allQuestions[questionNum]\
                        .split('|||')[0].split(':')[1]
                    
                    # add the question to the list
                    self.chosenQuestions.append(currentQuestion)
                    
                    # put the current chosen question on the screen
                    self.question = tk.Label\
                        (assignmentWindow,text=currentQuestion,\
                         font=("Helvetica", 28))
                    self.question.pack()
                    
                    # add an entry for the user to input
                    self.assignmentEntry = tk.Entry(assignmentWindow)
                    self.assignmentEntry.pack()
                    
                    # add a blank line to the GUI
                    tk.Label(assignmentWindow, text="\n").pack()
            assignmentWindow.geometry("%dx%d" % (2000, 2000))
            
            assignment_submit_button = tk.Button(assignmentWindow,\
                                                 text = "Submit",\
                                                 command=self.validate)
            assignment_submit_button.pack()
            
            tk.Button(assignmentWindow, text="Exit",\
                      command=assignmentWindow.destroy).pack()

    def RandomInRange(L):
        """
        len(L) == 2
        list[int(min), int(max)] -> int
        min <= max
        a function that return a integer randomly in the range(min,max)
        //RandomInRange(2, 6)
        //5
        """
        return random.randint(L[0], L[1])
    
    def makeAssignment(L):
        '''
        :param L: the list of all the selected questions [[q1], [q2], [q3]]
        '''
        result = []
        for question in L:
            allrange = question[3].split(',')
            vals = []
            for index in allrange:
                vals.append(RandomInRange(index.split('|')))
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