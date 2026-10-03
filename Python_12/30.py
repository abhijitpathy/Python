print("1-> placed,2-> Confirmed, 3-> preparing, 4 ->  out of delivery, 5 -> delivered, 6 -> cancelled")
status = int(input("enter order status"))

match status:
    case 1:
        print("your ordered is placed")
     
    case 2:
        print("your ordered is confirmed")
    case 3:
        print("your order is being prepared")
    case 4:
        print("your order is in the way")
    case 5:
        print("your order is delivers ")
    case 6:
        print("your ordered is cancelled")
    case _:
        print("invalid choice")
