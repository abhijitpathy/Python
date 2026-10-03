user = int(input("Enter user type: "))

match user:
    case 1:
        print("1 → View Courses")
        print("2 → View Marks")
        print("3 → View Attendance")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid option")

    case 2:
        print("1 → View Students")
        print("2 → Enter Marks")
        print("3 → View Attendance")

        option = int(input("Enter option: "))

        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid option")

    case _:
        print("Invalid user type")