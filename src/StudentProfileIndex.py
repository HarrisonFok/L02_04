from tkinter import *
from Student import *

# Event handler method for submit button
def createStudent(root, nameEntry, emailEntry, passwordEntry, passwordDupEntry, studentNumEntry):
	""" Create a student object and insert it into a .csv file """
	name = nameEntry.get()
	email = emailEntry.get()
	pwd = passwordEntry.get()
	pwdDup = passwordDupEntry.get()
	studentNum = studentNumEntry.get()

	resultLabel = Label(root, text="")
	resultLabel.grid(row=8, column=1)

	# check if fields are empty
	if (entryIsEmpty(name) or entryIsEmpty(email) or entryIsEmpty(pwd)
		or entryIsEmpty(pwdDup) or entryIsEmpty(studentNum)):
		resultLabel.config(text="One or more fields are empty.")
	else:
		if matchPasswords(pwd, pwdDup):
			# create student object
			s = Student(None, name, email, pwd, studentNum)
			resultLabel.config(text="Profile Successfully Created!")
			# insert into CSV
			s.insertStudent()
			# clear fields
			nameEntry.delete(0, 'end')
			emailEntry.delete(0, 'end')
			passwordEntry.delete(0, 'end')
			passwordDupEntry.delete(0, 'end')
			studentNumEntry.delete(0, 'end')
			# close the window
			root.destroy()
		else:
			resultLabel.config(text="Passwords don't match")

def matchPasswords(pwd, pwdDup):
	""" Returns true iff the password and confirm password fields match """
	if pwd == pwdDup:
		return True
	return False

def entryIsEmpty(entry):
	""" Returns true iff a field is empty """
	if len(entry) == 0:
		return True
	else:
		return False
# GUI 

def signUpIndex(root):
	""" Index page for the Profile Registration """

	header = Label(root, text="Student Profile Registration").grid(row=0,column=1)

	nameLabel = Label(root, text="Name:").grid(row=1)
	nameEntry = Entry(root, width=50)
	nameEntry.grid(row=1, column=1)

	emailLabel = Label(root, text="Email:").grid(row=2)
	emailEntry = Entry(root, width=50)
	emailEntry.grid(row=2, column=1)

	passwordLabel = Label(root, text="Password:").grid(row=3)
	passwordEntry = Entry(root, show="*", width=50)
	passwordEntry.grid(row=3, column=1)

	passwordDupLabel = Label(root, text="Confirm Password:").grid(row=4)
	passwordDupEntry = Entry(root, show="*", width=50)
	passwordDupEntry.grid(row=4, column=1)

	studentNumLabel = Label(root, text="Student Number:").grid(row=5)
	studentNumEntry = Entry(root, width=50)
	studentNumEntry.grid(row=5, column=1)

	submitBtn = Button(root, text="Submit", command = lambda: createStudent(root, nameEntry, emailEntry, passwordEntry, passwordDupEntry, studentNumEntry))
	submitBtn.grid(row=6, column=1)

	Label(root, text="Please restart the application after registration").grid(row=8, column=1)


	# set fixed window size
	root.resizable(width=False, height=False)

def displayProfile(root, user, button):
	""" Display the information about a user in a window. """
	button['state'] = 'disabled'
	root.attributes('-topmost', 'true')
	nameLabel = Label(root, text="Name: " + user.getName()).pack()
	emailLabel = Label(root, text="Email: " + user.getEmail()).pack()
	studentNumLabel = Label(root, text="Student Number: " + user.getPersonnelNumber()).pack()
