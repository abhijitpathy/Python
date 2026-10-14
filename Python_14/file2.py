while True:
    number = int(input("Enter a positive integer : "))
    if number > 0:
        break
    print("Invalid entry! The number must be greater than 0.")

print(f"Accepted number: {number}")
