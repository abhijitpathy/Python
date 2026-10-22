text = input("Enter a string: ")

first_repeated = ""

for i in range(len(text)):
  for j in range(i + 1, len(text)):
    if text[i] == text[j]:
      first_repeated = text[i]
      break
  if first_repeated:
    break

print(first_repeated)