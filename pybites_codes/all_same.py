# python Morsel

# make a function, all_same, that accepts a sequence and returns True if all the
# items in the given sequence are the same


# def all_same(seq):
#     return len(set(seq)) <= 1

def all_same(seq):
    for i in seq:
        if i != seq[0]:
            return False
    return True


print(all_same([1, 1, 1]))

print(all_same([1, 0, 1]))

print(all_same([(1, 'a'), (1, 'a')]))

print(all_same([(1, 'a'), (1, 'b')]))
