n = int(input("Enter N: "))

count = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        count = count + 1

print(count)