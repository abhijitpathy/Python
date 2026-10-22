n = int(input("enter number:"))

max_product = 0

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i * j > max_product:
      max_product = i * j

print("Max Product =", max_product)