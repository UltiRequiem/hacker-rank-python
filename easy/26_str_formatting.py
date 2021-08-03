def main() -> list:
    return [
        [str(i), str(oct(i)[2:]), str(hex(i)[2:]).upper(), str(bin(i)[2:])]
        for i in range(1, int(input()) + 1)
    ]


if __name__ == "__main__":
    results = main()
    width = len(results[-1][3])

    for item in results:
        print(*(rep.rjust(width) for rep in item))
