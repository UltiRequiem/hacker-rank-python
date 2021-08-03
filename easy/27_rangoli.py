from string import ascii_lowercase


def print_rangoli(n: int) -> str:
    alpha = ascii_lowercase
    lst = []
    for item in range(n):
        s = "-".join(alpha[item:n])
        lst.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))

    return "\n".join(lst[:0:-1] + lst)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
