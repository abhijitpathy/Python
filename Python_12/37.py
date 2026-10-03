onl_plt= int(input("Enter user type 1 -> Programming, 2-> Mathematics 3 -> communication : "))

match onl_plt:
    case 1:
        print("1 → python ")
        print("2 → java")
        print("3 -> c++")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed pyhton")
            case 2:
                print("choosed java")
            case 3:
                print("choosed c++")
            case _:
                print("Invalid option")

    case 2:
        print("1 → Alegebra")
        print("2 → Calculus")
        print("3 -> statistics")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("choosed Alegebra")
            case 2:
                 print("choosed calculus")
            case 3:
                print("choosed statistics")

            case _:
                print("Invalid option")


    case 3:
        print("1 → English")
        print("2 → Presentation")
        print("3 -> Interview Skills")
         
    
        option = int(input("Enter option: "))
    
        match option:
            case 1:
                print("choosed english")
            case 2:
                print("choosed presentation")
            case 3 :
                print("choosed Interview skills")
            case _:
                print("Invalid option")