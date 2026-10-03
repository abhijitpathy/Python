total = 0
for i in range(6):
    n = int(input("enter no of units:"))
    if n<100:
        bill = ((100-n)*5)
    elif n<200:
        bill = (500+((200-n)*7))
    elif n<400:
        bill = (1200+((400-n)*10))
    else:
        bill = ((3200+((n-400)*15)))

    if bill <1000:
        group = "low"
    elif bill<3000:
        group = "medium"
    else:
        group = "high"
    print("the electricity bill is",bill)
    print("your electricity bill is ",group)
    total += bill
    
print("Total Revenue:", total)




