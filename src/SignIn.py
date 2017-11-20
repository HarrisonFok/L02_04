from tkinter import *
import tkinter.messagebox
from Student import *
from Professor import *
import StudentProfileIndex
import ProfessorProfileIndex
import csv
import io
import os

## Parent Class for all users

def readUser():
    return readUserFile("Users.csv")

def readUserFile(filename):
    csv_file = open("Users.csv", "r")

    Users = []

    lines = list(csv.reader(csv_file)) # Represents file as List of Lists, first list is of rows, deeper list is of row contents.

    for l in lines:

        # Could make the user and email pair now, instead of doing it when making the object...

        if l[5] == "P":
            Users.append(Professor(l[1], l[2], l[3], l[4]))
        elif l[5] == "S":
            Users.append(Student(l[1], l[2], l[3], l[4]))

    csv_file.close()
    # Should set it so it returns 0 if the file isn't there, then report that to the user.

    return Users

## Remember, Python or Tkinter or whatever doesn't check if these frames exist. these functions, when called by a buttonpress, act as if they're in the same scope as the button, or something.

def StudentRegistering(event):
    """ Execute the registration menu """

    newWindow = Toplevel()
    StudentProfileIndex.signUpIndex(newWindow)

def ProfessorRegistering(event):
    """ Execute the registration menu """ 

    newWindow = Toplevel()
    ProfessorProfileIndex.signUpIndex(newWindow)

def SignIn(event):

    # Need to declare globals locally, if modifying them, from inside a function?

    global CurrentUsr
    global Usrs

    Usrs = readUser()

    Em = EmailEntry.get()

    Pass = PassEntry.get()

    # Check if either name or email exist separately. Bad for security? Maybe not.
    EmEx = False
    PassEx = False

    for Usr in Usrs:

        if CurrentUsr is None:

            #If we have no idea who the correct user could be...
            if (Usr.getEmail() == Em):
                EmEx = True
                CurrentUsr = Usr

            if (Usr.getPassword() == Pass):
                PassEx = True
                CurrentUsr = Usr

        if not (CurrentUsr is None):

            if (Usr.getEmail() == Em):
                EmEx = True

            if (Usr.getPassword() == Pass):
                PassEx = True

            if (EmEx & PassEx):
                tkinter.messagebox.showinfo('Logged In', ('You are now logged in,' + " " + Usr.getName() + "."))

                # open a new window with the credentials of the user
                newWindow = Toplevel()
                systemStr = ""
                if Usr.getType() == 'S':
                    StudentProfileIndex.displayProfile(newWindow, Usr)
                    systemStr = 'python3 StudentTransitionScreen.py'
                elif Usr.getType() == 'P':
                    ProfessorProfileIndex.displayProfile(newWindow, Usr)
                    systemStr = 'python3 ProfessorTransitionScreen.py'

                newWindow.geometry("400x400")
                os.system(systemStr)
                break

    if not (EmEx and PassEx):
        tkinter.messagebox.showinfo('Invalid Credentials', "Invalid Credentials")

#### Okay... So bound functions can't take parameters...

root = Tk()

CredFrame = Frame(root)
CredFrame.pack()

EmailText = StringVar()
PassText = StringVar()

EmailLabel = Label(CredFrame, text="Email")
PassLabel = Label(CredFrame, text="Password")

EmailEntry = Entry(CredFrame, textvariable=EmailText)
PassEntry = Entry(CredFrame, show="*", textvariable=PassText)

# widgets centered by default, sticky option to change
EmailLabel.grid(row=1, sticky=E)
PassLabel.grid(row=2, sticky=E)

EmailEntry.grid(row=1, column=1)
PassEntry.grid(row=2, column=1)

checked = 0

c = Checkbutton(CredFrame, text="Keep me logged in", variable=checked)
c.grid(columnspan=2)

BottomFrame = Frame(root)
BottomFrame.pack(side=BOTTOM)

ButtonFrame = Frame(BottomFrame)
ButtonFrame.pack(side=BOTTOM)

if checked: print("hi!") #Do stuff

global Usrs

Usrs = readUser()

global CurrentUsr

CurrentUsr = None

RegisterButton = Button(ButtonFrame, text="Student Registration")
RegisterButton.pack(side=LEFT)
RegisterButton.bind("<Button-1>", StudentRegistering)

RegisterButton = Button(ButtonFrame, text="Professor Registration")
RegisterButton.pack(side=LEFT)
RegisterButton.bind("<Button-1>", ProfessorRegistering)

SignInButton = Button(ButtonFrame, text="Sign In")
SignInButton.bind("<Button-1>", SignIn)

if Usrs is not None:
    SignInButton.pack(side=RIGHT)

root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...:
