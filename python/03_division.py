"""
The provided code stub reads two integers, "a"  and "b", from STDIN.

Add logic to print two lines.
The first line should contain the result of integer division, "a" // "b" .
The second line should contain the result of float division,  "a" / "b" .
"""


def format_division(a: int, b: int) -> str:
    return f"{a//b}\n{a/b}"


if __name__ == "__main__":
    print(format_division(3, 5))
