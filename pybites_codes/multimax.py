def multimax(iterable):
    empty = []
    iterable = list(iterable)
    max_item = max(iterable, default=None)
    for i in iterable:
        if max_item == i:
            empty.append(i)
    return empty


print(multimax([1, 2, 4, 3]))
print(multimax([1, 1, 1, 1]))
print(multimax([1, 4, 2, 4, 3]))
print(multimax([]))
# print(multimax([]))
