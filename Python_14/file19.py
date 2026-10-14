while True:
    quantity = int(input("Enter product quantity: "))
    if quantity > 0:
        break
    print("Invalid quantity. Must be a positive integer.")

while True:
    unit_price = float(input("Enter unit price: "))
    if unit_price > 0:
        break
    print("Invalid price. Must be greater than zero.")

total_cost = quantity * unit_price
print(f"Total Cost: {total_cost}")
