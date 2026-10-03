print("1-> +, 2-> - ,3 -> *,4->/")
operation = int(input("enter operation number :"))
first_num = int(input("enter  first number :"))
second_num = int(input("enter second number :"))

match operation:
    case 1:
        print(first_num + second_num)
    case 2:
        print(first_num - second_num)
    case 3:
        print(first_num * second_num)
    case 4:
        print(first_num / second_num)
    case _:
        print("invalid operation !")