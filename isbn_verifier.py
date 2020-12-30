
def is_valid(isbn):
    new_isbn = list(reversed([int(k) for k in isbn.replace("-", "")]))
    sum = 0
    for i in range(0, len(new_isbn)):
        sum += (i + 1) * new_isbn[i]
    return sum % 11

if __name__ = "__main__":
    if is_valid() == 0:
        print("The code is valid")
    else:
        print("This one is not valid")