"""
This is my favorite exercise until the moment
"""


def main() -> None:
    print("Welcome To UltiList!")

    lst = []
    len_of_list = int(input("Enter the len of the list: "))

    commands = {
        "append": lambda arg: lst.append(arg),
        "print": lambda: print(lst),
        "remove": lambda arg: lst.remove(arg),
        "insert": lambda pos, item: lst.insert(pos, item),
        "pop": lambda: lst.pop(),
        "sort": lambda: lst.sort(),
        "reverse": lambda: lst.reverse(),
    }

    while len(lst) <= len_of_list:
        print(">> ", end="")
        args = input().strip().split(" ")
        try:
            commands[f"{args[0]}"](int(args[1]))
        except IndexError:
            commands[f"{args[0]}"]()
        except TypeError:
            commands[f"{args[0]}"](int(args[1]), int(args[2]))
        except KeyError:
            print("That's not a valid command!")


if __name__ == "__main__":
    main()

# codereview.stackexchange.com/questions/264384/python-code-style-if-elif-else
