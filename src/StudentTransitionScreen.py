from tkinter import *
import os
from StudentProfileIndex import *

root = Tk()

def callDisplayAllAssignments():
	os.system('python3 DisplayAllAssignments.py')

Label(root, text="To view your information, close the window\n").pack()
Button(root, text="Display Assignment", command=callDisplayAllAssignments).pack()
#Button(root, text="My Info").pack()

root.mainloop()