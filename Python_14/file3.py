while True:
    age = int(input("Enter your age (0 to 120): "))
    if 0 <= age <= 120:
        break
    print("Error: Age must be between 0 and 120.")

print(f"Accepted age: {age}")
