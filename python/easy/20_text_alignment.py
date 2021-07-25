def main(t: int, c: str) -> None:
    print((c * i).rjust(t - 1) + c + (c * i).ljust(t - 1) for i in range(t))

    print((c * t).center(t * 2) + (c * t).center(t * 6) for i in range(t + 1))

    print((c * t * 5).center(t * 6) for i in range((t + 1) // 2))

    print((c * t).center(t * 2) + (c * t).center(t * 6) for i in range(t + 1))

    print(
        ((c * (t - i - 1)).rjust(t) + c + (c * (t - i - 1)).ljust(t)).rjust(t * 6)
        for i in range(t)
    )


if __name__ == "__main__":
    main(int(input()), "H")
