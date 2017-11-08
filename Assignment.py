class Assignment:
    '''Class for an assignment'''
    
    def __init__(self, assignment_no, list_of_questions):
        '''(Assignment, String, Question]) -> NoneType
        Initialize an Assignment object
        '''
        self._assignment_no = assignment_no
        self._visibility = False
        self._list_of_questions = list_of_questions
        
    def getAssignmentNo(self):
        return self._assignment_no
    
    def setAssignmentNo(self, assignment_no):
        self._assignment_no = assignment_no
        
    def getListOfQuestions(self):
        return self._list_of_questions
    
    def setListOfQuestions(self, list_of_questions):
        '''(Assignment, [Question]) -> NoneType
        Sets the list of questions (list of Question objects)
        '''
        self._list_of_questions = list_of_questions
        
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