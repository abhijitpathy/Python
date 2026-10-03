sentence = input("Enter a sentence: ").split()
vowels = 0
consonants = 0
for word in sentence:
    for ch in word.lower():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

    if vowels > consonants:
         result= "Vowel Heavy"
    elif consonants > vowels:
        result = "Consonant Heavy"
    else:
        result = "Balanced"

    print(word, "=", result)