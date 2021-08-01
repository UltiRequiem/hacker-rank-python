def minion_game(string):
    VOWELS = ["A", "E", "I", "O", "U"]
    S = 0
    K = 0

    for i in range(len(string)):
        if string[i] in VOWELS:
            K += len(string) - i
        else:
            S += len(string) - i

    if S > K:
        print(f"Stuart {S}")
    elif K > S:
        print(f"Kevin {K}")
    else:
        print("Draw")
