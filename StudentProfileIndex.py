from tkinter import *

root = Tk()

header = Label(root, text="Student Profile Registration").grid(row=0,column=1)

emailLabel = Label(root, text="Email:").grid(row=1)
emailEntry = Entry(root, width=50).grid(row=1, column=1)

passwordLabel = Label(root, text="Password:").grid(row=2)
passwordEntry = Entry(root, width=50).grid(row=2, column=1)

submitBtn = Button(root, text="Submit").grid(row=3, column=1)

root.mainloop()
