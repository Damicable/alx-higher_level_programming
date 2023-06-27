#!/usr/bin/python3

"""A module that defines a square """


class Square:
    """This is a class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: This represnets the size of the square defined
        Raises:
            TypeError: if the size is not integer
            ValueError: if the size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
