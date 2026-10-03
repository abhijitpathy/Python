print("1-> savings,2-> current")
account = int(input("enter account to choice"))

match account:
    case 1:
        print("savings account")
        withdrawl = int(input("enter withdrawl ammount"))
        if withdrawl >=0:
            print(" withdrawl amount",withdrawl)
        else:
            print("invalid Amount ")
    case 2:
        print("current account")
        withdrawl = int(input("enter withdrawl ammount"))
        if withdrawl >=0:
            print(" withdrawl amount",withdrawl)
        else:
            print("invalid Amount ")
    case _:
        print("invalid choice")
