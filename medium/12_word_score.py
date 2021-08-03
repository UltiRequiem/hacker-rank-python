def score_words(words: str) -> int:
    return sum(sum(char in "aeiouy" for char in word) % 2 or 2 for word in words)
