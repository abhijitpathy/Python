text = input("Enter a string: ")
times = 0
for i in text:
    for character in text:
        if i == character:
            times += 1

    if times > 1:
        if times == 2:
            print(i, "Duplicate")
        elif times <= 4:
            print(i, "Repeated")
        else:
            print(i, "Highly Repeated")