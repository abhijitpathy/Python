words = input("Enter sentence: ").split()

for i in range(len(words)):
  for j in range(len(words)):
    w1 = words[i]
    w2 = words[j]

    if w1[0] == w2[0]:
      comparision = "Same"  
    else:
      comparision = "Different"  

    print(
        f"Pair: ({w1}, {w2})  Lengths: {len(w1)}, {len(w2)}  First-chararacter:"
        f" {comparision}"
    )