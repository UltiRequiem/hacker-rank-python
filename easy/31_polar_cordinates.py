from cmath import polar


def run() -> None:
    print(*polar(complex(input())), sep="\n")


if __name__ == "__main__":
    run()
