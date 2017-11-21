import unittest
import sys
sys.path.insert(0, '../src')
import Question

class TestQuestion(unittest.TestCase):

	def test_get_question_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_id = "25306175"
		self.assertTrue(question_a.getQuestionId() == question_id)

	def test_set_question_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_id = "000"
		question_a.setQuestionId(question_id)
		self.assertTrue(question_a.getQuestionId() == question_id)

	def test_get_question_type(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_type = "MCQ"
		self.assertTrue(question_a.getQuestionType() == question_type)

	def test_set_question_type(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_type = "FIB"
		question_a.setQuestionType(question_type)
		self.assertTrue(question_a.getQuestionType() == question_type)

	def test_get_question(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question = "What is 13 + 13"
		self.assertTrue(question_a.getQuestion() == question)

	def test_set_question(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question = "What is 0 + 0"
		question_a.setQuestion(question)
		self.assertTrue(question_a.getQuestion() == question)

	def test_get_answer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		answer = "26"
		self.assertTrue(question_a.getAnswer() == answer)

	def test_set_answer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		answer = "26"
		question_a.setAnswer(answer)
		self.assertTrue(question_a.getAnswer() == answer)

	def test_get_assignment_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		assignment_id = "1"
		self.assertTrue(question_a.getAssignmentId() == assignment_id)

	def test_set_assignment_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		new_assignment_id = "6"
		question_a.setAssignmentId(new_assignment_id)
		self.assertTrue(question_a.getAssignmentId() == new_assignment_id)

	def test_get_assignment_name(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		assignment_name = "Unit 1 Test"
		self.assertTrue(question_a.getAssignmentName() == assignment_name)

	def test_set_assignment_name(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		assignment_name = "Unit 2 Test"
		question_a.setAssignmentName(assignment_name)
		self.assertTrue(question_a.getAssignmentName() == assignment_name)

	def test_get_due_date(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		dueDate = "01-Nov-17"
		self.assertTrue(question_a.getDueDate() == dueDate)

	def test_set_due_date(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		newDueDate = "03-Nov-17"
		question_a.setDueDate(newDueDate)
		self.assertTrue(question_a.getDueDate() == newDueDate)

	def test_get_prof_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		prof_id = "1"
		self.assertTrue(question_a.getProfessorId() == prof_id)

	def test_set_prof_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		newProfId = "23"
		question_a.setProfessorId(newProfId)
		self.assertTrue(question_a.getProfessorId() == newProfId)

	def test_get_student_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		studId = "1"
		self.assertTrue(question_a.getStudentId() == studId)

	def test_set_student_id(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		newStudId = "2"
		question_a.setStudentId(newStudId)
		self.assertTrue(question_a.getStudentId() == newStudId)

	def test_get_student_answer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		self.assertTrue(question_a.getStudentAnswer() == None)

	def test_set_student_answer(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		studentAnswer = "5"
		question_a.setStudentAnswer(studentAnswer)
		self.assertTrue(question_a.getStudentAnswer() == studentAnswer)

	def test_get_correctness(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_a.setStudentAnswer("25")
		self.assertFalse(question_a.getCorrectness())

	def test_equals(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_b = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		self.assertTrue(question_a == question_b)

	def test_not_equals(self):
		question_a = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		question_b = Question.Question("25306175", "FIB", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		self.assertFalse(question_a == question_b)

if __name__ == '__main__':
    unittest.main(exit=False)