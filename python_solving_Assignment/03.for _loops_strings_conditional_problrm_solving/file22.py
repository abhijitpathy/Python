sentance = input("Enter string: ")

result = ""
count = 1

for i in range(len(sentance)):
    if i < len(sentance) - 1 and sentance[i] == sentance[i + 1]:
        count += 1
    else:
        result += sentance[i] + str(count)
        count = 1

print(result)

