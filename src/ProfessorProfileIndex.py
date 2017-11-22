from tkinter import *
from Professor import *

# Event handler method for submit button
def createProfessor(root, nameEntry, emailEntry, passwordEntry, passwordDupEntry, pNumEntry):
	""" Create a professor object and insert it into a .csv file """
	name = nameEntry.get()
	email = emailEntry.get()
	pwd = passwordEntry.get()
	pwdDup = passwordDupEntry.get()
	pNum = pNumEntry.get()

	resultLabel = Label(root, text="")
	resultLabel.grid(row=8, column=1)

	# check if fields are empty
	if (entryIsEmpty(name) or entryIsEmpty(email) or entryIsEmpty(pwd)
		or entryIsEmpty(pwdDup) or entryIsEmpty(pNum)):
		resultLabel.config(text="One or more fields are empty.")
	else:
		if matchPasswords(pwd, pwdDup):
			# create professor object
			p = Professor(name, email, pwd, pNum)
			resultLabel.config(text="Profile Successfully Created!")
			# insert into CSV
			p.insertProfessor()
			# clear fields
			nameEntry.delete(0, 'end')
			emailEntry.delete(0, 'end')
			passwordEntry.delete(0, 'end')
			passwordDupEntry.delete(0, 'end')
			pNumEntry.delete(0, 'end')
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
	# root = Tk()

	header = Label(root, text="Professor Profile Registration").grid(row=0,column=1)

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

	pNumLabel = Label(root, text="Personnel Number:").grid(row=5)
	pNumEntry = Entry(root, width=50)
	pNumEntry.grid(row=5, column=1)

	submitBtn = Button(root, text="Submit", command = lambda: createProfessor(root, nameEntry, emailEntry, passwordEntry, passwordDupEntry, pNumEntry))
	submitBtn.grid(row=6, column=1)


	# set fixed window size
	root.resizable(width=False, height=False)

	# root.mainloop()

def displayProfile(root, user, button):
	button['state'] = 'disabled'
	""" Display the information about a user in a window with these widgets. """
	nameLabel = Label(root, text="Name: " + user.getName()).pack()
	emailLabel = Label(root, text="Email: " + user.getEmail()).pack()
	pNumLabel = Label(root, text="Personnel Number: " + user.getPersonnelNumber()).pack()



