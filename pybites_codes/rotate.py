# from collections import deque
#
#
# def rotate(string, n):
#     """Rotate characters in a string.
#        Expects string and n (int) for number of characters to move.
#     """
#     comy = ''
#
#     stringy = deque(string)
#     stringy.rotate(n)
#     for i in stringy:
#         comy += i
#     return comy
#
#
# print(rotate('hello', -2))
# print(rotate('hello', 2))
#
# print(rotate('bob and julian love pybites!', -15))
# print(rotate('bob and julian love pybites!', 15))
#
#
# # print('bob and julian love pybites!'[])

from collections import defaultdict, Counter
wordy = 'oh what a day what a lovely day'
wordy2 = "don't stop believing"
wordy3 = "Oh what a day what a lovely day"
wordy4 = "Oh what a day, what a lovely day!"


def count_words(sent):
    """
    count the number of words in sentence
    """
    comby = {}
    sy = ''
    sent = sent.lower()
    for j in sent:
        j = j.strip(',')
        j = j.strip('!')
        sy += j

        splity = sy.split()
    for i in splity:
        comby[i] = splity.count(i)

    return comby


print(count_words(wordy))
print(count_words(wordy2))
print(count_words(wordy3))
print(count_words(wordy4))
