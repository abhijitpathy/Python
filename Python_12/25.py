print("1-> Regular,2-> premimum, 3-> vip")
ticket = int(input("enter menu to choice"))

match ticket:
    case 1:
        age = int(input("enter age"))
        if  age <5:
            print(" free entry")
        else:
            print("no free entry")
    case 2:
        print("selected premimum ticket")
    case 3:
        print("selected vip ticket")
    case 4:
        print("exit")
    case _:
        print("invalid choice")