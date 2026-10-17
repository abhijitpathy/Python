a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < 0:
    a = -a

if b < 0:
    b = -b

if a > b:
    larger = a
else:
    larger = b

for i in range(larger, a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break