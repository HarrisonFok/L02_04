import random
import io
import csv

def RandomInRange(L):
    """
    len(L) == 2
    list[int(min), int(max)] -> int
    min <= max
    a function that return a integer randomly in the range(min,max)

    //RandomInRange(2, 6)
    //5

    """
    return random.randint(int(L[0]), int(L[1]))

def makeAssignment(L):
    '''

    :param L: the list of all the selected questions [[q1], [q2], [q3]]
    '''
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
            i += 1
        result.append([question[0], question[2], Q_B, Q_A])

    with open("Assignment.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)


if __name__ == '__main__':
    makeAssignment([["25306175", "Topic_5", "MCQ", "What is VAR0 + VAR1", "12|15, 13|16", "VAR0+VAR1"],["25306175", "Topic_5", "MCQ", "What is VAR0 + VAR1", "12|15, 13|16", "VAR0+VAR1"] ])
