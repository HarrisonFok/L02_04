# Countdown using Tkinter
from tkinter import *
import time
import tkinter.messagebox

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.entryWidget = Entry(frame)
        self.entryWidget["width"] = 15
        self.entryWidget.pack(side=LEFT)
        self.hi_there = Button(frame,text="Start",command=self.start)
        self.hi_there.pack(side=LEFT)
        self.button = Button(frame,text="QUIT",fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
    def start(self):
        text = self.entryWidget.get().strip()
        if text != "":
            num = int(text)
            self.countDown(num)

    def countDown(self,seconds):
        lbl1.config(bg='yellow')
        lbl1.config(height=3, font=('times',20,'bold'))
        for k in range(seconds, 0, -1):
            lbl1["text"] = k
            root.update()
            time.sleep(1)
        lbl1.config(bg='red')
        lbl1.config(fg='white')
        lbl1["text"] = "Time up!"
        tkinter.messagebox.showinfo("Time up!","Time up!")

root = Tk()
root.title("Countdown")
lbl1 = Label()
lbl1.pack(fill=BOTH, expand=1)
app = App(root)
root.mainloop()