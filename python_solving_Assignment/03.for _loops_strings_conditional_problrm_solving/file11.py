digit = 0
underscore = 0
special = 0
for i in range(5):
    username = input("Enter username: ")


    for i in username:
        if i >= '0' and i <= '9':
            digit += 1
        elif i == '_':
            underscore += 1
        elif not (i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z'):
            special += 1

    print("Length:", len(username))
    print("First character:", username[0])
    print("Digits:", digit)
    print("Underscores:", underscore)

    if special > 0:
        print("invalid")
    elif len(username)  < 5 or underscore < 0:
        print("Needs Improvement")
    else:
        print("Valid")
    
    

