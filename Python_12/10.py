print('''upi
card
cash
wallet''')
payment_method = (input("Enter payment method :")).lower()

match payment_method:
    case "upi":
        print("upi payment selected")
    case "card":
        print("Card method selected")
    case "cash":
        print("cash payment selected")
    case "wallet":
        print("wallet payment selected")
    case _:
        print("Invalid Choice")