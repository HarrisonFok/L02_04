from tkinter import *

root = Tk()

header = Label(root, text="Student Profile Registration").grid(row=0,column=1)

emailLabel = Label(root, text="Email:").grid(row=1)
emailEntry = Entry(root, width=50).grid(row=1, column=1)

passwordLabel = Label(root, text="Password:").grid(row=2)
passwordEntry = Entry(root, show="*", width=50).grid(row=2, column=1)

passwordDupLabel = Label(root, text="Confirm Password:").grid(row=3)
passwordDupEntry = Entry(root, show="*", width=50).grid(row=3, column=1)

studentNumLabel = Label(root, text="Student Number:").grid(row=4)
studentNumEntry = Entry(root, width=50).grid(row=4, column=1)

submitBtn = Button(root, text="Submit").grid(row=5, column=1)

# set fixed window size
root.resizable(width=False, height=False)

root.mainloop()
