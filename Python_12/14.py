print('''1 → Low
2 → Medium
3 → High
4 → Critical''')
priority = (input("priority number :")).lower()

match priority:
    case "low"| "1":
        print("Normal Priority")
    case "Medium"| "2":
        print("Normal priority")
    case "High"| "3":
        print("Urgent priority")
    case "Critical"| "4":
         print("urgent priority")
            
    case _:
        print("Invalid Choice")