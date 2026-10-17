n = int(input("Enter number: "))

if n >= 0 and str(n) == str(n)[::-1]:
    print(True)
else:
    print(False)