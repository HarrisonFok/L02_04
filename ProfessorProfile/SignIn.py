from tkinter import *

class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email


class Professor(User):
    def __init__(self, name, email):
        User.__init__(self, name, email)


class Student(User):
    def __init__(self, name, email):
        User.__init__(self, name, email)

def writeUser(User):
    f = open("Users.txt", "w")

    if isinstance(User, Student):
        f.writelines("S" + " " + User.getName() + " " + User.getName())

    if isinstance(User, Professor):
        f.writelines("P" + " " + User.getName() + " " + User.getName())

    f.close()

def writeUserFile(filename, User):
    f = open("filename", "w")

    if isinstance(User, Student):
        f.writelines("S" + " " + User.getName() + " " + User.getName())

    if isinstance(User, Professor):
        f.writelines("P" + " " + User.getName() + " " + User.getName())

    f.close()

def readUser():
    f = file("Users.txt", "r")

    Users = []
    
    lines = f.readlines()
    
    for i in len(lines):
        l = line.split()

        # Could make the user and email pair now, instead of doing it when making the object...

        if l[0] == "P":
            Users[i] = Professor(l[1], l[2])

        if l[0] == "S":
            Users[i] = Student(l[1], l[2])

    f.close()

    # Should set it so it returns 0 if the file isn't there, then report that to the user.
    
    return Users
    
def readUserFile(filename):
    f = file("filename" + ".txt", "r")

    Users = []
    
    lines = f.readlines()
    
    for i in len(lines):
        l = line.split()

        # Could make the user and email pair now, instead of doing it when making the object...

        if l[0] == "P":
            Users[i] = Professor(l[1], l[2])

        if l[0] == "S":
            Users[i] = Student(l[1], l[2])

    f.close()

    # Should set it so it returns 0 if the file isn't there, then report that to the user.
    
    return Users

## Remember, Python or Tkinter or whatever doesn't check if these frames exist. these functions, when called by a buttonpress, act as if they're in the same scope as the button, or something.

def Registering(event):
    ButtonFrame.pack_forget()

    PassFrame = Frame(BottomFrame)
    PassFrame.pack(side=BOTTOM)

    button_1 = Button(PassFrame, text="Print Message")
    button_1.bind("<Button-1>", writeUser(User(NameEntry.get(), Email.get())))
    button_1.pack()

def SignIn(event):
    CredFrame.pack_forget()
    SignInForm("Student")

def SignInForm(Type):
    return Type

#### Okay... So bound functions can't take parameters...

root = Tk()

CredFrame = Frame(root)
CredFrame.pack()

entrytext = StringVar()

NameLabel = Label(CredFrame, text="Name")
label_2 = Label(CredFrame, text="Email")
NameEntry = Entry(CredFrame, textvariable=entrytext)
Email = Entry(CredFrame, textvariable=entrytext)

entrytext.set("Test")

# widgets centered by default, sticky option to change
NameLabel.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

NameEntry.grid(row=0, column=1)
Email.grid(row=1, column=1)

checked = 0

c = Checkbutton(CredFrame, text="Keep me logged in", variable=checked)
c.grid(columnspan=2)

BottomFrame = Frame(root)
BottomFrame.pack(side=BOTTOM)

ButtonFrame = Frame(BottomFrame)
ButtonFrame.pack(side=BOTTOM)

if checked: print("hi!") #Do stuff

RegisterButton = Button(ButtonFrame, text="Register")
RegisterButton.bind("<Button-1>", Registering)
RegisterButton.pack(side=LEFT)

SignInButton = Button(ButtonFrame, text="Sign In")
SignInButton.bind("<Button-1>", SignIn)
SignInButton.pack(side=RIGHT)

root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...:
