"""
Program: test_string_functions.py
Author:  Cara Krug cjkrug@dmacc.edu
Date: 10/04/2020
a call to multiple_string with message
 Ayah and number 3 would return 'AyahAyahAyah'.
"""



def  multiply_string(message, n):
    """
    Use reST style.
    :param message: this is what the first parameter represents
    :param n: this is what is returned
    :raises keyError: raises an exception
    """
    return message*n
print(multiply_string("Ayah", 4))

if __name__ == '__main__':
    multiply_string('Ayah', 4)
