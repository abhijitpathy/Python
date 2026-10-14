while True:
    marks = float(input("Enter marks (0 to 100): "))
    if 0 <= marks <= 100:
        break
    print("Invalid marks. Please enter a value between 0 and 100.")

if marks >= 75:
    result = "Distinction"
elif 60 <= marks < 75:
    result = "First Class"
elif 35 <= marks < 60:
    result = "Pass"
else:
    result = "Fail"

print(f"Result: {result}")
