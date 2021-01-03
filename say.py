NUMBERS = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
           10: "ten",
           11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifthteen", 16: "sixteen", 17: "seventeen",
           18: "eighteen", 19: "nineteen", 20: "twenty",
           30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
           100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion"
           }


def say(number):
    remain = 0
    seperator = " "
    if number < 0:
        raise ValueError("Number must be positive")
    elif number < 21:
        result = NUMBERS[number]
    elif number < 100:
        result = NUMBERS[int(number/10)*10]
        remain = number % 10
        seperator = "-"
    elif number < 1000:
        result = NUMBERS[int(number/100)] + seperator + NUMBERS[100]
        remain = number % 100
    elif number < 1000000:
        result = say(int(number/1000)) + seperator + NUMBERS[1000]
        remain = number % 1000
    elif number < 1000000000:
        result = say(int(number/1000000)) + seperator + NUMBERS[1000000]
        remain = number % 1000000
    elif number < 1000000000000:
        result = say(int(number/1000000000)) + seperator + NUMBERS[1000000000]
        remain = number % 1000000000
    else:
        raise ValueError("Value must not be greater than 999999999999")
    if remain > 0:
        result += seperator + say(remain)
    return result


print(say(991))