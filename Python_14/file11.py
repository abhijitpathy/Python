while True:
    number = int(input("Enter an integer between 10 and 50: "))
    if 10 <= number <= 50:
        break
    print("Invalid input. Number must be between 10 and 50.")

if number % 2 == 0:
    print(f"Accepted number {number} is Even.")
else:
    print(f"Accepted number {number} is Odd.")
