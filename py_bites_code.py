# MIN_DRIVING_AGE = 18
#
#
# def allowed_driving(name, age):
#     """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
#        checking the passed in age against the MIN_DRIVING_AGE constant"""
#     if age >= MIN_DRIVING_AGE:
#         print(f'{name} is allowed to drive')
#     else:
#         print(f'{name} is not allowed to drive')
#
#
# print(allowed_driving('Ayo', 18))


# VALID_COLORS = ['blue', 'yellow', 'red']
#
#
# def print_colors():
#     """In the while loop ask the user to enter a color,
#        lowercase it and store it in a variable. Next check:
#        - if 'quit' was entered for color, print 'bye' and break.
#        - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
#        - otherwise print the color in lower case."""
#     while True:
#         res = input('Enter a color > ').lower()
#         if res == 'quit':
#             break
#         elif res in VALID_COLORS:
#             print(res.lower())
#         else:
#             print('Not a color')
#             continue
#
#     print('bye')
#
#
# print_colors()


# games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)
#
#
# def print_game_stats(games_won=games_won):
#     """Loop through games_won's dict (key, value) pairs (dict.items)
#        printing (print, not return) how many games each person has won,
#        pluralize 'game' based on number.
#
#        Expected output (ignore the docstring's indentation):
#
#        sara has won 0 games
#        bob has won 1 game
#        tim has won 5 games
#        julian has won 3 games
#        jim has won 1 game
#
#        (Note that as of Python 3.7 - which we're using atm - dict insert order is retained
#         so no sorting is required for this Bite.)
#     """
#
#     for i, num in games_won.items():
#         if num == 1:
#             print(f'{i} has won {num} game')
#         else:
#             print(f'{i} has won {num} games')
#
#
# print_game_stats(games_won=games_won)


# message = """Hello world!
# We hope that you are learning a lot of Python.
# Have fun with our Bites of Py.
# Keep calm and code in Python!
# Become a PyBites ninja!"""
#
#
# def split_in_columns(message=message):
#     """Split the message by newline (\n) and join it together on '|'
#        (pipe), return the obtained output"""
#     end_split = message.split('\n')
#     pipe_j = "|".join(end_split)
#     return pipe_j
#
#
# print(split_in_columns(message=message))


# from string import ascii_lowercase
#
# text = """
# One really nice feature of Python is polymorphism: using the same operation
# on different types of objects.
# Let's talk about an elegant feature: slicing.
# You can use this on a string as well as a list for example
# 'pybites'[0:2] gives 'py'.
# The first value is inclusive and the last one is exclusive so
# here we grab indexes 0 and 1, the letter p and y.
# When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
# but here is the kicker: you can use this on a list too!
# ['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
# and now you know about slicing from the end as well :)
# keep enjoying our bites!
# """
#
# other_test = """Take the block of text provided and strip() off the whitespace at the ends.
# Split the whole block up by newline (\n).
#  if the first character is lowercase, split it into words and add the last word
# of that line to the results list.
# Strip the trailing dot (.) and exclamation mark (!) from the word first.
# finally return the results list!"""
#
#
# def slice_and_dice(text):
#     """Strip the whitespace (newlines) off text at both ends,
#        split the text string on newline (\n).
#        Next check if the first char of each (stripped) line is lowercase,
#        if so split the line into words and append the last word to
#        the results list. Make sure that you strip off any trailing
#        exclamation marks (!) and dots (.), Return the results list."""
#     results = []
#     text = text.strip()
#     text = text.split('\n')
#     for i in text:
#         remove_trail = i.strip()
#         if remove_trail[0].islower() == True:
#             into_words = remove_trail.split()
#             results.append(into_words[-1].strip('!').strip('.'))
#     return results
#
#
# print(slice_and_dice(text))


text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
vowels = 'aeiou'


def strip_vowels(text) -> (str, int):
    county = 0

    """Replace all vowels in the input text string by a star
       character (*).
       Return a tuple of (replaced_text, number_of_vowels_found)

       So if this function is called like:
       strip_vowels('hello world')

       ... it would return:
       ('h*ll* w*rld', 3)

       The str/int types in the function defintion above are part
       of Python's new type hinting:
       https://docs.python.org/3/library/typing.html"""
    for i in text.lower():
        if i in vowels:
            county += 1
            text = text.replace(i, '*')
    return county


print(strip_vowels(text))
# import re
# vowel = 'aeiou'
# gey = ''
# cot = 0
#
# sentence = 'the spate of killing in the country has skyrocket over the years'
#
# for i in list(sentence):
#     if i in vowel:
#         sentence = sentence.replace(i, '*')
# print(sentence)
