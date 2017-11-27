import unittest
import sys
sys.path.insert(0, '../src')
from randomalgo import *

class TestRandomalgo(unittest.TestCase):

    # test the check operation function
    def test_is_operation(self):
        self.assertTrue(is_operation('+'), "not work for +")
        self.assertTrue(is_operation('-'), "not work for -")
        self.assertTrue(is_operation('*'), "not work for *")
        self.assertTrue(is_operation('/'), "not work for /")
        self.assertFalse(is_operation('2'), "expected false when its not an operation")

    # test mixed_operation function
    def test_mixed_operation(self):
        self.assertEqual(mixed_operation("1+3"), [1, '+', 3], "not work for single operation")
        self.assertEqual(mixed_operation("1+3*6"), [1, '+', 3, '*', 6], "not work for mutilple operation")
        self.assertEqual(mixed_operation("136"), [136], "not work for no operation")

    # test calculate simple operation
    def test_aob(self):
        self.assertEqual(get_aob(1, '+', 3), 4, "can not get a + b")
        self.assertEqual(get_aob(1, '-', 3), -2, "can not get a - b")
        self.assertEqual(get_aob(1, '*', 3), 3, "can not get a * b")
        self.assertEqual(get_aob(3, '/', 1), 3, "can not get a / b")

    # test calculate two operation
    def test_cal_op1_op2(self):
        self.assertEqual(cal_op1_op2([1, '+', 3], '+', '-'), [4], "not work for + - ")
        self.assertEqual(cal_op1_op2([1, '+', 3, '*', 1], '*', '/'), [1, '+', 3], "not work for * / ")

    # test calculate the expression
    def test_cal_exp(self):
        self.assertEqual(cal_exp([1, '+', 3, '*', 1]), 4, "can not calculate the expression list ")

    # test Random in range method
    def test_RandomInRange(self):
        self.assertTrue(1 <= RandomInRange([1, 10]) and RandomInRange([1,10]) <= 10, "can not random correctly")

    # make assignment method i messed up with the question object u may just skip it.

if __name__ == '__main__':
    unittest.main(exit=False)