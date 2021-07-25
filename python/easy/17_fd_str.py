def count_substring(string: str, sub_string: str):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == "__main__":
    print(count_substring(input().strip(), input().strip()))
