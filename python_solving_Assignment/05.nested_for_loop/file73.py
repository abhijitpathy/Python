s1 = input("Student 1 marks: ").split()
s2 = input("Student 2 marks: ").split()
s3 = input("Student 3 marks: ").split()

t1, t2, t3 = 0, 0, 0

for m in s1:
  t1 += int(m)

for m in s2:
  t2 += int(m)

for m in s3:
  t3 += int(m)

print("Student totals:", t1, t2, t3)
print("Student averages:", t1 / len(s1), t2 / len(s2), t3 / len(s3))