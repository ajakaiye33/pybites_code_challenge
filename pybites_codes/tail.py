
# Morsel code challenge
# challenge: make a function that takes a sequence(like a list string, or tuple)
# and a number n and return the last n element from the given sequence, as a list


# def tail(seq, n):
#     if n <= 0:
#         res = seq[:n]
#     elif n > 0:
#         res = list(seq[-n:])
#
#     return list(res)
#
#
# print(tail([1, 2, 3, 4, 5], 3))
# print(tail('hello', 2))
# print(tail('hello', 0))
# #print(tail('hello', -2))
# square = (i ** 2 for i in range(10))
# print(list(square))
# print(tail(square, 3))
#

# fill = ['hello']
# print(fill[:-2])

# bonus 1: As a bonus, make your function return an empty list for negative values of n
# bonus 2: make sure your function works with any iterable, not just sequences.

def tail(seq, n):
    if n <= 0:
        return list(seq)[:0]
    else:
        return list(seq)[-n:]


print(tail([1, 2, 3, 4, 5], 3))
print(tail('hello', 2))
print(tail('hello', 0))
print(tail('hello', -2))
square = (i ** 2 for i in range(10))
print(tail(square, 3))
