fail = 0
pas = 0
good = 0
excellent = 0

for i in range(10):
    marks = int(input("Enter marks: "))

    if marks < 35:
        print("Fail")
        fail += 1
    elif marks < 50:
        print("Pass")
        pas += 1
    elif marks < 75:
        print("Good")
        good += 1
    else:
        print("Excellent")
        excellent += 1

print("Fail:", fail)
print("Pass:", pas)
print("Good:", good)
print("Excellent:", excellent)