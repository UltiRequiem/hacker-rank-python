from collections import namedtuple


def run():
    n, score = int(input()), namedtuple("Score", input().split())
    scores = [score(*input().split()).MARKS for i in range(n)]
    print("%.2f" % (sum(map(int, scores)) / n))


if __name__ == "__main__":
    run()
