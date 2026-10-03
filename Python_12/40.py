role = int(input("Enter role: "))

match role:

    case 1:
        option = int(input(
            "1 → Profile\n"
            "2 → Marks\n"
            "3 → Attendance\n"
            "4 → Courses\n"
            "Enter option: "
        ))

        match option:
            case 1:
                print("Opening Student Profile")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case 4:
                print("Opening Student Courses")
            case _:
                print("Invalid Student Option")

    case 2:
        option = int(input(
            "1 → Students\n"
            "2 → Enter Marks\n"
            "3 → Attendance\n"
            "4 → Courses\n"
            "Enter option: "
        ))

        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Enter Marks")
            case 3:
                print("Opening Teacher Attendance")
            case 4:
                print("Opening Teacher Courses")
            case _:
                print("Invalid Teacher Option")

    case 3:
        option = int(input(
            "1 → Fees\n"
            "2 → Admissions\n"
            "3 → Notices\n"
            "4 → Departments\n"
            "Enter option: "
        ))

        match option:
            case 1:
                print("Opening Fees")
            case 2:
                print("Opening Admissions")
            case 3:
                print("Opening Notices")
            case 4:
                print("Opening Departments")
            case _:
                print("Invalid Administration Option")

    case _:
        print("Invalid Role")