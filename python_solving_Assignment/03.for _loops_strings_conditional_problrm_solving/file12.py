sentence = input("Enter a sentence: ").lower()
vowels = 0
consonants = 0
a = e = i = o = u = 0

for ch in sentence:
    if ch in "aeiou":
        vowels += 1

        if ch == 'a':
            a += 1
        elif ch == 'e':
            e += 1
        elif ch == 'i':
            i += 1
        elif ch == 'o':
            o += 1
        elif ch == 'u':
            u += 1

    else:
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

if vowels > consonants:
    print("Vowels Win")
elif consonants > vowels:
    print("Consonants Win")
else:
    print("Draw")

print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)