def main(a: int, b: int) -> str:
    return "{0}\n{1}\n({0}, {1})".format(*divmod(a, b))


if __name__ == "__main__":
    print(main(int(input()), int(input())))
