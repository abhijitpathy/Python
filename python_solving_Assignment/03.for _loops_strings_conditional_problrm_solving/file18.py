balance = int(input("Enter starting balance: "))

deposit = 0
withdrawal = 0

for i in range(7):
    print("Day", i + 1)

    d = int(input("Enter deposit amount 0 if no deposit: "))
    w = int(input("Enter withdrawal amount 0 if no withdrawl: "))

    if d > 0:
        balance += d
        deposit += 1

    if w > 0:
        if w <= balance:
            balance -= w
            withdrawal += 1
        else:
            print("Withdrawal rejected")

    if balance < 1000:
        print("Low Balance")

print("Final Balance:", balance)
print("Deposits:", deposit)
print("Withdrawals:", withdrawal)




