import random
import io
import csv

from Assignment import *
from Question import *

# judgment a char is a operation or not
def is_operation(oper):
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        return True
    else:
        return False


# split expression
def mixed_operation(exp):
    exp_list = list(exp)
    temp = ''
    behavor_list = []
    i = 0
    length = len(exp_list)
    for item in exp_list:
        if is_operation(item):
            behavor_list.append(int(temp))
            behavor_list.append(item)
            temp = ''
        else:
            temp += item

        if i == length - 1:
            behavor_list.append(int(temp))
            break;

        i += 1

    return behavor_list


# cal a o b
def get_aob(a, o, b):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a / b


# Calculation op1 and op2('*' and '/' or '+' and '-')
def cal_op1_op2(exp_list, op1, op2):
    if len(exp_list) == 1:
        return exp_list

    i = 0
    has_op = False
    for i in range(2, len(exp_list), 2):
        a = exp_list[i - 2]
        o = exp_list[i - 1]
        b = exp_list[i]
        if o == op1 or o == op2:
            has_op = True
            exp_list[i - 2] = get_aob(a, o, b)
            del exp_list[i]
            del exp_list[i - 1]
            break

    if has_op == False:
        return exp_list

    return cal_op1_op2(exp_list, op1, op2)


# cal exp
def cal_exp(exp_list):
    exp_list = cal_op1_op2(exp_list, '*', '/')
    exp_list = cal_op1_op2(exp_list, '+', '-')

    return exp_list[0]

def RandomInRange(L):
    """
    A function that return a integer randomly in the range(min,max)
    len(L) == 2
    list[int(min), int(max)] -> int
    min <= max
    
    >>> RandomInRange(2, 6)
    >>> 5
    """
    return random.randint(int(L[0]), int(L[1]))

def makeAssignment(L, addInfo, profId, assignmentId):
    '''(list, list, str, str) -> Assignment
    Return an Assignment object based on the given questions in L, the additional information in addInfo, the professor id, and the assignment id
    Note: the returned Assignment object will consist of Question objects
    Note: L is the list of all the selected questions [[q1], [q2], [q3], ...], where each q consists of the question id, question topic, question type, question body, range of variables, and question formula
    '''
    questionObjs = []
    result = []
    for question in L:
        allrange = question[4].split(',')
        vals = []
        for index in allrange:
            vals.append(RandomInRange(index.split('|')))
        i = 0
        Q_B = question[3]
        Q_A = question[5]
        for val in vals:
            old = 'VAR'+ str(i)
            Q_B = Q_B.replace(old, str(vals[i]))
            Q_A = Q_A.replace(old, str(vals[i]))
            leftk = Q_B.find('(')
            rightk = Q_B.find(')')
            Q_B = Q_B[:leftk] + Q_B[rightk + 1:]
            i += 1
        answer = cal_exp(mixed_operation(Q_A))
        # Initialize a new Question object
        newQ = Question(question[0], question[2], Q_B, answer, assignmentId, addInfo[0], addInfo[1], profId, addInfo[2])
        # Append the new question into questionObjs
        questionObjs.append(newQ)
        # Append the necessary question info into result
        result.append([question[0], question[2], Q_B, answer, assignmentId, addInfo[0], addInfo[1], profId, addInfo[2]])

    newAssignmentObj = Assignment(assignmentId, questionObjs)
    
    with open("Assignment.csv", "a") as csvfile:
        csvfile.seek(0)
        writer = csv.writer(csvfile)
        writer.writerows(result)

    return newAssignmentObj

if __name__ == '__main__':
    makeAssignment([["25306175", "Topic_5", "MCQ", "What is VAR0 + VAR1", "12|15, 13|16", "VAR0+VAR1"],["25306175", "Topic_5", "MCQ", "What is VAR0 + VAR1", "12|15, 13|16", "VAR0+VAR1"] ], ["Unit 20 Test", "01-Nov-19", "2"], "1", "12")
    #makeAssignment([["25306175", "Topic_5", "MCQ", "What is VAR0 + VAR1", "12|15, 13|16", "VAR0+VAR1", "1", "Unit 1 Test", "01-Nov-17", "1", "1"], ["25306175", "Topic_5", "MCQ", "What is VAR0 + VAR1", "12|15, 13|16", "VAR0+VAR1", "1", "Unit 1 Test", "01-Nov-17", "1", "1"]])
