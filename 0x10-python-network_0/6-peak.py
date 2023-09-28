#!/usr/bin/python3
""" This defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of an unsorted integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    k = int(length / 2)
    li = list_of_integers

    if k - 1 < 0 and k + 1 >= length:
        return li[k]
    elif k - 1 < 0:
        return li[k] if li[k] > li[k + 1] else li[k + 1]
    elif k + 1 >= length:
        return li[k] if li[k] > li[k - 1] else li[k - 1]

    if li[k - 1] < li[k] > li[k + 1]:
        return li[k]

    if li[k + 1] > li[k - 1]:
        return find_peak(li[k:])
    return find_peak(li[:k])
