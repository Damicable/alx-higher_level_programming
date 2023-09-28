#!/usr/bin/python3
"""This module defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ This finds the peak in a list of unsorted integer"""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    k = int(length / 2)
    l = list_of_integers

    if k - 1 < 0 and k + 1 >= length:
        return l[k]
    elif k - 1 < 0:
        return l[k] if l[k] > l[k + 1] else l[k + 1]
    elif k + 1 >= length:
        return l[k] if l[k] > l[k - 1] else l[k - 1]

    if l[k - 1] < l[k] > l[k + 1]:
        return l[k]

    if l[k + 1] > l[k - 1]:
        return find_peak(l[k:])
    return find_peak(l[:k])
