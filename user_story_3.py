from tkinter import *
root = Tk()

def MCQ():
    def write_questions():
        nq = 'MCQ: ' + new_question.get('1.0',END)
        fh = open('questions.txt', 'a')
        fh.write(nq)
        fh.close()
        question_window.destroy()
        
    question_window = Toplevel(root)
    question_window.geometry('600x300')
    question_window.title('Multiple Choice window')
    
    Label(question_window, text='Type your quetion here: ', font=20,pady=20).pack()
    new_question = Text(question_window, width=40, height=10)
    new_question.pack()
    
    
    confirm_button = Button(question_window,text='Confirm', command=write_questions)
    exit_button = Button(question_window,text='Exit', command=question_window.destroy)
    confirm_button.pack(side=LEFT,padx=150)
    exit_button.pack(side=LEFT,padx=50)
  
def FBQ():
    def write_questions():
        nq = 'FBQ: ' + new_question.get('1.0',END)
        fh = open('questions.txt', 'a')
        fh.write(nq)
        fh.close()
        question_window.destroy()
        
    question_window = Toplevel(root)
    question_window.geometry('600x300')
    question_window.title('Fill in the blank window')   
    
    Label(question_window, text='Type your quetion here: ', font=20,pady=20).pack()
    new_question = Text(question_window, width=40, height=10)
    new_question.pack()
    
    confirm_button = Button(question_window,text='Confirm', command=write_questions)
    exit_button = Button(question_window,text='Exit', command=question_window.destroy)
    confirm_button.pack(side=LEFT,padx=150)
    exit_button.pack(side=LEFT,padx=50)
def MAQ():
    def write_questions():
        nq = 'MAQ: ' + new_question.get('1.0',END)
        fh = open('questions.txt', 'a')
        fh.write(nq)
        fh.close()
        question_window.destroy()
        
    question_window = Toplevel(root)
    question_window.geometry('600x300')
    question_window.title('Matching window')   
    
    Label(question_window, text='Type your quetion here: ', font=20,pady=20).pack()
    new_question = Text(question_window, width=40, height=10)
    new_question.pack()
    
    confirm_button = Button(question_window,text='Confirm', command=write_questions)
    exit_button = Button(question_window,text='Exit', command=question_window.destroy)
    confirm_button.pack(side=LEFT,padx=150)
    exit_button.pack(side=LEFT,padx=50)



top_Label = Label(root, text = 'Choose your question type here:')

 
MCQbutton=Button(text="Multiple Choice", command=MCQ)
FBQbutton=Button(text="Fill in the blanks", command=FBQ)
MAQbutton=Button(text="Matching", command=MAQ)



root.title("Create Questions")
top_Label.pack()
MCQbutton.pack(side = LEFT)
FBQbutton.pack(side = LEFT)
MAQbutton.pack(side = LEFT)

root.mainloop()