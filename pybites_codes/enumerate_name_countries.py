names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for i, items in enumerate(zip(names, countries), 1):
        res = '{0}.  {1:<11}     {2:<8}'.format(i, items[0], items[1])
        print(res)


print(enumerate_names_countries())
