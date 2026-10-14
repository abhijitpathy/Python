while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    trimmed_username = username.strip()
    
 
    username_valid = len(trimmed_username) >= 5 and " " not in trimmed_username
    
    
    password_valid = len(password) >= 8 and password.strip() != ""
    
    if username_valid and password_valid:
        break
        
    print("Invalid input. Please ensure username is >= 5 chars with no internal spaces, and password is >= 8 chars and not blank.")

print("Success: Both fields are valid.")




# for space in password


while True:
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if len(username) >= 5 and " " not in username and len(password) >= 8 and " " not in password and password.strip() != "":
        print("Username and password are valid!")
        break
    else:
        print("Invalid username or password. Try again.")


