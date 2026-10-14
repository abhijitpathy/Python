SECRET_PIN = "2468"
attempts = 3

for i in range(attempts):
    pin = input("Enter your PIN: ")
    if pin == SECRET_PIN:
        print("Access granted.")
        break
    
    remaining = attempts - (i + 1)
    if remaining > 0:
        print(f"Incorrect PIN. You have {remaining} attempts left.")
else:
    print("Access denied. Too many incorrect attempts.")

