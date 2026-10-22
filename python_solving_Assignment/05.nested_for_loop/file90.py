text = input("Enter a string: ")

best = ""
for ch in text:
  if text.count(ch) == 2 and ch not in best:
    if best:
      best += " or "
    best += ch

print(best)
