
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def sublist(list_one, list_two):

    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL

def is_sublist(list_one, list_two):
    list_one_dim = len(list_two)
    if list_one_dim == len(set(list_two).union(set(list_one))):
        return True
    else:
        return False
