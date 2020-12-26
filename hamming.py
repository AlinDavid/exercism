

def distance(strand_a, strand_b):
    if len(strand_b) != len(strand_a):
        raise ValueError("Those 2 strings must be equal")

    return sum(a != b for a, b in zip(strand_a, strand_b))

