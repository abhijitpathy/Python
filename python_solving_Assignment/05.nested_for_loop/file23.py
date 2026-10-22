s = input("enter word: ")
for i  in s:
    for j in s:
        if i == j:
            print(f"{i}/{j} is same ",end="")
        else:
            print(f"{i}/{j} are different ",end="")
    print()