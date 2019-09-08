MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if age >= MIN_DRIVING_AGE:
        print(f'{name} is allowed to drive')
    else:
        print(f'{name} is not allowed to drive')


print(allowed_driving('Ayo', 18))


VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        res = input('Enter a color > ').lower()
        if res == 'quit':
            break
        elif res in VALID_COLORS:
            print(res.lower())
        else:
            print('Not a color')
            continue

    print('bye')


print_colors()
