def main(atrr, times: int) -> int:

    for _ in range(times):
        (command, new__set) = (input().split()[0], set(map(int, input().split())))
        getattr(atrr, command)(new__set)

    return sum(atrr)


if __name__ == "__main__":
    (_, a) = (int(input()), set(map(int, input().split())))
    print(main(a, int(input())))
