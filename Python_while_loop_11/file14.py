# 14. Divisible by both 2 and 3
n = int(input("Enter n: "))
i = 1

while i <= n:
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")
    i = i + 1