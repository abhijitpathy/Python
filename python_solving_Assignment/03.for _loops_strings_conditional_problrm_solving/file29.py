for i in range(5):
    email = input("Enter email: ")

    count = 0
    position = -1
    space = False

    for j in range(len(email)):
        if email[j] == "@":
            count += 1
            position = j

        if email[j] == " ":
            space = True

    if count != 1 or space:
        print("Invalid")
    else:
        before = email[:position]
        domain = email[position + 1:]

        if before == "" or domain == "" or "." not in domain:
            print("Invalid")
        else:
            print("Valid")