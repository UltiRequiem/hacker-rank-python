def main(_, rooms, single, multiple):

    for room in rooms:
        single.add(room) if room not in single else multiple.add(room)


    return single.difference(multiple).pop()


if __name__ == "__main__":
    k, rooms, single, multiple = input(), input().split(), set(), set()
    print(main(k, rooms, single, multiple))
