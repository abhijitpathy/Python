Day = (input("Enter day :")).lower()

match Day:
    case "monday"| "1":
        print("weekday")
    case "tuesday"| "2":
        print("weekday")
    case "wednesday"| "3":
        print("weekday")
    case "thursday"| "4":
         print("weekday")
    case "friday"| "5":
        print("weekday")
    case "saturday"| "6":
            print("weekend")
    case "sunday"| "7":
            print("weekend")
            
    case _:
        print("Invalid Choice")