from tkinter import *
import random
import csv

root = Tk()
root.attributes('-topmost', 'true')

def getRange(new_q):
    ''' Parses the new variables for their ranges '''

    res = ''
    while new_q.find('VAR') != -1:

        index1 = new_q.find('(')
        index2 = new_q.find('|')
        index3 = new_q.find(')')
        res += (new_q[index1 +1 : index2] + '|' + new_q[index2+1:index3] + ',')
        new_q = new_q[index3+1:]

    return res[:-1]



def MCQ():
    li = [0]

    def write_questions():
        new_q = new_question.get('1.0', END).strip()

        # get the range

        varRanges = getRange(new_q)

        nq = (
            str(random.randrange(10000000, 99999999)),
            get_topic(),
            'MCQ',
            new_q,
            varRanges,
            answer_formula.get('1.0', END),
            )
        fh = open('questions.csv', 'a')
        writer = csv.writer(fh, delimiter=',')
        writer.writerow(nq)
        fh.close()
        question_window.destroy()

    def insert_var():
        new_question.insert('insert', ' VAR' + str(li[0]) + '(min|max)'
                             + ' ')
        li[0] += 1

    def insert_plus():
        answer_formula.insert('insert', ' + ')

    def insert_minus():
        answer_formula.insert('insert', ' - ')

    def insert_time():
        answer_formula.insert('insert', ' * ')

    def insert_divided():
        answer_formula.insert('insert', ' / ')

    def get_topic():
        return topic_num.get()

    question_window = Toplevel(root)
    question_window.geometry('810x750')
    question_window.attributes('-topmost', 'true')
    question_window.title('Multiple Choice window')

    topic_L = Label(question_window, text='Related topic:', font=20,
                    pady=20)
    topic_L.pack()
    topic_L.place(bordermode=OUTSIDE, x=10, y=0)
    topic_num = StringVar(question_window)
    topic_num.set('choose here')  # default value
    topic = OptionMenu(
        question_window,
        topic_num,
        'Topic_1',
        'Topic_2',
        'Topic_3',
        'Topic_4',
        'Topic_5',
        )
    topic.pack()
    topic.place(bordermode=OUTSIDE, x=10, y=50)


    Label(question_window, text='Type your question here:', font=20,
          pady=20).pack()

    new_question = Text(question_window, relief=GROOVE, width=40, height=10, borderwidth=2, highlightthickness=0)
    new_question.pack()

    var_button = Button(question_window, text='Insert Variable',
                        command=insert_var)
    var_button.pack()

    Label(question_window, text='Type your answer formula here: ',
          font=20, pady=20).pack()
    answer_formula = Text(question_window, width=40, height=5, relief=GROOVE, borderwidth=2, highlightthickness=0)
    answer_formula.pack()

    operator_button1 = Button(question_window, text="insert ' + '",
                              command=insert_plus)
    operator_button1.pack()
    operator_button1.place(bordermode=OUTSIDE, x=50, y=320)

    operator_button2 = Button(question_window, text="insert ' - '",
                              command=insert_minus)
    operator_button2.pack()
    operator_button2.place(bordermode=OUTSIDE, x=50, y=370)

    operator_button3 = Button(question_window, text="insert ' * '",
                              command=insert_time)
    operator_button3.pack()
    operator_button3.place(bordermode=OUTSIDE, x=620, y=320)

    operator_button4 = Button(question_window, text="insert ' / '",
                              command=insert_divided)
    operator_button4.pack()
    operator_button4.place(bordermode=OUTSIDE, x=620, y=370)

    Label(question_window, text='', font=20, pady=20).pack()
    confirm_button = Button(question_window, text='Confirm',
                            command=write_questions)
    
    instructions = """ Instructions:\n\n 1. Choose a topic from the 'Related Topic'\n 
        2. Type your question in the first text field and use the "Insert
        Variable" button to insert a new variable into the question. Set the max and min
        values for the range of possible random variables for each variable as follows: VAR0(1|20).\n
        3. Type your answer formula in the second text field. (ie. VAR0 + VAR1) This will be used to calculate the
        correct answer for the question based on the random values generated for each variable. Use the insert <operator>
        buttons to add an operator to your question formula. """

    Label(question_window, text=instructions, font=20, pady=20).pack()

    exit_button = Button(question_window, text='Exit',
                         command=question_window.destroy)
    confirm_button.pack(side=LEFT, padx=150)
    exit_button.pack(side=LEFT, padx=50)

    exit_button.place(x=400, y=680)
    confirm_button.place(x=300, y=680)



