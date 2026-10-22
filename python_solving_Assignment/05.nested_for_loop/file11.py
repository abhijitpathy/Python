n = int(input("enter number rows"))
l = int(input("enter number column"))
for i in range(1,n+1):
    for j in range(1,l+1):
        if j % 2 == 0:
            print(j,end=" ")
    print()

    