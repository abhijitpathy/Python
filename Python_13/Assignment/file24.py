n = int(input("enter a number"))
for i in range(1,n+1):
    if (n-2)/i ==0:
        print("not prime")
        break
else:
    print("prime")