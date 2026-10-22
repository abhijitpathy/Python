str = input("Enter the sentence: ")
words = str.split()

for w1 in words:
  for w2 in words:
    if w1[-1] == w2[-1]:
      print(f"{w1} {w2}")