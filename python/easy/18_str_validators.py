"""
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
"""


def main(string: str) -> None:
    print(any(char.isalnum() for char in string))
    print(any(char.isalpha() for char in string))
    print(any(char.isdigit() for char in string))
    print(any(char.islower() for char in string))
    print(any(char.isupper() for char in string))


if __name__ == "__main__":
    main(input())
