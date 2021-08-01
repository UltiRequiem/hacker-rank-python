"""
The Classic FizzBuzz :D
"""


def fizz_buzz(num: int):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and not num % 5 == 0:
        return "Fizz"
    elif num % 5 == 0 and not num % 3 == 0:
        return "Buzz"
    else:
        return num


if __name__ == "__main__":
    n = 5
    for num in range(1, n + 1):
        print(fizz_buzz(num))
