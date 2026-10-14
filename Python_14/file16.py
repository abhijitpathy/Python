num1 = float(input("Enter the first number: "))

while True:
    operator = input("Enter an operator (+, -, *, /): ").strip()
    if operator in ["+", "-", "*", "/"]:
        break
    print("Invalid operator. Please try again.")

while True:
    num2 = float(input("Enter the second number: "))
    if operator == "/" and num2 == 0:
        print("Error: Division by zero .")
        continue
    break

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(f"Result: {num1} {operator} {num2} = {result}")
