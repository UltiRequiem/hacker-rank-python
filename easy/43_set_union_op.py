from functools import reduce as rd


def main() -> int:
    return len(
        rd(lambda a, b: a | b, [set(input().strip().split()) for j in range(4)][1::2])
    )


if __name__ == "__main__":
    print(main())
