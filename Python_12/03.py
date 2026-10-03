print(''' 1 → Check Balance
2 → Withdraw Money
3 → Deposit Money
4 → Change PIN
5 → Exit''')
Atm_menu = int(input("Enter menu :"))

match Atm_menu:
    case 1:
        print("check Balance")
    case 2:
        print("Withdrawl Money")
    case 3:
        print("Deposit")
    case 4:
        print("change Pin")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")