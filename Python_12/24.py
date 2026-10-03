print("1-> start exam,2-> view result, 3-> exit")
account = int(input("enter menu to choice"))

match account:
    case 1:
        age = int(input("enter withdrawl ammount"))
        if  age >=18:
            print(" you can start the exam")
        else:
            print("not eligible for exam")
    case 2:
        print("view results")
    case 3:
        print("exit")
    case _:
        print("invalid choice")

        