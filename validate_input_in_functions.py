"""
Program: validate_input_in_functions.py
Author:  Cara Krug
Date: 10/04/2020 cjkrug@dmacc.edu
Write a function score_input() that takes (as parameter arguments) a test_name, test_score,
and invalid_message that validates the test_score,
asking the user for a valid test score until it is in the range,
then prints valid input as 'Test name: ##'.
"""



def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):

    try:
        if test_score < 0 or test_score > 100:
             return invalid_message
        else:
            test_name_and_score = (test_name + ": " + str(test_score))
    except TypeError as err:
            raise TypeError
    else:
            return test_name_and_score




if __name__ == '__main__':
    try:
     print(score_input("math", "test"))
    except TypeError as err:
        print("TypeError encountered")