def FBQ():
    li = [0]

    def write_questions():
        new_q = new_question.get('1.0', END).strip()

        # get the range

        varRanges = getRange(new_q)

        nq = (
            str(random.randrange(10000000, 99999999)),
            get_topic(),
            'FBQ',
            new_q,
            varRanges,
            answer_formula.get('1.0', END),
            )
        fh = open('questions.csv', 'a')
        writer = csv.writer(fh, delimiter=',')
        writer.writerow(nq)
        fh.close()
        question_window.destroy()

    def insert_var():
        new_question.insert('insert', ' VAR' + str(li[0]) + '(min|max)'
                             + ' ')
        li[0] += 1

    def insert_plus():
        answer_formula.insert('insert', ' + ')

    def insert_minus():
        answer_formula.insert('insert', ' - ')

    def insert_time():
        answer_formula.insert('insert', ' * ')

    def insert_divided():
        answer_formula.insert('insert', ' / ')

    def get_topic():
        return topic_num.get()

    question_window = Toplevel(root)
    question_window.attributes('-topmost', 'true')
    question_window.geometry('810x750')
    question_window.title('Fill in the blank window')

    topic_L = Label(question_window, text='Related topic:', font=20,
                    pady=20)
    topic_L.pack()
    topic_L.place(bordermode=OUTSIDE, x=10, y=0)
    topic_num = StringVar(question_window)
    topic_num.set('choose here')  # default value
    topic = OptionMenu(
        question_window,
        topic_num,
        'Topic_1',
        'Topic_2',
        'Topic_3',
        'Topic_4',
        'Topic_5',
        )
    topic.pack()
    topic.place(bordermode=OUTSIDE, x=10, y=50)

    Label(question_window, text='Type your question here: ', font=20,
          pady=20).pack()
    new_question = Text(question_window, width=40, height=10)
    new_question.pack()

    var_button = Button(question_window, text='insert Variable',
                        command=insert_var)
    var_button.pack()

    Label(question_window, text='Type your answer formula here: ',
          font=20, pady=20).pack()
    answer_formula = Text(question_window, width=40, height=5)
    answer_formula.pack()

    operator_button1 = Button(question_window, text="insert ' + '",
                              command=insert_plus)
    operator_button1.pack()
    operator_button1.place(bordermode=OUTSIDE, x=50, y=300)

    operator_button2 = Button(question_window, text="insert ' - '",
                              command=insert_minus)
    operator_button2.pack()
    operator_button2.place(bordermode=OUTSIDE, x=50, y=350)

    operator_button3 = Button(question_window, text="insert ' * '",
                              command=insert_time)
    operator_button3.pack()
    operator_button3.place(bordermode=OUTSIDE, x=620, y=300)

    operator_button4 = Button(question_window, text="insert ' / '",
                              command=insert_divided)
    operator_button4.pack()
    operator_button4.place(bordermode=OUTSIDE, x=620, y=350)

    instructions = """ Instructions:\n\n 1. Choose a topic from the 'Related Topic'\n 
        2. Type your question in the first text field and use the "Insert
        Variable" button to insert a new variable into the question. Set the max and min
        values for the range of possible random variables for each variable as follows: VAR0(1|20).\n
        3. Type your answer formula in the second text field. (ie. VAR0 + VAR1) This will be used to calculate the
        correct answer for the question based on the random values generated for each variable. Use the insert <operator>
        buttons to add an operator to your question formula. """

    Label(question_window, text=instructions, font=20, pady=20).pack()

    confirm_button = Button(question_window, text='Confirm',
                            command=write_questions)
    exit_button = Button(question_window, text='Exit',
                         command=question_window.destroy)

    confirm_button.pack(side=LEFT, padx=150)
    exit_button.pack(side=LEFT, padx=50)

    exit_button.place(x=400, y=680)
    confirm_button.place(x=300, y=680)


top_Label = Label(root, text='Choose your question type here:')

button1 = Button(text='Multiple Choice', command=MCQ)
button2 = Button(text='Fill in the blanks', command=FBQ)

root.title('Create Questions')
# set the size of the window
top_Label.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)

if __name__ == "__main__":
    root.mainloop()