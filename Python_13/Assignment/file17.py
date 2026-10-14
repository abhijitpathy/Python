word = input("enter a word: ")
vowels = "aeiou"
count = 0

for char in word:
  if char in vowels:
    continue
  count += 1

print("Non-vowel count:", count)

