sentance = input("Enter sentence: ")

digit = dot = atr = repeat = 0

for i in range(len(sentance)):
    if '0' <= sentance[i] <= '9':
        digit = 1
    if sentance[i] == '.':
        dot = 1
    if sentance[i] == '@':
        atr = 1
    if i > 0 and sentance[i] == sentance[i-1]:
        repeat = 1

if digit and (dot or atr) or repeat:
    print("Suspicious")
elif digit or dot or atr:
    print("Review")
else:
    print("Safe")
