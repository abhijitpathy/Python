for i in range(5):
    num = input("Enter a number: ")
    even = 0
    odd = 0

    for digit in (num):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    if even > odd:
        print("Even occurs more")
    elif odd > even:
        print("Odd occurs more")
    else:
        print("Equal")