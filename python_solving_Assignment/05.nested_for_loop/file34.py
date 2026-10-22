word = input("Enter the text: ")

for c1 in word:
  for c2 in word:
    diff = abs(ord(c1) - ord(c2))
    print(f"{c1} {c2} -> {diff}")