"""
The provided code stub reads two integers from STDIN,"a" and "b". Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""


def format_arithmetic(a: int, b: int) -> str:
    return f"{a+b}\n{a-b}\n{a*b}"


if __name__ == "__main__":
    print(format_arithmetic(2, 4))
