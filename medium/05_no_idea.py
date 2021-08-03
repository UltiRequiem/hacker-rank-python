def main() -> int:
    unused_one, unused_two = input().split()

    input_one = input().split()

    input_three = set(input().split())
    input_four = set(input().split())

    return sum([(item in input_three) - (item in input_four) for item in input_one])


if __name__ == "__main__":
    print(main())
