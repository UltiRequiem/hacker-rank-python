def main() -> int:
    _, a = input(), set(input().split())
    _, b = input(), set(input().split())

    return len(a.intersection(b))


if __name__ == "__main__":
    print(main())
