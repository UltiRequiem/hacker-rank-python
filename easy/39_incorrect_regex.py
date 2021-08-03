import re


def is_valid_regex(regex):
    try:
        re.compile(regex)
    except re.error:
        return False
    return True


if __name__ == "__main__":
    for _ in range(int(input())):
        print(is_valid_regex(input()))
