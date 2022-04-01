from re import match, findall

regex_integer_in_range = r"_________"
regex_alternating_repetitive_digit_pair = r"_________"

if __name__ == "__main__":
    string = input()
    print(
        bool(
            match(r"^[1-9][\d]{5}$", string)
            and len(findall(r"(\d)(?=\d\1)", string)) < 2
        )
    )
