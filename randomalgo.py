import random
import SelectQuestions

def RandomInRange(L):
    """
    len(L) == 2
    list[int(min), int(max)] -> int
    min <= max
    a function that return a integer randomly in the range(min,max)

    //RandomInRange(2, 6)
    //5

    """
    return random.randint(L[0], L[1])

def makeAssignment(Assignment):
    """
    !!!to Harrison i dont know where is the lines in ur code to make the assignment.txt
    read the following code to add them to urs I comment for select questions

    :param Assignment: a file Assignment.txt with all selected questions variable unknown
    :return: 0 but the variable all randomized
    """
    Ques = open("question.txt", 'r')
    allQ = Ques.readlines()
    # select the questiones in ur way as sel_Q
    # sel_Q is the list of every questions seperated by \n
    sel_Q = SelectQuestions.chosenQuestions

    AS = open("Assignment.txt", 'w')
    for question in sel_Q:
        # replace the var with the random value using the range after them and save them in Assignment.txt
        nl = ""
        formatq = question
        while(formatq.find('$')!=-1):
            left = formatq.find('$')
            right = formatq.find('$', left + 1)
            nl += formatq[:left]
            minv = int(formatq[formatq.find('[') + 1])
            maxv = int(formatq[formatq.find(']') - 1])
            L = [minv, maxv]
            var = str(L.RandomInRange())
            nl = nl + ' ' + var + ' '
            formatq = formatq[maxv + 2:]
        nl += '\n'
        AS.write(nl)
    AS.close()
