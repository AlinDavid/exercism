def is_armstrong_number(number):
    return number == sum(int(i) ** len(list(str(number))) for i in list(str(number)))

