def main(a, b, c, d):
    return pow(a, b) + pow(c, d)


if __name__ == "__main__":
    a, b, c, d = (int(input()) for _ in range(4))
    print(main(a, b, c, d))
