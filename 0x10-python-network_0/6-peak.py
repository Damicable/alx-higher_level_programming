#!/usr/bin/python3
"""This module defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ This finds the peak in a list of unsorted integer"""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    k = int(length / 2)
    lis = list_of_integers

    if k - 1 < 0 and k + 1 >= length:
        return lis[k]
    elif k - 1 < 0:
        return lis[k] if lis[k] > lis[k + 1] else lis[k + 1]
    elif k + 1 >= length:
        return lis[k] if lis[k] > lis[k - 1] else lis[k - 1]

    if lis[k - 1] < lis[k] > lis[k + 1]:
        return lis[k]

    if lis[k + 1] > lis[k - 1]:
        return find_peak(lis[k:])
    return find_peak(lis[:k])
