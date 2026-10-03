Shp_menu = int(input("Enter student portal menu :"))

match Shp_menu:
    case 1:
        print("electronics")
    case 2:
        print("clothing")
    case 3:
        print("Books")
    case 4:
        print("Grocery")
    case 5:
        print("exit")
    case _:
        print("Invalid Shopping menu")