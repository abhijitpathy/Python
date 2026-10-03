print('''1 → View Profile
2 → View Courses
3 → View Marks
4 → View Attendance
5 → Logout
''')
Std_menu = int(input("Enter student portal menu :"))

match Std_menu:
    case 1:
        print("View profile")
    case 2:
        print("view courses")
    case 3:
        print("view marks")
    case 4:
        print("view Attendance")
    case 5:
        print("logout")
    case _:
        print("Invalid Choice")