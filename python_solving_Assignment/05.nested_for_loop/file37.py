str = input("Enter the sentence: ")
words = str.split()

for w1 in words:
  for w2 in words:
    if len(w1) == len(w2):
      print(f"{w1} {w2}")