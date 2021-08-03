def run() -> None:
    N, _ = map(int, input().split())
    rows = [input() for _ in range(N)]
    K = int(input())

    for row in sorted(rows, key=lambda row: int(row.split()[K])):
        print(row)


if __name__ == "__main__":
    run()
