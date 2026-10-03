print("1-> Light,2-> Fan, 3-> AC, 4 ->  TV")
device = int(input("enter menu to choice"))

match device:
    case 1:
        print("entered device 1")
        print("light on")
     
    case 2:
        print("entered device 2")
        print("fan on")
    case 3:
        print("entered device 3")
        print("AC controlled opened")
    case 4:
        print("entered device 4")
        print("TV controlled on ")
    case 5:
        print("exit")
    case _:
        print("invalid choice")