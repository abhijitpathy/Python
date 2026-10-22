text = input("Enter a string: ")

repeated = ""

for i in range(len(text)):
  for j in range(i + 1, len(text)):
    if text[i] == text[j] and text[i] not in repeated:
      repeated += text[i]

output = " ".join(repeated)
print(f"Repeated characters: {output}.")