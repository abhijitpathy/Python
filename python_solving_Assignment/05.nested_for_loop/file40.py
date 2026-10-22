str = input("Enter the sentence: ")
words = str.split()

for w1 in words:
  for w2 in words:
    for c in w1:
      if c in w2:
        print(f"{w1} {w2}")
        break