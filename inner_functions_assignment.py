"""
Program: inner_functions_assignment.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/04/2020
Create in your source_files directory, create a python file inner_functions_assignment.py.
In your test directory, create a unit test file test_inner_functions.py.
In your inner_functions_assignment.py, write a function measurements that accepts a
list of measurements for a rectangle and returns a string with perimeter and area
"""

"""""
    Use reST style.
    :parameter a: name of the test
    :parameter b: name of the test
    :parametere p: name of the test
    :returns a and b and p in string
    """
def measurements(a_list):
    a = area(a_list)
    p = perimeter(a_list)
    string = "Perimeter = " + str(p) + " Area = " + str(a)
    return string

def area(a_list):

    if len(a_list) == 1:
        a = a_list[0] * a_list[0]
    elif len(a_list) == 2:
        a = a_list[0] * a_list[1]
    else:
        a = -1
    return a

def perimeter(a_list):

    if len(a_list) == 1:
        p = 4 * a_list[0]
    elif len(a_list) == 2:
        p = 2 * (a_list[0] + a_list[1])
    else:
     p = -1
    return p

if __name__ == '__main__':
    print(measurements('a_list'))
    print(area('a_list'))
    print(perimeter('a_list'))
