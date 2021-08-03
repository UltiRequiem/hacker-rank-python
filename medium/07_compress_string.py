from itertools import groupby


def main():
    return [(len(list(c)), int(k)) for k, c in groupby(input())]


if __name__ == "__main__":
    print(*main())
