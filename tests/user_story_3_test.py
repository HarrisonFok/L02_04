import unittest
import sys
sys.path.insert(0, '../src')
import user_story_3
class Test_user_story_3(unittest.TestCase):
    '''
    Only function getRange can be tested
    '''
    
    def test_getRange(self):
        question = 'What is the answer of VAR0(2|5) + VAR1(4|10)?'
        self.assertEqual(user_story_3.getRange(question), '2|5,4|10')
    def test_getRange2(self):
        question = 'What is the answer of VAR0(100|500) + VAR1(400|1000)'
        self.assertEqual(user_story_3.getRange(question), '100|500,400|1000')
    def test_getRange3(self):
        question = 'What is the answer of VAR0(1|2) + 2'
        self.assertEqual(user_story_3.getRange(question), '1|2')
    def test_getRange4(self):
        question = 'What is the answer of VAR0(0|1) * VAR1(-1|0)'
        self.assertEqual(user_story_3.getRange(question), '0|1,-1|0')    


if __name__ == '__main__':
    unittest.main(exit=False)