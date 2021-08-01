import textwrap


def wrap(string: str, max_width: int):
    # return "\n".join([string[i : i + max_width] for i in range(len(string), max_width)])
    return "\n".join(textwrap.wrap(string, max_width))


if __name__ == "__main__":
    print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))
