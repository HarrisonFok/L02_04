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
import sys

## Parent Class for all users

def readUser():
    return readUserFile("Users.csv")

def readUserFile(filename):
    csv_file = open(filename, "r")

    Users = []

    # list([open_csv_file]) represents lines in CSV as List of Lists.
    # First list is of rows, deeper lists are of row contents.

    for l in list(csv.reader(csv_file)):

        # If there's an empty line in the file, which only happens if it's empty.
        if l == []:
            continue
        
        # Make the users.

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

def SignIn(root, Usrs):
    """ Check that the person signing in has credentials that correspond to a actual user, and setting them as the current user."""

    # Iterate through the provided list of users from readUser to see if any matches the user input.

    for Usr in Usrs:

        # If any user profile matches the one entered... And the "and True" is needed because "False and False == True".

        if (Usr.getEmail() == EmailEntry.get() and Usr.getPassword() == PassEntry.get() and True):

            # Log in and transition to a different screen depending on the type of user.

            tkinter.messagebox.showinfo('Logged In', ('You are now logged in,' + " " + Usr.getName() + "."))
            goToTransitionScreen(Usr)

            # hide the sign in menu
            root.withdraw()
            return 0

    # If this runs, then either the email or the password or both don't match any existing user profile
    tkinter.messagebox.showinfo('Invalid Credentials', "Invalid Credentials")

def goToTransitionScreen(user):
    """ Display the transistion screen between signing in / registering and User specific functions."""

    # Create a new window
    newWindow = Toplevel()
    newWindow.attributes('-topmost', 'true')
    newWindow.title("Options Menu")
    newWindow.geometry("650x400")

    if (user.getType() == 'S'):
        AssignmentsDescription = "Display Assignments: Display all your assignments.\n"
        AddQuestionDescription = ""
    if (user.getType() == 'P'):
        AssignmentsDescription = "Display Assignments: Display all assignments you have created.\n\n"
        AddQuestionDescription = "Add Question: Add a question to the .csv file to be used in an assignment.\n"

    description = """ Please choose from the following:\n""" + AssignmentsDescription + AddQuestionDescription + """
    My Info: View your account information such as name, email and personnel number.\n
    Sign Out: Log out and exit the program.
    """
    Label(newWindow, text=description).pack()

    # Create a button that calls the method callDisplayAllAssignments when clicked
    Button(newWindow, text="Display Assignments", command=lambda:callDisplayAllAssignments(newWindow, user)).pack()

    # Create a different transition screen based on the type of user

    if (user.getType() == 'S'):
        studInfoBut = Button(newWindow, text="My Info", command=lambda:StudentProfileIndex.displayProfile(newWindow, user, studInfoBut))
        studInfoBut.pack()

    elif (user.getType() == 'P'):
        addQuestionFormsBtn = Button(newWindow, text="Add Question", command=lambda:callAddQuestionFormulas(newWindow, user))
        addQuestionFormsBtn.pack()
        profInfoBut = Button(newWindow, text="My Info", command=lambda:ProfessorProfileIndex.displayProfile(newWindow, user, profInfoBut))
        profInfoBut.pack()

    Button(newWindow, text="Sign Out", command=lambda:signOut(newWindow)).pack()

def signOut(newWindow):
    # destroy the options menu
    newWindow.destroy()
    # close the application
    sys.exit()

def callDisplayAllAssignments(newWindow, user):
    # Destroy the previous window
    newWindow.destroy()

    # Run different files depending on the type of user
    DisplayAllAssignments.displayListOfAssignments(user)

def callAddQuestionFormulas(newWindow, user):
    # Destroy the previous window
    newWindow.destroy()

    # Run the file that allows professors to add question formulas
    user_story_3.runUserStory3(user)

# Note: Bound functions can't take parameters


if __name__ == '__main__':

    # Create the window
    root = Tk()
    root.title("Sign In")
    root.attributes('-topmost', 'true')

    Label(root, text="Welcome! Enter your credentials to sign in or register.").pack()

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

    Usrs = readUser()

    # Add a button for users to register as a student
    RegisterButton = Button(ButtonFrame, text="Student Registration")
    RegisterButton.pack(side=LEFT)
    RegisterButton.bind("<Button-1>", StudentRegistering)

    # Add a button for users to register as a professor
    RegisterButton = Button(ButtonFrame, text="Professor Registration")
    RegisterButton.pack(side=LEFT)
    RegisterButton.bind("<Button-1>", ProfessorRegistering)

    # Add a sign in button for users to sign in
    SignInButton = Button(ButtonFrame, text="Sign In", command=lambda:SignIn(root, Usrs))

    if ((Usrs is not None) and (Usrs != []) and True):
        SignInButton.pack(side=RIGHT)

    root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...:
