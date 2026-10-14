while True:
    temperature = float(input("Enter temperature (-20 to 45): "))
    if -20 <= temperature <= 45:
        break
    print("Error: Temperature must be between -20 and 45.")

print(f"Accepted temperature: {temperature}")
