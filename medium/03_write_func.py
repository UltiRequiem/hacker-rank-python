def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


if __name__ == "__main__":
    print(is_leap(int(input())))
