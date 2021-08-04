from collections import deque


def main(d: deque) -> list:
    for _ in range(int(input())):
        inp = input().split()
        getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    return [item for item in d]


if __name__ == "__main__":
    print(*main(deque()))
