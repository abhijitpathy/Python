n = int(input("enter number :"))
a, b = 0, 1
print(a,end="")
print(b,end="")
for i in range(2, n):
    next_num = a + b
    print(next_num,end=" ")
    a = b
    b = next_num