while True:
    number = int(input("Enter a positive integer divisible by both 3 and 5: "))
    if number > 0 and number % 3 == 0 and number % 5 == 0:
        break
    print("Invalid number. It must be greater than 0 and divisible by both 3 and 5.")

print(f"Accepted number: {number}")
