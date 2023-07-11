#!/usr/bin/python
"""This module contains the inherits_from function
"""

def inherits_from(obj, a_class):
    """This returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(typ(obj), a_class) and type(obj) != a_class)