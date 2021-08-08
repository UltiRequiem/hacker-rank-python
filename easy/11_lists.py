from os import name, system

HELP_MESSAGE = """
    commands = {
        "append": lambda arg: lst.append(arg),
        "print": lambda: print(lst),
        "remove": lambda arg: lst.remove(arg),
        "insert": lambda pos, item: lst.insert(pos, item),
        "pop": lambda: lst.pop(),
        "sort": lambda: lst.sort(),
        "reverse": lambda: lst.reverse(),
        "clear": lambda: clear_console(),
        "exit": lambda: exit(),
    }
"""


def get_lst_max_length(len_of_list=0) -> int:
    while len_of_list < 1:
        try:
            len_of_list = int(
                input("Enter the len of the list, it has to be more than one!: ")
            )
        except ValueError:
            print("You have to pass a number!")

    return len_of_list


def main() -> None:

    print("Welcome To UltiList!")

    len_of_list = get_lst_max_length()

    lst = []

    commands = {
        "append": lambda arg: lst.append(arg),
        "print": lambda: print(lst),
        "remove": lambda arg: lst.remove(arg),
        "insert": lambda pos, item: lst.insert(pos, item),
        "pop": lambda: lst.pop(),
        "sort": lambda: lst.sort(),
        "reverse": lambda: lst.reverse(),
        "clear": lambda: system("cls" if name in ("nt", "dos") else "clear"),
        "exit": lambda: exit(),
        "help": lambda: print(HELP_MESSAGE),
    }

    while len(lst) <= len_of_list:
        print(">> ", end="")
        args = input().strip().split(" ")
        try:
            try:
                commands[f"{args[0]}"](int(args[1]))
            except ValueError:
                print(f"You have to pass a number! Not a {type(args[1])}")
        except IndexError:
            commands[f"{args[0]}"]()
        except TypeError:
            try:
                commands[f"{args[0]}"](int(args[1]), int(args[2]))
            except ValueError:
                print(
                    f"You have to pass two numbers! Not a {type(args[1])} and {type(args[2])}"
                )
        except KeyError:
            print("That's not a valid command!")


if __name__ == "__main__":
    main()

# codereview.stackexchange.com/questions/264384
