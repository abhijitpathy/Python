for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

# # 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2

# the outer loop continues because here break has affected the ineer loop and not the outer loop