print("1-> General medicine,2-> cardiology, 3-> orthopedics, 4 ->  pediatrics, 5 -> Emergency,6->Exit")
department = int(input("enter medical departmentto choice"))

match department:
    case 1:
        print("General medicine")
     
    case 2:
        print("cardiology")
    case 3:
        print("orthopedics")
    case 4:
        print("pediatrics")
    case 5:
        print("Emergency")
    case 6:
        print("exit")
    case _:
        print("invalid Department")


