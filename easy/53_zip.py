def main(n, x):
    for i in zip(*[map(float, input().split()) for _ in range(x)]):
        print(sum(i) / len(i))


if __name__ == "__main__":
    n, x = map(int, input().split())
    main(n, x)
