def check(limit):
    for num in range(2, limit + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            yield num


def primes(limit):
    num_list = [i for i in check(limit)]
    return num_list
