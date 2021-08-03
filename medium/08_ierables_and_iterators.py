from itertools import combinations


def main():
    unused_one = int(input())
    lst = input().split()
    num = int(input())

    C = list(combinations(lst, num))
    F = filter(lambda c: "a" in c, C)

    return "{0:.3}".format(len(list(F)) / len(C))


if __name__ == "__main__":
    print(main())
