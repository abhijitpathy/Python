for i in range(1, 5):
    if i == 3:
        pass
    print(i)


for i in range(1, 5):
    if i == 3:
        continue
    print(i)

# here the difference is clear in the 1st one it prints 1234 whereas in continue one it skips 3 and print 124 .
# pass does nothing so 3 gets to be printed whereas continue skips that iteration .
