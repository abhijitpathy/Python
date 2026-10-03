movie_booking = int(input("Enter movie booking time :"))

match movie_booking:
    case 1:
        print("Morning show")
    case 2:
        print("Afternoon show")
    case 3:
        print("Evening show")
    case 4:
        print("night show")
    case _:
        print("Invalid Choice")