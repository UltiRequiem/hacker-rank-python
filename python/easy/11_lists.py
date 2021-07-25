"""
This is my favorite exercise until the moment
"""


def main() -> None:
    print("Welcome To UltiList!")

    L = []
    len_of_list = int(input("Enter the len of the list: "))

    while len(L) < (len_of_list + 1):
        print(">> ", end="")
        args = input().strip().split(" ")

        if args[0] == "append":
            L.append(int(args[1]))
        elif args[0] == "insert":
            L.insert(int(args[1]), int(args[2]))
        elif args[0] == "remove":
            L.remove(int(args[1]))
        elif args[0] == "pop":
            L.pop()
        elif args[0] == "sort":
            L.sort()
        elif args[0] == "reverse":
            L.reverse()
        elif args[0] == "print":
            print(L)
        elif args[0] == "exit":
            print("Bye!")
            exit()
        else:
            print("That's not a valid command!")


if __name__ == "__main__":
    main()
