a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < 0:
    a = -a

if b < 0:
    b = -b

if a < b:
    smaller = a
else:
    smaller = b

for i in range(smaller, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break