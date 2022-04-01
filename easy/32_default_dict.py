from collections import defaultdict


def run():
    d = defaultdict(list)

    n, m = map(int, input().split())

    for i in range(1, n + 1):
        d[input()].append(str(i))

    for i in range(m):
        print(" ".join(d[input()]) or -1)


if __name__ == "__main__":
    run()
