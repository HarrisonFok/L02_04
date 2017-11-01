from tkinter import *
import random
root = Tk()
QID = 00000000
def MCQ():
    li = [0]
    def write_questions():
        nq = 'MCQ'+"_"+str(random.randrange(99999999)) + ": " + new_question.get('1.0',END).strip() +' ||| Answer Formula:'+ answer_formula.get('1.0',END)
        fh = open('questions.txt', 'a')
        fh.write(nq)
        fh.close()
        question_window.destroy()
    def insert_var():
        new_question.insert("insert", " VAR"+str(li[0])+' ')
        li[0]+=1
    def insert_plus():
        answer_formula.insert("insert", " + ")
    def insert_minus():
        answer_formula.insert("insert", " - ")
    def insert_time():
        answer_formula.insert("insert", " * ")
    def insert_divided():
        answer_formula.insert("insert", " / ")    
        
    question_window = Toplevel(root)
    question_window.geometry('600x530')
    question_window.title('Multiple Choice window')   
    
    Label(question_window, text='Type your quetion here: ', font=20,pady=20).pack()
    new_question = Text(question_window, width=40, height=10)
    new_question.pack()
    
    var_button = Button(question_window,text="insert Variable",command=insert_var)
    var_button.pack()    
    
    Label(question_window, text='Type your answer formula here: ', font=20,pady=20).pack()
    answer_formula = Text(question_window, width=40, height=5)
    answer_formula.pack()
    
    operator_button1 = Button(question_window,text="insert ' + '",command=insert_plus)
    operator_button1.pack()
    operator_button1.place(bordermode=OUTSIDE, x=50, y=320)
    
    operator_button2 = Button(question_window,text="insert ' - '",command=insert_minus)
    operator_button2.pack()
    operator_button2.place(bordermode=OUTSIDE, x=50, y=370)
    
    operator_button3 = Button(question_window,text="insert ' * '",command=insert_time)
    operator_button3.pack()
    operator_button3.place(bordermode=OUTSIDE, x=480, y=320)
    
    operator_button4 = Button(question_window,text="insert ' / '",command=insert_divided)
    operator_button4.pack()
    operator_button4.place(bordermode=OUTSIDE, x=480, y=370)
    
    
    Label(question_window, text='', font=20,pady=20).pack()
    confirm_button = Button(question_window,text='Confirm', command=write_questions)
    exit_button = Button(question_window,text='Exit', command=question_window.destroy)
    confirm_button.pack(side=LEFT,padx=150)
    exit_button.pack(side=LEFT,padx=50)
  
def FBQ():
    li = [0]
    
    def write_questions():
        nq = 'FBQ'+"_"+str(random.randrange(99999999)) + ": " + new_question.get('1.0',END).strip() +' ||| Answer Formula:'+ answer_formula.get('1.0',END)
        fh = open('questions.txt', 'a')
        fh.write(nq)
        fh.close()
        question_window.destroy()
    def insert_var():
        new_question.insert("insert", " VAR"+str(li[0])+' ')
        li[0]+=1
    def insert_plus():
        answer_formula.insert("insert", " + ")
    def insert_minus():
        answer_formula.insert("insert", " - ")
    def insert_time():
        answer_formula.insert("insert", " * ")
    def insert_divided():
        answer_formula.insert("insert", " / ")    
        
    question_window = Toplevel(root)
    question_window.geometry('600x530')
    question_window.title('Fill in the blank window')   
    
    Label(question_window, text='Type your quetion here: ', font=20,pady=20).pack()
    new_question = Text(question_window, width=40, height=10)
    new_question.pack()
    
    var_button = Button(question_window,text="insert Variable",command=insert_var)
    var_button.pack()    
    
    Label(question_window, text='Type your answer formula here: ', font=20,pady=20).pack()
    answer_formula = Text(question_window, width=40, height=5)
    answer_formula.pack()
    
    operator_button1 = Button(question_window,text="insert ' + '",command=insert_plus)
    operator_button1.pack()
    operator_button1.place(bordermode=OUTSIDE, x=50, y=320)
    
    operator_button2 = Button(question_window,text="insert ' - '",command=insert_minus)
    operator_button2.pack()
    operator_button2.place(bordermode=OUTSIDE, x=50, y=370)
    
    operator_button3 = Button(question_window,text="insert ' * '",command=insert_time)
    operator_button3.pack()
    operator_button3.place(bordermode=OUTSIDE, x=480, y=320)
    
    operator_button4 = Button(question_window,text="insert ' / '",command=insert_divided)
    operator_button4.pack()
    operator_button4.place(bordermode=OUTSIDE, x=480, y=370)    
    
    confirm_button = Button(question_window,text='Confirm', command=write_questions)
    exit_button = Button(question_window,text='Exit', command=question_window.destroy)
    confirm_button.pack(side=LEFT,padx=150)
    exit_button.pack(side=LEFT,padx=50)




top_Label = Label(root, text = 'Choose your question type here:')

 
button1=Button(text="Multiple Choice", command=MCQ)
button2=Button(text="Fill in the blanks", command=FBQ)



root.title("Create Questions")
top_Label.pack()
button1.pack(side = LEFT)
button2.pack(side = LEFT)

root.mainloop()