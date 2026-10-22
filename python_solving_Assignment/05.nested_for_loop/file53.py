a = int(input("Enter A: "))
b = int(input("Enter B: "))

for i in range(1, a + 1):
  for j in range(1, b + 1):
    if i == j:
      if a % i == 0:
        if b % i == 0:
          print(i, end=" ")