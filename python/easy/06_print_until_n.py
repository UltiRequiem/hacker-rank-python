"""
Without using any string methods, try to print the following:
    123...n

Note that "..." represents the consecutive values in between.

Example:
n = 5
Print the string "12345".
"""


def print_until_n(n: int) -> None:
    print(*range(1, n + 1), sep="")


if __name__ == "__main__":
    print_until_n(5)
