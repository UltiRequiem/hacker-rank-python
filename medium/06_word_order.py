from collections import Counter, OrderedDict


# I nned a class that inherits Counter and OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass


def main():
    ordered_counter_instance = OrderedCounter(input() for _ in range(int(input())))

    print(len(ordered_counter_instance))
    print(*ordered_counter_instance.values())


if __name__ == "__main__":
    main()
