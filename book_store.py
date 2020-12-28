def total(basket):
    book_price = 800

    if len(basket) == 0:
        return 0

    book_sets = [set()]
    for book in basket:
        allocated = False
        for book_set in book_sets:
            if book not in book_set:
                book_set.add(book)
                allocated = True
                break
        if not allocated:
            book_sets.append({book})

    sets_of_three = [s for s in book_sets if len(s) == 3]
    sets_of_five = [s for s in book_sets if len(s) == 5]
    for set_five, set_three in zip(sets_of_five, sets_of_three):
        book = (set_five - set_three).pop()
        set_five.remove(book)
        set_three.add(book)

    total_sum = 0
    discount = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}

    for book_set in book_sets:
        set_total = len(book_set) * book_price
        set_total -= set_total * discount[len(book_set)] / 100
        total_sum += set_total

    return total_sum
