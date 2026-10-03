for i in range(5):
    password = input("Enter password: ")

    count = 0
    upper = 0
    lower = 0
    digit = 0
    special = 0

    if len(password) >= 8:
        count += 1

    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            upper = 1
        elif ch >= 'a' and ch <= 'z':
            lower = 1
        elif ch >= '0' and ch <= '9':
            digit = 1
        else:
            special = 1

    count += upper + lower + digit + special

    if count == 5:
        print("Strong")
    elif count >= 3:
        print("Medium")
    else:
        print("Weak")