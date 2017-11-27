import unittest
import sys
sys.path.insert(0, '../src')
import Student

class Test_Student(unittest.TestCase):
    
    def test_Student(self):
        '''
        basic cases
        '''
        setup = Student.Student('s_id',"s_name", "s_email", "s_pwd", "s_num")
        self.assertEqual(setup.getName(), 's_name')
        self.assertEqual(setup.getEmail(), 's_email')
        self.assertEqual(setup.getPassword(), 's_pwd')
        self.assertEqual(setup.getPersonnelNumber(), 's_num')
        self.assertEqual(setup.getType(), 'S')
    
    def test_Student2(self):
        '''
        cases with new functions
        '''
        setup = Student.Student('s_id',"s_name", "s_email", "s_pwd", "s_num")        
        setup.addAssignment('12345678')
        setup.addAssignment('87654321')
        setup.addAssignment('66666666')
        self.assertEqual(setup.getAssignmentIds(), ['12345678','87654321','66666666'])

if __name__ == '__main__':
    unittest.main(exit=False)