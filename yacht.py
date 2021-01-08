def YACHT(dice):
    if dice.count(dice[0]) == 5:
        return 50
    else:
        return 0

def ONES(dice):
    return 1 * dice.count(1)

def TWOS(dice):
    return 2 * dice.count(2)

def THREES(dice):
    return 3 * dice.count(3)

def FOURS(dice):
    return 4 * dice.count(4)

def FIVES(dice):
    return 5 * dice.count(5)

def SIXES(dice):
    return 6 * dice.count(6)

def FULL_HOUSE(dice):
    first_digit = dice.count(dice[0])

    for digit in dice[1:]:
        if digit != first_digit:
            second_digit = dice.count(digit)
            break

    return sum(dice) if (first_digit == 2 and second_digit == 3) or (first_digit == 3 and second_digit == 2) else 0

def FOUR_OF_A_KIND(dice):
    dice.sort()
    if dice.count(dice[2]) >= 4:
        return 4 * dice[2]
    else:
        return 0

def LITTLE_STRAIGHT(dice):
    for i in range(1, 6):
        if dice.count(i) != 1:
            return 0

    return 30

def BIG_STRAIGHT(dice):
    for i in range(2, 7):
        if dice.count(i) != 1:
            return 0

    return 30

def CHOICE(dice):
    return sum(dice)

def score(dice, category):
    return category(dice)
