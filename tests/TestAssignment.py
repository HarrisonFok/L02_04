import unittest
import sys
sys.path.insert(0, '../src')
import Assignment
import Question

class TestAssignment(unittest.TestCase):

	def testInit(self):
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionB = Question.Question("25301111", "MCQ", "What is 56 - 26", "30", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionA, questionB]
		myAssignment = Assignment.Assignment("123", listOfQ)
		initSuccess = ((len(myAssignment.getAssignmentId()) == 3) and (myAssignment.getVisibility() == False) and
			(myAssignment.getDeadline() == None) and (myAssignment.getName() == None) and
			myAssignment.getListOfQuestions() == listOfQ)
		self.assertTrue(initSuccess)

	def testGetDeadline(self):
		deadline = "01-Nov-17"
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		ass1 = Assignment.Assignment([questionA])
		ass1.setDeadline(deadline)
		self.assertTrue(ass1.getDeadline() == deadline)

	def testSetDeadline(self):
		deadline = "17-Apr-17"
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		ass1 = Assignment.Assignment("123", [questionA])
		ass1.setDeadline(deadline)
		self.assertTrue(ass1.getDeadline() == deadline)

	def testGetAssignmentId(self):
		deadline = "23-May-17"
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		ass1 = Assignment.Assignment("123", [questionA])
		newId = "123"
		ass1.setAssignmentId(newId)
		self.assertTrue(ass1.getAssignmentId() == newId)

	def testSetAssignmentId(self):
		deadline = "02-Feb-18"
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		ass1 = Assignment.Assignment("123", [questionA])
		newId = "123"
		ass1.setAssignmentId(newId)
		self.assertTrue(ass1.getAssignmentId() == newId)

	def testGetListOfQuestions(self):
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionB = Question.Question("21111111", "MCQ", "What is 13 + 14", "27", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionA, questionB]
		ass1 = Assignment.Assignment("123", listOfQ)
		self.assertTrue(ass1.getListOfQuestions() == listOfQ)

	def testSetListOfQuestions(self):
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionB = Question.Question("21111111", "MCQ", "What is 13 + 14", "27", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionA, questionB]
		ass1 = Assignment.Assignment("123", listOfQ)

		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "77", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ2 = [questionC, questionD]
		ass1.setListOfQuestions(listOfQ2)
		self.assertTrue(ass1.getListOfQuestions() == listOfQ2)

	def testSetStudentAnswerAtIndex(self):
		questionA = Question.Question("25306175", "MCQ", "What is 13 + 13", "26", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionB = Question.Question("21111111", "MCQ", "What is 13 + 14", "27", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionA, questionB]
		ass1 = Assignment.Assignment("123", listOfQ)

		studentAnswer = 27
		ass1.setStudentAnswerAtIndex(1, studentAnswer)

		self.assertTrue(questionB.getStudentAnswer() == studentAnswer)

	def testCheckIfPerfectFalse(self):
		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "44", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionC, questionD]
		ass1 = Assignment.Assignment("123", listOfQ)
		self.assertFalse(ass1.checkIfPerfect())

	def testCheckIfPerfectTrue(self):
		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "77", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionC, questionD]
		ass1 = Assignment.Assignment("123", listOfQ)
		self.assertFalse(ass1.checkIfPerfect())

	def testSetVisibilityFalse(self):
		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "77", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionC, questionD]
		ass1 = Assignment.Assignment("123", listOfQ)
		self.assertFalse(ass1.getVisibility())

	def testSetVisibilityTrue(self):
		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "77", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionC, questionD]
		ass1 = Assignment.Assignment(listOfQ)
		ass1.setVisibility(True)
		self.assertTrue(ass1.getVisibility())

	def testGetNameNone(self):
		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "77", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionC, questionD]
		ass1 = Assignment.Assignment("123", listOfQ)
		self.assertTrue(ass1.getName() == None)

	def testGetNameSome(self):
		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "77", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionC, questionD]
		ass1 = Assignment.Assignment("123", listOfQ)
		assName = "Some"
		ass1.setName(assName)
		self.assertTrue(ass1.getName() == assName)

	def testSetName(self):
		questionC = Question.Question("33333333", "MCQ", "What is 22 + 33", "55", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		questionD = Question.Question("44444444", "MCQ", "What is 33 + 44", "77", "1", "Unit 1 Test", "01-Nov-17", "1", "1")
		listOfQ = [questionC, questionD]
		ass1 = Assignment.Assignment("123", listOfQ)
		assName = "Unit 1 Test"
		ass1.setName(assName)
		self.assertTrue(ass1.getName() == assName)

if __name__ == '__main__':
	unittest.main(exit=False)