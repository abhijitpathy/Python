while True:
    username = input("Enter a username: ").strip()
    if len(username) >= 5 and " " not in username:
        break
    print("Invalid username. Must be at least 5 characters long and contain no spaces.")

print(f"Accepted username: {username}")
