from math import hypot, degrees, acos


def calc(ab: int, bc: int):
    return round(degrees(acos(bc / hypot(ab, bc)))), chr(176)


if __name__ == "__main__":
    res, degree = calc(int(input()), int(input()))
    print(res, degree, sep="")
