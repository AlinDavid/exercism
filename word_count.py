from re import findall
from collections import Counter


def count_words(sentence):
    regexp = r'[a-z]+\'*[a-z]+|[a-z0-9]'
    counter_dict = findall(regexp, sentence.lower())

    return Counter(counter_dict)

print(count_words())
