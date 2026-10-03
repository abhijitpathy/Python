print("1-> celcious to farhenite, 2->  fahrenite to Celcius")
operation = int(input("enter operation number :"))
temp = int(input("enter  temp :"))


match operation:
    case 1:
        print( (temp * 9/5) + 32)
    case 2:
        print( (temp - 32) * 5/9)
  
    case _:
        print("invalid operation !")