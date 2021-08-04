def main(num: int) -> int:
    return len(set(input() for i in range(num)))


if __name__ == "__main__":
    print(main(int(input())))
