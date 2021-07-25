import math


def main(c: str, w: int) -> None:
    print((c * 2).center(w // 2) * 2)

    for i in range(1, w // 10 + 1):
        print(
            (
                (c * int(math.sin(math.radians(i * w // 2)) * w // 4)).rjust(w // 4)
                + (c * int(math.sin(math.radians(i * w // 2)) * w // 4)).ljust(w // 4)
            )
            * 2
        )

    for i in range(w // 4, 0, -1):
        print(((c * i * 4).center(w)))

    print((c * 2).center(w))


if __name__ == "__main__":
    main("*", 40)
