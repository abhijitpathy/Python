choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print("Engine")
        option = int(input("1 → Start\n2 → Stop\nEnter choice: "))

        match option:
            case 1:
                print("Engine Started")
            case 2:
                print("Engine Stopped")
            case _:
                print("Invalid choice")

    case 2:
        print("Lights")
        option = int(input("1 → Headlights\n2 → Indicators\n3 → Hazard Lights\nEnter choice: "))

        match option:
            case 1:
                print("Headlights ON")
            case 2:
                print("Indicators ON")
            case 3:
                print("Hazard Lights ON")
            case _:
                print("Invalid choice")

    case 3:
        print("Music")
        option = int(input("1 → Play\n2 → Pause\n3 → Next\n4 → Previous\nEnter choice: "))

        match option:
            case 1:
                print("Music Playing")
            case 2:
                print("Music Paused")
            case 3:
                print("Next Song")
            case 4:
                print("Previous Song")
            case _:
                print("Invalid choice")

    case 4:
        print("Navigation")
        option = int(input("1 → Start Navigation\n2 → Stop Navigation\nEnter choice: "))

        match option:
            case 1:
                print("Navigation Started")
            case 2:
                print("Navigation Stopped")
            case _:
                print("Invalid choice")

    case _:
        print("Invalid choice")