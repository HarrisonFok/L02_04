import unittest
import sys
sys.path.insert(0, '../src')
import StudentProfileIndex

class Test_StudentIndex(unittest.TestCase):
    
    def test_matchPassword(self):
        self.assertTrue(StudentProfileIndex.matchPasswords('123','123'))
        self.assertFalse(StudentProfileIndex.matchPasswords('123','321'))
        
    def test_isempty(self):
        self.assertTrue(StudentProfileIndex.entryIsEmpty(''))
        self.assertFalse(StudentProfileIndex.entryIsEmpty('nope'))
        
        
if __name__ == '__main__':
    unittest.main(exit=False)