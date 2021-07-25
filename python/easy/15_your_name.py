"""
You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following:
    Hello firstname lastname! You just delved into python.
"""


def delved_into_python(first, last):
    return f"Hello {first} {last}! You just delved into python."


if __name__ == "__main__":
    print(delved_into_python(input(), input()))
