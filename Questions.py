try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

questionNum = 0

class Questions:
	def __init__(self, master):
		self.questionNum = 0
		self.master = master
		master.title("Add Questions")

		# Create a label so that it is user-friendly
		self.label = Label(master, text="Hi!  You can add questions to the text file here.")
		self.label.pack()

		# Allow the professor to type the question
		self.entry = Entry(root)
		self.entry.pack()

		# Create an add button that adds the question to a text file when pressed
		self.add_button = Button(master, text="Add", command=self.add)
		self.add_button.pack()

	def add(self):
		# If there is indeed something typed and they are not all empty spaces, 
		# then it should not be added to the text file
		if (len(self.entry.get().strip()) != 0):
			with open('questions.txt', 'a') as f:
				# str(self.questionNum+1)
				f.write(self.entry.get() + '\n')
			self.questionNum += 1

		# TODO (feature): notify the user that the question has been added to the text file and
		#                 clear what the user just wrote

	def retrieve(self, questionNum):
		# TODO: retrieve the question
		print("HI")

root = Tk()

addGui = Questions(root)

mainloop()
