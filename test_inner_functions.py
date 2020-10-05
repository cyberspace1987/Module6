"""
Program: test_inner_functions_assignment.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/04/2020
Create in your source_files directory, create a python file inner_functions_assignment.py.
In your test directory, create a unit test file test_inner_functions.py.
In your inner_functions_assignment.py, write a function measurements that accepts a
list of measurements for a rectangle and returns a string with perimeter and area
"""
import unittest
import unittest.mock as mock
from more_functions import inner_functions_assignment as main_test

class MyTestCase(unittest.TestCase):

    def test_measurements_rectangle(self):
        self.assertEqual(main_test.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")
    def test_measurements_square(self):
        self.assertEqual(main_test.measurements([3.5]), "Perimeter = 14.0 Area = 12.25")


if __name__ == '__main__':
    unittest.main()

"""""
    Use reST style.
    :parameter a: name of the test
    :parameter b: name of the test
    :parametere p: name of the test
    :returns a and b and p in string
    """
