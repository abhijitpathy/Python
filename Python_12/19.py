food_preference = int(input("Enter user type 1 -> Vegetarian, 2-> Non-vegetarian: "))

match food_preference:
    case 1:
        print("1 → paneer")
        print("2 → Dal")
        print("3 → Veg biriyani")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("paneer")
            case 2:
                print("Dal")
            case 3:
                print("Veg bIriyani")
            case _:
                print("Invalid option")

    case 2:
        print("1 → chicken biriyani")
        print("2 → chicken curry")
        print("3 → fish curry")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("chicken biriyani")
            case 2:
                 print("chicken curry")
            case 3:
                print("Fish Fry")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")