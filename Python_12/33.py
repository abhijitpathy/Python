Travel_Booking_system= int(input("Enter user type 1 -> Flight, 2-> Train -> Bus "))

match Travel_Booking_system:
    case 1:
        print("1 → Economy")
        print("2 → Business")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed economy")
            case 2:
                print("choosed Buissness")
            case _:
                print("Invalid option")

    case 2:
        print("1 → Sleeper")
        print("2 → Ac")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed sleeper")
            case 2:
                 print("choosed ac")
            case _:
                print("Invalid option")

 
    case 3:
        print("1 →ordinary")
        print("2 →  volvo")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Choosed ordinary")
            case 2:
                 print("choosed Volvo")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")