a = int(input("Enter A: "))
b = int(input("Enter B: "))
limit = int(input("Enter limit: "))

for i in range(1, limit + 1):
  for j in range(1, limit + 1):
    for k in range(1, limit + 1):
      if i == j * a:
        if i == k * b:
          print(i, end=" ")