d20 = d15 = d10 = 0
total_discount = 0

for i in range(10):
    price = int(input("Enter price: "))

    if price >= 5000:
        discount = price * 20 / 100
        d20 += 1
    elif price >= 3000:
        discount = price * 15 / 100
        d15 += 1
    elif price >= 1000:
        discount = price * 10 / 100
        d10 += 1
    else:
        discount = 0

    final = price - discount
    total_discount += discount

    print("Final price:", final)

print("20 discount:", d20)
print("15 discount:", d15)
print("10  discount:", d10)
print("Total discount:", total_discount)

