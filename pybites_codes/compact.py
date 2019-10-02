from collections import Counter


def comapact(lst):
    return list(set([i for i in lst]))


print(comapact([1, 1, 1]))
print(comapact([1, 1, 2, 2, 3, 2]))
