settings = int(input("Enter menu :"))

match settings:
    case 1:
        print("Wifi")
    case 2:
        print("Bluetooth")
    case 3:
        print("Mobile Data")
    case 4:
        print("Airplane mode")
    case 5:
        print("Exit")
    case _:
        print("Invalid Choice")
    