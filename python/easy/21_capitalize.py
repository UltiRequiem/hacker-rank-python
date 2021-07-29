def capitalize(string: str):
    return " ".join([word.capitalize() for word in string.split(" ")])


if __name__ == "__main__":
    print(capitalize("sabare reque"))
