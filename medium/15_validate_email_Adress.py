from re import compile


def fun(s):
    return compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$").match(s)
