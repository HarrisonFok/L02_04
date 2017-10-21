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

def writeName(event):
    #fi = file("C:\\Users\\Andy\\Desktop\\fi", "w")

    #fi.write((entry_1).get())
    #fi.write((entry_2).get())

    #fi.close()
    return 0

def readName(event):
    #fi = file("C:\\Users\\Andy\\Desktop\\fi", "w")

    #fi.write((entry_1).get())
    #fi.write((entry_2).get())

    #fi.close()
    return 0

def SignInForm(typeof):
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
    button_1.bind("<Button-1>", writeName)
    button_1.grid(columnspan=3)

    if checked: print("hi!")#Do stuff

button_1 = Button(root, text="Sign in as Professor")
button_1.bind("<Button-1>", SignInForm("professor"))
button_1.grid(side=BOTTOM)

button_1 = Button(root, text="Sign in as Student")
button_1.bind("<Button-1>", SignInForm("student"))
button_1.grid(side=BOTTOM)

root.mainloop()

### You can also put the form code inside the def function to make a form pop up when you click that button...:
