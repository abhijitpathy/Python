junior = mid = senior = executive = 0
total = 0

for i in range(8):
    salary = int(input("Enter salary: "))
    total += salary

    if salary < 25000:
        junior += 1
        print("Junior")

    elif salary <= 50000:
        mid += 1
        print("Mid")

    elif salary <= 100000:
        senior += 1
        print("Senior")

    else:
        executive += 1
        print("Executive")

print("Junior:", junior)
print("Mid:", mid)
print("Senior:", senior)
print("Executive:", executive)
print("Average:", total / 8)

