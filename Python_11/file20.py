# 20. Product from 1 to n
n = int(input("Enter n: "))
i = 1
product = 1

while i <= n:
    product = product * i
    i = i + 1

print(product)