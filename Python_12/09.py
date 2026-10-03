weather = (input("Enter weather :")).lower()

match weather:
    case "sunny":
        print("wear sunglasses")
    case "rainy":
        print("carry an umbrella")
    case "cloudy":
        print("weather may change")
    case "snowy":
        print("wear warm clothes")
    case _:
        print("Invalid Choice")