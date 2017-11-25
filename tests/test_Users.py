import unittest
import sys
sys.path.insert(0, '../src')
import User

class Test_User(unittest.TestCase):
    
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
        
        
if __name__ == '__main__':
    unittest.main(exit=False)