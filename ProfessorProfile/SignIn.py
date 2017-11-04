from tkinter import *
import tkinter.messagebox
from Student import *

## Parent Class for all users

class User(Student):
    def __init__(self, name, email, password, studentNumber):
        Student.__init__(self, name, email, password, studentNumber)

class Professor(User):
    def __init__(self, name, email, password, studentNumber):
        User.__init__(self, name, email, password, studentNumber)

def writeUser(User):
    writeUserFile("Students.csv", User)

def writeUserFile(filename, User):
    f = open(filename, "w")

    if isinstance(User, Student):
        f.writelines("S" + " " + User.getName() + " " + User.getEmail())

    if isinstance(User, Professor):
        f.writelines("P" + " " + User.getName() + " " + User.getEmail())
    f.close()

def readUser():
    return readUserFile("Students.csv")

def readUserFile(filename):
    csv_file = open("Students.csv", "r")

    Users = []

    lines = list(csv.reader(csv_file)) # Represents file as List of Lists, first list is of rows, deeper list is of row contents.

    for l in lines:

        # Could make the user and email pair now, instead of doing it when making the object...

        if l[5] == "P":
            Users.append(Professor(l[1], l[2], l[3], l[4]))

        if l[5] == "S":
            Users.append(Student(l[1], l[2], l[3], l[4]))

    csv_file.close()

    # Should set it so it returns 0 if the file isn't there, then report that to the user.

    return Users

## Remember, Python or Tkinter or whatever doesn't check if these frames exist. these functions, when called by a buttonpress, act as if they're in the same scope as the button, or something.

def Registering(event):
    ButtonFrame.pack_forget()

    PassFrame = Frame(BottomFrame)
    PassFrame.pack(side=BOTTOM)

    RegProf = Button(PassFrame, text="Register as Professor")
    RegProf.bind("<Button-1>", writeUser(Professor(NameEntry.get(), EmailEntry.get())))
    RegProf.pack()

    RegStudBut = Button(PassFrame, text="Register as Student")
    RegStudBut.bind("<Button-1>", writeUser(Student(NameEntry.get(), EmailEntry.get())))
    RegStudBut.pack()

    PassFrame.pack_forget()
    ButtonFrame.pack()
    SignInButton.pack(side=RIGHT)

def SignIn(event):

    # It appears that we need to declare globals locally, if we're modifying them, from inside a function. Not sure if true, but haven't found a workaround.

    global CurrentUsr
    global Usrs

    Nam = NameEntry.get()

    Em = EmailEntry.get()

    Pass = PassEntry.get()

    NamEx = False
    EmEx = False
    PassEx = False

    for Usr in Usrs:

        #print(Usr.getName())
        #print(Usr.getEmail())
        #print(Usr.getPassword())

        if CurrentUsr is None:

            #If we have no idea who the correct user could be...

            if (Usr.getName() == Nam):
                NamEx = True
                CurrentUsr = Usr

            if (Usr.getEmail() == Em):
                EmEx = True
                CurrentUsr = Usr

            if (Usr.getPassword() == Pass):
                PassEx = True
                CurrentUsr = Usr

        if not (CurrentUsr is None):

            if (Usr.getName() == Nam):
                NamEx = True

            if (Usr.getEmail() == Em):
                EmEx = True

            if (Usr.getPassword() == Pass):
                PassEx = True

            if (NamEx & EmEx & PassEx & True):
                tkinter.messagebox.showinfo('Logged In', ('You are now logged in,' + " " + Usr.getName() + "."))
                break

    if not (NamEx & EmEx & True):
        tkinter.messagebox.showinfo('Invalid Credentials', ('There is no user with the name of:' + " " + Nam + " " + "nor an email of" + " " + Em +  "."))

    elif not NamEx:
        tkinter.messagebox.showinfo('Invalid Credentials', ('There is a user that\'s named:' + " " + Nam + " " + ", but they don't have an email of" + " " + Em + "."))

    elif not EmEx:
        tkinter.messagebox.showinfo('Invalid Credentials', ('There is no user that\'s named:' + " " + Nam + " " + ", but there is someone with an email of" + " " + Em + "."))

#### Okay... So bound functions can't take parameters...

root = Tk()

CredFrame = Frame(root)
CredFrame.pack()

NameText = StringVar()
EmailText = StringVar()
PassText = StringVar()

NameLabel = Label(CredFrame, text="Name")
EmailLabel = Label(CredFrame, text="Email")
PassLabel = Label(CredFrame, text="Password")

NameEntry = Entry(CredFrame, textvariable=NameText)
EmailEntry = Entry(CredFrame, textvariable=EmailText)
PassEntry = Entry(CredFrame, textvariable=PassText)

NameText.set("Test")
EmailText.set("Test")
PassText.set("Pass")

# widgets centered by default, sticky option to change
NameLabel.grid(row=0, sticky=E)
EmailLabel.grid(row=1, sticky=E)
PassLabel.grid(row=2, sticky=E)

NameEntry.grid(row=0, column=1)
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

#print(CurrentUsr)

RegisterButton = Button(ButtonFrame, text="Register")
RegisterButton.bind("<Button-1>", Registering)
RegisterButton.pack(side=LEFT)

SignInButton = Button(ButtonFrame, text="Sign In")
SignInButton.bind("<Button-1>", SignIn)

if Usrs is not None:
    SignInButton.pack(side=RIGHT)

root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...: