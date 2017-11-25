import unittest
import sys
sys.path.insert(0, '../src')
import CheckUserType

class TestCheckUserType(unittest.TestCase):
    
    def test_CheckUserType(self):
        self.assertEqual(CheckUserType.checkUserType('0'), 'S')
        self.assertEqual(CheckUserType.checkUserType('1'), 'P')
        self.assertEqual(CheckUserType.checkUserType('2'), 'S')
        self.assertEqual(CheckUserType.checkUserType('3'), 'S')
        self.assertEqual(CheckUserType.checkUserType('4'), 'P')
        
if __name__ == '__main__':
    unittest.main(exit=False)