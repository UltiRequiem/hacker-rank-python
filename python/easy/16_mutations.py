"""
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.
"""


def mutate_string(string, pos, char):
    return string[:pos] + char + string[pos + 1 :]


if __name__ == "__main__":
    i, c = input().split()
    print(mutate_string(input(), int(i), c))
