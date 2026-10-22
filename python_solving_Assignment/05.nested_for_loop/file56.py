n = int(input("Enter N: "))
target = int(input("Enter target: "))

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i + j == target:
      print(i, j)
