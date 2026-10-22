num_students = int(input("Enter number of students: "))

best_student = 1
max_present = int(input(f"Enter present count for Student 1: "))  

for i in range(2, num_students + 1):
  present = int(input(f"Enter present count for Student {i}: "))

  if present > max_present:
    max_present = present
    best_student = i

print(f"Student {best_student} has highest attendance.")