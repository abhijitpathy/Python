total = 0
budget = 0
regular = 0
premium = 0
luxury = 0

for i in range(8):
    price = int(input("Enter product price: "))
    total += price

    if price < 500:
        print("Budget")
        budget += 1

    elif price < 2000:
        print("Regular")
        regular += 1

    elif price < 5000:
        print("Premium")
        premium += 1

    else:
        print("Luxury")
        luxury += 1

average = total / 8

print("Total:", total)
print("Budget:", budget)
print("Regular:", regular)
print("Premium:", premium)
print("Luxury:", luxury)
print("Average:", average)