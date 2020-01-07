"""
This week I'd like you to write a function called minmax, which accepts a list
and returns a tuple of the minimum and maximum values in that list.

Your function should work like this:

>>> minmax([0, 1, 2, 3, 4])
(0, 4)
>>> minmax([10, 8, 7, 5.0, 3, 6, 2])
(2, 10)
"""


def minmax(lst):
    mi = min(lst)
    ma = max(lst)
    return mi, ma


print(minmax([0, 1, 2, 3, 4]))
print(minmax([10, 8, 7, 5.0, 3, 6, 2]))
print(minmax([]))
