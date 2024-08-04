#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""

def add_integer(a, b = 98):
     """ Function that adds two integer and/or float numbers

    Args:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

     if type(a) not in (float, int):
          raise TypeError("a must be an integer")
     if type(b) not in (float, int):
          raise TypeError("b must be an integer")
     a = int(a)
     b = int(b)
     return (a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
