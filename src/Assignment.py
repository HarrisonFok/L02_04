from Question import *

from random import randint

class Assignment:
    '''Class for an assignment'''
    
    def __init__(self, list_of_questions, name):
        '''(Assignment, String, [Question]) -> NoneType
        Initialize an Assignment object
        '''
        self._assignment_id = randint(000000000, 999999999)
        self._visibility = False
        self._list_of_questions = list_of_questions
        self._deadline = None
        self._name = name
        
    def getDeadline(self):
        return self._deadline
    
    def setDeadline(self, newDeadline):
        '''(Assignment, str) -> NoneType
        Sets the deadline of the assignment
        '''
        self._deadline = newDeadline
        
    def getAssignmentId(self):
        return self._assignment_id
    
    def setAssignmentId(self, newId):
        self._assignment_id = newId
        
    def getNumQuestions(self):
        return len(self.getListOfQuestions())
        
    def getListOfQuestions(self):
        '''(Assignment) -> [Question]
        Returns the list of Question objects
        '''
        return self._list_of_questions
    
    def setListOfQuestions(self, list_of_questions):
        '''(Assignment, [Question]) -> NoneType
        Sets the list of questions (list of Question objects)
        '''
        self._list_of_questions = list_of_questions
        
    def setStudentAnswerAtIndex(self, index, studentAnswer):
        '''(Assignment, int, str) -> NoneType
        Sets the student answer of the Question object at index i
        '''
        for i in range(len(self.getListOfQuestions())):
            if i == index:
                self.getListOfQuestions()[i].setStudentAnswer(studentAnswer)
                
    def checkIfPerfect(self):
        '''(Assignment) -> bool
        Returns whether or not the assignment is done perfectly
        '''
        perfect = False
        numCorrect = 0
        for Q in self.getListOfQuestions():
            if Q.getCorrectness() == True:
                numCorrect += 1
        
        if numCorrect == len(self.getListOfQuestions()):
            perfect = True
            
        return perfect
        
    def assignTo(self, student):
        '''(Assignment, Student) -> NoneType
        Assigns an Assignment to a Student
        '''
        student.assignTo(self)
        
    def setVisibility(self, visibility):
        '''(Assignment, bool) -> NoneType
        Sets the visibility of an Assignment
        '''
        self._visibility = visibility

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

