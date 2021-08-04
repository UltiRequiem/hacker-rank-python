def main(_, n):
    return all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n])


if __name__ == "__main__":
    _, n = int(input()), input().split()
    print(main(_, n))
