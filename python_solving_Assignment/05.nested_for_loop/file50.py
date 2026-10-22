n = int(input("enter number:"))
for i in range(1, n + 1):
  divisior_sum = 0
  for j in range(1, i):
    if i % j == 0:
      divisior_sum += j

  if divisior_sum == i:
    print(i, end="")
print()