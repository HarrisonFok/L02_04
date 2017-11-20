import unittest
import sys
sys.path.insert(0, '../src')
import Professor
import ProfessorProfileIndex
import Student
import StudentProfileIndex
import User
import CheckUserType

class TestJasonCode(unittest.TestCase):
    '''
    This is the unittest for Professor.py, ProfessorProfileIndex.py, 
    Student.py, StudentProfileIndex.py, User.py
    '''
    
    def test_User(self):
        '''
        basic cases
        '''
        setup = User.User('test_name', "test_email", "test_pwd", 'test_num', 'P')
        self.assertEqual(setup.getName(), 'test_name')
        self.assertEqual(setup.getEmail(), 'test_email')
        self.assertEqual(setup.getPassword(), 'test_pwd')
        self.assertEqual(setup.getPersonnelNumber(), 'test_num')
        self.assertEqual(setup.getType(), 'P')
        
    def test_User2(self):
        '''
        cases with setter
        '''
        setup = User.User('test_name', "test_email", "test_pwd", 'test_num', 'P')
        setup.setName('name2')
        self.assertEqual(setup.getName(), 'name2')
        setup.setEmail('email2')
        self.assertEqual(setup.getEmail(), 'email2')
        setup.setPassword("pwd2")
        self.assertEqual(setup.getPassword(), 'pwd2')
        setup.setPersonnelNumber("num2")
        self.assertEqual(setup.getPersonnelNumber(), 'num2')
    
    def test_Professor(self):
        '''
        basic cases
        '''
        setup = Professor.Professor("p_name", "p_email", "p_pwd", "p_num")
        self.assertEqual(setup.getName(), 'p_name')
        self.assertEqual(setup.getEmail(), 'p_email')
        self.assertEqual(setup.getPassword(), 'p_pwd')
        self.assertEqual(setup.getPersonnelNumber(), 'p_num')
        self.assertEqual(setup.getType(), 'P')
        
    def test_Professor2(self):
        '''
        cases with new functions
        '''
        setup = Professor.Professor("p_name", "p_email", "p_pwd", "p_num")        
        setup.addCourse('CSCC01')
        setup.addCourse('CSCC02')
        setup.addCourse('CSCC03')
        self.assertEqual(setup.getAllCourses(), ['CSCC01','CSCC02','CSCC03'])
        setup.removeCourse('CSCC01')
        self.assertEqual(setup.getAllCourses(), ['CSCC02','CSCC03'])
  
    def test_Student(self):
        '''
        basic cases
        '''
        setup = Student.Student("s_name", "s_email", "s_pwd", "s_num")
        self.assertEqual(setup.getName(), 's_name')
        self.assertEqual(setup.getEmail(), 's_email')
        self.assertEqual(setup.getPassword(), 's_pwd')
        self.assertEqual(setup.getPersonnelNumber(), 's_num')
        self.assertEqual(setup.getType(), 'S')
    
    def test_Student2(self):
        '''
        cases with new functions
        '''
        setup = Student.Student("s_name", "s_email", "s_pwd", "s_num")        
        setup.addAssignment('12345678')
        setup.addAssignment('87654321')
        setup.addAssignment('66666666')
        self.assertEqual(setup.getAssignmentIds(), ['12345678','87654321','66666666'])
        
    def test_ProfessorProfileIndex(self):
        '''
        Only 2 functions can be tested
        '''
        self.assertTrue(ProfessorProfileIndex.matchPasswords('123','123'))
        self.assertFalse(ProfessorProfileIndex.matchPasswords('123','321'))
        self.assertTrue(ProfessorProfileIndex.entryIsEmpty(''))
        self.assertFalse(ProfessorProfileIndex.entryIsEmpty('nope'))
    
    def test_StudentProfileIndex(self):
        '''
        Only 2 functions can be tested
        '''
        self.assertTrue(StudentProfileIndex.matchPasswords('123','123'))
        self.assertFalse(StudentProfileIndex.matchPasswords('123','321'))
        self.assertTrue(StudentProfileIndex.entryIsEmpty(''))
        self.assertFalse(StudentProfileIndex.entryIsEmpty('nope'))
    
    def test_CheckUserType(self):
        self.assertEqual(CheckUserType.checkUserType('0'), 'S')
        self.assertEqual(CheckUserType.checkUserType('1'), 'P')
        self.assertEqual(CheckUserType.checkUserType('2'), 'S')
        self.assertEqual(CheckUserType.checkUserType('3'), 'S')
        self.assertEqual(CheckUserType.checkUserType('4'), 'P')
        

if __name__ == '__main__':
    unittest.main(exit=False)