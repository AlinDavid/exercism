def response(hey_bob):
    hey_bob = hey_bob.strip()
    is_yelled = hey_bob.isupper()
    is_question = hey_bob.endswith('?')
    if is_yelled and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelled:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    elif not hey_bob:
        return "Fine. Be that way!"
    else:
        return "Whatever."