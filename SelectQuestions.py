try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

class SelectQuestions:
	def __init__(self, master):
		self.master = master
		master.title("Select Questions to be on the Assignment")

		self.asNumQues = 0
		self.questions = None
		self.allQuestions = None
		self.singleQuestion = None
		self.chosenQuestions = None

		self.entry = Entry(master)

		# Have a greeting to make it user-friendly
		self.greetings = Label(master, text="WELCOME!!\nPlease choose questions to appear on an assignment\n")
		self.greetings.pack()

		# TODO (FEATURE)
		# This keeps track of the number of questions chosen by the user
		self.currNum = Label(master, text="Current number of questions: " + str(self.asNumQues) + "\n\n")
		self.currNum.pack()

		# Create a button with the text "Display Questions"
		self.display_button = Button(master, text="Display Questions", command=self.display)
		self.display_button.pack()

		# Create a button with the text "Submit"
		self.submit_button = Button(master, text="Submit", command=self.submit)

	def display(self):
		# Display every question below and have a checkbox beside every one of them
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
				c = Checkbutton(self.master, variable=is_checked, command=lambda: self.update(is_checked))
				c.pack(side="left")
				'''

				# display the question
				self.singleQuestion = Label(self.master, text=self.allQuestions[i])
				self.singleQuestion.pack(side="left")

		self.submit_button.pack()

		# TODO: To be user-friendly, add a label telling the user that the question numbers
		#       start from 1
		# IMPORTANT: For now, we will have the user choose the questions in the
		# format of a, b, c, etc., where a,b,c are integers
		self.entry.pack()

	'''
	def update(self, is_checked):
		print("HELLO")
		print(is_checked.get())
	'''

	def submit(self):
		print(self.entry.get())

		# Get the question numbers (starting from one) that the user chose
		self.chosenQuestions = self.entry.get().split(',')
		self.asNumQues = len(self.chosenQuestions)
		# Transition to Assignment.py

class Assignment:
	def __init__(self, master):
		self.master = master
		master.title("EXERCISE")

		# Read questions.txt and all questions
		with open('questions.txt', 'r') as f:
			self.questions = f.read()
			self.allQuestions = self.questions.split('\n')

		self.title = Label(master, text="EXERCISE\n\n")
		self.title.pack()

		self.intro = Label(master, text="Please answer the following questions to the best of your ability\n\n\n")
		self.intro.pack()

		self.extractQuestions()

root = Tk()

addGui = SelectQuestions(root)

mainloop()