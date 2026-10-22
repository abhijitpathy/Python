str = input("Enter the sentence: ")
words = str.split()

for w1 in words:
  for w2 in words:
    diff = abs(len(w1) - len(w2))
    print(f"{w1} {w2} -> {diff}")