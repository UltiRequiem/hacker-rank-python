"""
Given an integer, *n*, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""


# This was my first idea
def weird_or_not(n: int) -> str:
    if n % 2:
        return "Weird"

    return "Not Weird" if n in range(2, 5) or n > 20 else "Weird"


# What I don't like about this is having to define a dict...
def weird_or_not_two(n: int) -> str:
    options = {True: "Not Weird", False: "Weird"}
    return options[n % 2 == 0 and n in range(2, 6) or n > 20]


if __name__ == "__main__":
    print(weird_or_not_two(22))
