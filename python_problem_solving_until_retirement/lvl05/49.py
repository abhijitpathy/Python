text = input("Enter a string: ")
result = ""

for ch in text:
    if not ch.isdigit():
        result += ch

print(result)