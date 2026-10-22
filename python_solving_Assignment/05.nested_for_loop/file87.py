words = input("Enter words: ").split()
longest = ""

for word in words:
  if word == word[::-1] and len(word) > len(longest):
    longest = word

print(longest)