# 13. Divisible by 3
n = int(input("Enter n: "))
i = 1

while i <= n:
    if i % 3 == 0:
        print(i, end=" ")
    i = i + 1