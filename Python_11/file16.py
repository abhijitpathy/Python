# 16. Sum from 1 to n
n = int(input("Enter n: "))
i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print(sum)