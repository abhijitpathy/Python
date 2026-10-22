n = int(input("enter number of grid"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j % 2 == 1:
            print(j,end=" ")
    print()
