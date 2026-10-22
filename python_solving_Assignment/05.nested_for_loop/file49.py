n = int(input("enter number:"))
for i in range(1,n+1):
    print(f"{i} ->", end="")
    for j in range(1,i+1):
        if i %j ==0:
            print(j,end="")
    print()