from tkinter import *

def Radios(FrameName, LabelText, ButtonTexts, Variable=v, DisplaySettings=None):

  if DisplaySettings is None:
  
    Radio = [Label(FrameName, text=LabelText, justify = LEFT, padx = 20).pack()]

    for t in ButtonTexts:

      Radio.append(Radiobutton(FrameName, text=t, padx = 20, variable=v, value=1).pack(anchor=W))
