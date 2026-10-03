print('''admin
teacher
student
guest''')
user_role = (input("Enter roles :")).lower

match user_role:
    case "admin":
        print("full acess")
    case "teacher":
        print("Teacher dashboard")
    case "student":
        print("student dashboard")
    case "guest":
        print("limited Acess")
    case _:
        print("Invalid Role")