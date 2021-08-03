from itertools import product


def run(a, b):
    print(*product(a, b))


if __name__ == "__main__":
    run(list(map(int, input().split())), list(map(int, input().split())))
