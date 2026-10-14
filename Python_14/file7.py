balance = 5000

while True:
    withdrawal = float(input(f"Enter withdrawal amount (Available: ₹{balance}): "))
    if 0 < withdrawal <= balance:
        break
    print("Invalid amount. Must be greater than 0 and less than or equal to your balance.")

balance -= withdrawal
print(f"Withdrawal successful. Updated balance: ₹{balance}")
