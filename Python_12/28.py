print("1-> Book Ticket,2-> cancel Ticket, 3-> check PNR , 4 ->  Train schedule,5 ->Exit")
device = int(input("enter menu to choice"))

match device:
    case 1:
        print("Book Ticket")
     
    case 2:
        print("cancel Ticket")
    case 3:
        print("Check PNR")
    case 4:
        print('Train schedule')
    case 5:
        print("exit")
    case _:
        print("invalid choice")