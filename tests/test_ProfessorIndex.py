import unittest
import sys
sys.path.insert(0, '../src')
import ProfessorProfileIndex

class Test_Professor_Index(unittest.TestCase):
    
    def test_matchPassword(self):
        self.assertTrue(ProfessorProfileIndex.matchPasswords('123','123'))
        self.assertFalse(ProfessorProfileIndex.matchPasswords('123','321'))
        
    def test_isempty(self):
        self.assertTrue(ProfessorProfileIndex.entryIsEmpty(''))
        self.assertFalse(ProfessorProfileIndex.entryIsEmpty('nope'))    


if __name__ == '__main__':
    unittest.main(exit=False)