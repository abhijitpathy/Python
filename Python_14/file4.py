while True:
    print("\n1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice in [1, 2, 3, 4]:
        break
    print("Invalid choice. Please try again.")

print(f"Accepted choice: {choice}")
