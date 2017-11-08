class Question:
    '''Class for a question'''
    
    def __init__(self, question_id, question_type, question, answer,\
                 student_answer):
        self._question_id = question_id
        self.question_type = question_type
        self.question = question
        self.answer = answer
        self.student_answer = student_answer
        
    def get_question_id(self):
        return self._question_id
    
    def set_question_id(self, question_id):
        self._question_id = question_id
        
    def get_question_type(self):
        return self.question_type
    
    def set_question_type(self, question_type):
        self.question_type = question_type
        
    def get_question(self):
        return self.question
    
    def set_question(self, question):
        self.question = question
        
    def get_answer(self):
        return self.answer
    
    def set_answer(self, answer):
        self.answer = answer
        
    def get_student_answer(self):
        return self.student_answer
    
    def set_student_answer(self, student_answer):
        self.student_answer = student_answer