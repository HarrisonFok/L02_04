from tkinter import *

root = Tk()

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

def writeUser(event, filename, User):
    f = file("filename", "w")

    if User.isinstance(Student):
        f.writelines("student" + " " + User.getName() + " " + User.getName())

    if User.isinstance(Professor):
        f.writelines("professor" + " " + User.getName() + " " + User.getName())

    f.close()

def readUsers(event, filename):
    f = file("filename", "r")

    Users = []

    # Need to count lines as that line count is the index for the users in Users that you're presumably returning!

    # Gonna call it "li for now..."

    for line in f.readlines():
        l = line.split()

        # Could make the user and email pair now, instead of doing it when making the object...

        if l[0] == "Professor":
            Users[li] = Professor(l[1], l[2])

        if l[0] == "Student":
            Users[li] = Student(l[1], l[2])

    f.close()

    return Users

def SignInFormProf(event):
    SignInForm("Professor")

def SignInFormStud(event):
    SignInForm("Student")

def SignInForm(Type):

    print(Type)

    label_1 = Label(root, text="Name")
    label_2 = Label(root, text="Email")
    entry_1 = Entry(root)
    entry_2 = Entry(root)

    # widgets centered by default, sticky option to change
    label_1.grid(row=0, sticky=E)
    label_2.grid(row=1, sticky=E)

    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)

    checked = 0

    c = Checkbutton(root, text="Keep me logged in", variable=checked)
    c.grid(columnspan=2)

    button_1 = Button(root, text="Print Message")

    button_1.bind("<Button-1>", writeUser)
    button_1.grid(columnspan=3)

    if checked: print("hi!") #Do stuff


#### Okay... So bound functions can't take parameters...

button_1 = Button(root, text="Sign in as Professor")
button_1.bind("<Button-1>", SignInFormProf)
button_1.pack()

button_2 = Button(root, text="Sign in as Student")
button_2.bind("<Button-1>", SignInFormStud)
button_2.pack()

root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...:
