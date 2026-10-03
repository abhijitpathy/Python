Banking_sys= int(input("Enter user type 1 -> Personal, 2-> Buissness Banking: "))

match Banking_sys:
    case 1:
        print("1 → Balance")
        print("2 → Transfer")
        print("3 → Loan")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("View Balance")
            case 2:
                print("choosed Transfer")
            case 3:
                print("choosed loan")
            case _:
                print("Invalid option")

    case 2:
        print("1 → Balance")
        print("2 → Payroll")
        print("3 → Buissness Loan")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("View balance")
            case 2:
                 print("view payroll")
            case 3:
                print("BUissness Loan")
            case _:
                print("Invalid option")
