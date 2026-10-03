choice = int(input("1 → Employee\n2 → Manager\nEnter choice: "))

match choice:

    case 1:
        option = int(input(
            "1 → View Profile\n"
            "2 → Apply Leave\n"
            "3 → View Salary\n"
            "Enter choice: "
        ))

        match option:
            case 1:
                print("Viewing Profile")

            case 2:
                days = int(input("Enter number of leave days: "))

                if days > 0:
                    print("Leave Request Submitted")
                else:
                    print("Invalid Leave Days")

            case 3:
                print("Viewing Salary")

            case _:
                print("Invalid Employee Option")

    case 2:
        option = int(input(
            "1 → View Team\n"
            "2 → Approve Leave\n"
            "3 → View Reports\n"
            "Enter choice: "
        ))

        match option:
            case 1:
                print("Viewing Team")

            case 2:
                print("Leave Approved")

            case 3:
                print("Viewing Reports")

            case _:
                print("Invalid Manager Option")

    case _:
        print("Invalid Main Choice")
