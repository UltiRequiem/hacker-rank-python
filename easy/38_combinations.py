from itertools import combinations


def run():
    s, n = input().split()

    for i in range(1, int(n) + 1):
        for j in combinations(sorted(s), i):
            print("".join(j))


if __name__ == "__main__":
    run()
