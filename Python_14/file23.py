while True:
    score1 = float(input("Enter score 1 (0-100): "))
    if 0 <= score1 <= 100:
        break
    print("Invalid score. Must be between 0 and 100.")

while True:
    score2 = float(input("Enter score 2 (0-100): "))
    if 0 <= score2 <= 100:
        break
    print("Invalid score. Must be between 0 and 100.")

while True:
    score3 = float(input("Enter score 3 (0-100): "))
    if 0 <= score3 <= 100:
        break
    print("Invalid score. Must be between 0 and 100.")

total = score1 + score2 + score3
average = total / 3

print(f"Total: {total}")
print(f"Average: {average}")
