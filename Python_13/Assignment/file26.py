for x in range(3):
    continue
else:
    print("A")

# here the else blocks get printed because continue only skips the iteration and the loops get completed

for x in range(3):
    break
else:
    print("B")

# here if the break get executes the else condition wont get printed

for x in range(0):
    print(x)
else:
    print("C")

# here the loops get completed so else case will be printed
