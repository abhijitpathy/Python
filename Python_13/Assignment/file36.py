n = [12,-98,43,-23,-24,23,46,57]
for i in n:
    if i<0:
        continue
    if i == 23:
        print("target found")
        break
    print(i)
else:
    print("target not found")

    
