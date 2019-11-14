def mod3(n):
    more0 = []
    more1 = []
    more2 = []
    gather = {}
    for i in n:
        wey = i % 3
        if wey == 2:
            more2.append(i)
            gather[wey] = more2
        elif wey == 1:
            more1.append(i)
            gather[wey] = more1
        elif wey == 0:
            more0.append(i)
            gather[wey] = more0
    return gather


def groupby(n, key_fun=mod3):
    key_fun = mod3(n)
    return key_fun


print(groupby([1, 4, 5, 6, 8, 19, 34, 55]))
