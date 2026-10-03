Res_ord_sys= int(input("Enter user type 1 -> starters, 2-> Main course 3 -> Desserts 4 -> Drinks "))

match Res_ord_sys:
    case 1:
        print("1 → soup")
        print("2 → spring roll")
        print("3 → Garlic Bread")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed soup")
            case 2:
                print("choosed spring roll")
            case 3:
                print("choosed Garlic bread")
            case _:
                print("Invalid option")

    case 2:
        print("1 → Pizza")
        print("2 → Pasta")
        print("3 → Biriyani")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed pizza")
            case 2:
                 print("choosed  pasta")
            case 3:
                print("choosed Biriyani")
            case _:
                print("Invalid option")


    case 3:
        print("1 → Ice cream")
        print("2 → cake")
        print("3 → Gulab jamun")
         
    
        option = int(input("Enter option: "))
    
        match option:
            case 1:
                print("choosed ice cream")
            case 2:
                print("choosed cake")
            case 3:
                print("choosed Gulab jamun")
            case _:
                print("Invalid option")

 
    case 4:
        print("1 → coffee")
        print("2 →  Tea")
        print("3 → Juice")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed coffee")
            case 2:
                 print("choosed Tea")
            case 3:
                print("choosed Juice")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")
    