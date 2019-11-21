# I want you to write a function that accepts an iterable and an object and returns
# a new iterable with all items from the original iterable except any item at the
# beginning of the iterable which is equal to the object should be skipped.


def lystrip(iterable, strip_value):
    '''
    remove iterable with strip_value items remove from begining
    '''
    striped = []
    is_begining = True
    for item in iterable:
        if is_begining and item == strip_value:
            continue
        is_begining = False
        striped.append(item)
    return striped


print(lystrip([0, 0, 0, 1, 0, 2, 3], 0))
print(lystrip(' hello', ' '))
