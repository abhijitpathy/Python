n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        x = i * j

        if x % 5 == 0:
            print("F", end=" ")
        elif x % 2 == 0:
            print("E", end=" ")
        else:
            print("O", end=" ")

    print()
