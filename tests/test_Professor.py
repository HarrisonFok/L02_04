import unittest
import sys
sys.path.insert(0, '../src')
import Professor

class test_Professor(unittest.TestCase):
    
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

if __name__ == '__main__':
    unittest.main(exit=False)