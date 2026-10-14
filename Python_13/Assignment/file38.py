for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")


# output 
#1. 1,1 1,3 inner loop completed 2,1  2,3  inner loop completed
#2. not any inner loop finishes without break
#3. no its not it doest printed for the 3nd loop 