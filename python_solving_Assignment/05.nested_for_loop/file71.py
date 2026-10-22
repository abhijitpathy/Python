word = input("Enter word: ")

for i in range(len(word)):
  for j in range(len(word)):
    if i - j > 5:
      print(word[i], word[j])