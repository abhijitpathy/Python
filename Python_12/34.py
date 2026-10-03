print("1-> Start game,2-> Load Game, 3-> Settings, 4 ->  Exit:")
status = int(input("enter order status"))

match status:
    case 1:
        print("started game")
     
    case 2:
        print("loading game")
    case 3:
        print("settings")
        print("1 → Sounds")
        print("2 → Graphics")
        print("3 -> controls")
        
        option = int(input("Enter option: "))
        
        match option:
            case 1:
                print("choosed sounds")
            case 2:
                print("choose graphics")
            case 3:
                print("choosed Controls")
            case _:
                print("invalid choice")
    case 4:
        print("Exit")

    case _: 
        print("invalid choice")
