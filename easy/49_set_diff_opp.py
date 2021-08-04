def main() -> int:

    unused_one = input()
    set_one = set(map(int, input().split()))

    unused_two = input()
    set_two = set(map(int, input().split()))

    return len(set_one - set_two)


if __name__ == "__main__":
    print(main())
