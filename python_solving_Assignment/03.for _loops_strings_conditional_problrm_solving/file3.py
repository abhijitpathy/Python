sentence = input("Enter a sentence: ").lower()

words = sentence.split()

highest_score = 0
highest_word = ""

for i in words:
    score = 0

    for ch in i:
        if ch in "aeiou":
            score += 2
        elif ch >= "a" and ch <= "z" :
            score += 1
        elif ch >= "0" and ch <= "9":
            score += 3
        else:
            score += 4

    print(i, "=", score)

    if score > highest_score:
        highest_score = score
        highest_word = i

print("Highest scoring word:", highest_word)
print("Score:", highest_score)

