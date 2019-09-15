NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return [i.title() for i in set(names)]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # ...
#     for i in names:
#         splity = i.split()
#         checky = sorted(splity, key=lambda x: x[0], reverse=True)
#         print(','.join(checky))
    return sorted(sorted(names), key=lambda x: x.split()[1], reverse=True)

#


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    return min([i.split()[0] for i in names])


print(dedup_and_title_case_names(NAMES))
names = dedup_and_title_case_names(NAMES)


print(sort_by_surname_desc(names))

print(shortest_first_name(names))
