names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries(n, c):
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for i, (name, country) in enumerate(zip(names, countries), 1):
        print('{0}. {1:<10} {2}'.format(i, name, country))


print(enumerate_names_countries(names, countries))
