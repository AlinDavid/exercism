
def abbreviate(words):
    if type(words) != str:
        raise ValueError("You have to type a string type word")

    list_word = [x[0].upper() for x in words.replace("-", " ").split()]
    acronym = "".join(list_word)

    return acronym
