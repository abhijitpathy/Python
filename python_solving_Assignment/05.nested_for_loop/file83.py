sent1 = input("Enter first sentence: ").split()
sent2 = input("Enter second sentence: ").split()

common = ""

for word1 in sent1:
  for word2 in sent2:
    if word1 == word2 and word1 not in common:
      if common:
        common += " "
      common += word1

print(f"Expected Output: {common}")