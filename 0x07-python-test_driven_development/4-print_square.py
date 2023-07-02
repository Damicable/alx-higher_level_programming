#!/usr/bin/python3
"""This module defines a square_printing function"""

def print_square(size):
     """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float:
        raise TypeError("size must be an integer")
    for i in range(0, size):
        for j in range(size):
            print("#", end= '')
        print('')
