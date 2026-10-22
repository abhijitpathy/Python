text = input("Enter a string: ")

max_char = text[0]
max_count = 0

for char in text:
  count = 0
  for c in text:
    if c == char:
      count += 1
  if count > max_count:
    max_count = count
    max_char = char

print(max_char)
