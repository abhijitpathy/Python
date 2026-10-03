poor = 0
average = 0
good = 0
excellent = 0
outstanding = 0
total = 0

for i in range(10):
    rating = float(input("Enter rating: "))
    total = total + rating

    if rating <= 3:
        poor += 1
    elif rating <= 5:
        average += 1
    elif rating <= 7:
        good += 1
    elif rating <= 9:
        excellent += 1
    else:
        outstanding += 1

print("Poor:", poor)
print("Average:", average)
print("Good:", good)
print("Excellent:", excellent)
print("Outstanding:", outstanding)
print("Average rating:", total / 10)