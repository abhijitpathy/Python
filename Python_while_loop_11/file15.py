# 15. Count even numbers
n = int(input("Enter n: "))
i = 1
count = 0

while i <= n:
    if i % 2 == 0:
        count = count + 1
    i = i + 1

print(count)