rows = int(input("Enter rows: "))
seats = int(input("Enter seats per row: "))

for i in range(rows):
  for j in range(1, seats + 1):
    if j % 2 != 0:
      cost = 100
    else:
      cost = 150

    print(cost, end=" ")

  print() 