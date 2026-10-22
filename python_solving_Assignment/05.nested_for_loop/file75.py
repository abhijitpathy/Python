num_students = int(input("Enter number of students: "))

for i in range(1, num_students + 1):
  days = input(f"Enter attendance for Student {i} (e.g., P A P P): ").split()

  present = 0
  absent = 0

  for status in days:
    if status == "P":
      present += 1
    elif status == "A":
      absent += 1

  print(f"Student {i} Present={present} Absent={absent}")