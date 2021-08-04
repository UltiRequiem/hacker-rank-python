def main(n: int) -> int:

    s = set(map(int, input().split()))

    for _ in range(int(input())):

        c, *args = map(str, input().split())

        getattr(s, c)(*(int(x) for x in args))

    return sum(s)


if __name__ == "__main__":
    print(main(int(input())))
