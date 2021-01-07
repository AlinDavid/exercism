def square(number):
    square_list = [2 ** i for i in range(64)]
    if number > len(square_list) - 1:
        raise ValueError("This value is not on the chess table")
    else:
        return square_list[number]


def total():
    return sum([2 ** i for i in range(64)])
