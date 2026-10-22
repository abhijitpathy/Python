h=(input("enter word: "))
n = int(input("enter number"))

for i in range(len(h)):
    for j in range(1,n+1):
        print(h[i]+str(j),end="")
    print()