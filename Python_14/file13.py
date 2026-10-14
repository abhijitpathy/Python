while True:
    number = int(input("Enter an integer between 1 and 100: "))
    if 1 <= number <= 100:
        break
    print("Invalid input. Number must be between 1 and 100.")

print(f"Accepted number: {number}")
