account = int(input("Enter user type 1 -> savings, 2-> Current: "))

match account:
    case 1:
        print("1 → check balanace")
        print("2 → Deposit")
        print("3 → withdraw")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("check balance")
            case 2:
                print("Deposits")
            case 3:
                print("withdraw")
            case _:
                print("Invalid option")

    case 2:
        print("1 → check balanace")
        print("2 → Deposit")
        print("3 → withdraw")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("check balance")
            case 2:
                 print("Deposits")
            case 3:
                print("withdraw")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")