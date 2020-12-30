from datetime import timedelta


def add(moment):
    gigsec = timedelta(seconds=10 ** 9)
    return moment + gigsec
