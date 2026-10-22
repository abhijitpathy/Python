s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

best, max_count = "", 0

for ch in s1:
  if ch in s2:
    count = s1.count(ch)
    if count > max_count:
      max_count = count
      best = ch

print(best)

