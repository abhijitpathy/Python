high = 0
top = ""

for i in range(5):
    name = input("Name: ")
    marks = int(input("Marks: "))

    vowel = 0

    for ch in name:
        if ch in "aeiouAEIOU":
            vowel += 1

    c = len(name) - vowel

    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F")

    print("Vowels:", vowel)
    print("Characters:", len(name))

    if vowel > c:
        print("More vowels")
    else:
        print("More consonants")

    if marks > high:
        high = marks
        top = name

print("Highest:", top, high)

