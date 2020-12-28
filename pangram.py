

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence.lower():
            return False


if is_pangram("Jock nymphs waqf drug vex blitz") is False:
    print("This sentence is not a pangram")
else:
    print("This sentence is a pangram")
