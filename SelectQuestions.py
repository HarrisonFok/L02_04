try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

class SelectQuestions(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.label = tk.Label(self, text="WELCOME!!\nPlease choose questions\
to appear on an assignment\n")
        self.label.pack()

        self.display_button = tk.Button(self, text="Display Questions", \
                                        command=self.display)
        self.display_button.pack()

        self.submit_button = tk.Button(self, text="Submit", \
                                       command=self.create_window)

        self.entry = tk.Entry(self)

    def display(self):
        # Display every question below and have a checkbox beside everyone
        # of them
        with open('questions.txt', 'r') as f:
            # read the file and then split them by newline character
            self.questions = f.read()
            self.allQuestions = self.questions.split('\n')

            # add every question to the GUI
            for i in range(len(self.allQuestions)-1):
                # TODO (FEATURE)
                '''
                is_checked = IntVar()
                # create a checkbox 
                c = Checkbutton(self.master, variable=is_checked, \
                command=lambda: self.update(is_checked))
                c.pack(side="left")
                '''

                # display the question
                self.singleQuestion = tk.Label(self, text=str(i) + ":" + \
                                               self.allQuestions[i])
                self.singleQuestion.pack(side="left")

        self.submit_button.pack(side="bottom")

        # TODO: To be user-friendly, add a label telling the user that the 
        # question numbers start from 1
        # IMPORTANT: For now, we will have the user choose the questions in the
        # format of a, b, c, etc., where a,b,c are integers
        self.entry.pack()

    def create_window(self):
        # Create a new window for the assignment
        assignmentWindow = tk.Toplevel(self)
        assignmentWindow.wm_title("ASSIGNMENT")

        # Get the list of question numbers the user chose and search in the 
        # text file
        chosenQuestionNums = self.entry.get().split(',')

        # Read all the questions in questions.txt and split them into a list
        with open('questions.txt', 'r') as f:
            self.questions = f.read()
            self.allQuestions = self.questions.split('\n') 
            for questionNum in range(len(self.allQuestions)):
                if str(questionNum) in chosenQuestionNums:
                    self.question = tk.Label\
                        (assignmentWindow,text=self.allQuestions[questionNum])
                    self.question.pack()

root = tk.Tk()
main = SelectQuestions(root)
main.pack(side="top", fill="both", expand=True)
root.mainloop()