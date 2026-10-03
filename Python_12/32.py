school_management_sys= int(input("Enter user type 1 -> student, 2-> Teacher 3 -> parent: "))

match school_management_sys:
    case 1:
        print("1 → marks")
        print("2 → Attendence")
        print("3 → Homework")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("View marks scored")
            case 2:
                print("View attendence")
            case 3:
                print("view Homework")
            case _:
                print("Invalid option")

    case 2:
        print("1 → Enter Marks")
        print("2 → Attendence")
        print("3 → Assign homework")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Enter marks")
            case 2:
                 print("view attendence")
            case 3:
                print("Assign homework")
            case _:
                print("Invalid option")

 
    case 3:
        print("1 → Child  Marks")
        print("2 →  Child Attendence")
        print("3 → Contact Teacher")
     

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("view child marks")
            case 2:
                 print("view child attendence")
            case 3:
                print("conatact teacher")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")
    