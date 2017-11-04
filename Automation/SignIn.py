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

def readProf(event, filename):
    f = file("filename" + ".txt", "r")

    Prof = []

    # Need to count lines as that line count is the index for the users in Users that you're presumably returning!

    # Gonna call it "li for now..."

    for line in f.readlines():
        l = line.split()

        # Could make the user and email pair now, instead of doing it when making the object...

        if l[0] == "P":
            Users[li] = Professor(l[1], l[2])

        if l[0] == "S":
            Users[li] = Student(l[1], l[2])

    f.close()

    return 0

## Remember, Python or Tkinter or whatever doesn't check if these frames exist. these functions, when called by a buttonpress, act as if they're in the same scope as the button, or something.

def Registering(event):
    ButtonFrame.pack_forget()

    PassFrame = Frame(BottomFrame)
    PassFrame.pack(side=BOTTOM)

    button_1 = Button(PassFrame, text="Register")
    button_1.bind("<Button-1>", writeUser(User(NameEntry.get(), Email.get())))
    button_1.pack()

def SignIn(event):
    CredFrame.pack_forget()
    SignInForm("Student")

def SignInForm(Type):
    return Type

#### Okay... So bound functions can't take parameters...

global UserAttribs, StudAttribs, ProfAttribs # User, Student, and Professor Attributes.

UserAttribs = {"Name":[], "Email":[]}

UserWords = [StringVar()]*len(UserAttribs) ## This is where it breaks. I have no idea why I can't use StringVar() like this...

FormFrame(UserAttribs, UserWords, root)

root = Tk()

def FrameMake(locations):
    # Returns a list of frames, or a dictionary of frames or something, that corresponds to the locations...

    frames = []

    for l in locations:
        frames.append(Frame(root).pack(side=l))

def FormFrame(AttribList, textlist, pf):

    # pf = ParentFrame = The Frame where you want the Form Frame to be in.

    Frame(root).pack()

    kys = list(UserAttribs.keys())

    if textlist != None:
        for i in len(UserAttribs):
            Ent = [Label(Frame(root), text=UserAttribs[i]), Entry(Frame(root), textvariable=textlist[i])]
            Ent[0].grid(row=i, sticky=E)
            Ent[1].grid(row=i+1, sticky=E)
            UserAttribs[kys[i]].extend(Ent)

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
