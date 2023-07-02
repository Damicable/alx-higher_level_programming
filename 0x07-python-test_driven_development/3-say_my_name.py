#!/usr/bin/python3
"""This module defines a name_printing function"""

def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str) and if not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
