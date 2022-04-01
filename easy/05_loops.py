"""
The provided code stub reads and integer, b, from STDIN.
For all non-negative integers i < n, print i**2.
"""


def potency_while_minor_than_n(n: int) -> None:
    for i in range(n):
        print(i**2)


if __name__ == "__main__":
    potency_while_minor_than_n(5)
