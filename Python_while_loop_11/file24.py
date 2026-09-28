# 24. Count "a"
text = input("Enter a string: ")
i = 0
count = 0

while i < len(text):
    if text[i] == "a":
        count = count + 1
    i = i + 1

print(count)