def decode(string):
    result = ''
    count = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            if count == '':
                count = 1
            result += int(count) * char
            count = ''
    return result

def encode(string):
    result = ''
    count = 1
    last_char = ''
    if not string:
        return ''
    for char in string:
        if last_char != char:
            if count == 1:
                result += last_char
            else:
                result += str(count) + last_char
            last_char = char
            count = 1
        else:
            count += 1
    if count == 1:
        result += last_char
    else:
        result += str(count) + last_char
    return result