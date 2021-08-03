from datetime import datetime as dt


def main(date_format: str) -> None:
    for _ in range(int(input())):

        print(
            int(
                abs(
                    (
                        dt.strptime(input(), date_format)
                        - dt.strptime(input(), date_format)
                    ).total_seconds()
                )
            )
        )


if __name__ == "__main__":
    main("%a %d %b %Y %H:%M:%S %z")
