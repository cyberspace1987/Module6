"""
Program: test_valid_input_in_functions.py
Author:  Cara Krug
Date: 10/04/2020 cjkrug@dmacc.edu
Write a function score_input() that takes (as parameter arguments) a test_name, test_score,
and invalid_message that validates the test_score,
asking the user for a valid test score until it is in the range,
then prints valid input as 'Test name: ##'.
"""
import unittest
import unittest.mock as mock
from more_functions import validate_input_in_functions as main_test, validate_input_in_functions
"""""
    Use reST style.
    :parameter test_name: name of the test
    :parameter test_score: optional test score
    :param invalid_message: optional invalid
    :returns test_name and test_score in string
    """

class FunctionTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(validate_input_in_functions.score_input("math"), "math: 0")

    def test_score_input_test_score_valid(self): #this is where I test for input 88
        self.assertEqual(validate_input_in_functions.score_input("math", 88), "math: 88")

    def test_score_input_test_score_below_range(self): #this is where I test for input -1
        self.assertEqual(validate_input_in_functions.score_input("math", -1), "Invalid test score, try again!")

    def test_score_input_test_score_above_range(self): #this is where I test for input 101
        self.assertEqual(validate_input_in_functions.score_input("math", 101), "Invalid test score, try again!")

    def test_test_score_non_numeric(self): #this is where I assertRaise for both math and test
        with self.assertRaises(TypeError):
            validate_input_in_functions.score_input("math", "test")

    def test_score_input_invalid_message(self):
        self.assertEqual(validate_input_in_functions.score_input("math", 95, "Bad score input"), "math: 95")

if __name__ == '__main__':
    unittest.main()
