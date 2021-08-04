def main(x, k):
    return k == eval(input())


if __name__ == "__main__":
    x, k = map(int, input().split())
    print(main(x, k))
