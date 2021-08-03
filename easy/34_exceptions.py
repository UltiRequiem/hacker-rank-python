def main():
    for _ in range(int(input())):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except BaseException as e:
            print("Error Code:", e)


if __name__ == "__main__":
    main()
