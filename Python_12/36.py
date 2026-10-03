dig_pay_sys= int(input("Enter user type 1 -> upi, 2-> Card 3 -> wallet : "))

match dig_pay_sys:
    case 1:
        print("1 → scan qr")
        print("2 → enter upi id")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed scan qr")
            case 2:
                print("choosed upi id")
            case _:
                print("Invalid option")

    case 2:
        print("1 → credit card")
        print("2 → Debit card")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed credit card")
            case 2:
                 print("choosed Debit card")

            case _:
                print("Invalid option")


    case 3:
        print("1 → Add  money")
        print("2 → Pay using wallet")
         
    
        option = int(input("Enter option: "))
    
        match option:
            case 1:
                print("add money")
            case 2:
                print("Pay using wallet")
            case _:
                print("Invalid option")

