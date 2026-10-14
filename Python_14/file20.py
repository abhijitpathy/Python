while True:
    count = int(input("enter numbers "))
    if 1 <= count <= 20:
        break
    print("Invalid count.")

total_sum = 0
for i in range(count):
    while True:
        value = float(input(f"Enter number {i + 1}: "))
        if 0 <= value <= 100:
            break
        print("Invalid value. Must be between 0 and 100.")
    total_sum += value

average = total_sum / count
print(f"Average: {average}")
