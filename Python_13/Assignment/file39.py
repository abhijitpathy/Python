n = [3,-7,19,-25,37,12,46,42,74]
for i in n:
    if i % 4 == 0 and i % 6 == 0:
        print("founded" , i)
        break
    if i<0:
        continue
    print(i)

else:
    print("no matching found")
