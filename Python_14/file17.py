balance = 10000.0

while True:
    print("\n--- Banking Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        print(f"Current Balance: ₹{balance:,.2f}")
        
    elif choice == '2':
        while True:
            deposit = float(input("Enter deposit amount: "))
            if deposit > 0:
                balance += deposit
                print(f"Successfully deposited ₹{deposit:,.2f}. New Balance: ₹{balance:,.2f}")
                break
            print("Invalid deposit..")
            
    elif choice == '3':
        while True:
            withdrawal = float(input("Enter withdrawal amount: "))
            if 0 < withdrawal <= balance:
                balance -= withdrawal
                print(f"Successfully withdrew ₹{withdrawal:,.2f}. New Balance: ₹{balance:,.2f}")
                break
            print(f"Invalid withdrawal. Amount must be greater than zero and cannot exceed ₹{balance:,.2f}.")
            
    elif choice == '4':
        print("exit")
        break
        
    else:
        print("Invalid choice. Please select an option between 1 and 4.")
