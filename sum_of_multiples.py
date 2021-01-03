def sum_of_multiples(limit, multiples):
    return sum(set(i for factor in multiples
                   if factor != 0
                   for i in range(factor, limit, factor)))

