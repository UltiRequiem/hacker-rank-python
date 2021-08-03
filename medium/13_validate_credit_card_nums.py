from re import compile


def run(DATA):
    for _ in range(int(input().strip())):
        print("Valid" if DATA.search(input().strip()) else "Invalid")


if __name__ == "__main__":
    run(compile(r"^" r"(?!.*(\d)(-?\1){3})" r"[456]" r"\d{3}" r"(?:-?\d{4}){3}" r"$"))
