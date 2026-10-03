print('''red
yellow
green''')
Traffic_signal = (input("Enter Traffic color :")).lower()

match Traffic_signal:
    case "red" :
        print("Stop")
    case "yellow":
        print("wait")
    case "green":
        print("go")
    case _:
        print("Invalid signal")