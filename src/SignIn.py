from tkinter import *
import tkinter.messagebox
from Student import *
from Professor import *
import DisplayAllAssignments
import StudentProfileIndex
import ProfessorProfileIndex
import DisplayProfessorsAssignments
import user_story_3
import csv
import io
import os

## Parent Class for all users

def readUser():
    return readUserFile("Users.csv")

def readUserFile(filename):
    csv_file = open(filename, "r")

    Users = []

    # Represents file as List of Lists, first list is of rows, deeper list is of row contents.
    lines = list(csv.reader(csv_file))

    for l in lines:

        # Make the user and email pair

        if l[5] == "P":
            Users.append(Professor(l[0], l[1], l[2], l[3], l[4]))
        elif l[5] == "S":
            s = Student(l[0], l[1], l[2], l[3], l[4])
            Users.append(s)

    csv_file.close()
    # Should set it so it returns 0 if the file isn't there, then report that to the user.

    return Users

## Python or Tkinter or whatever doesn't check if these frames exist. 
## These functions, when called by a button press, act as if they're in the same scope as the button.

def StudentRegistering(event):
    """ Execute the registration menu for students."""

    newWindow = Toplevel()
    newWindow.attributes('-topmost', 'true')
    StudentProfileIndex.signUpIndex(newWindow)

def ProfessorRegistering(event):
    """ Execute the registration menu for profesors."""

    newWindow = Toplevel()
    newWindow.attributes('-topmost', 'true')
    ProfessorProfileIndex.signUpIndex(newWindow)

def SignIn(event):
    """ Check that the person signing in has credentials that correspond to a actual user, and setting them as the current user."""

    # Need to declare globals locally
    global CurrentUsr
    global Usrs

    # Read all the users in Users.csv
    Usrs = readUser()

    # Get the email and password that the user entered
    Em = EmailEntry.get()
    Pass = PassEntry.get()

    # Variables to check if either name or email exist separately
    EmEx = False
    PassEx = False

    # Iterate through the list of users to see if any matches the user input
    for Usr in Usrs:

        # If we have no idea who the correct user could be
        if CurrentUsr is None:

            if (Usr.getEmail() == Em):
                EmEx = True
                CurrentUsr = Usr

            if (Usr.getPassword() == Pass):
                PassEx = True
                CurrentUsr = Usr

        # If any user profile matches the one entered
        if not (CurrentUsr is None):

            if (Usr.getEmail() == Em):
                EmEx = True

            if (Usr.getPassword() == Pass):
                PassEx = True

            # Log in and transition to a different screen depending on the type of user
            if (EmEx & PassEx):
                tkinter.messagebox.showinfo('Logged In', ('You are now logged in,' + " " + Usr.getName() + "."))
                goToTransitionScreen(Usr)
                break

    # If either the email or the password or both don't match any existing user profile
    if not (EmEx and PassEx):
        tkinter.messagebox.showinfo('Invalid Credentials', "Invalid Credentials")

def goToTransitionScreen(user):
    """ Display the transistion screen between signing in / registering and User specific functions."""
    
    # Create a new window
    newWindow = Toplevel()
    newWindow.attributes('-topmost', 'true')

    # Create a button that calls the method callDisplayAllAssignments when clicked
    Button(newWindow, text="Display Assignment", command=lambda:callDisplayAllAssignments(newWindow, user)).pack()

    # Create a different transition screen based on the type of user
    if (user.getType() == 'S'):
        studInfoBut = Button(newWindow, text="My Info", command=lambda:StudentProfileIndex.displayProfile(newWindow, user, studInfoBut))
        studInfoBut.pack()
    elif (user.getType() == 'P'):
        addQuestionFormsBtn = Button(newWindow, text="Add a question formula", command=lambda:callAddQuestionFormulas(newWindow, user))
        addQuestionFormsBtn.pack()
        profInfoBut = Button(newWindow, text="My Info", command=lambda:ProfessorProfileIndex.displayProfile(newWindow, user, profInfoBut))
        profInfoBut.pack()

def callDisplayAllAssignments(newWindow, user):
    # Destroy the previous window
    newWindow.destroy()

    # Run different files depending on the type of user
    if (user.getType() == 'S'):
        DisplayAllAssignments.displayListOfAssignments(user.getId())
    elif (user.getType() == 'P'):
        print(user.getId())
        DisplayProfessorsAssignments.getProfessorsAssignments(user.getId())
        
def callAddQuestionFormulas(newWindow, user):
    # Destroy the previous window
    newWindow.destroy()

    # Run the file that allows professors to add question formulas
    user_story_3.runUserStory3(user)
    os.system('python3 user_story_3.py')

# Note: Bound functions can't take parameters


if __name__ == '__main__':
        
    # Create the window
    root = Tk()
    root.title("Sign In Page")
    root.attributes('-topmost', 'true')

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

    BottomFrame = Frame(root)
    BottomFrame.pack(side=BOTTOM)

    ButtonFrame = Frame(BottomFrame)
    ButtonFrame.pack(side=BOTTOM)

    global Usrs

    Usrs = readUser()

    global CurrentUsr

    CurrentUsr = None

    # Add a button for users to register as a student
    RegisterButton = Button(ButtonFrame, text="Student Registration")
    RegisterButton.pack(side=LEFT)
    RegisterButton.bind("<Button-1>", StudentRegistering)

    # Add a button for users to register as a professor
    RegisterButton = Button(ButtonFrame, text="Professor Registration")
    RegisterButton.pack(side=LEFT)
    RegisterButton.bind("<Button-1>", ProfessorRegistering)

    # Add a sign in button for users to sign in
    SignInButton = Button(ButtonFrame, text="Sign In")
    SignInButton.bind("<Button-1>", SignIn)

    if Usrs is not None:
        SignInButton.pack(side=RIGHT)

    root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...:
