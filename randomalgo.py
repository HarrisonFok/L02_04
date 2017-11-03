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
    return random.randint(L[0], L[1])

def makeAssignment(L):
    '''

    :param L: the list of all the selected questions [[q1], [q2], [q3]]
    '''
    result = []
    for question in L:
        allrange = question[3].split(',')
        vals = []
        for index in allrange:
            vals.append(RandomInRange(index.split('|')))
        i = 0
        for val in vals:
            old = "VAR"+ str(i)
            Q_B = question[2]
            Q_A = question[4]
            Q_B.replace(old, vals[i])
            Q_A.replace(old, vals[i])
            i += 1
        result.append([question[1], Q_B, Q_A])

    with open("Assignment.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(result)


if __name__ == '__main__':
    makeAssignment()
