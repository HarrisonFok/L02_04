from tkinter import *
import os
from ProfessorProfileIndex import *

root = Tk()

def callDisplayAllAssignments():
	root.destroy()
	os.system('python3 DisplayProfessorsAssignments.py')

#Label(root, text="To view your information, close the window\n").pack()
Button(root, text="Display Assignment", command=callDisplayAllAssignments).pack()
Button(root, text="My Info").pack()

root.mainloop()