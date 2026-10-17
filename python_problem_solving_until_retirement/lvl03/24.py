n = int(input("Enter number: "))

if n < 0:
    print(-int(str(-n)[::-1]))
else:
    print(int(str(n)[::-1]))