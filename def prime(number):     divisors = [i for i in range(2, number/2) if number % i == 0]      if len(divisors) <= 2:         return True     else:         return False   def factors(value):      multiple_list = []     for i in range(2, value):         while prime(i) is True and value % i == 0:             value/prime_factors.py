
def prime(number):
    divisors = [i for i in range(2, number // 2) if number % i == 0]

    if len(divisors) <= 2:
        return True
    else:
        return False


def factors(value):

    multiple_list = []
    for i in range(2, value):
        while prime(i) is True and value % i == 0:
            value /= i
            multiple_list.append(i)

    return multiple_list
