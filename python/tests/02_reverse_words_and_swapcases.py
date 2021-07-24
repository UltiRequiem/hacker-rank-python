"""
Implement a function that takes a string consisting of words separated by
single spaces and returns a string containing all those words but in the
reverse order and such that all cases of letters in the original
string are swapped, i.e. lowercase letters become uppercase and
uppercase letters become lowercase.
"""


def reverse_words_order_and_swap_cases(sentence: str) -> str:
    return " ".join([word.swapcase() for word in reversed(sentence.split())])


if __name__ == "__main__":
    print(reverse_words_order_and_swap_cases("fAST. rUNS dOG"))
