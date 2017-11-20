class Question:
    '''Class for a question'''
    
    def __init__(self, question_id, question_type, question, answer, assignment_id,\
        assignment_name, due_date, professor_id,  student_id, student_answer=None, correctness=False):
        self._question_id = question_id
        self._question_type = question_type
        self._question = question
        self._answer = answer
        self._assignment_id = assignment_id
        self._assignment_name = assignment_name
        self._due_date = due_date
        self._professor_id = professor_id
        self._student_id = student_id
        # Additional attributes
        self._student_answer = student_answer
        self._correctness = correctness
        
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

    def getAssignmentId(self):
        return self._assignment_id

    def setAssignmentId(self, assignment_id):
        self._assignment_id = assignment_id

    def getAssignmentName(self):
        return self._assignment_name

    def setAssignmentName(self, assignment_name):
        self._assignment_name = assignment_name

    def getDueDate(self):
        return self._due_date

    def setDueDate(self, due_date):
        self._due_date = due_date

    def getProfessorId(self):
        return self._professor_id

    def setProfessorId(self, professor_id):
        self._professor_id = professor_id

    def getStudentId(self):
        return self._student_id

    def setStudentId(self, student_id):
        self._student_id = student_id
        
    def getStudentAnswer(self):
        return self._student_answer
    
    def setStudentAnswer(self, student_answer):
        self._student_answer = student_answer
        
    def getCorrect(self):
        return self._correct
    
    def getCorrectness(self):
        return self._correctness
    
    def setCorrectness(self, correctness):
        '''(Question, bool) -> NoneType
        Sets whether the question is answered correctly
        '''
        self._correctness = correctness
        
    def __eq__(self, otherQ):
        return ((self._question_id == otherQ._question_id) and
                (self._question_type == otherQ._question_type) and 
                (self._question == otherQ._question) and 
                (self._answer == otherQ._answer))