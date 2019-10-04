# python Morsels Challenge


def comapact(lst):
    """
    Return new iterable with adjacent duplicate values removed
    """
    dup = []
    for indx, item in enumerate(lst):
            if indx == 0 or item != lst[indx-1]:
                dup.append(item)
        return dup



print(comapact([1, 1, 1]))
print(comapact([1, 1, 2, 2, 3, 2]))
