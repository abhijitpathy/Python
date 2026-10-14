while True:
    marks = int(input("Enter marks (0 to 100): "))
    
    if 0 <= marks <= 100:
        break  
        
    print("Invalid marks! Please enter a value between 0 and 100.")

print(f"Accepted marks: {marks}")
