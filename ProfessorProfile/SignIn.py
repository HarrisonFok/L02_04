from tkinter import *
import tkinter.messagebox

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
    writeUserFile("Users.txt", User)

def writeUserFile(filename, User):
    f = open(filename, "w")

    if isinstance(User, Student):
        f.writelines("S" + " " + User.getName() + " " + User.getEmail())

    if isinstance(User, Professor):
        f.writelines("P" + " " + User.getName() + " " + User.getEmail())
    f.close()

def readUser():
    readUserFile("Users.txt")
    
def readUserFile(filename):
    f = open(filename, "r")

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

    button_1 = Button(PassFrame, text="Register")
    button_1.bind("<Button-1>", writeUser(User(NameEntry.get(), EmailEntry.get())))
    button_1.pack()

def SignIn(event):
    
    Usrs = readUser()
    
    Nam = NameEntry.get()
    
    Em = EmailEntry.get()

    # Check if either name or email exist separately. Bad for security? Maybe not.
    
    NamEx = 0
    EmEx = 0

    for Usr in Usrs:
        if ((Usr.getName() == Nam) & (Usr.getEmail() == Em)):
            tkinter.messagebox.showinfo('Logged In', ('You are now logged in,' + " " + Usr.getName() + "."))
            break
    
    if (NamEx & EmEx):
        tkinter.messagebox.showinfo('Invalid Credentials', ('There is no user that\'s both named:' + " " + Nam + "and an email of" + "Em" + "."))
        
    elif NamEx:
        tkinter.messagebox.showinfo('Invalid Credentials', ('There is a user that\'s named:' + " " + Nam + ", but they don't have an email of" + "Em" + "."))
    
    elif EmEx:
        tkinter.messagebox.showinfo('Invalid Credentials', ('There is no user that\'s named:' + " " + Nam + ", but there is someone with an email of" + "Em" + "."))    
    
    else:
        tkinter.messagebox.showinfo('Invalid Credentials', ('There is no user with the name of:' + " " + Nam + "and an email of" + "Em" + "."))

def SignInForm(Type):
    return Type

#### Okay... So bound functions can't take parameters...

root = Tk()

CredFrame = Frame(root)
CredFrame.pack()

entrytext = StringVar()

NameLabel = Label(CredFrame, text="Name")
EmailLabel = Label(CredFrame, text="Email")
NameEntry = Entry(CredFrame, textvariable=entrytext)
EmailEntry = Entry(CredFrame, textvariable=entrytext)

entrytext.set("Test")

# widgets centered by default, sticky option to change
NameLabel.grid(row=0, sticky=E)
EmailLabel.grid(row=1, sticky=E)

NameEntry.grid(row=0, column=1)
EmailEntry.grid(row=1, column=1)

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
