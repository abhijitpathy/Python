sentence = input("Enter the sentence: ")
words = sentence.split()

shortest = words[0]
longest = words[0]

for w in words:
  if len(w) < len(shortest):
    shortest = w
  if len(w) > len(longest):
    longest = w

print(f"Longest = {longest}")
print(f"Shortest = {shortest}")