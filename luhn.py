class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if len(self.card_num) <= 1:
            raise ValueError("trings of length 1 or less are not valid.")
        else:
            if self.card_num.isdigit():
                list_digit = [int(item) for item in self.card_num]
                for index in range(len(list_digit) - 2, -1, -2):
                    list_digit[index] = list_digit[index]*2 if list_digit[index] < 5 else list_digit[index]*2 - 9
                if sum(list_digit) % 10 == 0:
                    return "The card {} is valid".format(self.card_num)
                else:
                    return "The card {} is not valid".format(self.card_num)


my_card = Luhn("1214")
print(my_card.valid())
