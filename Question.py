class Question:
    '''Class for a question'''
    
    def __init__(self, question_id, question_type, question, answer,\
                 student_answer=None):
        self._question_id = question_id
        self._question_type = question_type
        self._question = question
        self._answer = answer
        self._student_answer = student_answer
        
    def getQuestionId(self):
        return self._question_id
    
    def setQuestionId(self, question_id):
        self._question_id = question_id
        
    def getQuestionType(self):
        return self.question_type
    
    def setQuestionType(self, question_type):
        self._question_type = question_type
        
    def getQuestion(self):
        return self._question
    
    def setQuestion(self, question):
        self._question = question
        
    def getAnswer(self):
        return self._answer
    
    def setAnswer(self, answer):
        self._answer = answer
        
    def getStudentAnswer(self):
        return self._student_answer
    
    def setStudentAnswer(self, student_answer):
        self._student_answer = student_answer
        
    def __eq__(self, otherQ):
        return ((self._question_id == otherQ._question_id) and
                (self._question_type == otherQ._question_type) and 
                (self._question == otherQ._question) and 
                (self._answer == otherQ._answer))