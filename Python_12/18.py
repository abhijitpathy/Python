category = int(input("Enter user type 1 -> electronics, 2-> Clothing: "))

match category:
    case 1:
        print("1 → mobile")
        print("2 → laptop")
        print("3 → clothing")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("mobile")
            case 2:
                print("laptop")
            case 3:
                print("Head phones")
            case _:
                print("Invalid option")

    case 2:
        print("1 → shirts")
        print("2 → jeans")
        print("3 →  shoes")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("shirts")
            case 2:
                 print("Jeans")
            case 3:
                print("shoes")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")