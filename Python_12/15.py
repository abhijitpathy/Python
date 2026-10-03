shp_memb = (input("shop membership :")).lower()

match shp_memb:
    case "Bronze"| "1":
        print("Basic Membership")
    case "silver"| "2":
        print("basic membership")
    case "gold"| "3":
        print("premium membership")
    case "platinum"| "4":
         print("premium membership")
            
    case _:
        print("Invalid Choice")