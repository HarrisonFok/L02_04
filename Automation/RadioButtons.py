from tkinter import *

def Radios(FrameName, LabelText, ButtonTexts, Variable, DisplaySettings=None):

  if DisplaySettings is None:
  
    Radio = [Label(FrameName, text=LabelText, justify = LEFT, padx = 20).pack()]

    for t in ButtonTexts

    Radiobutton(root, text="Python", padx = 20, variable=v, value=1).pack(anchor=W)

    Radiobutton(root, text="Perl", padx = 20, variable=v, value=2).pack(anchor=W)

    return(Variable)
