str = input("enter a word")
for i in str:
    if i == "s":
        print("character exists")
        break
else:
    print("character missing")