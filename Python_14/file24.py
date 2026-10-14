balance = 10000

while True:
    withdrawal = int(input(f"Enter withdrawal amount (Available: ₹{balance}): "))
    
    if withdrawal <= 0:
        print("Invalid amount. Must be greater than 0.")
    elif withdrawal > balance:
        print("Invalid amount. Cannot exceed your available balance.")
    elif withdrawal % 100 != 0:
        print("Invalid amount. Must be a multiple of ₹100.")
    else:
        break

balance -= withdrawal
print(f"Withdrawn amount: ₹{withdrawal}")
print(f"Remaining balance: ₹{balance}")
