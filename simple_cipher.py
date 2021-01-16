import random

class Cipher:
    def __init__(self, key = None):
        self.key = key
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "]
        if not self.key:
            self.key = ''.join(random.choice(self.alphabet) for i in range(101))

    def encode(self, text):
        new_text = []
        index = 0
        for x in text:
            new_text.append(self.alphabet[(self.alphabet.index(x) +
                                           self.alphabet.index(self.key[index % len(self.key)])) % 26])
            index += 1
        return "".join(new_text)

    def decode(self, text):
        new_text = []
        index = 0
        for x in text:
            new_text.append(self.alphabet[(self.alphabet.index(x) -
                                           self.alphabet.index(self.key[index % len(self.key)])) % 26])
            index += 1
        return "".join(new_text)
