print("1-> km to m , 2-> m to km ,3 ->  kg to grams,4-> grams to kg")
operation = int(input("enter operation number :"))
value = int(input("enter  value :"))


match operation:
    case 1:
        print(value*1000)
    case 2:
        print(value/1000)
    case 3:
        print(value*1000)
    case 4:
        print(value/1000)
    case _:
        print("invalid operation !")

