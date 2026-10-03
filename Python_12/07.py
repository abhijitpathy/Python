bnk_app = int(input("Enter bank application menu :"))

match bnk_app:
    case 1:
        print("Account balance")
    case 2:
        print("Mini Statement")
    case 3:
        print("Fund Transfer")
    case 4:
        print("bill payment")
    case 5:
        print("Customer Support")
    case _:
        print("Invalid Choice")