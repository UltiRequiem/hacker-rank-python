from itertools import permutations


def run() -> None:
    s, n = input().split()

    print(*["".join(i) for i in permutations(sorted(s), int(n))], sep="\n")

if __name__ == "__main__":
    run()
