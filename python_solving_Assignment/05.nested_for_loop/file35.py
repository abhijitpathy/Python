str = input("Enter the text: ")

for c1 in str:
  for c2 in str:
    if c1 < c2:
      status = "Increasing"
    elif c1 > c2:
      status = "Decreasing"
    else:
      status = "Same"

    print(f"{c1}→{c2} {status}")