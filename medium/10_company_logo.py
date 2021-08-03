from collections import Counter


def main() -> None:
    [print(*c) for c in Counter(sorted(input())).most_common(3)]


if __name__ == "__main__":
    main()
