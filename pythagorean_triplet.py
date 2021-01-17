def triplets_with_sum(number):

    default_list = triplets_in_range(1, number)

    return [i for i in default_list if sum(i) == number]

def triplets_in_range(start, end):

    a, b, c, m = 0, 0, 0, 2
    triplets_list = []

    while c:
        for i in range(start, m):

            a = m * m - i * i
            b = 2 * m * i
            c = m * m + i * i

            if c > end:
                break

            triplets_list.append([a, b, c])

        m += 1

    return triplets_list

def is_triplet(triplet):
    a, b, c = triplet

    if a**2 + b**2 == c**2:
        return "This triplet {} is a pythagorean triplet".format(triplet)
    else:
        return "This one is not a triplet"
