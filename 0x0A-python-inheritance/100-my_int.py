#!/usr/bin/python3
"""
This module contains the class MyInt
"""


class MyInt(int):
    """A rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """his creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
