def prime(number):

    limit, i = 0, 2
    prime_list = []

    while limit < number:
        if check_prime(i):
            prime_list.append(i)
            limit += 1
        i += 1

    return prime_list[- 1]

def check_prime(number):

    divisors = 0

    for i in range(2, number//2 + 1):
        if number % i == 0:
            divisors += 1

    if divisors < 1:
        return True
    else:
        return False
