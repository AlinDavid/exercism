import collections


def is_isogram(string):
    letter_cont = collections.Counter(list(string.lower().strip()))
    x = 0
    for i in letter_cont:
        if letter_cont[i] > 1:
            x = 1
    if x == 1:
        return "The word {} is not an isogram".format(string)
    else:
        return "The word {} is an isogram".format(string)
