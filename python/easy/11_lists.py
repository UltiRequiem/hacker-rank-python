"""
This is my favorite exercise until the moment
"""


def main() -> None:
    print("Welcome To UltiList!")

    lst = []
    len_of_list = int(input("Enter the len of the list: "))

    while len(lst) <= len_of_list:
        print(">> ", end="")
        args = input().strip().split(" ")

        if args[0] == "append":
            lst.append(int(args[1]))
        elif args[0] == "insert":
            lst.insert(int(args[1]), int(args[2]))
        elif args[0] == "remove":
            lst.remove(int(args[1]))
        elif args[0] == "pop":
            lst.pop()
        elif args[0] == "sort":
            lst.sort()
        elif args[0] == "reverse":
            lst.reverse()
        elif args[0] == "print":
            print(lst)
        elif args[0] == "exit":
            print("Bye!")
            exit()
        else:
            print("That's not a valid command!")


if __name__ == "__main__":
    main()
