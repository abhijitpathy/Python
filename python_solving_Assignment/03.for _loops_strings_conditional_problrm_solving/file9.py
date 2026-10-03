n = input("Enter string: ").lower()

vowels = 0
consonants = 0
digits = 0
special = 0

for i in range(len(n)):
    ch = n[i]

    if i % 2 == 0:
        position = "Even"
    else:
        position = "Odd"

    if ch in "aeiou":
        category = "Vowel"
        vowels += 1

    elif ('a' <= ch <= 'z') :
        category = "Consonant"
        consonants += 1

    elif '0' <= ch <= '9':
        category = "Digit"
        digits += 1

    else:
        category = "Special Character"
        special += 1

    print(ch, i, position, category)

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)