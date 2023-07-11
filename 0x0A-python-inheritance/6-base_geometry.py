#!/usr/bin/python3
"""
This module contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """This raises an exception when called"""
        raise Exception("area() is not implemented")
