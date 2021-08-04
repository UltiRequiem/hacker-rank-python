from itertools import combinations_with_replacement as cwr


def main(s, k) -> None:
    for c in cwr(sorted(s), int(k)):
        print("".join(c))


if __name__ == "__main__":
    s, k = input().split()
    main(s, k)
