words = input("Enter a sentence: ").split()

repeated = ""

for i in range(len(words)):
  for j in range(i + 1, len(words)):
    if words[i] == words[j] and words[i] not in repeated:
      if repeated:
        repeated += " "
      repeated += words[i]
      break

print(repeated)