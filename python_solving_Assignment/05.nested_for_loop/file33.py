word = input("Enter the text: ")
result = ""

for c1 in word:
  for c2 in word:
    if c1.isupper() == c2.isupper():
      result += f"{c1}-{c2}, "
print(result.rstrip(", "))