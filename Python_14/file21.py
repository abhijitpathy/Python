while True:
    password = input("Enter password: ")

    upper = 0
    lower = 0
    digit = 0
    space = 0

    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            upper += 1
        elif ch >= 'a' and ch <= 'z':
            lower += 1
        elif ch >= '0' and ch <= '9':
            digit += 1
        elif ch.isspace():
            space += 1

    if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and space == 0:
        print("Valid password")
        break
    else:
        print("Invalid password. Try again.")