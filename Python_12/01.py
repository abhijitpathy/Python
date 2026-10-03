menu = int(input("Enter menu :"))

match menu:
    case 1:
        print("pizza")
    case 2:
        print("Burger")
    case 3:
        print("pasta")
    case 4:
        print("sandwich")
    case _:
        print("Invalid Choice")