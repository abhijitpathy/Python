while True:
    month = int(input("Enter a month number (1-12): "))
    day = int(input("Enter a day number (1-31): "))
    
    if 1 <= month <= 12:
        if month == 2 and 1 <= day <= 29:
            break
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            break
        elif month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            break
            
    print("Invalid combination. Please enter a valid day for the chosen month.")

print(f"Accepted Date: Month {month}, Day {day}")

