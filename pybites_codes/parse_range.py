def parse_range(col):
    mk_iter = []
    splitty = col.split('-')
    for i in splitty:
        rm_combo = i.split(',')
        for j in rm_combo:
            mk_iter.append(int(j))
    return mk_iter


print(parse_range('1-2, 4-4, 8-10'))
print(parse_range('0-0, 4-8, 20-20, 43-45'))
