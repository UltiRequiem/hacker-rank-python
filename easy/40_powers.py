def main():
    a, b, m = [int(input()) for _ in "123"]
    print(pow(a, b), pow(a, b, m), sep="\n")


if __name__ == "__main__":
    main()
