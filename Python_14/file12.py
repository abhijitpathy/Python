balance = 2000

while True:
    deposit = float(input("Enter deposit amount: "))
    if deposit > 0:
        break
    print("Invalid amount. Deposit must be greater than 0.")

balance += deposit
print(f"Deposit successful. Updated balance: ₹{balance}")
