from collections import Counter


def find_anagrams(word, candidates):
    return [i for i in candidates if word.lower() != i.lower() and Counter(word) == Counter(i)]
