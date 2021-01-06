def is_armstrong_number(number):
    number_list = list(str(number))
    number_length = len(list(str(number)))
    return number == sum([int(i) ** number_length for i in number_list])
