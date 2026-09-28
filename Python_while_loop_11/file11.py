# 11. Even numbers from 1 to n
n = int(input("Enter n: "))
i = 1

while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1