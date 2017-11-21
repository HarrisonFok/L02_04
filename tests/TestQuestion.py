import unittest
import sys
sys.path.insert(0, '../src')
import Question

class TestQuestion(unittest.TestCase):

	def testInit(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		
		question_id = "25306175"
		question_type = "MCQ"
		question = "What is 13 + 13"
		answer = "26"
		assignment_id = "1"
		assignment_name = "Unit 1 Test"
		dueDate = "01-Nov-17"
		professor_id = "1"
		student_id = "1"
		student_answer = None
		correctness = False

		creationSuccess = ((question_a.getQuestionId() == question_id) and
			(question_a.getQuestionType() == question_type) and 
			(question_a.getQuestion() == question) and (question_a.getAnswer() == answer)
			and (question_a.getAssignmentId() == assignment_id) and 
			(question_a.getAssignmentName() == assignment_name) and 
			(question_a.getDueDate() == dueDate) and (question_a.getProfessorId() == professor_id)
			and (question_a.getStudentId() == student_id) and 
			(question_a.getStudentAnswer() == student_answer) and (question_a.getCorrectness() == correctness))

		self.assertTrue(creationSuccess)

	def testGetQuestionId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_id = "25306175"
		self.assertTrue(question_a.getQuestionId() == question_id)

	def testSetQuestionId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_id = "000"
		question_a.setQuestionId(question_id)
		self.assertTrue(question_a.getQuestionId() == question_id)

	def testGetQuestionType(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_type = "MCQ"
		self.assertTrue(question_a.getQuestionType() == question_type)

	def testSetQuestionType(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_type = "FIB"
		question_a.setQuestionType(question_type)
		self.assertTrue(question_a.getQuestionType() == question_type)

	def testGetQuestion(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question = "What is 13 + 13"
		self.assertTrue(question_a.getQuestion() == question)

	def testSetQuestion(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question = "What is 0 + 0"
		question_a.setQuestion(question)
		self.assertTrue(question_a.getQuestion() == question)

	def testGetAnswer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		answer = "26"
		self.assertTrue(question_a.getAnswer() == answer)

	def testSetAnswer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		answer = "26"
		question_a.setAnswer(answer)
		self.assertTrue(question_a.getAnswer() == answer)

	def testGetAssignmentId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		assignment_id = "1"
		self.assertTrue(question_a.getAssignmentId() == assignment_id)

	def testSetAssignmentId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		new_assignment_id = "6"
		question_a.setAssignmentId(new_assignment_id)
		self.assertTrue(question_a.getAssignmentId() == new_assignment_id)

	def testGetAssignmentName(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		assignment_name = "Unit 1 Test"
		self.assertTrue(question_a.getAssignmentName() == assignment_name)

	def testSetAssignmentName(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		assignment_name = "Unit 2 Test"
		question_a.setAssignmentName(assignment_name)
		self.assertTrue(question_a.getAssignmentName() == assignment_name)

	def testGetDueDate(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		dueDate = "01-Nov-17"
		self.assertTrue(question_a.getDueDate() == dueDate)

	def testSetDueDate(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		newDueDate = "03-Nov-17"
		question_a.setDueDate(newDueDate)
		self.assertTrue(question_a.getDueDate() == newDueDate)

	def testGetProfId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		prof_id = "1"
		self.assertTrue(question_a.getProfessorId() == prof_id)

	def testSetProfId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		newProfId = "23"
		question_a.setProfessorId(newProfId)
		self.assertTrue(question_a.getProfessorId() == newProfId)

	def testGetStudentId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		studId = "1"
		self.assertTrue(question_a.getStudentId() == studId)

	def testSetStudentId(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		newStudId = "2"
		question_a.setStudentId(newStudId)
		self.assertTrue(question_a.getStudentId() == newStudId)

	def testGetStudentAnswer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		self.assertTrue(question_a.getStudentAnswer() == None)

	def testSetStudentAnswer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		studentAnswer = "5"
		question_a.setStudentAnswer(studentAnswer)
		self.assertTrue(question_a.getStudentAnswer() == studentAnswer)

	def testGetCorrectness(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_a.setStudentAnswer("25")
		self.assertFalse(question_a.getCorrectness())

	def testEquals(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_b = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		self.assertTrue(question_a == question_b)

	def testNotEquals(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_b = Question.Question("25306175", "FIB", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		self.assertFalse(question_a == question_b)

if __name__ == '__main__':
    unittest.main(exit=False)