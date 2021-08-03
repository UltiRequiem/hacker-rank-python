from collections import OrderedDict


def run():
    d = OrderedDict()

    for _ in range(int(input())):
        item, _, quantity = input().rpartition(" ")
        d[item] = d.get(item, 0) + int(quantity)
    for item, quantity in d.items():
        print(item, quantity)


if __name__ == "__main__":
    run()
