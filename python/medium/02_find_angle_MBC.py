import math


def calc(ab, bc):
    return round(math.degrees(math.acos(bc / math.hypot(ab, bc)))), chr(176)


if __name__ == "__main__":
    res, degree = calc(int(input()), int(input()))
    print(res, degree, sep="")
