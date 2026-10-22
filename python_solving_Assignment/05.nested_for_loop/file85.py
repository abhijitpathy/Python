words = input("Enter a sentence: ").split()

unique_words = ""

for i in range(len(words)):
  count = 0
  for j in range(len(words)):
    if words[i] == words[j]:
      count += 1

  if count == 1 and words[i] not in unique_words:
    if unique_words:
      unique_words += ", "
    unique_words += words[i]

print(unique_words)