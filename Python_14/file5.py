while True:
    password = input("Enter a password (at least 8 characters): ").strip()
    if len(password) >= 8:
        break
    print("Error: Password must be at least 8 characters long.")

print("Success: Valid password entered.")
