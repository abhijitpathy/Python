num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

common_count = 0

for d in num1:
  if d in num2:
    common_count += 1
    num2 = num2.replace(d, "", 1)

print(f"Common digit count = {common_count}.")