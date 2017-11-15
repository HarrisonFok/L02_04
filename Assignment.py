from Question import *

class Assignment:
    '''Class for an assignment'''
    
    def __init__(self, list_of_questions):
        '''(Assignment, String, [Question]) -> NoneType
        Initialize an Assignment object
        '''
        #self._assignment_no = assignment_no
        self._visibility = False
        self._list_of_questions = list_of_questions
        
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