def main(a: set, b: set) -> int:
    return len(a.symmetric_difference(b))


if __name__ == "__main__":
    _, a = input(), set(input().split())
    _, b = input(), set(input().split())
    print(main(a, b))
