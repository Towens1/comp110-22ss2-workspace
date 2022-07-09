"""EX05 - 'list' Utility Functions."""
__author__ = "730237027"

import random


def only_evens(a: list[int]) -> list[int]:
    """Function takes a list of integers and returns a list of the even integers in the list."""
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
    return even


def is_equal(a: list[int], b: list[int]) -> bool:
    """Given two lists of int values, function returns True if lists are equivalent and otherwise returns False."""
    if len(a) != len(b):
        return False
    if len(a) == 0 and len(b) == 0:
        return True
    if len(a) == 0 or len(b) == 0:
        return False
    n: int = 0
    for i in a:
        if i != b[n]:
            return False
        n += 1
    return True


def sub(a: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and end index, function generates a list which is a subset of the given list, between the specified start and end indices."""
    new = []
    if len(a) == 0:
        return new
    if end < 1:
        return new
    if start > len(a) - 1:
        return new
    if start < 0:
        start = 0
    if end > len(a):
        end = len(a) - 1

    for item in a:
        new.append(item)
    n: int = random.randint(start, end)
    while len(new) > n:
        new.pop()
    return new    