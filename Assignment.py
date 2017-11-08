class Assignment:
    '''Class for an assignment'''
    
    def __init__(self, student_no, student_name, list_of_questions):
        '''(Assignment, string, string, [Question]) -> NoneType
        Initialize an Assignment object
        '''
        self._student_no = student_no
        self._student_name = student_name
        self._list_of_questions = list_of_questions
        
    def get_student_no(self):
        return self._student_no
    
    def set_student_no(self, student_no):
        self._student_no = student_no
        
    def get_student_name(self):
        return self._student_name
    
    def set_student_name(self, student_name):
        self._student_name = student_name
        
    def get_list_of_questions(self):
        return self._list_of_questions
    
    def set_list_of_questions(self, list_of_questions):
        '''(Assignment, [Question]) -> NoneType
        Sets the list of questions (list of Question objects)
        '''
        self._list_of_questions = list_of_questions