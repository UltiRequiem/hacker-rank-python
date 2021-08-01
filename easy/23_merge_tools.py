def merge_the_tools(s, k):
    for part in zip(*[iter(s)] * k):
        d = dict()
        print("".join([d.setdefault(c, c) for c in part if c not in d]))


if __name__ == "__main__":
    merge_the_tools(input(), int(input()))
